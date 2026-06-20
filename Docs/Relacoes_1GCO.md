# Relações entre Tabelas — 1GCO (Gestão Comercial)

> **AVISO** — Estas relações são **DERIVADAS** (chaves partilhadas + presença de colunas no dicionário),
> **não são foreign keys nativas**. O dicionário Sage 100c não tem FKs. Antes de usar qualquer JOIN,
> **confirma sempre os nomes EXATOS das colunas no `.txt` da tabela** (`Sage 100c Docs/DD/1GCO/<TABELA>.txt`).
> Substitui `<SIGLA>` pela sigla da empresa (ex.: `DEMO_1GCO`). Schema = `dbo`.

---

## 1. Documentos: cabeçalho ↔ linhas

Cada par CAB/LIN partilha a chave de documento, mas **atenção aos renomes de coluna** entre cabeçalho e linha.

| Par | PK Cabeçalho | PK Linha | Nota de rename |
|---|---|---|---|
| `DOCGCCAB` / `DOCGCLIN` (comercial) | ANO+**TPDOC**+SERIE+NNUMDOC | ANO+**TPDOCUM**+SERIE+NNUMDOC+NUMLINHA | cab `TPDOC` → lin `TPDOCUM` |
| `DOCOBCAB` / `DOCOBLIN` (obras) | ANO+**TPDOC**+SERIE+NNUMDOC | ANO+**TPDOCUM**+SERIE+NNUMDOC+NUMLINHA | cab `TPDOC` → lin `TPDOCUM` |
| `DOCCCCAB` / `DOCCCLIN` (conta-corrente) | ANO+**TPDOC**+**SERIEPGT**+**NUMDOC** | ANO+**TIPOD**+**SERIED**+**NUMD**+NUMLIN | nomes totalmente diferentes (ver mapa abaixo) |
| `AVENCAB` / `AVENLIN` (avenças) | CLIENTE+TIPOCNTR+NUMCNTR+ANO | TIPOCNTR+NUMCNTR+ANO+LINHA | linha **não** tem CLIENTE; junta por TIPOCNTR+NUMCNTR+ANO |
| `STATCAB` / `STATLIN` (intrastat) | TPDOC+NNUMDOC+SERIE+ANO | TPDOC+SERIE+ANO+NNUMDOC+NUMLIN | mesmos nomes |
| `TRBANCAB` / `TRBANLIN` (transf. bancárias) | TPDOC+NUMDOC+SERIE+ANO | TPDOC+NUMDOC+SERIE+ANO+LINHA | mesmos nomes |

### DOCGCCAB ↔ DOCGCLIN (comercial)
```sql
SELECT c.TPDOC, c.SERIE, c.NNUMDOC, c.TERCEIRO, l.NUMLINHA, l.ARTIGO, l.QUANT, l.VALOR
FROM   <SIGLA>_1GCO.dbo.DOCGCCAB c
JOIN   <SIGLA>_1GCO.dbo.DOCGCLIN l
       ON  l.ANO     = c.ANO
       AND l.TPDOCUM = c.TPDOC      -- rename: lin.TPDOCUM = cab.TPDOC
       AND l.SERIE   = c.SERIE
       AND l.NNUMDOC = c.NNUMDOC
ORDER  BY l.NUMLINHA;
```

### DOCOBCAB ↔ DOCOBLIN (obras) — mesma lógica do comercial
```sql
SELECT c.TPDOC, c.SERIE, c.NNUMDOC, l.NUMLINHA, l.ARTIGO, l.QUANT
FROM   <SIGLA>_1GCO.dbo.DOCOBCAB c
JOIN   <SIGLA>_1GCO.dbo.DOCOBLIN l
       ON  l.ANO = c.ANO AND l.TPDOCUM = c.TPDOC AND l.SERIE = c.SERIE AND l.NNUMDOC = c.NNUMDOC;
```

### DOCCCCAB ↔ DOCCCLIN (conta-corrente) — mapeamento de colunas

