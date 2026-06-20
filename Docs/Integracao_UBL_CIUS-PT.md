# Faturação Eletrónica UBL 2.1 (CIUS-PT) — Referência

> Fonte: `Sage 100c Docs/Manuais/Sage_100c_UBL2.1(CIUS-PT).txt` (Sage, junho 2021).
> Spec técnica de implementação. Os elementos XML, identificadores (BT-…), valores fixos e
> mapeamentos para o 100c reproduzem o que consta na fonte. Onde a fonte é vaga, indica-se "ver fonte".

---

## 1. Visão geral

A Sage 100c disponibiliza a emissão do documento em formato **XML UBL 2.1**, segundo o
**modelo de dados semânticos CIUS-PT**, conforme definido pelo **eSPap**.

- **UBL 2.1** (*Universal Business Language*) — formato XML para documentos de negócio (faturas, notas de crédito, etc.).
- **CIUS-PT** — *Core Invoice Usage Specification* portuguesa: customização nacional da norma europeia **EN 16931** (norma semântica da faturação eletrónica). Cada campo semântico é identificado por um código **BT-n** (*Business Term*).
- **eSPap** — entidade que define a especificação CIUS-PT para Portugal (faturação eletrónica no setor público / B2G).

O identificador da customização é colocado em `cbc:CustomizationID` com o **valor fixo**:

```
urn:cen.eu:en16931:2017#compliant#urn:feap.gov.pt:CIUS-PT:2.0.0
```

Este valor permite ao recetor aplicar a validação do documento de acordo com as regras da customização CIUS-PT.

**Relação com a AT / SAF-T (PT).** O UBL CIUS-PT é um formato de *transmissão* do documento; não substitui o SAF-T. Contudo, o documento UBL transporta dados de certificação AT, exportados como **notas** no elemento `cbc:Note` (ver §4):

- Número de certificado AT: `#NUMBER@ATCERTIFIEDPROGRAM#2649/AT#`
- Chave do documento (Hash) do SAF-T (PT): `#HASHCODE@ATCERTIFIEDPROGRAM#<hashcode>#`

> Nota: o ficheiro UBL e o SAF-T (PT) são artefactos distintos — não confundir. O UBL é o documento individual estruturado segundo a EN 16931/CIUS-PT.

---

## 2. Documentos suportados

A fonte documenta dois tipos de documento UBL:

| Documento UBL | Elemento raiz | Código de tipo (BT-3) | Origem 100c |
|---|---|---|---|
| **Fatura** | `<Invoice>` | `380` Fatura · `383` Nota de débito · `FS` Fatura simplificada · `FR` Fatura-recibo | Tipos de documento de venda |
| **Nota de Crédito** | `<CreditNote>` | `381` (valor fixo) | Documento retificativo / devolução |

O código funcional vai em:

- **Fatura** → `cbc:InvoiceTypeCode` (BT-3): `380`, `383`, `FS` ou `FR`.
- **Nota de Crédito** → `cbc:CreditNoteTypeCode` (BT-3): valor fixo `381`.

> Nota da fonte: o exemplo XML da Nota de Crédito abre com `<Invoice ...>` no cabeçalho do manual, mas o elemento de fecho e a linha são `</CreditNote>` / `<cac:CreditNoteLine>`. Tratar a Nota de Crédito como documento `CreditNote`.

---

## 3. Estrutura do documento UBL

Namespaces declarados na raiz:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"
         xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
         xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2">
