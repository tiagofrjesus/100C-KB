# Relações entre Tabelas — 1GAT (Gestão de Ativos)

> **Aviso:** o dicionário do Sage 100c **não tem foreign keys nativas**. As relações abaixo são
> **DERIVADAS** das chaves (PK/índices) e da presença de colunas homónimas. Confirma sempre os nomes
> **exatos** das colunas em `Sage 100c Docs/DD/1GAT/<TABELA>.txt` antes de escrever a query.
> Base de dados: `<SIGLA>_1GAT`, schema `dbo`. Contexto funcional em `Docs/Funcional_Ativos.md`.

> **Dualidade IMO vs ACTIVOS (crítico):** existem **dois masters de ficha** em paralelo:
> - **`IMO`** (PK `FICHA`) — ficha de ativo "clássica"/POC. Movimentos clássicos ligam por **`FICHA`**.
> - **`ACTIVOS`** (PK `CODIGO`) — ficha SNC (uso atual). Tabelas novas ligam por **`CODIGO`**.
>
> Não há FK declarada entre `IMO.FICHA` e `ACTIVOS.CODIGO`; convivem como duas estruturas de
> cadastro do mesmo conceito (o código do ativo é a chave de negócio). Em instalações SNC, o master
> operacional é `ACTIVOS` + `MOVIMENTOS_ACTIVO`. Verifica qual está populado na tua BD.

---

## 1. Ficha de ativo e seus movimentos

### 1.1 Eixo SNC — `ACTIVOS` (PK `CODIGO`)

Master atual. As tabelas-satélite e o livro de movimentos ligam por **`CODIGO`** (Text(20)).

| Tabela filho | Coluna FK | Conteúdo | Cardinalidade |
|---|---|---|---|
| `MOVIMENTOS_ACTIVO` | `CODIGO` | Livro único de movimentos (aquisições, depr., reaval., imparidades, abates…) — distinguidos por `TIPO_MOVIMENTO` | 1:N |
| `ACTIVOS_CALCULADOS` | `CODIGO` | Valores calculados/acumulados (PK `CODIGO`) | 1:1 |
| `ACTIVOS_DEPRECIACAO` | `CODIGO` | Snapshot do ativo no cálculo de depreciações | 1:1 |
| `DISTRIBUICAO_CUSTOS` | `CODIGO` | Distribuição por conta 9 (PK `CODIGO`+`CONTA_9`) | 1:N |
| `ACTIVOS_CONTAGEM` | `CODIGO` | Ativos numa contagem | 1:N |
| `PARAMETRIZACAO_ACTIVO` | `ACTIVO` (= código) | Contas por ativo+exercício (PK `EXERCICIO`+`ACTIVO`) | 1:N |
| `ACTIVOS_REAVALIA_FISCAL`, `ACTIVOS_REAVALIA_ESPECIAL`, `ACTIVOS_RECLASSIFICACAO`, `ACTIVOS_DESRECONHECIMENTO`, `ACTIVOS_INTRODUCAO_DECRETO`, `ACTIVOS_PREPARACAO_EMISSAO`, `ACTIVOS_EMISSAO_ETIQUETAS`, `SIMULACAO` | `CODIGO` | Tabelas de trabalho de assistentes/processos | 1:N |

> `MOVIMENTOS_ACTIVO` é o coração do eixo SNC. PK = `CODIGO+DATA_OCORRENCIA+TIPO_MOVIMENTO+NUMERO_ORDENA`.
> O tipo de operação está em `TIPO_MOVIMENTO` (Integer) — **confirma os valores em `Docs/Validacoes_1GAT.md`**
> antes de filtrar (não assumas inteiros).

