# PROJECT.md — Contexto do projeto Sage 100c

> Preenche este ficheiro por cliente/projeto. O Claude lê-o quando ativas `/sage100c`.
> Mantém-no atualizado — informação desatualizada gera bases de dados/queries erradas.

---

## 1. Identificação

| Campo | Valor |
|---|---|
| Cliente | <!-- ex.: Megavale --> |
| Projeto | <!-- ex.: Integração 100c --> |
| Versão 100c | <!-- ex.: 2070 / v3234 --> |

---

## 2. Base de dados

| Campo | Valor |
|---|---|
| Servidor SQL | <!-- ex.: SRV-SQL01\SAGE --> |
| Sigla da empresa | <!-- ex.: DEMO — base = DEMO_1GCO --> |
| Bases de dados | <!-- ex.: DEMO_1GCO, DEMO_1GAT --> |

> A base de dados de cada módulo é `<SIGLA>_<MODULO>` (ex.: `DEMO_1GCO`).

---

## 3. Módulos ativos

- [ ] 1GCO — Gestão Empresarial / Comercial
- [ ] 1GAT — Gestão de Ativos
- [ ] 1GEP — Salários

---

## 4. Integração / Desenvolvimento

| Campo | Valor |
|---|---|
| Forma principal | <!-- SQL direto / SDK COM / API .NET --> |
| API — login/pwd/sigla | <!-- ApiService.Ini: Login, Pwd, Sigla --> |
| Pasta de mapas Crystal | <!-- caminho dos .rpt --> |

---

## 5. Trabalho ativo / Sprint

> Descreve o que está a ser construído ou corrigido agora, para o Claude ter contexto imediato.

<!-- Exemplo:
- Mapa de vendas por vendedor (1GCO, tabelas DOCGCCAB/DOCGCLIN/VENDEDORES)
- Integração de encomendas via API DocumentoComercial
-->

---

## 6. Regras específicas do projeto

> O que estende/sobrepõe o CLAUDE.md para este cliente.

<!-- Exemplos:
- Tabelas customizadas do cliente com prefixo Z (escrita SQL permitida)
- Usar sempre WITH (NOLOCK) em queries de relatório
-->
