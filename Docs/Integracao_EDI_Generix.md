# Integração EDI (GENERIX) — Estrutura de Ficheiros

> **Versão:** v.2020.001
> **Fonte:** `Sage 100c Docs/Manuais/Estrutura de Ficheiros Sage EDI.Generix.v.2020.001.txt`

Referência de implementação dos ficheiros EDI de largura fixa do Sage 100c (tradutor **GENERIX**).
Reproduz fielmente os layouts de campos (posições, comprimentos, formatos, observações) para quem
implementa a importação de encomendas e a exportação de documentos de venda.

---

## 1. Visão geral

| Ficheiro | Nome | Direção | Conteúdo |
|---|---|---|---|
| Encomendas | `Encomenda.TXT` | **Importação** (entrada no 100c) | Encomendas de clientes recebidas via EDI |
| Documentos de venda | `Factura.TXT` | **Exportação** (saída do 100c) | Faturas, Notas de Crédito e Guias de Remessa |

- **Tradutor:** GENERIX.
- **Formato:** texto de **largura fixa** (campos posicionais). A legenda das colunas posicionais é
  **I – Início do campo**, **C – Comprimento do campo**, **F – Fim do campo**.
- **Configuração na aplicação:** no manual da **Gestão (Comercial)** as ligações EDI configuram-se em
  **"EDI – Localizações"** e em **"Tradutores de EDI"**.

> Direção do fluxo de negócio: a encomenda EDI (`Encomenda.TXT`) é importada e gera encomendas no
> 100c ("Next"); dessas encomendas resultam documentos de venda que são exportados em `Factura.TXT`.

---

## 2. Ficheiro de importação (de encomendas) — `Encomenda.TXT`

### 2.1 Cabeçalho (1 linha única)

| Campo | Posição (I) | Comprimento (C) | Fim (F) | Formato / Valores | Observações |
|---|---|---|---|---|---|
| Tipo de registo | 1 | 1 | 1 | `"C"` (Cabeçalho) | |
| Número Encomenda | 2 | 15 | 16 | | Vosso Número de Encomenda |
| Documento O/D | 17 | 3 | 19 | 9=Original, 7=Duplicado | |
| Tipo Encomenda | 20 | 3 | 22 | 220=Normal | |
| Data Encomenda | 23 | 8 | 30 | (yyyymmdd) | |
| Hora Encomenda | 31 | 4 | 34 | (hhmm) | |
| Data Entrega | 35 | 8 | 42 | (yyyymmdd) | |
| Hora Entrega | 43 | 4 | 46 | (hhmm) | |
| Código Fornecedor | 47 | 20 | 66 | | Código EAN Interno do Fornecedor |
| Código Comprador | 67 | 15 | 81 | | Código EAN Interno do Cliente |
| Moeda do Documento | 82 | 5 | 86 | Sempre EUR=Euros | |
| Código Local Entrega | 87 | 20 | 106 | | Código EAN Local Entrega |
| Observações 1 | 107 | 70 | 176 | | |
| Observações 2 | 177 | 70 | 246 | | |
| Observações 3 | 247 | 70 | 316 | | |
| Departamento | 317 | 15 | 331 | | |
| Sucursal | 332 | 15 | 346 | | |

### 2.2 Detalhe (N linhas repetitivas)

