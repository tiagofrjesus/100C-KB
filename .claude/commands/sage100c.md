You are now in **Sage 100c development mode** for the rest of this session.

Sage 100c is a Portuguese ERP (Sage Gestão Empresarial / Comercial, Ativos, Salários) running on **SQL Server**. You help write **SQL queries**, **mapas Crystal Reports**, **SDK automation (COM)** and **API .NET** code, always grounded in the knowledge base — never guess table or field names.

---

## Step 1 — Load project context (do this first)

Read `PROJECT.md` from the root of the current workspace. Extract and hold in mind:

- **Empresa / Sigla** — the company database prefix (e.g. `DEMO`, `MODELO`, or a client sigla). Combined with the module gives the SQL Server database name: `<SIGLA>_<MODULO>` (e.g. `DEMO_1GCO`).
- **Módulos ativos** — which of 1GCO/1GAT/1GEP are in scope.
- **Versão / Servidor SQL** — connection context.
- **Trabalho ativo** — what is being built right now.

If `PROJECT.md` is missing or the sigla is blank, **ask the user for the empresa/sigla and module before writing any SQL**.

---

## Knowledge Base location

All indexes live at `C:\100C-KB\`. Use absolute paths. They are pre-built from the official Sage 100c documentation (data dictionary, API help, SDK help) and are authoritative.

| Resource | Path |
|---|---|
| Catálogo de tabelas — Gestão Comercial (1GCO) | `C:\100C-KB\Docs\DD_Catalog_1GCO.md` |
| Catálogo de tabelas — Ativos (1GAT) | `C:\100C-KB\Docs\DD_Catalog_1GAT.md` |
| Catálogo de tabelas — Salários (1GEP) | `C:\100C-KB\Docs\DD_Catalog_1GEP.md` |
| Schema completo de uma tabela (colunas, tipos, chaves) | `C:\100C-KB\Sage 100c Docs\DD\<MODULO>\<TABELA>.txt` |
| Vistas (views da aplicação) | `C:\100C-KB\Docs\Vistas_<MODULO>.md` |
| Validações (listas de valores / lookups de campos de estado) | `C:\100C-KB\Docs\Validacoes_<MODULO>.md` |
| API .NET — catálogo de classes | `C:\100C-KB\Docs\API_Index.md` |
| API .NET — membros de uma classe | `C:\100C-KB\Sage 100c Docs\API\<Classe>.txt` |
| SDK — modelo de objetos (automação COM) | `C:\100C-KB\Docs\SDK_ObjectModel.md` |
| Mapas Crystal e como emiti-los | `C:\100C-KB\Docs\Mapas_Crystal.md` |
| Visão geral / módulos / bases de dados | `C:\100C-KB\Docs\Modulos.md` |

---

## Módulos e bases de dados

| Código | Módulo | Base de dados SQL |
|---|---|---|
| `1GCO` | Sage Gestão Empresarial / Comercial | `<SIGLA>_1GCO` |
| `1GAT` | Sage Gestão de Ativos | `<SIGLA>_1GAT` |
| `1GEP` | Sage Salários | `<SIGLA>_1GEP` |

Empresas de demonstração: `DEMO` e `MODELO`.

---

## Lookup rules — segue ANTES de escrever qualquer query ou código

Estas regras existem porque inventar nomes de tabelas/campos produz erros silenciosos.

- **Precisas de uma tabela** → grep `C:\100C-KB\Docs\DD_Catalog_<MODULO>.md` por nome ou descrição para obter o nome exato e a chave primária.
- **Vais escrever uma query que toca numa tabela** → lê `C:\100C-KB\Sage 100c Docs\DD\<MODULO>\<TABELA>.txt` PRIMEIRO, para a lista completa de colunas, tipos e chaves. Nomes de colunas não se adivinham.
- **Filtras por um campo de estado/tipo (Integer com poucos valores)** → consulta `C:\100C-KB\Docs\Validacoes_<MODULO>.md`. Se a validação for "Tabela Interna", os valores válidos estão nessa tabela (faz lookup); nunca assumas valores inteiros.
- **Precisas de juntar cabeçalho + linhas de documentos** → confirma as chaves de ligação nos ficheiros `.txt` das duas tabelas antes de escrever o JOIN (ex.: cabeçalho `DOCGCCAB` ↔ linhas `DOCGCLIN`).
- **Vais usar a API** → grep `C:\100C-KB\Docs\API_Index.md` pela classe (ex.: `DocumentoComercial`, `Clientes`, `Artigos`) e lê `Sage 100c Docs\API\<Classe>.txt` para a assinatura, input/output e propósito dos membros.
- **Vais usar o SDK (COM)** → lê `C:\100C-KB\Docs\SDK_ObjectModel.md`. Ponto de entrada: objeto `Aplicacao`.
- **Vais emitir/criar um mapa** → lê `C:\100C-KB\Docs\Mapas_Crystal.md`.

---

## SQL — queries diretas (SQL Server / T-SQL)

Regras obrigatórias:

1. **Base de dados** = `<SIGLA>_<MODULO>` (ex.: `DEMO_1GCO`). Em queries entre módulos qualifica com a BD: `DEMO_1GCO.dbo.CLIENTES`.
2. Usa o **nome exato da tabela** do catálogo. As tabelas 100c **não têm prefixo de schema próprio nem sufixo `_0`** (ao contrário do X3) — o schema é `dbo`.
3. Os nomes de coluna são exatamente os do dicionário (`.txt` da tabela). Confirma-os antes de escrever.
4. **Antes de filtrar um campo de estado/tipo** no `WHERE`, vê os valores válidos em `Validacoes_<MODULO>.md`.
5. Para leitura/relatórios usa `WITH (NOLOCK)` em ambientes onde seja política da casa; caso contrário deixa o utilizador decidir.

```sql
-- Exemplo: clientes ativos com saldo (1GCO)
SELECT c.CODIGO, c.NOME, c.NIF
FROM   DEMO_1GCO.dbo.CLIENTES c
WHERE  c.CODIGO LIKE '43%'
ORDER  BY c.CODIGO;

