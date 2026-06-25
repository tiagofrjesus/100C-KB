# Sage 100c — queries e campos usados (POS Vesteherois)

Referência das tabelas, colunas e queries do Sage 100c usadas na migração do POS.
Serve de base para atualizar a skill `/sage100c`.

> Gerado a partir do esquema real das bases `VESTEHEROIS_POS` e `VESTEHEROIS_1GCO`
> (SQL Server 2022) e da análise do projeto Windev `M100C_POS_SQL`.

## Conexões

| Alias na app | Base de dados | Papel |
|---|---|---|
| `Pos` (`PosDbContext`) | **VESTEHEROIS_POS** | BD do POS: utilizadores, config (`NextPos_*`, `Setores_Series`), numeração (`D7_NumDoc`), staging, caixa. |
| `Sage` (`SageReadContext`, **só leitura**) | **VESTEHEROIS_1GCO** | Sage 100c Gestão Comercial: masters e documentos. |

A **escrita** no Sage nunca é feita por SQL/EF — é sempre pela **API REST `Sage100cAPI`** (ver secção final).
O `SageReadContext` só faz leituras.

## Convenções do Sage 100c

- **Booleanos** são `smallint` com valores **0 / -1** (estilo Windev). Na app: `coluna != 0`.
- **Chave dos masters** é `CODIGO` (`nvarchar`).
- **Escalões de preço** no artigo: `PVPSIVA/PVPCIVA` (PVP), `PVALSIVA/PVALCIVA` (PVAL), `PVP3_SEM_IVA/PVP3_COM_IVA` (PVP3) — sufixo `SIVA`/`SEM_IVA` = sem IVA, `CIVA`/`COM_IVA` = com IVA.
- `ARTIGOS.IVA` e `CLIENTES.REGIVA` referenciam o regime de IVA (`RGIVA`) — a taxa efetiva resolve-se aí (TODO na app).
- Documentos de gestão comercial: `DOCGCCAB` (cabeçalho) + `DOCGCLIN` (linhas), chave `TPDOC + SERIE + ANO + NNUMDOC (+ NUMLINHA)`.

---

## Queries implementadas (leitura)

### CLIENTES — pesquisa
**Repositório:** `ClientRepository.PesquisarAsync` · **Campos:** `CODIGO, NOME, NCONTRIB, LOCAL, INACTIVO`
```sql
SELECT TOP (@max) CODIGO, NOME, NCONTRIB, LOCAL
FROM CLIENTES
WHERE INACTIVO = 0
  AND (CODIGO LIKE @f+'%' OR NOME LIKE '%'+@f+'%' OR NCONTRIB LIKE @f+'%')
ORDER BY NOME;
```

### CLIENTES — detalhe
**Repositório:** `ClientRepository.ObterAsync` · **Campos:** `CODIGO, NOME, NCONTRIB, MORADA, MORADA2, LOCAL, CDPOSTAL, PAIS, TELEF, EMAIL, TPPRECO, REGIVA, DESCCAB, MOEDA, PASSIVO, IVAINC, INACTIVO`
```sql
SELECT CODIGO, NOME, NCONTRIB, MORADA, MORADA2, LOCAL, CDPOSTAL, PAIS, TELEF, EMAIL,
       TPPRECO, REGIVA, DESCCAB, MOEDA, PASSIVO, IVAINC, INACTIVO
FROM CLIENTES WHERE CODIGO = @codigo;
```
- `TPPRECO` → escalão de preço (mapeamento para PVP/PVAL/PVP3 a confirmar).
- `DESCCAB` → desconto de cabeçalho (%). `PASSIVO`/`IVAINC` → flags (smallint).

### ARTIGOS — pesquisa
**Repositório:** `ArticleRepository.PesquisarAsync` · **Campos:** `CODIGO, NOME, CODBARRA, FAMILIA, PVPCIVA, STDISP, INACTIVO`
```sql
SELECT TOP (@max) CODIGO, NOME, CODBARRA, FAMILIA, PVPCIVA, STDISP
FROM ARTIGOS
WHERE INACTIVO = 0
  AND (CODIGO LIKE @f+'%' OR NOME LIKE '%'+@f+'%' OR CODBARRA = @f)
ORDER BY NOME;
```