| Campo | Posição (I) | Comprimento (C) | Fim (F) | Formato / Valores | Observações |
|---|---|---|---|---|---|
| Tipo de registo | 1 | 1 | 1 | `"D"` (Detalhe) | |
| Numero Linha | 2 | 6 | 7 (?) | | (?) — ver nota abaixo |
| Artigo Identificador artigo | 8 | 20 | 27 | | |
| Identificador artigo Fornecedor | 28 | 20 | 47 | | |
| Identificador artigo Comprador | 48 | 20 | 67 | | |
| Descrição do artigo | 68 | 35 | 102 | | |
| Quantidade Encomendada | 103 | 10 | 112 | | |
| Quantidade Gratuita | 113 | 10 | 122 | | |
| Data Entrega | 123 | 8 | 130 | (yyyymmdd) | |
| Hora Entrega | 131 | 4 | 134 | (hhmm) | |
| Preço Líquido Unitário | 135 | 15 | 149 | | |
| Preço Ilíquido Unitário | 150 | 15 | 164 | | |
| Preço/Unidade Medida | 165 | 15 | 179 | | Produtos Peso Variável |
| Unidade Medida | 180 | 3 | 182 | Exemplo: KGM=Quilograma | |
| Quantidade Embalagens | 183 | 10 | 192 | | |
| Quantidade Grátis | 193 | 10 | 202 | | |
| Tipo Embalagens | 203 | 10 | 212 | Exemplo: BX=Caixa | |
| Taxa IVA | 213 | 5 | 217 | | |
| Montante IVA | 218 | 15 | 232 | | |
| Montante IEC | 233 | 15 | 247 | | Produtos alcoólicos |
| Níveis Lastro | 248 | 10 | 257 | | |
| (campo final) | 258 | 10 | 267 | | (?) — o texto-fonte lista um par de posições `258 10 267` sem nome de campo explícito após "Níveis Lastro" |

> **Nota sobre o Detalhe da importação:** o texto extraído do PDF apresenta no início do bloco a
> sequência `1 1 1 "D" (detalhe) 267 8 20 27`. O valor `267` corresponde ao **Fim** total do registo
> (comprimento total da linha de detalhe = 267) e não a um campo; o primeiro campo de dados começa na
> posição 8 (Identificador artigo). A coluna **Numero Linha** (posições 2–7) está implícita entre o
> Tipo de registo (pos. 1) e o primeiro identificador (pos. 8); o seu comprimento exato (6) é
> deduzido das posições e está marcado com "(?)".

---

## 3. Ficheiro de exportação (de documentos de venda) — `Factura.TXT`

### 3.1 Cabeçalho (1 linha única)

| Campo | Posição (I) | Comprimento (C) | Fim (F) | Formato / Valores | Observações |
|---|---|---|---|---|---|
| Tipo de registo | 1 | 1 | 1 | `"C"` (Cabeçalho) | |
| Numero documento | 2 | 15 | 16 | | nota p) |
| Data Documento | 17 | 8 | 24 | (yyyymmdd) | |
| Tipo Documento | 25 | 3 | 27 | 380=Factura, 381=Nota de Crédito, 351=Guia de Remessa | nota a) |
| Tipo Documento Referido | 28 | 3 | 30 | ON, IV, DQ, DL | nota b) — Para a Encomenda |
| Número Doc. Referido | 31 | 15 | 45 | | nota c) — Para a Encomenda |
| Código EAN Fornecedor | 46 | 20 | 65 | | nota h) |
| Código EAN Local de Entrega | 66 | 20 | 85 | | nota l) |
| Código EAN Facturado | 86 | 20 | 105 | | nota m) |
| Código EAN Recebedor | 106 | 20 | 125 | | nota n) |
| Código EAN Comprador | 126 | 20 | 145 | | nota o) |
| Montante Documento | 146 | 15 | 160 | | nota d) |
| Montante Linhas Artigo | 161 | 15 | 175 | | nota e) |
| Montante Tributável | 176 | 15 | 190 | | nota f) |
| Montante Imposto | 191 | 15 | 205 | | nota g) |
| Montante Custo Embalagem | 206 | 15 | 220 | | |
| Moeda do Documento | 221 | 3 | 223 | Sempre EUR=Euros | |
| N.º Dias Vencimento | 224 | 3 | 226 | | |
| Data Vencimento | 227 | 8 | 234 | (yyyymmdd) | |
| N.º Dias Desconto Financeiro1 | 235 | 3 | 237 | | |
| Data Vencimento Desconto1 | 238 | 8 | 245 | (yyyymmdd) | |
| Percentagem Desconto 1 | 246 | 5 | 250 | | |
| Valor Desconto1 | 251 | 15 | 265 | | |
| N.º Dias Desconto Financeiro2 | 266 | 3 | 268 | | |
| Data Vencimento Desconto 2 | 269 | 8 | 276 | (yyyymmdd) | |
| Percentagem Desconto 2 | 277 | 5 | 281 | | |
| Valor Desconto2 | 282 | 15 | 296 | | |
| Tipo Documento Referido | 297 | 3 | 299 | DQ | nota j) — Para a Guia de Remessa |
| Número Doc. Referido | 300 | 15 | 314 | | nota k) — Para a Guia de Remessa |
| Data de Entrega da Mercadoria | 315 | 8 | 322 | (yyyymmdd) | nota i) |
| Nome do Cliente | 323 | 35 | 357 | | |
| Texto Livre 2 + Texto Livre 3 | 358 | 250 | 607 | | |
| Observações Fiscais | 608 | 70 | 677 | | Soma de 70 + 79 antigos |
| Departamento | 678 | 15 | 692 | | |
| Sucursal | 693 | 15 | 707 | | |
| Número Cabimento | 708 | 20 | 727 | | nota q) |
| Número Contrato | 728 | 20 | 747 | | |
| Número Compromisso | 748 | 20 | 767 | | |
| NIF Fornecedor/Empresa | 768 | 20 | 787 | | |
| Designação Fornecedor/Empresa | 788 | 80 | 867 | | |
| Morada Fornecedor/Empresa | 868 | 60 | 927 | | |
| Localidade Fornecedor/Empresa | 928 | 50 | 977 | | |
| Código Postal Fornecedor/Empresa | 978 | 8 | 985 | | |
| Capital Social Fornecedor/Empresa em Euros | 986 | 20 | 1005 | | |
| Registo Conservatória Fornecedor/Empresa | 1006 | 20 | 1025 | | |
| NIF comprador | 1026 | 20 | 1045 | | |
| Designação/Nome comprador | 1046 | 80 | 1125 | | |
| Morada comprador | 1126 | 60 | 1185 | | |
| Localidade comprador | 1186 | 50 | 1235 | | |
| Código Postal comprador | 1236 | 8 | 1243 | | |
| Hash | 1244 | 5 | 1248 | | |
| e-Mail Cliente | 1249 | 100 | 1348 | | Exclusivo formato MINSAIT |
| Nº Certificado Software | 1349 | 50 | 1398 | | |
| ATCUD | 1399 | 100 | 1498 | | nota q) |