```sql
-- Movimentos de um ativo (eixo SNC)
SELECT a.CODIGO, a.DESCRICAO, m.DATA_OCORRENCIA, m.TIPO_MOVIMENTO, m.VALOR_MOVIMENTO
FROM   DEMO_1GAT.dbo.ACTIVOS a
JOIN   DEMO_1GAT.dbo.MOVIMENTOS_ACTIVO m ON m.CODIGO = a.CODIGO
ORDER  BY a.CODIGO, m.DATA_OCORRENCIA, m.NUMERO_ORDENA;

-- Ficha + valores calculados
SELECT a.CODIGO, a.DESCRICAO, c.VALOR_AQUISICAO_NAO_REAVALIADO,
       c.DEPRECIACOES_ACUMULADAS_NAO_REAVALIADAS
FROM   DEMO_1GAT.dbo.ACTIVOS a
JOIN   DEMO_1GAT.dbo.ACTIVOS_CALCULADOS c ON c.CODIGO = a.CODIGO;
```

### 1.2 Eixo clássico/POC — `IMO` (PK `FICHA`)

Os movimentos históricos ligam por **`FICHA`** (Text(15)/Text(20)).

| Tabela filho | Coluna FK (chave) | Operação |
|---|---|---|
| `AQUISICO` | `FICHA` (PK `REGISTO`+`FICHA`) | Aquisições |
| `REINTEGR` | `FICHA` (PK `FICHA`+`ANO`+`CONTADOR`) | Depreciações |
| `REAVALIA` | `FICHA` (PK `REGISTO`+`FICHA`; idx `FICHA`+`DATA`) | Reavaliações fiscais |
| `ABATE` | `FICHA` (PK `FICHA`) | Alienações / sinistros / abates |
| `CONSERVA` | `FICHA` (PK `NLINHA`+`FICHA`) | Conservação / reparações |
| `CORRFISC` | `FICHA` (PK `SITUACAO`+`FICHA`) | Correções fiscais (ajustes) |
| `HISTCORF` | `FICHA` | Histórico de correções fiscais |
| `MAISVALI` | `FICHA` (PK `FICHA`+`ANO`) | Mais-valias por ano |
| `DISTCUST` | `FICHA` (PK `REGISTO`; idx `FICHA`) | Distribuição de custos por conta/D-C |
| `SEGURO` | `FICHA` (PK `FICHA`+`NAPO`+`DATA`) | Seguros do bem |
| `AVALIACA` | `FICHA` | Avaliações extra-contabilísticas |
| `PFINACEI` | `FICHA` | Plano financeiro (leasing) |
| `LEASING` | `FICHA` (PK `FICHA`) | Contrato de locação financeira |
| `CBARRAS` | `FICHA` (idx `FICHA`+`CBARRAS`) | Códigos de barras do bem |
| `PREVISAO`, `PREVISAO_SNC`, `PROREAVA`, `PROREINT` | `FICHA` | Previsões / provisórios |
| `MAPA31`, `MAPOBS` | `FICHA` | Mapa 31 (mais/menos valias) / observações |

```sql
-- Depreciações de um ativo (eixo clássico)
SELECT i.FICHA, i.DESCRI, r.ANO, r.TAXA, r.VREEXNR, r.VREEXRV
FROM   DEMO_1GAT.dbo.IMO i
JOIN   DEMO_1GAT.dbo.REINTEGR r ON r.FICHA = i.FICHA
ORDER  BY i.FICHA, r.ANO, r.CONTADOR;
```

---

## 2. Pares Cabeçalho/Linha (CAB/LIN)

Único par CAB/LIN do módulo é a **contagem física**:

| Cabeçalho | Linhas | JOIN |
|---|---|---|
| `CONTCAB` (PK `DATAREF`) | `CONTLIN` (PK `DATAREF`+`CODBARRA`) | por `DATAREF` |

```sql
SELECT h.DATAREF, h.RESPONSA, l.CODBARRA, l.LOCALIZ, l.DTCONTAG
FROM   DEMO_1GAT.dbo.CONTCAB h
JOIN   DEMO_1GAT.dbo.CONTLIN l ON l.DATAREF = h.DATAREF
ORDER  BY h.DATAREF, l.CODBARRA;
```

> `CONTCAB` define o intervalo da contagem por **valores** (`FICHAINI/FICHAFIM`, `SECTINI/SECTFIM`,
> `LOCALINI/LOCALFIM`) — são limites, **não** FKs para uma linha específica.
> `ACTIVOS_CONTAGEM` (FK `CODIGO`→`ACTIVOS`) é a tabela de trabalho associada à contagem.