| Cabeçalho (DOCCCCAB) | Linha (DOCCCLIN) |
|---|---|
| ANO | ANO |
| TPDOC | TIPOD |
| SERIEPGT | SERIED |
| NUMDOC | NUMD |
| (linha tem ainda) | NUMLIN |

```sql
SELECT c.TPDOC, c.SERIEPGT, c.NUMDOC, c.TERCEIRO, l.NUMLIN, l.VLPAGO
FROM   <SIGLA>_1GCO.dbo.DOCCCCAB c
JOIN   <SIGLA>_1GCO.dbo.DOCCCLIN l
       ON  l.ANO    = c.ANO
       AND l.TIPOD  = c.TPDOC       -- TPDOC -> TIPOD
       AND l.SERIED = c.SERIEPGT    -- SERIEPGT -> SERIED
       AND l.NUMD   = c.NUMDOC      -- NUMDOC -> NUMD
ORDER  BY l.NUMLIN;
```
> `DOCCCLIN` tem ainda um índice secundário `DOCTERC` (TPTERC+TERCEIRO+ANOL+TPDOCL+SERIEL+NUMDOCL) e `DOCPAGO`
> (ANOL+TPDOCL+SERIEL+NUMDOCL) que apontam para o **documento liquidado** (o pendente que o recibo abate).

### AVENCAB ↔ AVENLIN
```sql
SELECT c.CLIENTE, c.TIPOCNTR, c.NUMCNTR, c.ANO, l.LINHA, l.ARTIGO, l.QUANT
FROM   <SIGLA>_1GCO.dbo.AVENCAB c
JOIN   <SIGLA>_1GCO.dbo.AVENLIN l
       ON  l.TIPOCNTR = c.TIPOCNTR AND l.NUMCNTR = c.NUMCNTR AND l.ANO = c.ANO;
```

### STATCAB ↔ STATLIN / TRBANCAB ↔ TRBANLIN
```sql
SELECT *
FROM   <SIGLA>_1GCO.dbo.STATCAB c
JOIN   <SIGLA>_1GCO.dbo.STATLIN l
       ON l.TPDOC = c.TPDOC AND l.SERIE = c.SERIE AND l.ANO = c.ANO AND l.NNUMDOC = c.NNUMDOC;

SELECT *
FROM   <SIGLA>_1GCO.dbo.TRBANCAB c
JOIN   <SIGLA>_1GCO.dbo.TRBANLIN l
       ON l.TPDOC = c.TPDOC AND l.NUMDOC = c.NUMDOC AND l.SERIE = c.SERIE AND l.ANO = c.ANO;
```
> `TRBANLIN` liga ainda ao pendente pago via colunas `PEN*` (PENANO, PENDOC, PENSERIE, PENNUM, PENTERC…).

---

## 2. Documento comercial → entidades e tabelas mestras

Ligações de `DOCGCCAB` (cabeçalho comercial) às mestras. Coluna FK confirmada no `.txt`.

| Mestra | PK da mestra | Coluna(s) FK em DOCGCCAB | Observação |
|---|---|---|---|
| Cliente/Fornecedor | `CLIENTES.CODIGO` / `FORNEC.CODIGO` | `TPTERC` + `TERCEIRO` | **polimórfico** — ver secção 3 |
| Vendedor | `VENDEDOR.CODIGO` | `VENDEDOR` | também existe em DOCGCLIN (por linha) |
| Tipo de documento | `TPDOC.CODIGO` | `TPDOC` | |
| Série | `NOMSERIE` (PK **TIPODOC+SERIE**) | `TPDOC` + `SERIE` | `NOMSERIE.TIPODOC = TPDOC`, `NOMSERIE.SERIE = SERIE` |
| Moeda | `MOEDAS.CODIGO` | `MOEDA` | (confirmar uso de MOEDAS vs ISO4217) |
| País | `PAISES.COD` | `PAIS` (e `PAISDSG`) | |
| Sector | `SECTORES.CODIGO` | `SECTOR` | também em DOCGCLIN |
| Modo de pagamento | `MODOPGT.CODIGO` | `MODOPGT` | |
| Tipo de IVA | `RGIVA.CODIGO` | `RGIVA` | |
| Modo de expedição | `EXPEDIR.CODIGO` | `EXPEDIR` | |