#### Notas do Cabeçalho (exportação)

- **a)** 380=Factura, 381=Nota de Crédito, 351=Guia de Remessa. Deve poder exportar Facturas, Notas de Crédito e Guias de Remessa.
- **b)** ON=Nota de Encomenda, IV=Factura, DQ=Guia de Remessa, DL=Nota Débito. Neste caso será sempre o tipo de documento de Origem do EDI, ou seja "ON".
- **c)** Número do documento Referido de Origem, ó número da Encomenda do EDI que vem no Vosso Número de Documento.
- **d)** Montante do documento = Montante total da factura com imposto.
- **e)** Montante das linhas de artigo.
- **f)** Montante de incidência do IVA.
- **g)** Montante de imposto = Montante total do IVA + Montante total do IEC.
- **h)** Código Interno da Empresa, está definido como parâmetro no Responsável de Sistema.
- **i)** Data de Movimento da primeira linha do Documento contendo um Artigo (`DocGcLin.Data`).
- **j)** Sempre = DQ. Se o documento de Origem for uma guia de remessa.
- **k)** Núm. do Doc. de Origem da primeira linha do Documento contendo um Artigo (`DocGcLin.OrNum`). Se o documento de Origem for uma guia de remessa.
- **l)** Colocar código do Local de Entrega que vem no Cabeçalho da Encomenda do EDI ou, caso este esteja vazio, colocar o Código GLN da Morada de "Onde Enviar Mercadoria".
- **m)** Código GLN da Morada de "Onde Cobrar".
- **n)** Código GLN da Morada de "Onde Enviar Documento".
- **o)** Colocar código do Comprador que vem no Cabeçalho da Encomenda do EDI.
- **p)** Só número de documento, ou série + número de documento `SS-NNNNNNNNNNNNN`.
- **q)** Campos dependentes de licenciamento com Módulo "EP".