---

## 3. Configuração e ligação à contabilidade

### 3.1 Grupo de ativos e parametrização de contas

`ACTIVOS.GRUPO_ACTIVOS` (Text(10)) + `ACTIVOS.TIPO_ACTIVO` (Integer) determinam as contas via
parametrização. **Prioridade: contas por ativo > contas por grupo** (ver `Funcional_Ativos.md` §6).

| Tabela | Chave | Liga a |
|---|---|---|
| `GRUPO_ACTIVOS` | PK `CODIGO`+`SNC` | referenciada por `ACTIVOS.GRUPO_ACTIVOS` (= `CODIGO`) |
| `PARAMETRIZACAO_CONTABILISTICA` | PK `EXERCICIO`+`TIPO_ACTIVO`+`GRUPO_ACTIVOS` | contas gerais por grupo |
| `PARAMETRIZACAO_ACTIVO` | PK `EXERCICIO`+`ACTIVO` | contas por ativo (prevalece) |

```sql
-- Contas de um ativo: por ativo (override) e por grupo (fallback)
SELECT a.CODIGO, a.GRUPO_ACTIVOS, a.TIPO_ACTIVO,
       pa.AQUISICAO            AS conta_aquis_activo,
       pg.AQUISICAO            AS conta_aquis_grupo
FROM   DEMO_1GAT.dbo.ACTIVOS a
LEFT   JOIN DEMO_1GAT.dbo.PARAMETRIZACAO_ACTIVO pa
       ON pa.ACTIVO = a.CODIGO AND pa.EXERCICIO = 2026
LEFT   JOIN DEMO_1GAT.dbo.PARAMETRIZACAO_CONTABILISTICA pg
       ON pg.GRUPO_ACTIVOS = a.GRUPO_ACTIVOS
      AND pg.TIPO_ACTIVO   = a.TIPO_ACTIVO
      AND pg.EXERCICIO     = 2026;
```

> As colunas de conta nas tabelas de parametrização (`AQUISICAO`, `GASTO_DEPRECIACAO`, etc.) são
> **radicais/códigos de conta Text(15)** que casam com `DESCONTA.CODIGO` e `CNTANA.CONTA`.

### 3.2 Contas, sectores e centros de custo

| Conceito | Coluna na ficha/movimento | Tabela-tipo (PK) |
|---|---|---|
| Conta | `IMO.CONTAPOC`/`CONTARED`/`CONTAREC`; `ACTIVOS_CALCULADOS.CONTA`; `DISTCUST.CONTA`; `LIGCTB.CONTA` | `DESCONTA` (PK `CODIGO`), `CNTANA` (PK `CONTA`) |
| Sector | `ACTIVOS.SECTOR` / `IMO.SECTOR` (Text(3)); `LIGCTB.SECTOR` (Text(5)) | `SECTORES` (PK `CODIGO`, Text(3)) |
| Centro de custo | `ACTIVOS.CCECU1..CCECU4` (Long); `LIGCTB.CCECU1..4`; `CENCU.CCECU` | `CENCU1..CENCU4` (PK `CCECU`, Long) |
| Repartição sector→CC | — | `REPSECTO` (PK `RUBRICA`+`SECTOR`+`CCUSTO`) |

```sql
-- Ficha + sector + centro de custo da tabela 1
SELECT a.CODIGO, a.SECTOR, s.DESCR  AS sector_desc,
       a.CCECU1, c1.DESCR AS cc1_desc
FROM   DEMO_1GAT.dbo.ACTIVOS a
LEFT   JOIN DEMO_1GAT.dbo.SECTORES s  ON s.CODIGO = a.SECTOR
LEFT   JOIN DEMO_1GAT.dbo.CENCU1   c1 ON c1.CCECU = a.CCECU1;
```

> **Atenção (falso amigo de domínios):** `SECTORES.CCUSTO` é **Text(6)** e `REPSECTO.CCUSTO` é
> **Text(6)**, mas `ACTIVOS.CCECU1..4` / `CENCU.CCECU` são **Long**. São centros de custo de
> domínios distintos — **não** faças JOIN direto entre `SECTORES.CCUSTO` e `CENCU.CCECU` sem confirmar.