```

Convenção: `cbc:` = *Common Basic Components* (elementos simples); `cac:` = *Common Aggregate Components* (estruturas).

### 3.1 Cabeçalho do documento

| Elemento XML | BT | Descrição | Mapeamento 100c |
|---|---|---|---|
| `cbc:CustomizationID` | BT-24 | Nome da customização CIUS-PT | Valor fixo `urn:cen.eu:en16931:2017#compliant#urn:feap.gov.pt:CIUS-PT:2.0.0` |
| `cbc:ID` | BT-1 | Nº de referência do documento (emitido pelo fornecedor) | `<Ano> <Código Tipo documento> <Série>/<Número documento>` |
| `cbc:IssueDate` | BT-2 | Data de emissão | Data de emissão do documento |
| `cbc:DueDate` | BT-9 | Data de vencimento (só Fatura) | Data de vencimento do documento |
| `cbc:InvoiceTypeCode` | BT-3 | Tipo funcional (Fatura) | `380` / `383` / `FS` / `FR` |
| `cbc:CreditNoteTypeCode` | BT-3 | Tipo funcional (Nota de Crédito) | Valor fixo `381` |
| `cbc:Note` | BT-21 / BT-22 | Assunto / nota textual não estruturada | Notas AT exportadas (nº certificado, hash SAF-T) |
| `cbc:DocumentCurrencyCode` | BT-5 | Moeda do documento | Código ISO 4217 da moeda do documento |
| `cbc:AccountingCost` | BT-19 | Número do compromisso | Nº compromisso, separador *Fatura eletrónica* |
| `cbc:BuyerReference` | BT-10 | Referência do cliente | Código EDI definido no cliente (código EAN) |

### 3.2 Referências (encomenda, contrato, anexos, ATCUD, QR)

| Elemento XML | BT | Descrição | Mapeamento 100c |
|---|---|---|---|
| `cac:OrderReference / cbc:ID` | BT-13 | Nº da nota de encomenda | "Vosso Número" indicado no documento |
| `cac:ContractDocumentReference / cbc:ID` | BT-12 | Nº do contrato | Nº contrato, separador *Fatura eletrónica* |
| `cac:AdditionalDocumentReference / cbc:ID` | BT-18 / BT-122 | Identificador do processo de registo de entrada / anexo | `<Código tipo documento> <Série><Número>` |
| `cac:AdditionalDocumentReference / cbc:ID` | BT-18 | Nº Único do Documento (ATCUD) | Código único do documento (ATCUD). *"Enquanto não sair legislação sobre o tema, deverá ser colocado `0`."* |

**Anexos.** Há blocos `cac:AdditionalDocumentReference` para incorporar artefactos:

| Elemento XML | BT | Conteúdo | Valor / mapeamento |
|---|---|---|---|
| `cbc:DocumentDescription` | — | Descrição do anexo (QR Code) | Valor fixo `QR_CODE` |
| `cac:Attachment / cbc:EmbeddedDocumentBinaryObject` (`mimeCode`, `filename`) | — | Objeto binário | QRCODE em Base64 |
| `cbc:DocumentDescription` | BT-123 | Descrição do anexo (PDF) | Valor fixo `INVOICE_REPRESENTATION` (Fatura) / `CREDITNOTE_REPRESENTATION` (Nota de Crédito) |
| `cac:Attachment / cbc:EmbeddedDocumentBinaryObject` | BT-125 | Documento binário | Documento PDF |
| `cac:ExternalReference / cbc:URI` | BT-124 | Endereço para documento externo | Valor fixo `www.espap.gov.pt` |

### 3.3 Fornecedor — `cac:AccountingSupplierParty`

Os dados vêm da **Ficha de empresa** e dos **Parâmetros de aplicação**.

| Elemento XML | BT | Descrição | Mapeamento 100c |
|---|---|---|---|
| `cbc:EndpointID` (`schemeID`) | BT-34 | Endereço eletrónico do fornecedor | Email da empresa (Ficha de empresa) |
| `cac:PartyIdentification / cbc:ID` (`schemeID`) | BT-29 / BT-90 | Identificação do vendedor / ID bancário (credor) | Código EAN empresa (Parâmetros aplicação → Identificação) |
| `cac:PartyName / cbc:Name` | BT-28 | Nome comercial do fornecedor | Designação da empresa (Ficha → Identificação) |
| `cac:PostalAddress / cbc:StreetName` | BT-35 | Linha 1 da morada | Morada da empresa |
| `cbc:CityName` | BT-37 | Cidade | Localidade da empresa |
| `cbc:PostalZone` | BT-38 | Código postal | Código postal da empresa |
| `cbc:CountrySubentity` | BT-39 | Região/Província | Localidade da empresa |
| `cac:Country / cbc:IdentificationCode` | BT-40 | Código do país | Código país da empresa |
| `cac:PartyTaxScheme / cbc:CompanyID` | BT-31 | NIF do fornecedor | Prefixo código país + NIF da empresa |
| `cac:PartyTaxScheme / cac:TaxScheme / cbc:ID` | BT-32 | Esquema fiscal | Valor fixo `VAT` |
| `cac:PartyLegalEntity / cbc:RegistrationName` | BT-27 | Nome legal registado | Designação da empresa (Ficha → Identificação) |
| `cac:PartyLegalEntity / cbc:CompanyLegalForm` | BT-33 | Informação sobre o capital social | Capital social (Ficha → Dados fiscais) |

