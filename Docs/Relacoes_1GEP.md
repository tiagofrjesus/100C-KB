# Relações entre Tabelas — 1GEP (Salários/RH)

> **Aviso:** o dicionário do Sage 100c **não tem foreign keys nativas**. As relações abaixo são
> **DERIVADAS** das chaves primárias e da presença de colunas com o mesmo significado.
> Confirma sempre os nomes **exatos** de coluna em `Sage 100c Docs/DD/1GEP/<TABELA>.txt`
> antes de escrever a query. Base de dados `<SIGLA>_1GEP`, schema `dbo`.
>
> Hub do funcionário: `FUNC1` (PK `NFUNC`). Recibo: `CABPROC` (PK `ANO+NFUNC+DATA+TPREC+NORDEMRE`).
> Histórico mensal: `LOGPROC` (PK `ANO+MES+NFUNC`). Códigos de remuneração: `ADF` (PK `COD`).

---

## 1. Funcionário e tabelas relacionadas

`FUNC1` (PK `NFUNC`, Text(10)) é o hub. **75 tabelas** referenciam o funcionário pela coluna
`NFUNC`. As mais relevantes (todas com `NFUNC` confirmado no índice invertido):

| Tabela | Conteúdo | Chave / nota |
|---|---|---|
| `CABPROC` | Cabeçalho de recibo | `NFUNC` (PK composta) |
| `LOGPROC` | Histórico de processamento (mensal) | PK `ANO+MES+NFUNC` |
| `MOV` / `MOV_DETALHE` | Movimentos do recibo | `NFUNC` |
| `ADFIX` | Valores fixos do funcionário | PK `NFUNC+CODABDES` |
| `ADDIA` | Abonos/descontos diários | PK `NFUNC+CODABDES` |
| `AGRFAM` | Agregado familiar | `NFUNC` |
| `PARAMSS` | Parâmetros Seg. Social | PK `NFUNC` (1:1) |
| `IRSDIF` | Diferenças de IRS | PK `NFUNC` (1:1) |
| `PERFER` | Períodos de férias | `NFUNC` |
| `HORPOR` | Horas para processamento | `NFUNC` |
| `LIGCONT` | Linhas de ligação à contabilidade | `NFUNC` |
| `HISTADM` / `HISTCES` / `HISTPRO` | Histórico admissões/cessações/promoções | `NFUNC` |
| `FUNCGA` / `FUNC_POR` | Func. CGA / Portal | PK `NFUNC` (1:1) |
| `SIMFUN` e família `SIM*` | Simulação | `NFUNC` |

Lista completa de famílias com `NFUNC`: medicina/risco/SHST (`ACTMED`, `HIGSEG`, `RISCO_*`,
`EXAMES_COMPLEMENTARES*`, `DOENCASPROFISSIONAIS`, `ACCOES_*`), formação (`FORPRO`), despesas
(`DESPESAS`, `PAGAMENTODESPESAS`), declarações (`LINM10`, `MAPASEGUROS`, `RELSS`, `RELPRO`,
`QPESS`), conta corrente (`PCCFAL`), expressões (`FUNXDEF`), entre outras.

```sql
-- Funcionário + recibo + histórico mensal
SELECT f.NFUNC, f.NOME, c.ANO, c.MES, c.TOTLIQ, l.VENCIM
FROM   DEMO_1GEP.dbo.FUNC1   f
JOIN   DEMO_1GEP.dbo.CABPROC c ON c.NFUNC = f.NFUNC
LEFT   JOIN DEMO_1GEP.dbo.LOGPROC l
       ON l.NFUNC = f.NFUNC AND l.ANO = c.ANO AND l.MES = c.MES;
```

---

## 2. Processamento de salários

**Recibo → movimentos.** `CABPROC` (PK `ANO+NFUNC+DATA+TPREC+NORDEMRE`) é o cabeçalho; as linhas
estão em `MOV` (PK `ANO+MES+TPREC+NORDEMRE+NFUNC+CDALT+ORIG`). Ligam-se por `NFUNC` + os campos
de recibo. **Atenção:** `CABPROC` tem `DATA`; `MOV` tem `ANO+MES`. O elo estável é
`NFUNC+ANO+TPREC+NORDEMRE` (`CABPROC.MES` existe no índice `COD2`).

```sql
-- Cabeçalho do recibo + linhas de movimento
SELECT c.NFUNC, c.ANO, c.MES, c.TPREC, c.NORDEMRE, m.CDALT, m.VALBRUT, m.VALLIQ
FROM   DEMO_1GEP.dbo.CABPROC c
JOIN   DEMO_1GEP.dbo.MOV     m
       ON m.NFUNC = c.NFUNC AND m.ANO = c.ANO AND m.MES = c.MES
      AND m.TPREC = c.TPREC AND m.NORDEMRE = c.NORDEMRE;
```

