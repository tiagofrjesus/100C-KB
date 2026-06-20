# Sage 100c — Development Guide

Reference for Sage 100c development: SQL queries, Crystal Reports (mapas), SDK automation (COM)
and the .NET business API. Sage 100c is a Portuguese ERP running on **SQL Server**.
See `PROJECT.md` for project-specific context (empresa/sigla, modules, active work).

> When working on a 100c project, type `/sage100c` to activate the full ruleset.

---

## 1. Stack

| Componente | Detalhe |
|---|---|
| Base de dados | Microsoft SQL Server (schema `dbo`) |
| Bases por módulo | `<SIGLA>_1GCO` (Comercial), `<SIGLA>_1GAT` (Ativos), `<SIGLA>_1GEP` (Salários) |
| Automação | SDK 100C — `C100SDK.exe`, COM/ActiveX, VBScript/VBA, objeto `Aplicacao` |
| API negócio | `Sage1GCOApi` (.NET / COM) — documentos e entidades com lógica completa |
| Relatórios | Crystal Reports (`.rpt`), emitidos por `Aplicacao.EmitirCrystal` |

---

## 2. Reference Documentation

A documentação oficial foi processada em índices compactos em `Docs\` e ficheiros por entidade em
`Sage 100c Docs\`. **Antes de escrever qualquer query, mapa ou código, consulta os índices.**

| Ficheiro | Conteúdo | Quando usar |
|---|---|---|
| `Docs/Modulos.md` | Módulos, bases de dados, tipos de entidade, camadas de dev | Visão geral / qual a BD |
| `Docs/DD_Catalog_1GCO.md` | 403 tabelas da Gestão Comercial — nome, descrição, #cols, chave | Encontrar uma tabela 1GCO |
| `Docs/DD_Catalog_1GAT.md` | 162 tabelas dos Ativos | Encontrar uma tabela 1GAT |
| `Docs/DD_Catalog_1GEP.md` | 267 tabelas dos Salários | Encontrar uma tabela 1GEP |
| `Sage 100c Docs/DD/<MOD>/<T>.txt` | Schema completo da tabela: colunas, tipos, comprimentos, chaves/índices | Antes de escrever código que toca na tabela |
| `Docs/Vistas_<MOD>.md` | Vistas da aplicação (muitas queryáveis em SQL) | Procurar uma view |
| `Docs/Validacoes_<MOD>.md` | Listas de valores / lookups de campos de estado | Antes de filtrar campos de estado/tipo |
| `Docs/API_Index.md` | 90 classes da API .NET — propósito e nº de membros | Criar/alterar documentos e entidades |
| `Sage 100c Docs/API/<Classe>.txt` | Membros da classe: assinatura, input/output, propósito | Implementar chamadas à API |
| `Docs/SDK_ObjectModel.md` | Modelo de objetos do SDK (Aplicacao, Contexto, Iterador, Campo, Empresa, Utilizador) | Automação COM |
| `Docs/Mapas_Crystal.md` | Como modelar e emitir mapas Crystal | Relatórios |
| `Docs/Funcional_Gestao.md` | Referência funcional da Gestão/Comercial (1GCO): ciclos, entidades, documentos, fluxos | Perceber o domínio antes de tocar em 1GCO comercial |
| `Docs/Funcional_Contabilidade.md` | Referência funcional da Contabilidade (1GCO): contas, IVA, diários, exploração, modelos fiscais | Perceber contabilidade/movimentos |
| `Docs/Funcional_Ativos.md` | Referência funcional dos Ativos (1GAT): ficha, depreciações, reavaliações, mapas fiscais | Perceber o domínio 1GAT |
| `Docs/Funcional_RH.md` | Referência funcional de RH/Salários (1GEP): processamento, declarações, obrigações legais | Perceber o domínio 1GEP |
| `Docs/Funcional_Sistema.md` | Sistema/administração: empresas, utilizadores, parâmetros, customização, executáveis | Configuração/automação de plataforma |
| `Docs/Integracao_EDI_Generix.md` | Layout de largura fixa dos ficheiros EDI (GENERIX) — importação/exportação | Integrações por ficheiro EDI |
| `Docs/Integracao_UBL_CIUS-PT.md` | Faturação eletrónica UBL 2.1 (CIUS-PT): estrutura XML, regras, mapeamentos | Faturação eletrónica estruturada |
| `Docs/Boletins_Tecnicos.md` | Histórico de versões (novidades/correções) 2018/2023/2026 | Saber se/desde quando existe uma funcionalidade |
| `Docs/Relacoes_<MOD>.md` | Relações DERIVADAS entre tabelas (JOINs canónicos verificados, renomes, falsos amigos) | Antes de escrever um JOIN |
| `Sage 100c Docs/Manuais/*.txt` | Texto completo dos manuais oficiais (grepável) | Detalhe que o índice funcional não cobre |

### Lookup rules

- **Não percebes o domínio/fluxo** → lê primeiro a `Docs/Funcional_<MOD>.md` do módulo; dá vocabulário e aponta tabelas. Depois confirma sempre no `DD_Catalog`/`.txt`.
- **Tabela** → grep `Docs/DD_Catalog_<MOD>.md`; depois lê `Sage 100c Docs/DD/<MOD>/<TABELA>.txt` **antes** de escrever a query.
- **JOIN entre tabelas** → vê o JOIN canónico em `Docs/Relacoes_<MOD>.md` (chaves verificadas); confirma sempre as colunas nos `.txt`. Não há FKs nativas — são relações derivadas.
- **Campo de estado/tipo** → vê valores válidos em `Docs/Validacoes_<MOD>.md` (não assumas inteiros).
- **API** → grep `Docs/API_Index.md` pela classe, lê `Sage 100c Docs/API/<Classe>.txt`.
- **SDK** → `Docs/SDK_ObjectModel.md`.
- **Integração EDI / faturação eletrónica** → `Docs/Integracao_EDI_Generix.md` / `Docs/Integracao_UBL_CIUS-PT.md`.

---

## 3. Direct SQL (SQL Server / T-SQL)

1. Base de dados = `<SIGLA>_<MODULO>` (ex.: `DEMO_1GCO`); schema `dbo`.
2. Nomes de tabela/coluna **exatos** do dicionário — sem prefixo próprio nem sufixo `_0` (≠ X3).
3. Confirma colunas no `.txt` da tabela antes de escrever.
4. Campos de estado/tipo → confirma valores nas Validações antes do `WHERE`.

```sql
SELECT c.CODIGO, c.NOME, c.NIF
FROM   DEMO_1GCO.dbo.CLIENTES c
WHERE  c.CODIGO LIKE '43%'
ORDER  BY c.CODIGO;
```

---

## 4. As três camadas

- **SQL direto** — leitura/relatórios; escrita só em tabelas do cliente.
- **SDK (COM)** — automação; `Aplicacao.ExecutarSql`, `CriarIteradorSql`, `EmitirCrystal`, `AbrirVista`.
- **API .NET** — criar/alterar documentos e entidades com lógica de negócio completa.

> **Regra de ouro:** nunca inserir/alterar documentos (comerciais, contabilísticos, financeiros)
> por SQL direto — usa a **API**. SQL direto de escrita só em tabelas criadas pelo cliente.

---

## 5. What NOT to do

- Não inventar nomes de tabelas/colunas/membros — verificar sempre no KB.
- Não inserir documentos por SQL — usar a API.
- Não assumir valores de campos de estado — consultar Validações.
- Não misturar módulos sem qualificar a base de dados.
- Não editar ficheiros de configuração/catálogos da aplicação sem o utilizador pedir.