### 3.4 Cliente — `cac:AccountingCustomerParty`

Os dados vêm da **Ficha do cliente → Informação**.

| Elemento XML | BT | Descrição | Mapeamento 100c |
|---|---|---|---|
| `cbc:EndpointID` (`schemeID`) | BT-49 | Endereço eletrónico do cliente | Email do cliente |
| `cac:PartyIdentification / cbc:ID` | BT-46 | Identificador do cliente | Código EDI do cliente (código EAN) |
| `cac:PartyName / cbc:Name` | BT-45 | Nome comercial do cliente | Nome do cliente |
| `cac:PostalAddress / cbc:StreetName` | BT-50 | Linha 1 da morada | Morada do cliente |
| `cbc:AdditionalStreetName` | BT-51 | Linha 2 da morada | Morada 2 do cliente |
| `cbc:CityName` | BT-52 | Cidade | Localidade do cliente |
| `cbc:PostalZone` | BT-53 | Código postal | Código postal do cliente |
| `cbc:CountrySubentity` | BT-54 | Região/Província | Localidade do cliente |
| `cac:Country / cbc:IdentificationCode` | BT-55 | Código do país | Código país do cliente |
| `cac:PartyTaxScheme / cbc:CompanyID` | BT-48 | NIF do cliente | Prefixo código país + NIF do cliente |
| `cac:PartyTaxScheme / cac:TaxScheme / cbc:ID` | — | Esquema fiscal | Valor fixo `VAT` |
| `cac:PartyLegalEntity / cbc:RegistrationName` | BT-44 | Nome legal do cliente | Nome do cliente |

### 3.5 Entrega — `cac:Delivery`

| Elemento XML | BT | Descrição | Mapeamento 100c |
|---|---|---|---|
| `cbc:ActualDeliveryDate` | BT-72 | Data da entrega | Data de movimento das linhas |
| `cac:DeliveryLocation / cbc:ID` | BT-71 | Identificador do local de entrega | Código GLN do campo "Onde entregar a mercadoria" (separador *Informação do documento*) |
| `cac:Address / cbc:StreetName` | BT-75 | Linha 1 morada de entrega | Morada de descarga |
| `cbc:CityName` | BT-77 | Cidade da entrega | Localidade de descarga |
| `cbc:PostalZone` | BT-78 | Código postal da entrega | Código postal descarga |
| `cbc:CountrySubentity` | BT-79 | Região/Província | Localidade de descarga |
| `cac:Country / cbc:IdentificationCode` | BT-80 | Código do país | País descarga |

(Todos os campos de descarga ficam no separador *Informação do documento*.)

### 3.6 Meios de pagamento — `cac:PaymentMeans`

| Elemento XML | BT | Descrição | Mapeamento 100c |
|---|---|---|---|
| `cbc:PaymentMeansCode` (`name`) | BT-81 / BT-82 | Código do método de pagamento | Para meio de pagamento SAF-T "Transferência bancária ou débito direto autorizado": `TB` |
| `cac:PayeeFinancialAccount / cbc:ID` | BT-84 | Identificador do pagamento (IBAN) | IBAN da conta por omissão (Parâmetros aplicação → Bancos) |
| `cac:PayeeFinancialAccount / cbc:Name` | BT-85 | Identificação da conta | Nº da conta por omissão (Parâmetros aplicação → Bancos) |
| `cac:FinancialInstitutionBranch / cbc:ID` | BT-86 | Código da instituição bancária (SWIFT) | BIC da conta por omissão (Parâmetros aplicação → Bancos) |