-- Exemplo: cabeçalho + linhas de documento comercial.
-- Chave composta (verificada nos .txt): cab DOCGCCAB usa TPDOC; linhas DOCGCLIN usam TPDOCUM.
SELECT h.TPDOC, h.SERIE, h.NNUMDOC, l.ARTIGO, l.QUANT
FROM   DEMO_1GCO.dbo.DOCGCCAB h
JOIN   DEMO_1GCO.dbo.DOCGCLIN l
       ON  l.ANO     = h.ANO
       AND l.TPDOCUM = h.TPDOC
       AND l.SERIE   = h.SERIE
       AND l.NNUMDOC = h.NNUMDOC
ORDER  BY h.NNUMDOC;
```

---

## As três formas de interagir com a aplicação

| Forma | Quando usar | Referência |
|---|---|---|
| **SQL direto** | Leitura/relatórios, análises, alimentar mapas Crystal. Escrita direta só em tabelas próprias do cliente. | `DD_Catalog_*`, `DD/<MOD>/*.txt` |
| **SDK (COM, C100SDK)** | Automação a partir de scripts/customização: executar SQL, criar iteradores, emitir mapas Crystal, abrir vistas. Linguagem: VBScript/VBA. Entrada: `Aplicacao`. | `SDK_ObjectModel.md` |
| **API .NET (Sage1GCOApi)** | Criar/alterar documentos e entidades com **toda a lógica de negócio** (impostos, descontos, vencimentos, stocks). Nunca inserir documentos diretamente por SQL. | `API_Index.md`, `API/*.txt` |

> **Regra de ouro:** nunca inserir/alterar documentos comerciais, contabilísticos ou financeiros por SQL direto — usa sempre a **API** (`DocumentoComercial`, `DocumentoContabilistico`, etc.). Inserções diretas corrompem totais, contas-correntes e séries. SQL direto de escrita só em tabelas criadas pelo cliente.

---

## Mapas (Crystal Reports)

Os mapas são Crystal Reports cuja fonte de dados são queries SQL sobre as tabelas/vistas do dicionário. Para desenhar um mapa:

1. Identifica as tabelas/vistas envolvidas no catálogo e lê os `.txt` para colunas e chaves.
2. Escreve/valida a query que alimenta o mapa (regras de SQL acima).
3. Para emitir a partir de código usa o SDK: `Aplicacao.EmitirCrystal(NomeMapa, Destino)` — `Destino`: 0 = ecrã, 2 = impressora (confirma em `SDK_ObjectModel.md`).

Detalhes em `C:\100C-KB\Docs\Mapas_Crystal.md`.

---

## Não fazer

- **Não inventar** nomes de tabelas, colunas ou membros de API — verifica sempre no KB primeiro.
- **Não inserir documentos por SQL** — usa a API.
- **Não assumir valores inteiros** de campos de estado — consulta as Validações.
- **Não editar** ficheiros de configuração da aplicação (`*.Ini`, catálogos) sem o utilizador pedir.
- **Não misturar módulos** sem qualificar a base de dados na query.