Na **linha** `DOCGCLIN`:

| Mestra | PK | Coluna FK em DOCGCLIN |
|---|---|---|
| Artigo | `ARTIGOS.CODIGO` | `ARTIGO` |
| Armazém | `ARMAZENS.CODIGO` | `ARMAZEM` |
| Unidade | `UNID.COD` | `UNIDADE` |
| Vendedor | `VENDEDOR.CODIGO` | `VENDEDOR` |
| Sector | `SECTORES.CODIGO` | `SECTOR` |

```sql
-- Documento comercial com cliente, vendedor, tipo doc e série
SELECT  c.TPDOC, c.SERIE, c.NNUMDOC, c.DATA,
        cl.NOME AS CLIENTE_NOME,
        v.CODIGO AS VENDEDOR,
        td.DESCR AS TIPO_DOC,
        ns.DESCR AS SERIE_DESCR
FROM    <SIGLA>_1GCO.dbo.DOCGCCAB c
LEFT JOIN <SIGLA>_1GCO.dbo.CLIENTES cl ON cl.CODIGO = c.TERCEIRO AND c.TPTERC = 1  -- confirmar valor TPTERC
LEFT JOIN <SIGLA>_1GCO.dbo.VENDEDOR v  ON v.CODIGO  = c.VENDEDOR
LEFT JOIN <SIGLA>_1GCO.dbo.TPDOC    td ON td.CODIGO = c.TPDOC
LEFT JOIN <SIGLA>_1GCO.dbo.NOMSERIE ns ON ns.TIPODOC = c.TPDOC AND ns.SERIE = c.SERIE;

-- Linhas com artigo e armazém
SELECT  l.NNUMDOC, l.NUMLINHA, a.NOME AS ARTIGO_NOME, l.ARMAZEM, l.QUANT
FROM    <SIGLA>_1GCO.dbo.DOCGCLIN l
JOIN    <SIGLA>_1GCO.dbo.ARTIGOS  a ON a.CODIGO = l.ARTIGO;
```

> Em `DOCGCLIN`, `ARTIGO` pode conter um **artigo** (`ARTIGOS.CODIGO`) ou um **descritor** (`DESCRIT.COD`) —
> a descrição da coluna no `.txt` é "Artigo ou Descritor". A coluna `RUBRICA` aponta para descritor.

---

## 3. Polimorfismo de Terceiro (`TPTERC` + `TERCEIRO`)

O par `TPTERC` (Integer, tipo de terceiro) + `TERCEIRO` (Text(15), código) é **polimórfico**:
a mesma coluna `TERCEIRO` aponta para `CLIENTES.CODIGO` **ou** `FORNEC.CODIGO` consoante o valor de `TPTERC`.

- Convenção habitual no Sage 100c: `TPTERC` distingue **Cliente** vs **Fornecedor** (lookup `TPTERC`/tabela interna `TERCEIRO`).
  **(confirmar os valores inteiros exatos antes de filtrar — não estão enumerados em `Validacoes_1GCO.md`,
  que apenas mapeia o código de validação `TPT`/`TPTE` à tabela interna.)**

```sql
-- Resolver o terceiro de forma polimórfica
SELECT d.TPTERC, d.TERCEIRO,
       COALESCE(cl.NOME, f.NOME) AS NOME_TERCEIRO
FROM   <SIGLA>_1GCO.dbo.DOCGCCAB d
LEFT JOIN <SIGLA>_1GCO.dbo.CLIENTES cl ON d.TERCEIRO = cl.CODIGO  /* AND d.TPTERC = <cliente> */
LEFT JOIN <SIGLA>_1GCO.dbo.FORNEC   f  ON d.TERCEIRO = f.CODIGO   /* AND d.TPTERC = <fornecedor> */;
```