### 3.7 Descontos/encargos de cabeçalho — `cac:AllowanceCharge`

`ChargeIndicator = false` → desconto; `= true` → encargo. Na Nota de Crédito este bloco surge apenas "caso tenha desconto cabeçalho".

| Elemento XML | BT (desc. / encargo) | Descrição | Valor / mapeamento 100c |
|---|---|---|---|
| `cbc:ChargeIndicator` | BT-… | Indicador desconto/encargo | Valor fixo `false` |
| `cbc:AllowanceChargeReasonCode` | BT-98 / BT-105 | Código do motivo | Valor fixo `95` |
| `cbc:AllowanceChargeReason` | BT-97 / BT-104 | Representação textual | Valor fixo `Desconto cabeçalho` |
| `cbc:MultiplierFactorNumeric` | BT-94 / BT-101 | Fator multiplicador sobre o montante base | Desconto cabeçalho do documento |
| `cbc:Amount` (`currencyID`) | BT-92 / BT-99 | Montante (sem impostos) | Valor do desconto de cabeçalho |
| `cbc:BaseAmount` (`currencyID`) | BT-93 / BT-100 | Montante base | Valor ilíquido do documento |
| `cac:TaxCategory / cbc:ID` | BT-95 / BT-102 | Código de imposto | `RED` / `INT` / `NOR` / `ISE` / `OUT` (ver §4) |
| `cac:TaxCategory / cbc:Percent` | BT-96 / BT-103 | Percentagem de imposto | Taxa de IVA |
| `cac:TaxScheme / cbc:ID` | — | Esquema fiscal | Valor fixo `VAT` |

### 3.8 Totais de imposto — `cac:TaxTotal`

| Elemento XML | BT | Descrição | Mapeamento 100c |
|---|---|---|---|
| `cbc:TaxAmount` (`currencyID`) | BT-110 / BT-111 | Total de imposto / total do IVA na moeda do fornecedor | Valor total do IVA |
| `cac:TaxSubtotal / cbc:TaxableAmount` | BT-116 | Montante base de incidência (por taxa) | Base de incidência (por taxa) |
| `cac:TaxSubtotal / cbc:TaxAmount` | BT-117 | Montante de imposto sobre a base | Valor do IVA (por taxa) |
| `cac:TaxCategory / cbc:ID` | BT-118 | Código de imposto do subtotal | `RED` / `INT` / `NOR` / `ISE` / `OUT` |
| `cac:TaxCategory / cbc:Percent` | BT-119 | Percentagem do subtotal | Taxa de IVA |
| `cbc:TaxExemptionReasonCode` | BT-121 | Código do motivo de isenção | Código do motivo de isenção da linha do artigo (se isento) |
| `cbc:TaxExemptionReason` | BT-120 | Descrição do motivo de isenção | Descrição do motivo de isenção da linha (se isento) |
| `cac:TaxScheme / cbc:ID` | — | Esquema fiscal | Valor fixo `VAT` |

### 3.9 Totais monetários — `cac:LegalMonetaryTotal`

| Elemento XML | BT | Descrição | Mapeamento / cálculo 100c |
|---|---|---|---|
| `cbc:LineExtensionAmount` | BT-106 | Soma das linhas (s/imposto) | `(Preço × Quantidade) − Valor desconto linha + Valor desconto cabeçalho` |
| `cbc:TaxExclusiveAmount` | BT-109 | Total do documento (s/imposto) | Valor base do documento |
| `cbc:TaxInclusiveAmount` | BT-112 | Total do documento (c/imposto) | Valor total do documento |
| `cbc:AllowanceTotalAmount` | BT-107 | Total de descontos do documento | Valor do desconto de cabeçalho |
| `cbc:PayableRoundingAmount` | BT-114 | Montante de arredondamento (c/imposto) | Valor do arredondamento |
| `cbc:PayableAmount` | BT-115 | Valor a pagar / montante ATM / montante DUC | Valor total do documento |

### 3.10 Linha do documento — `cac:InvoiceLine` / `cac:CreditNoteLine`