### 3.2 Detalhe (N linhas repetitivas)

| Campo | Posição (I) | Comprimento (C) | Fim (F) | Formato / Valores | Observações |
|---|---|---|---|---|---|
| Tipo de registo | 1 | 1 | 1 | `"D"` (Detalhe) | |
| Numero Linha | 2 | 6 | 7 | | (?) — ver nota abaixo |
| Código EAN do Artigo | 8 | 20 | 27 | | notas e) / x) |
| Identificador artigo Fornecedor | 28 | 20 | 47 | | notas h) / y) |
| Identificador artigo Comprador | 48 | 20 | 67 | | notas i) / z) |
| Descrição do artigo | 68 | 35 | 102 | | |
| Quantidade | 103 | 10 | 112 | | |
| Quantidade Grátis | 113 | 10 | 122 | | |
| Preço Líquido Unitário | 123 | 15 | 137 | | |
| Preço Ilíquido Unitário | 138 | 15 | 152 | | |
| Preço/Unidade Medida | 153 | 15 | 167 | | Produtos Peso Variável |
| Unidade Medida | 168 | 3 | 170 | KGM=Quilograma | |
| Montante Linha | 171 | 15 | 185 | | nota a) |
| Número Remessa | 186 | 15 | 200 | | nota f) |
| Quantidade Embalagens | 201 | 10 | 210 | | |
| Tipo Embalagens | 211 | 10 | 220 | | |
| Taxa IVA | 221 | 5 | 225 | | |
| Montante IVA | 226 | 15 | 240 | | |
| Tipo Imposto | 241 | 3 | 243 | IEC ou VAT (colocar sempre VAT) | nota d) |
| Montante IEC | 244 | 15 | 258 | | Produtos alcoólicos |
| Número do Lote | 259 | 10 | 268 | | nota b) |
| Data de Validade do Lote | 269 | 8 | 276 | (yyyymmdd) | nota c) |
| Pack Size | 277 | 10 | 286 | | nota g) |
| Motivo isenção imposto | 287 | 60 | 346 | | nota k1) |
| Código do motivo de isenção de imposto | 347 | 3 | 349 | | nota k2) |

> **Nota sobre o Detalhe da exportação:** tal como no detalhe da importação, o texto-fonte apresenta
> `1 1 1 "D" (Detalhe) 26 7 8 20 27`. O `26 7` (?) refere-se à coluna **Numero Linha**; o primeiro
> identificador de artigo começa na posição 8. O comprimento exato de "Numero Linha" está marcado
> com "(?)".

#### Notas do Detalhe (exportação)

- **a)** Montante de Linhas de artigo = Quantidade facturada × Preço líquido unitário.
- **b)** Número do Lote da primeira linha de lote do `Lotmovs`, respeitante a esta Linha.
- **c)** Data de Validade do Número de Lote da primeira linha de lote do `Lotmovs`, respeitante a esta Linha.
- **d)** Pode ser IEC ou VAT; no nosso caso colocar sempre **VAT**.
- **f)** Número da Guia de Remessa de Origem, se o doc. de Origem for Guia de Remessa.
- **g)** O pack size de momento será para gravar sempre com Valor a 1. Será, quando surgir a necessidade, a conversão da unidade que vai na encomenda para a unidade que vai na guia de remessa/factura. Exemplo: Encomenda 150 KGM a 1 Euro, Guia de Remessa 6 BX a 25 Euro; a Unidade de KGM = 1, a Unidade de BX = 25, logo o Pack Size = 25.

**Modos de identificação do artigo (colunas Código EAN / Identificadores):**

- **Modo 1**
  - **e)** 1.º Passo: colocar o EAN que veio na Encomenda. 2.º Passo: colocar o EAN do `AJUDAVND`. 3.º Passo: colocar o EAN da Tabela `CBARRAS`. Deve ser guardado no `DocGcLin` o EAN que foi importado via EDI, no campo Rubrica.
  - **h)** Igual ao Anterior.
  - **i)** Código do Artigo do Comprador. Referência do Comprador.