**Tabelas que contêm o par `TPTERC` + `TERCEIRO`** (do índice invertido; `TERCEIRO` em 18 tabelas, `TPTERC` em 24):

`ACTERLIN`, `ACUMTERC`, `ACUMULADOS_TERCEIRO_ARTIGOS`, `CCCAB2`, `CCLIN2`, `DOCCABDRF`, `DOCCCCAB`,
`DOCCCLIN`, `DOCGCCAB`, `DOCLINDRF`, `DOCOBCAB`, `EXTHIS`, `GCCAB2`, `LOTEMOVS`, `MORADAS`, `NSERMOVS`,
`PENDENTE`, `PVENBASE`.

Tabelas só com `TPTERC` (terceiro pode estar noutra coluna, ex. `TERC`): `ACIVA`, `ACUMPOC_CACHE`, `CTBTAG`,
`EDC_ENTIDADES`, `MOVCT`, `MOVCTB` (estas duas usam coluna `TERC`), `POC` (`TERC`).

> Nota: existem também colunas `CLIENTE`, `FORNEC`/`FORNECEDOR` **diretas** (não polimórficas) noutras tabelas
> — ver secção 4. Não confundir com o par polimórfico.

---

## 4. Mapa de entidade → quem a referencia

Listas derivadas do **índice invertido** (as tabelas listadas contêm mesmo a coluna). Confirmar sempre o `.txt`.

### Cliente — `CLIENTES.CODIGO`
- **Via par polimórfico** `TPTERC+TERCEIRO`: ver secção 3.
- **Via coluna direta `CLIENTE`** (10 tabelas): `AJUDAVND`, `AVENCAB`, `AVENPROC`, `CONTENC`, `ESTIMATECONFIG`,
  `EXCEPDES`, `EXCEPRSV`, `EXEPCOMI`, `PARAMAPL`, `TAG`.

### Fornecedor — `FORNEC.CODIGO`
- **Via par polimórfico** `TPTERC+TERCEIRO` (quando TPTERC = fornecedor).
- **Via coluna `FORNEC`** (4): `ARTIGOS`, `IMO`, `PREAPR`, `PVENBASE`.
- **Via coluna `FORNECEDOR`** (3): `DESPEQUIPCAB`, `DESPEQUIPLIN`, `NOMSERIE` (fornecedor de autofacturação).

### Artigo — `ARTIGOS.CODIGO` (FK = `ARTIGO`, ~49 tabelas)
`ACARTANO`, `ACARTMES`, `ACUMPREV`, `ACUMULADOS_TERCEIRO_ARTIGOS`, `AEXECUTA`, `AJUDACMP`, `AJUDAVND`,
`ARMAZEM_OBRA`, `ARTARM`, `ARTIDIOM`, `ARTIGOS_IVA`, `ARTLOT`, `ARTOPERA`, `AVENLIN`, `CADASTROEQUIPAMENTO`,
`CBARRAS`, `CLLOTES`, `DOCGCLIN`, `DOCOBCAB`, `DOCOBLIN`, `ECOEXCEP`, `ENCOMEND`, `ETIQUETA`, `EXCEPDES`,
`EXCEPLOT`, `EXCEPRSV`, `EXECUTAD`, `EXEPCOMI`, `GCLIN2`, `LOTEMOVS`, `NSEREXEP`, `NSEREXIS`, `NSERMOVS`,
`OPERAFAC`, `ORCAM`, `PALETLIN`, `PLANOREQUISICOES`, `PREAPR`, `PRECOS`, `PRECOSPREPARADOS`, `PVENBASE`,
`PVENDESG`, … (lista completa no `rel_1GCO.md`).
> Em `DOCGCLIN`/`DOCOBLIN` a coluna `ARTIGO` pode ser artigo **ou** descritor (ver secção 2).