| Elemento XML | BT | Descrição | Mapeamento 100c |
|---|---|---|---|
| `cbc:ID` | BT-126 | Identificador único da linha | Número da linha do documento |
| `cbc:Note` | BT-127 | Texto livre do item | Descrição da linha do documento |
| `cbc:InvoicedQuantity` (`unitCode`) | BT-129 | Quantidade faturada | Quantidade da linha; `unitCode` = código ISO 16931 da unidade |
| `cbc:LineExtensionAmount` | BT-131 | Montante da linha (s/imposto, c/ desc./encargos) | `Preço Unitário × Quantidade − Desconto linha` |
| `cac:DocumentReference / cbc:ID` | BT-128 | Identificador do objeto base da linha | Documento original: `Ano / Código Tipo Documento / Série / Número` |

**Unidades (`unitCode`).** Para descritores usa a *Unidade Fatura Eletrónica* da tabela Descritores → Informação; para taxas adicionais usa a *Unidade* da tabela Taxas → Informação.

#### Desconto/encargo de linha — `cac:AllowanceCharge`

| Elemento XML | BT (desc. / encargo) | Descrição | Valor / mapeamento |
|---|---|---|---|
| `cbc:ChargeIndicator` | BT-140 / BT-145 | Indicador | Valor fixo `false` |
| `cbc:AllowanceChargeReasonCode` | BT-140 / BT-145 | Código do motivo | Valor fixo `95` |
| `cbc:AllowanceChargeReason` | BT-139 / BT-144 | Representação textual | Valor fixo `Desconto de linha` |
| `cbc:MultiplierFactorNumeric` | BT-138 / BT-143 | Fator multiplicador | Desconto linha do documento |
| `cbc:Amount` | BT-136 / BT-141 | Montante | Valor do desconto de linha |
| `cbc:BaseAmount` | BT-137 / BT-142 | Montante base | `Preço × Quantidade` |

#### Item — `cac:Item`

| Elemento XML | BT | Descrição | Mapeamento 100c |
|---|---|---|---|
| `cbc:Description` | BT-154 | Descrição do item | Descrição RTF |
| `cbc:Name` | BT-153 | Nome do item | Descrição da linha do documento |
| `cac:BuyersItemIdentification / cbc:ID` | BT-156 | Código de material no ERP | Campo "Sua Referência" (Ajuda à venda) ou código de barras ativo |
| `cac:SellersItemIdentification / cbc:ID` | BT-155 | Código do fornecedor (partner number) | Campo "Seu EAN" (Ajuda à venda) ou código de barras ativo |
| `cac:StandardItemIdentification / cbc:ID` (`schemeID`) | BT-157 | Identificador padrão (EAN) | Campo "Seu EAN" (Ajuda à venda) ou código de barras ativo |
| `cac:ClassifiedTaxCategory / cbc:ID` | BT-151 | Código de imposto do item | `RED` / `INT` / `NOR` / `ISE` / `OUT` |
| `cac:ClassifiedTaxCategory / cbc:Percent` | BT-152 | Percentagem de imposto do item | Taxa de IVA |
| `cac:ClassifiedTaxCategory / cac:TaxScheme / cbc:ID` | — | Esquema fiscal | Valor fixo `VAT` |
| `cac:AdditionalItemProperty / cbc:Name` | BT-160 | Tipo da propriedade adicional | Para IVA isenta: `#TAXEXEMPTIONREASONCODE@CLASSIFIEDTAXCATEGORY#` |
| `cac:AdditionalItemProperty / cbc:Value` | BT-161 | Valor da propriedade | Descrição do motivo de isenção da linha (se isento) |

> Na **Nota de Crédito** há um segundo `cac:AdditionalItemProperty` para indicar a fatura devolvida:
> `cbc:Name` = `#ID@INVOICEDOCUMENTREFERENCE@BILLINGREFERENCE-001#`,
> `cbc:Value` = `<Ano>/<Código documento>/<Série>/<Número>`.

#### Preço — `cac:Price`