**Recibo → histórico mensal.** `LOGPROC` (PK `ANO+MES+NFUNC`) guarda o snapshot da ficha no mês
processado (1 registo por funcionário/mês). Liga a `CABPROC` por `NFUNC+ANO+MES`.

```sql
SELECT c.NFUNC, c.ANO, c.MES, c.TOTLIQ, l.VENCIM, l.TAXAIRS, l.SECTOR, l.CCUSTO
FROM   DEMO_1GEP.dbo.CABPROC c
JOIN   DEMO_1GEP.dbo.LOGPROC l
       ON l.NFUNC = c.NFUNC AND l.ANO = c.ANO AND l.MES = c.MES;
```

**Abonos/descontos (`ADF`).** `ADF` (PK `COD`, Text(10)) é a tabela mestra dos códigos de
remuneração. Entram no processamento pela coluna **`MOV.CDALT`** (Código Alteração = código de
remuneração), não por uma coluna chamada `COD`. Valores fixos do funcionário: `ADFIX.CODABDES` /
`ADDIA.CODABDES` → `ADF.COD`. Expressões: `ADFXDEF.ADF` → `ADF.COD`.

```sql
-- Linhas de movimento com a descrição do código de remuneração
SELECT m.NFUNC, m.CDALT, a.DESCR, a.TIPIFIC, m.VALBRUT
FROM   DEMO_1GEP.dbo.MOV m
JOIN   DEMO_1GEP.dbo.ADF a ON a.COD = m.CDALT;     -- ADF.COD = MOV.CDALT

-- Valores fixos do funcionário
SELECT x.NFUNC, x.CODABDES, a.DESCR, x.VALOR
FROM   DEMO_1GEP.dbo.ADFIX x
JOIN   DEMO_1GEP.dbo.ADF   a ON a.COD = x.CODABDES;
```

---

## 3. Tabelas de configuração

Ligam-se à ficha `FUNC1` (e ao snapshot `LOGPROC`) por colunas FK específicas — **não** assumir
nomes. Pares confirmados nos `.txt`:

| Conceito | Tabela mestra (PK) | FK em `FUNC1` | FK em `LOGPROC` |
|---|---|---|---|
| Segurança Social | `SEGSOC` (`COD`) | `CDSEGSOC` | `CDSEGSOG` ⚠️ (typo no schema) |
| Sindicato | `SINDIC` (`COD`) | `CDSINDIC` | `CDSINDIC` |
| Seguro | `SEGUROS` (`COD`) | `CDSEGURO` | `CDSEGURO` |
| Situação do funcionário | `SITFUNC` (`COD`) | `CDSITUAC` | `CDSITUAC` |
| Categoria profissional | `CATPRO` (`COD`) | `CDCATEG` | `CDCATEG` |
| Profissão | `PROF` (`COD`) | `CDPROFIS` | `CDPROFIS` |
| Horário | `DESHOR` (`COD`) | `CDHORA` | `CDHORA` |
| Subsídio de turno | `SUBTUR` (`COD`) | `SUBTURNO` | `SUBTURNO` |
| Centro de custo | `CCUST` (`COD`) | `CCUSTO` | `CCUSTO` |
| Setor | `SECTORES` (`COD`, Text(3)) | `SECTOR` | `SECTOR` |
| Departamento | `DEPARTAMENTOS` (`REFERENCE`) | `DEPARTAMENTO` | `DEPARTAMENTO` |
| Secção | `SECCOES` (`DEPARTAMENTO+REFERENCE`) | `DEPARTAMENTO`+`SECCAO` | `DEPARTAMENTO`+`SECCAO` |
| Estabelecimento | `ESTAB` (`COD`) | `ESTABEL` | `ESTABEL` |
| Tipo de contrato | `CONTR` (`COD`) | `TPCONTR` | `TPCONTR` |

```sql
-- Funcionário + Seg. Social + Sindicato + Setor
SELECT f.NFUNC, ss.DESCR AS segsoc, si.DESCR AS sindicato, se.DESCR AS setor
FROM   DEMO_1GEP.dbo.FUNC1    f
LEFT   JOIN DEMO_1GEP.dbo.SEGSOC   ss ON ss.COD = f.CDSEGSOC
LEFT   JOIN DEMO_1GEP.dbo.SINDIC   si ON si.COD = f.CDSINDIC
LEFT   JOIN DEMO_1GEP.dbo.SECTORES se ON se.COD = f.SECTOR;

-- Secção exige DEPARTAMENTO + REFERENCE (PK composta de SECCOES)
SELECT f.NFUNC, sc.NAME
FROM   DEMO_1GEP.dbo.FUNC1   f
JOIN   DEMO_1GEP.dbo.SECCOES sc
       ON sc.DEPARTAMENTO = f.DEPARTAMENTO AND sc.REFERENCE = f.SECCAO;
```