### ARTIGOS — info de linha + preços
**Repositório:** `ArticleRepository.ObterInfoAsync` / `ObterPrecosAsync`
**Campos:** `CODIGO, NOME, UNBASE, IVA, CODREF, ARTASSOC, TCOMPOSI, VLREXIST, STDISP, PVPSIVA, PVPCIVA, PVALSIVA, PVALCIVA, PVP3_SEM_IVA, PVP3_COM_IVA`
```sql
SELECT CODIGO, NOME, UNBASE, IVA, CODREF, ARTASSOC, TCOMPOSI, VLREXIST, STDISP,
       PVPSIVA, PVPCIVA, PVALSIVA, PVALCIVA, PVP3_SEM_IVA, PVP3_COM_IVA
FROM ARTIGOS WHERE CODIGO = @codigo;
```
- `CODREF` = SKU pai (agrupa variantes tamanho×cor). `TCOMPOSI != 0` = artigo composto.
- `STDISP` = stock disponível, `VLREXIST` = existências. `UNBASE` = unidade base.

### TPDOC — tipos de documento
**Repositório:** `CatalogRepository.TiposDocumentoAsync` · **Campos:** `CODIGO, DESCR, SINALCT, TPDSAFT, CREDITO`
```sql
SELECT CODIGO, DESCR, SINALCT, TPDSAFT, CREDITO FROM TPDOC ORDER BY CODIGO;
```
- `SINALCT` (1=débito/2=crédito), `TPDSAFT` (tipo SAF-T; 66 = fatura simplificada), `CREDITO` (flag NC).

### SECTORES
**Repositório:** `CatalogRepository.SectoresAsync` · **Campos:** `CODIGO, DESCR, ARMAZEM, IVAINC`
```sql
SELECT CODIGO, DESCR, ARMAZEM, IVAINC FROM SECTORES ORDER BY CODIGO;
```
- `ARMAZEM` = armazém por defeito do setor. `IVAINC` = preços com IVA incluído (lojas).

### ARMAZENS
**Repositório:** `CatalogRepository.ArmazensAsync` · **Campos:** `CODIGO, NOME, INACTIVO`
```sql
SELECT CODIGO, NOME FROM ARMAZENS WHERE INACTIVO = 0 ORDER BY CODIGO;
```

---

## Tabelas de apoio (VESTEHEROIS_POS, não Sage)

| Tabela | Campos usados | Uso |
|---|---|---|
| `Utilizadores` | `UtilizadoresID, Nome, PassWord, NomeC, Email, Administrador` | Login (password em texto simples — `varchar(10)`). |
| `Setores_Series` | `SECTOR, SERIE, Serie_Orc, Serie_Enc, Serie_Tra` | Série de faturação por setor. |
| `D7_NumDoc` | `Doc, Serie, Ano, NumDoc` | Próximo número (`MAX(NumDoc)+1`). |
| `NextPos_Conf1/2` | (a usar) | Config por utilizador: setor, desconto máx., docs permitidos por origem. |
| `MG_MODLIQ(_SECTOR)` | (a usar) | Meios de liquidação 1–9 → código Sage (`Sage_ML`) por setor. |

---

## Inventário de colunas (referência para a skill)

### CLIENTES (campos relevantes)
`CODIGO(15), NUMERO, NOME(80), CONTACTO, MORADA(50), MORADA2(50), LOCAL(35), CDPOSTAL(8), TELEF(15),`
`NCONTRIB(20), TPPRECO(smallint), REGIVA(3), DESCCAB(decimal), REGVCT, MODOPGT, VENDEDOR(10), EXPEDIR,`
`PLAFOND, MOEDA(3), PAIS(3), PASSIVO(smallint), INACTIVO(smallint), IVAINC(smallint), EMAIL(500),`
`SUJEITO_FATURASIMPLIFICADA, REGIME_IVA_CAIXA, CTRLDT, DIASTOL, CTRLPLF, ALTMOR, ZONAGEO, IDIOMA`