### 3.3 Geração da ligação à contabilidade

`LIGCTB` (PK `NUMLINHA`) é a tabela de **movimentos de ligação à CTB** gerados a partir dos movimentos
do ativo (por `TIPO_MOVIMENTO`). Não tem FK direta para `ACTIVOS`/`MOVIMENTOS_ACTIVO` no dicionário;
é o resultado da geração, com `CONTA`, `SECTOR`, `CCECU1..4`, `DC`, `VALOR`, datas e `CODTERC`.
`COPCTB` é a CTB compactada; `ACUMPOC` os acumulados POC (por `CONTA`).

```sql
SELECT lc.NUMLINHA, lc.DATA_CONTABILIDADE, lc.CONTA, lc.DC, lc.VALOR, lc.SECTOR
FROM   DEMO_1GAT.dbo.LIGCTB lc
WHERE  lc.TIPO_MOVIMENTO = /* ver Validacoes_1GAT.md */ 1;
```

---

## 4. Tabelas fiscais

A ficha guarda **códigos** que casam com as tabelas fiscais (sem FK declarada):

| Coluna na ficha | Casa com | Tabela (PK) |
|---|---|---|
| `ACTIVOS.CODIGO_TABELA` / `IMO.CTABELA` | código de tabela DR | `CODTAB` (PK `CODIGO`, Text(5)) |
| `ACTIVOS.CORRECCAO_FISCAL_1`/`_2`; `IMO.AJFIS1`/`AJFIS2` | código de ajuste | `AJFISC` (PK `CODIGO`, Integer) |
| `ACTIVOS.DECRETO_PROXIMA_REAVALIACAO`; `IMO.DTPRRV`/`DECULRV` | decreto | `DECRETOS` (PK `CODIGO`, Integer) |
| `REAVALIA.DECRETO`, `MOVIMENTOS_ACTIVO.DECRETO` | decreto aplicado | `DECRETOS` |
| `ACTIVOS.OBSERVACOES_ESPECIAIS`; `IMO.OBSSVESP`/`CODDECES` | obs. especiais | `DESESPEC` (PK `CODIGO`) |
| `DESCONTA.TPIMO` | tipo de ativo | `TPIMO` (PK `TIMO`) |
| Coeficientes de reavaliação por ano | — | `COEFREAV` (PK `ANO`), `PORTDM` (PK `CPORT`), `COEFDM` |

```sql
-- Ficha com descrição do código de tabela e do decreto da próxima reavaliação
SELECT a.CODIGO, a.CODIGO_TABELA, ct.DESCRICA AS desc_tabela,
       a.DECRETO_PROXIMA_REAVALIACAO, d.SIGLA  AS decreto_sigla
FROM   DEMO_1GAT.dbo.ACTIVOS a
LEFT   JOIN DEMO_1GAT.dbo.CODTAB   ct ON ct.CODIGO = a.CODIGO_TABELA
LEFT   JOIN DEMO_1GAT.dbo.DECRETOS d  ON d.CODIGO  = a.DECRETO_PROXIMA_REAVALIACAO;
```

> `CODTAB.DESCRICA` tem índice próprio mas a chave é `CODIGO`. As taxas por regime estão em
> `TX73781`, `TX290`, `TX252009`. O `ACTIVOS.REGIME`/`IMO.REGIME` (Integer) seleciona qual taxa
> aplicar — **confirma os valores de `REGIME` em `Docs/Validacoes_1GAT.md`**.

---

## 5. Mapa de entidade → quem a referencia

### 5.1 Ficha de ativo