| Elemento XML | BT | Descrição | Mapeamento 100c |
|---|---|---|---|
| `cbc:PriceAmount` (`currencyID`) | BT-146 | Montante do item após desconto | `Preço × Quantidade` |
| `cbc:BaseQuantity` (`unitCode`) | BT-149 | Quantidades que fazem o montante do preço | Quantidade unitária da linha (com fator); `unitCode` = ISO 16931 |
| `cac:AllowanceCharge / cbc:ChargeIndicator` | — | Indicador | Valor fixo `false` |
| `cac:AllowanceCharge / cbc:Amount` | BT-147 | Desconto sobre o preço do item | `0` |
| `cac:AllowanceCharge / cbc:BaseAmount` | BT-148 | Montante base do desconto | `Preço × Quantidade` |

---

## 4. Regras CIUS-PT

- **Identificador da customização** (`CustomizationID`, BT-24): valor fixo
  `urn:cen.eu:en16931:2017#compliant#urn:feap.gov.pt:CIUS-PT:2.0.0`.
- **Esquema fiscal** (`TaxScheme/ID`): sempre o valor fixo `VAT`.
- **NIF** (`PartyTaxScheme/CompanyID`, BT-31 fornecedor / BT-48 cliente): prefixo do código de país + NIF
  (ex.: `PT500000000`). O código de país do endpoint/identificação usa `schemeID`.
- **Códigos de categoria de imposto IVA** (BT-95/102/118/151): podem assumir
  `RED` (taxa reduzida), `INT` (taxa intermédia), `NOR` (taxa normal), `ISE` (isenta), `OUT` (outros).
- **Isenção de IVA**: quando a linha é isenta, preenche-se
  `TaxExemptionReasonCode` (BT-121) + `TaxExemptionReason` (BT-120) no subtotal,
  e replica-se em `AdditionalItemProperty` no item, com o código e a descrição do motivo de isenção da linha do artigo.
- **Código de tipo de documento** (BT-3): `380`/`383`/`FS`/`FR` na Fatura; `381` fixo na Nota de Crédito.
- **Motivo de desconto/encargo** (`AllowanceChargeReasonCode`): valor fixo `95`.
- **Meio de pagamento** (`PaymentMeansCode`, BT-81/82): `TB` para transferência bancária / débito direto autorizado (mapeamento do meio de pagamento SAF-T).
- **ATCUD** (BT-18): código único do documento. À data da fonte (jun-2021), *"enquanto não sair legislação sobre o tema, deverá ser colocado `0`."*
- **Unidades** (`unitCode`): código ISO 16931 — descritores usam a *Unidade Fatura Eletrónica* (tabela Descritores), taxas adicionais usam a *Unidade* (tabela Taxas).
- **Referência da fatura na Nota de Crédito**: `cac:BillingReference / cac:InvoiceDocumentReference / cbc:ID` =
  referência às faturas devolvidas `<Ano>/<Código documento><Série><Número>`; se não for devolução de faturas, usa o campo "Documento retificado" (separador *Informação documento*).
- **Anexos obrigatórios**: QR Code (`QR_CODE`, em Base64) e representação PDF (`INVOICE_REPRESENTATION` / `CREDITNOTE_REPRESENTATION`); referência externa fixa `www.espap.gov.pt`.

---

## 5. Geração / configuração no 100c

A maioria dos valores é alimentada por configuração existente; ao emitir o documento, o 100c monta o XML UBL a partir destes pontos:

| Bloco UBL | Onde se configura no 100c |
|---|---|
| Dados do fornecedor (nome, morada, NIF, capital social) | **Ficha de empresa** → Identificação / Dados fiscais |
| Código EAN da empresa | **Parâmetros de aplicação** → Identificação |
| IBAN / Nº conta / BIC | **Parâmetros de aplicação** → Bancos (conta por omissão da empresa) |
| Dados do cliente (nome, morada, NIF, email, EAN/EDI) | **Ficha do cliente** → Informação |
| Nº compromisso, nº contrato | Separador **Fatura eletrónica** do documento |
| Local/morada de entrega (GLN, descarga) | Separador **Informação do documento** |
| Documento retificado (Nota de Crédito) | Separador **Informação documento** |
| Unidade (fatura eletrónica) por descritor | Tabela **Descritores** → Informação |
| Unidade de taxas adicionais | Tabela **Taxas** → Informação |