### ARTIGOS (campos relevantes)
`CODIGO(15), CODBARRA(18), NOME(80), IVA(smallint), VLREXIST(decimal), STDISP(decimal), FORNEC, UNIDADEV,`
`UNBASE(3), FAMILIA(6), SUBFAMIL, GRUPO, CTRSTOCK, PVPCIVA, PVPSIVA, PVALSIVA, PVALCIVA,`
`PVP3_SEM_IVA, PVP3_COM_IVA, PCMPCIVA, PCMPSIVA, CODREF(15), ARTASSOC(15), ARTSUBST, TCOMPOSI(smallint),`
`INACTIVO(smallint), STRESOBR, STRESENC, TIPO_PRECO, E_LOTE, E_NUMERO_SERIE, CONTROLO_NUMSERIE`

### TPDOC (campos relevantes)
`CODIGO(3), DESCR(50), DIARIO, AREAG, TPOPER, ENTIDADE, NATCONTA, SINALCT(smallint), CREDITO(smallint),`
`TPMOVIVA, RESVSTCK, SUGRESV, TPDSAFT(smallint), DESCONTO_BASE, OBRIGA_CONTRIBUINTE, ANEXO_40, ANEXO_41,`
`DOCUMENTO_RECTIFICATIVO, ADIANTAMENTO_*, NRVIAS_MODELO_1..4`

### SECTORES
`CODIGO(3), DESCR(50), ARMAZEM(6), RESP, CCUSTO, CNTCAIXA, IVAINC(smallint), APLICIVA, CODENQ, PAIS`

### ARMAZENS
`CODIGO(6), NOME(80), MORADA, LOCALIDA, CODPOST, INACTIVO(smallint), TIPO, PAIS`

### DOCGCCAB / DOCGCLIN (documentos — leitura/escrita futura)
- **DOCGCCAB:** `TPDOC, SERIE, ANO, NNUMDOC, DATADOC, NCONTRIB, TERCEIRO, NOME, TOTDOC, TOTMERC, TOTIVA,`
  `DESCCAB, MOEDA, RGIVA, VENDEDOR, AREAG, NATCONTA, CONVERT, **HASHSIGN, HASHCERTIFICATE, QRCODE, ATCUD**`
  (os 4 últimos = artefactos de **certificação**, preenchidos pelo Sage; o POS apenas lê).
- **DOCGCLIN:** `TPDOC, SERIE, ANO, NNUMDOC, NUMLINHA, ARTIGO, DESCR, ARMAZEM, QUANT, PRUNIT, DESCONTO,`
  `IVA, VALOR, MOVSTC (2=saída/venda, 1=entrada/devolução), LINANU (0=ativa), UNIDADE`
- **ArtArm** (existências por artigo/armazém): `ARTIGO, ARMAZEM, EXISTENC`

---

## API REST Sage 100c (caminho de ESCRITA — `Sage100cAPI`)

Endpoint + Token vêm da tabela `ConfigAPI`. Operações (porte do WIN_Fat2017):

| Operação | Quando | Resultado |
|---|---|---|
| `CalcularValoresDoc()` | Após cada mutação de linha (doc não finalizado) | Totais e IVA (`STDocValores`). |
| `InserirDocComercial()` | Finalizar venda | Cria **e certifica** o documento; devolve TPDOC/Nº/Série/Ano. |
| `InserirDocFinanceiro()` | Recibos (FFA / recebimentos) | Documento financeiro (conta-corrente). |
| `AnularDocComercial()` | Anular (motivo obrigatório) | Anula no Sage. |
| `ExtendDOCGCCAB()` | Após criar | Liga processo/dados extra ao cabeçalho. |

A **numeração** e a **certificação** (HASHSIGN/HASHCERTIFICATE/QRCODE/ATCUD) são da responsabilidade do Sage —
o POS nunca calcula hash nem atribui número final.