- **Modo 2**
  - **x)** Sempre o EAN 14 do artigo, que veio na Encomenda, do `AJUDAVND` ou do `CBARRAS`.
  - **y)** Sempre o EAN 13 do artigo, que veio na Encomenda, do `AJUDAVND` ou do `CBARRAS`.
  - **z)** Código do Artigo do Comprador. Referência do Comprador.
- **k)** Conforme Portaria n.º 302/2016, de 2 de dezembro.
  - **k1)** 4.1.4.19.16. TaxExemptionReason.
  - **k2)** 4.1.4.19.17. TaxExemptionCode.

### 3.3 Taxas (N linhas repetitivas — mínimo de 1 linha)

| Campo | Posição (I) | Comprimento (C) | Fim (F) | Formato / Valores | Observações |
|---|---|---|---|---|---|
| Tipo de registo | 1 | 1 | 1 | `"R"` | |
| Tipo Imposto | 2 | 3 | 4 | VAT=IVA, ACT=IEC | |
| Taxa IVA | 5 | 10 | 14 | | (?) — ver nota abaixo |
| Total Taxa IVA | 15 | 10 | 24 | | |
| Total Base Iva | 25 | 15 | 39 | | nota a) |

> **Nota sobre o registo "R" (Taxas):** o texto-fonte apresenta a sequência
> `1 1 1 "R" 2 3 4 VAT=IVA, ACT=IEC 559 10 15 24 25 15 39`. As posições estão baralhadas; a
> reconstrução acima assume Tipo Imposto (2–4), Taxa IVA (5–14), Total Taxa IVA (15–24) e
> Total Base Iva (25–39). Os comprimentos/posições das colunas "Taxa IVA" e "Total Taxa IVA"
> estão marcados com "(?)" por o token `559` no texto não ter posição clara.
>
> - **a)** Total da Mercadoria respeitante à taxa de IVA (`DocGcCab.BaseX`).

---

## 4. Exemplo Pack Size

Nos casos em que a Unidade da Factura é diferente da Unidade da Encomenda, devem ser divididas as
quantidades da Encomenda pelas quantidades da Venda; assim obtém-se o Pack Size.

### Exemplo 1

| | Quantidade | Unidade Base | Unidade Embalagem | Factor Embalagem | Unidade Venda | Preço |
|---|---|---|---|---|---|---|
| **Encomenda** | 150 | KGM | BX | 25 | KGM | 1 |
| **Factura** | 6 | KGM | BX | 25 | BX | 1 |

**Pack Size = 150 / 6 = 25**

### Exemplo 2

| | Quantidade | Unidade Base | Unidade Embalagem | Factor Embalagem | Unidade Venda | Preço |
|---|---|---|---|---|---|---|
| **Encomenda** | 150 | KGM | BX | 25 | KGM | 1 |
| **Factura** | 2 | BX | BX | 1 | BX | 75 |

**Pack Size = 150 / 2 = 75**

---

## 5. Outras informações

### O que vem nas Encomendas em Texto?

**Encomenda — Cabeçalho**

- **Código Fornecedor** — Código de quem fornece (de quem tem o Next). Este código é sempre em
  Formato EAN. É guardado nas Encomendas geradas no Next e transportado também para as facturas
  resultantes. Deve ser rigorosamente este o código a mencionar nas Facturas exportadas em
  "Código Fornecedor". Se este código não vier preenchido, é colocado em seu lugar o Código EDI
  do Next.win.
- **Código Cliente** — Código de quem compra. Pode ser o código interno do Next ou EAN. Se for o
  código interno do Next, grava este código no cabeçalho das encomendas geradas. Se for o EAN, é
  efectuada uma pesquisa no ficheiro de clientes pelo campo Código EDI; encontrado o cliente com
  este Código EDI, é gravado o código de cliente interno do Next no cabeçalho das encomendas geradas.

**Encomenda — Linhas**

- **Identificador Artigo** — Código de Artigo. Pode ser o código interno do Next ou EAN. Se for o
  código interno do Next, grava este código nas linhas das encomendas geradas. Se for o EAN, é
  efectuada uma pesquisa no ficheiro de Códigos de Barras; encontrado o artigo com este Código EAN,
  é gravado o código do artigo interno do Next nas linhas das encomendas geradas.