### Conta POC — `POC` (PK **EXERCICIO+CONTA**, não só `CONTA`!)
> ⚠️ A coluna `CONTA` é **SOBRECARREGADA**: aparece em ~49 tabelas mas nem sempre é conta POC —
> pode ser conta bancária (ex.: `TRBANCAB.CONTA` = "Conta bancária" Text(21)), conta de reconciliação, etc.
> **Verifica o tipo/descrição no `.txt` antes de assumir POC.** Para POC, junta por `EXERCICIO+CONTA`.

Tabelas que usam `CONTA` como conta de plano (contabilidade/acumulados): `ACFLUX`, `ACGES`, `ACIVA`,
`ACPOCSEC`, `ACUMPOC`, `ACUMPOCCL9`, `ACUMPOCTODAS`, `ACUMPOC_CACHE`, `CNTANA`, `CNTRES`, `CTBORC`,
`GREGIVA`, `GRELHA_RETENCAO`, `GRPCONTA`, `MOVCT`, `MOVCTB`, `POC` (auto-ref CORRA/CORRB), `RECAPI`, …
Conta **bancária** (não POC): `BANMVBAN`, `BANMVEMP`, `BANSCHEDULEMV`, `RECONBANCAB`/`LIN`, `TRBANCAB`, `CNTBAN` (PK CONTAPOC).

```sql
-- Movimento contabilístico -> conta POC do exercício
SELECT m.CONTA, p.DESCR, m.VALOR, m.DBCR
FROM   <SIGLA>_1GCO.dbo.MOVCTB m
JOIN   <SIGLA>_1GCO.dbo.POC    p ON p.CONTA = m.CONTA AND p.EXERCICIO = m.EXERCICIO;
```

### Vendedor — `VENDEDOR.CODIGO` (FK = `VENDEDOR`, ~14 tabelas)
`ACUMVEND`, `AVENLIN`, `CCLIN2`, `CLIENTES`, `COMISSOES_LINHA`, `CONSULTA_VENDEDORES`, `DOCCCLIN`,
`DOCGCCAB`, `DOCGCLIN`, `DOCOBCAB`, `GCCAB2`, `PENDENTE`, `ROTAS`, `ZONAGEO`.

### Armazém — `ARMAZENS.CODIGO` (FK = `ARMAZEM`, ~19 tabelas)
`ACARTANO`, `ACARTMES`, `ACUMPREV`, `ARMAZEM_OBRA`, `ARTARM`, `ARTIGOS`, `ARTLOT`, `CLLOTES`, `DOCGCLIN`,
`DOCOBLIN`, `ETPDOC`, `GCLIN2`, `INVENTAR`, `LOTEMOVS`, `NSEREXIS`, `NSERMOVS`, `PALETLIN`, `PREAPR`,
`SECTORES`.

### Carteira — `CARTEIRA.CODIGO`
> A coluna literal `CARTEIRA` aparece só em `EXTHIS`, `GRPCONTA`. A carteira de pendentes está em
> `PENDENTE.TPCNT` (descrição "Carteira") e `DOCCCCAB.CARTDES`/`CARTORIG`. **(confirmar no `.txt`.)**

### Sector — `SECTORES.CODIGO` (FK = `SECTOR`, ~36 tabelas)
`ACGES`, `ACPOCSEC`, `AVENCAB`, `BALORC`, `BANCABDP`, `CCCAB2`, `CCLIN2`, `CTBORC`, `DISSSEC`, `DOCCABDRF`,
`DOCCCCAB`, `DOCCCLIN`, `DOCGCCAB`, `DOCGCLIN`, `DOCOBCAB`, `DOCOBLIN`, `MOVCT`, `MOVCTB`, `PENDENTE`,
`TRBANCAB`, … (lista completa no `rel_1GCO.md`).

### Centro de custo — `CCUSTO.COD`
FK `CCUSTO` (6 tabelas): `ARMAZENS`, `BALORC`, `CTBORC`, `MODELOS`, `REPSECTO`, `SECTORES`.
> Em `MOVCTB` o centro de custo orçamental está em `CCUSTORC` (Text(6)).