> A fonte centra-se no **mapeamento de campos**. Os passos exatos de menu para ativar a emissão UBL,
> bem como o canal de envio (email / WebService / Saphety / eSPap), **não estão detalhados na fonte** —
> ver fonte / documentação de utilizador do 100c.

---

## 6. Notas de implementação / exemplos

### Raiz e identificadores fixos (Fatura)

```xml
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"
         xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
         xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2">
  <cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:feap.gov.pt:CIUS-PT:2.0.0</cbc:CustomizationID>
  <cbc:ID><!-- <Ano> <Código Tipo documento> <Série>/<Número> --></cbc:ID>
  <cbc:IssueDate>1111-11-11</cbc:IssueDate>
  <cbc:DueDate>1111-11-11</cbc:DueDate>
  <cbc:InvoiceTypeCode>380</cbc:InvoiceTypeCode>
  <cbc:DocumentCurrencyCode><!-- ISO 4217 --></cbc:DocumentCurrencyCode>
```

### Anexo QR Code e PDF (representação)

```xml
<cac:AdditionalDocumentReference>
  <cbc:ID><!-- <Código tipo documento> <Série><Número> --></cbc:ID>
  <cbc:DocumentDescription>QR_CODE</cbc:DocumentDescription>
  <cac:Attachment>
    <cbc:EmbeddedDocumentBinaryObject mimeCode="" filename=""><!-- QRCODE em Base64 --></cbc:EmbeddedDocumentBinaryObject>
  </cac:Attachment>
</cac:AdditionalDocumentReference>
<cac:AdditionalDocumentReference>
  <cbc:ID><!-- <Código tipo documento> <Série><Número> --></cbc:ID>
  <cbc:DocumentDescription>INVOICE_REPRESENTATION</cbc:DocumentDescription>  <!-- CREDITNOTE_REPRESENTATION na Nota de Crédito -->
  <cac:Attachment>
    <cbc:EmbeddedDocumentBinaryObject mimeCode="" filename=""><!-- PDF --></cbc:EmbeddedDocumentBinaryObject>
    <cac:ExternalReference>
      <cbc:URI>www.espap.gov.pt</cbc:URI>
    </cac:ExternalReference>
  </cac:Attachment>
</cac:AdditionalDocumentReference>
```

### Notas AT exportadas em `cbc:Note`

```
Número certificado AT: #NUMBER@ATCERTIFIEDPROGRAM#2649/AT#
Chave do documento (Hash) do SAF-T (PT): #HASHCODE@ATCERTIFIEDPROGRAM#<hashcode>#
```

### Subtotal de imposto com isenção

```xml
<cac:TaxSubtotal>
  <cbc:TaxableAmount currencyID="">0.0</cbc:TaxableAmount>
  <cbc:TaxAmount currencyID="">0.0</cbc:TaxAmount>
  <cac:TaxCategory>
    <cbc:ID>ISE</cbc:ID>
    <cbc:Percent>0.0</cbc:Percent>
    <cbc:TaxExemptionReasonCode><!-- código motivo isenção da linha --></cbc:TaxExemptionReasonCode>
    <cbc:TaxExemptionReason><!-- descrição motivo isenção --></cbc:TaxExemptionReason>
    <cac:TaxScheme><cbc:ID>VAT</cbc:ID></cac:TaxScheme>
  </cac:TaxCategory>
</cac:TaxSubtotal>
```

### Referência à fatura devolvida (Nota de Crédito)

```xml
<cac:BillingReference>
  <cac:InvoiceDocumentReference>
    <cbc:ID><!-- <Ano>/<Código documento><Série><Número> --></cbc:ID>
  </cac:InvoiceDocumentReference>
</cac:BillingReference>
```

### Listas de códigos (referência externa, EN 16931)

A fonte remete para o CEF Digital da Comissão Europeia:

- O que é o eInvoicing: `https://ec.europa.eu/cefdigital/wiki/display/CEFDIGITAL/What+is+eInvoicing`
- Listas de códigos completas usadas na EN 16931: `https://ec.europa.eu/cefdigital/wiki/display/CEFDIGITAL/Code+lists`