**Tabelas de IRS.** `TAB1`/`TAB7`/`TAB10` (PK `ANO+TAB+LIMSUP+DOMFIS+DATA`). Não há FK direta de
`FUNC1` para a tabela — a ligação faz-se por valor: `FUNC1.TABELAIRS` (qual tabela), `FUNC1.DOMFIS`
(domicílio fiscal) e o ano de processamento determinam que linhas se aplicam. Não é um JOIN 1:1
trivial; depende da lógica de escalões (`LIMSUP`). Confirmar campos no `.txt` antes de usar.

---

## 4. Ligação à contabilidade e bancos

**Contabilidade.** `LIGCONT` (PK `ANO+MES+ID`) tem `NFUNC`, `CONTA` (Text(15)), `SECTOR`,
`CCUSTO`, `RUB`. Liga o processamento de um funcionário num ano/mês às contas geradas. `LIGCONT2`
é a variante por documento. As contas patronais/encargos da Seg. Social vivem em `SEGSOC`
(`CNTSS`, `CNTSSEP`, `CONTA` IGFSS).

```sql
-- Movimentos de ligação à contabilidade de um funcionário/mês
SELECT l.NFUNC, l.ANO, l.MES, l.CONTA, l.SECTOR, l.CCUSTO, l.DEBCRE, l.VALOR
FROM   DEMO_1GEP.dbo.LIGCONT l
WHERE  l.NFUNC = '0001' AND l.ANO = 2026 AND l.MES = 6;
```

**Bancos.** Os dados bancários do funcionário estão **na própria `FUNC1`** (não em tabela-filho):
`BNCFUN` (banco, Text(4)), `BALFUN` (balcão), `NIBFUN`, `NRIBAN`, `NRSWIFT`. O banco resolve-se
contra `BANCOS` (PK `COD`, Text(4)). Há também colunas de despesas (`BANCO_DESPESAS`,
`BALCAO_DESPESAS`, `NIB_DESPESAS`) e cartão refeição (`BANCO_CR`).

```sql
SELECT f.NFUNC, f.NIBFUN, b.DESCR AS nome_banco
FROM   DEMO_1GEP.dbo.FUNC1  f
LEFT   JOIN DEMO_1GEP.dbo.BANCOS b ON b.COD = f.BNCFUN;
```

> Nota: pagamentos por transferência/cheque usam tabelas próprias (`TRANSF` PK `ORDEM`,
> `CHEQUES` PK `ORDEM`), ligadas ao recibo por `NFUNC`+`TPREC` (índice invertido). Confirmar no `.txt`.

---

## 5. Mapa de entidade → quem a referencia

### Funcionário (`FUNC1.NFUNC`)
Referenciado por **75 tabelas** via `NFUNC`. Núcleo: `CABPROC`, `LOGPROC`, `MOV`, `MOV_DETALHE`,
`ADFIX`, `ADDIA`, `AGRFAM`, `PARAMSS`, `IRSDIF`, `PERFER`, `HORPOR`, `LIGCONT`,
`HISTADM`/`HISTCES`/`HISTPRO`, `FUNCGA`, `FUNC_POR`, família `SIM*`, e todas as tabelas de
SHST/medicina/formação/despesas/declarações.

### Conta contabilística (coluna `CONTA`)
Referenciada por: `LIGCONT`, `CNTDES` (param. despesas), `SEGSOC`, `CABIND` (cab. interno).

### Setor (`SECTORES.COD`)
Referenciado por `SECTOR` em: `FUNC1`, `LOGPROC`, `LIGCONT`, `SIMFUN`, `PARAMAPL` (default).

### Secção (`SECCOES`, PK `DEPARTAMENTO+REFERENCE`)
Referenciada por `SECCAO`+`DEPARTAMENTO` em: `FUNC1`, `LOGPROC`, `SIMFUN`, `FINDEP`.

### Centro de custo (`CCUST.COD`)
Referenciado por `CCUSTO` em: `FUNC1`, `LOGPROC`, `LIGCONT`, `SIMFUN`. Rateio múltiplo: `MCCUST`.

### ⚠️ Falsos amigos (não são FK)
- **`DESCR`** — é sempre "Descrição" textual (`ADF`, `SEGSOC`, `SINDIC`, `SECTORES`, `CCUST`…),
  nunca uma chave estrangeira.
- **`COD`** — genérico: é a **PK da própria tabela** mestra. Para juntar ao funcionário usa-se a
  FK específica na `FUNC1` (`CDSEGSOC`, `CDSINDIC`, `SECTOR`, `CCUSTO`…), não um `COD` partilhado.
- **`CDALT`** (em `MOV`) — é o código de remuneração (`ADF.COD`), apesar do nome "Código Alteração".
- **`LOGPROC.CDSEGSOG`** — grafia divergente de `CDSEGSOC`; é o mesmo conceito (Seg. Social).
- **`ANO`/`MES`** — fazem parte de chaves compostas de processamento; sozinhos não identificam nada.
```