> ⚠️ A entrada `DESCR` do índice invertido é a abreviatura de **"Descrição"** (coluna de texto livre presente
> em quase todas as tabelas: DOCGCLIN.DESCR, POC.DESCR, etc.) e **NÃO** é o FK para a tabela de descritores
> (`DESCRIT`, PK `COD`). Não tratar `DESCR` como relação. O FK real de descritor é `RUBRICA`/`ARTIGO` (descritor) ou `DESCRT`.

---

## 5. Conta-corrente / pendentes / contabilidade

### PENDENTE (PK `ANO+TPDOC+SERIE+NNUMDOC`)
O pendente representa um documento em aberto (a receber/pagar). Liga ao documento de origem pela mesma
chave de documento e ao terceiro pelo par polimórfico.

```sql
-- Pendente <-> documento comercial de origem
SELECT p.TPTERC, p.TERCEIRO, p.TPDOC, p.SERIE, p.NNUMDOC, p.VLPENDE, p.DATAVENC
FROM   <SIGLA>_1GCO.dbo.PENDENTE p
JOIN   <SIGLA>_1GCO.dbo.DOCGCCAB c
       ON c.ANO = p.ANO AND c.TPDOC = p.TPDOC AND c.SERIE = p.SERIE AND c.NNUMDOC = p.NNUMDOC;
```
> `PENDENTE` tem índices secundários por terceiro: `TERMDT` (TPTERC+TERCEIRO+MOEDA+TPCNT+DATAVENC) e
> `TPTERC` (TPTERC+TERCEIRO+TPDOC). `TPCNT` = carteira; `MOEDA` → `MOEDAS`.

### Recibos (DOCCC) que abatem pendentes
A linha de recibo `DOCCCLIN` aponta para o pendente liquidado pelas colunas `ANOL+TPDOCL+SERIEL+NUMDOCL`
(índice `DOCPAGO`), com o terceiro em `TPTERC+TERCEIRO` (índice `DOCTERC`).

```sql
SELECT l.TERCEIRO, l.TPDOCL, l.SERIEL, l.NUMDOCL, l.VLPAGO
FROM   <SIGLA>_1GCO.dbo.DOCCCLIN l
JOIN   <SIGLA>_1GCO.dbo.PENDENTE p
       ON p.ANO = l.ANOL AND p.TPDOC = l.TPDOCL AND p.SERIE = l.SERIEL AND p.NNUMDOC = l.NUMDOCL
      AND p.TPTERC = l.TPTERC AND p.TERCEIRO = l.TERCEIRO;
```

### MOVCTB — Movimentos de contabilidade (PK `ANO+TPDOC+SERIE+NUMDOC+NUMLINHA`)
Movimento contabilístico de uma linha de documento. Liga à conta POC (secção 4), ao terceiro
(`TPTERC`+coluna **`TERC`**, não `TERCEIRO`), ao sector (`SECTOR`), ao diário (`DIARIO`), à rubrica
orçamental (`RUBORC`), centro de custo orçamental (`CCUSTORC`), centro de custeio (`CUSTEIO`), fluxo (`CODFLU`).

```sql
SELECT m.ANO, m.TPDOC, m.SERIE, m.NUMDOC, m.NUMLINHA,
       m.CONTA, p.DESCR AS CONTA_DESCR, m.TERC, m.SECTOR, m.VALOR, m.DBCR
FROM   <SIGLA>_1GCO.dbo.MOVCTB m
JOIN   <SIGLA>_1GCO.dbo.POC    p ON p.CONTA = m.CONTA AND p.EXERCICIO = m.EXERCICIO
ORDER  BY m.NUMDOC, m.NUMLINHA;
```
> A coluna que liga o movimento ao documento comercial de origem é `LINCOM` ("Linha Comercial") e o flag
> `LIGADO`/índice `LIGCTB`. `MOVCT` (Movimentos Contabilísticos, tabela distinta) tem estrutura semelhante.

---

_Fonte: schemas `Sage 100c Docs/DD/1GCO/*.txt` e material `scratchpad/rel_1GCO.md`. Relações derivadas — verificar sempre o `.txt`._