| Master | Coluna PK | Referenciada por (coluna FK) |
|---|---|---|
| `ACTIVOS` | `CODIGO` | `MOVIMENTOS_ACTIVO.CODIGO`, `ACTIVOS_CALCULADOS.CODIGO`, `ACTIVOS_DEPRECIACAO.CODIGO`, `DISTRIBUICAO_CUSTOS.CODIGO`, `ACTIVOS_CONTAGEM.CODIGO`, `PARAMETRIZACAO_ACTIVO.ACTIVO`, `ACTIVOS_REAVALIA_FISCAL/_ESPECIAL.CODIGO`, `ACTIVOS_RECLASSIFICACAO.CODIGO`, `ACTIVOS_DESRECONHECIMENTO.CODIGO`, `ACTIVOS_INTRODUCAO_DECRETO.CODIGO`, `ACTIVOS_PREPARACAO_EMISSAO.CODIGO`, `ACTIVOS_EMISSAO_ETIQUETAS.CODIGO`, `SIMULACAO.CODIGO` |
| `IMO` | `FICHA` | `AQUISICO`, `REINTEGR`, `REAVALIA`, `ABATE`, `CONSERVA`, `CORRFISC`, `HISTCORF`, `MAISVALI`, `DISTCUST`, `SEGURO`, `AVALIACA`, `CBARRAS`, `CONTAGEM`, `MAPA31`, `MAPOBS`, `PFINACEI`, `LEASING`, `PREVISAO`, `PREVISAO_SNC`, `PROREAVA`, `PROREINT` (todas por `FICHA`) |

### 5.2 Conta (`CONTA`)

Não há master único de plano de contas no 1GAT; usa-se `DESCONTA` (PK `CODIGO`) / `CNTANA` (PK `CONTA`).
Referenciam contas: `ACTIVOS_CALCULADOS.CONTA`, `DISTCUST.CONTA`, `DISTRIBUICAO_CUSTOS.CONTA_9`,
`LIGCTB.CONTA`, `COPCTB.CONTA`, `ACUMPOC.CONTA`, `IMO.CONTAPOC/CONTARED/CONTAREC`,
e as 17 colunas de conta de `PARAMETRIZACAO_ACTIVO` / `PARAMETRIZACAO_CONTABILISTICA`.

### 5.3 Sector (`SECTORES`, PK `CODIGO`)

Referenciado por: `ACTIVOS.SECTOR`, `IMO.SECTOR`, `LIGCTB.SECTOR`, `COPCTB.SECTOR`, `REPSECTO.SECTOR`.

### 5.4 Centro de custo (`CENCU1..CENCU4`, PK `CCECU`)

Referenciado por: `ACTIVOS.CCECU1..CCECU4`, `LIGCTB.CCECU1..CCECU4`, `CENCU.CCECU1..CCECU5` (rateios).
`REPSECTO.CCUSTO` e `SECTORES.CCUSTO` são **Text** (domínio diferente — ver §3.2).

### 5.5 Falsos amigos / colunas sobrecarregadas

- `DESCR` / `DESCRI` / `DESCRICA` / `DESCRICAO` = **"Descrição"** — texto livre, **nunca** uma FK.
- `DESCRICAO_GRUPO` / `DESCGGRUP` / `GRANDE_GRUPO` / `SUB_GRUPO` / `DESCSUBG` = rótulos de
  agrupamento de mapas (Text(5)), **não** apontam para `GRUPO_ACTIVOS` (que é a config CTB).
- `GRUPO_HOMOGENEO` (Text(5)) → `GRUPOS_HOMOGENEOS` (PK `CODIGO`); distinto de `GRUPO_ACTIVOS`.
- `FORNECEDOR`/`FORNEC`/`FORNECED`: largura varia (`AQUISICO.FORNECED` Text(15) vs
  `ACTIVOS.FORNECEDOR` Text(30)) — confirma comprimento antes de JOIN a `FORNEC` (PK `CODIGO`).
- `CLIENTE` em `ACTIVOS`/`IMO` é Text(28)/Text(15) (nome "vendido a"), nem sempre o `CLIENTES.CODIGO`.
- `REGISTO`, `CONTADOR`, `NLINHA`, `NUMLINHA`, `NREG` = contadores internos de PK, **não** são FKs.
- `REAVALIA` aparece como **nome de tabela** e como **coluna Integer** (flag) em `IMO`/`DESCONTA`.
- Tipos/estados (`TIPO_MOVIMENTO`, `ESTADO`, `REGIME`, `METODO`, `TPABATE`, `INDTAXA`) são Integer
  com listas de valores — consulta `Docs/Validacoes_1GAT.md` antes de filtrar.