### O que vai nas Facturas em Texto?

**Facturas — Cabeçalho**

- **Identificação Fornecedor** — Código de quem fornece (de quem tem o Next). Este código é sempre
  em Formato EAN. É rigorosamente o que vem nas Encomendas importadas em "Código Fornecedor".
- **Código Cliente** — Código de quem compra. Este código é sempre em Formato EAN. É o Código EDI
  do cliente mencionado no cabeçalho das facturas. Se este código não vier preenchido, é colocado
  em seu lugar o Código EDI do Next.win.

**Facturas — Linhas**

- **Identificador Artigo** — Código de Artigo. Este código é sempre em formato EAN. É o código de
  barras referente aos artigos mencionado nas linhas da factura.

---

## 6. Notas de implementação

- **Largura fixa:** todos os campos são posicionais. Validar sempre `Início + Comprimento - 1 = Fim`.
  Preencher com espaços/zeros conforme o tipo (não há separadores entre campos).
- **Datas:** formato `yyyymmdd` (8 caracteres). Ex.: `20260620`.
- **Horas:** formato `hhmm` (4 caracteres). Ex.: `0930`.
- **Moeda:** sempre `EUR` (Euros). No cabeçalho de importação o campo tem 5 posições (87–91, comp. 5);
  no cabeçalho de exportação tem 3 posições (221–223, comp. 3).
- **Tipos de registo:** `"C"` = Cabeçalho, `"D"` = Detalhe (linhas de artigo), `"R"` = Taxas
  (apenas no ficheiro de exportação `Factura.TXT`).
- **Tipos de documento (exportação, pos. 25–27):** 380=Factura, 381=Nota de Crédito, 351=Guia de Remessa.
- **Tipo de documento referido (pos. 28–30):** ON=Nota de Encomenda, IV=Factura, DQ=Guia de Remessa,
  DL=Nota Débito (na origem EDI será sempre `ON`).
- **Tipo de imposto:** `VAT`=IVA, `ACT`/`IEC`=Imposto Especial de Consumo. No detalhe colocar sempre
  `VAT`; o IEC aplica-se a produtos alcoólicos (campo Montante IEC).
- **Códigos EAN / GLN:** os identificadores de empresa, cliente, fornecedor e locais de entrega são
  em formato EAN/GLN. Modo 1 vs. Modo 2 controla se se usa EAN genérico (cadeia de pesquisa
  Encomenda → `AJUDAVND` → `CBARRAS`) ou explicitamente EAN-14 / EAN-13 (ver notas e/h/i e x/y/z).
- **Unidades de medida:** ex. `KGM`=Quilograma; `BX`=Caixa (Tipo Embalagens). Produtos de peso
  variável usam o campo Preço/Unidade Medida.
- **Pack Size:** gravar sempre com valor `1` por defeito; só converter unidade encomenda → unidade
  guia/factura quando necessário (ver Exemplos Pack Size).
- **Campos dependentes de módulo/licenciamento:** Número Cabimento, ATCUD e afins dependem do módulo
  **"EP"** (nota q). O campo e-Mail Cliente (pos. 1249–1348) é exclusivo do formato **MINSAIT**.
- **Origem dos dados (exportação):** Data de Entrega = `DocGcLin.Data` da 1.ª linha com artigo;
  Número Doc. Referido (guia) = `DocGcLin.OrNum`; Total Base IVA = `DocGcCab.BaseX`; Lote e validade
  da 1.ª linha de `Lotmovs` da respetiva linha.
- **Configuração:** definir EDI – Localizações e Tradutores de EDI no módulo de Gestão.

> **Avisos de ambiguidade:** o texto-fonte foi extraído de PDF e algumas posições/comprimentos
> apareciam baralhados. Os valores reconstruídos por dedução (Numero Linha nos detalhes e as colunas
> intermédias do registo "R") estão marcados com "(?)" e devem ser confirmados contra um ficheiro
> real ou contra a especificação original em PDF antes de implementar.
