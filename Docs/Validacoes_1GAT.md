# Validacoes 1GAT (Sage Gestao de Ativos)
> Regras de validacao de campos. 'Tabela Interna' -> lookup noutra tabela; fixas -> lista de valores. Equivalente aos local menus do X3.

Total: 105 validacoes.

| Codigo | Descricao | Tipo | Tabela alvo |
|---|---|---|---|
| ACC | Tipo de Acção | Tabela Interna | TPACCAO |
| ACT | Tabela de Actualizaç | Tabela Interna | CORRE |
| ACTIVOS | Activos | Tabela de Aplicação | ACTIVOS |
| ANO | Aceita Ano | Numérica |  |
| ANUMEN | Anual / Mensal | Tabela Interna | ANUALMENSAL |
| ATIVOS_LISTA | Ativos (lista) | Tabela de Aplicação | ACTIVOS |
| CALC | Tipo de Calculo | Tabela Interna | TPCALCUL |
| CAMPOS_ATIVOS | Campos ficha ativos | Numérica |  |
| CENTROCUSTO | Centros de Custo | Tabela Interna | CENTRO_CUSTO |
| CENTROCUSTO2 | Centros de Custo 2 | Tabela de Aplicação | CENCU |
| CENTROCUSTO3 | Centros de Custo 3 | Tabela de Aplicação | CENCU |
| CENTROCUSTO_ACT1 | Centros de Custo Activos 1 | Tabela de Aplicação | CENCU1 |
| CENTROCUSTO_ACT2 | Centros de Custo Activos 2 | Tabela de Aplicação | CENCU2 |
| CENTROCUSTO_ACT3 | Centros de Custo Activos 3 | Tabela de Aplicação | CENCU3 |
| CENTROCUSTO_ACT4 | Centros de Custo Activos 4 | Tabela de Aplicação | CENCU4 |
| CLAS | Tabela de Classifica | Tabela de Aplicação | TPIMO |
| CLASS_POC | Classificações POC | Tabela de Aplicação | CLASSI |
| CLIENTE | Cliente Comprador | Tabela de Aplicação | CLIENT |
| CMB | Combo | Tabela de Aplicação | PARAMA |
| CNT | Plano Contas | Tabela de Aplicação | DESC02 |
| CORR | Correcção Automática | Tabela de Aplicação | CORREC |
| CPO | Codigo Postal | Tabela de Aplicação | CODPOS |
| CTAB | Codigo de Tabela | Tabela de Aplicação | CODIGO |
| DC | Débito ou Crédito | Tabela Interna | DC |
| DEC | Decretos | Tabela de Aplicação | TABELA |
| DEC_SNC | Decretos SNC | Tabela de Aplicação | DECRETOS |
| DIG4 | 4 Inteiros | Numérica |  |
| DMA | Data Formato dd-mm-a | Data |  |
| EAN | Exercicios Anos | Tabela Interna | ANOEX |
| ESP | Utilidade Esperada | Tabela Interna | UTESP |
| ESQUECIMENTO | Esquecimento | Tabela Interna | ESQUECIMENTO |
| ESTA | Estado do Activo | Tabela Interna | ESTACT |
| ESTAB | Estabelecimento | Tabela de Aplicação | ESTAB |
| EXER | Exercícios | Tabela de Aplicação | EXERC |
| FCN | Forn Cod/Num | Tabela de Aplicação | FORNEC |
| FOR | Ficha de Fornecedor | Tabela de Aplicação | FORNEC |
| FOR1 | Fornecedor Lista | Tabela de Aplicação | FORNEC |
| GRAC | Grupo Activos | Tabela de Aplicação | GRPACT |
| GRAC2 | Grupo Activos para Assistente Reclassificação | Tabela de Aplicação | GRPACT |
| GRAC3 | Grupo Activos | Tabela de Aplicação | GRPACT |
| GRPH | Grupo Homogeneo | Tabela de Aplicação | GRPHOM |
| IMO | Ficha de Imobilizado | Tabela de Aplicação | FICHA |
| IMP_GA_AQUISICAO | Importação da aquisição da GA | Tabela Interna | IMP_GA_AQUIS |
| IMP_GA_FICHAS | Importação de valores das Fichas na GA | Tabela Interna | IMP_GA_FICHA |
| INT3 | Inteiro ( 1 a 999) | Numérica |  |
| INT32500 | Inteiro até 32500 | Numérica |  |
| INT99999 | Inteiro até 99999 | Numérica |  |
| IV2 | Taxa de Iva | Tabela de Aplicação | TABE03 |
| IVA | Tabela de Iva | Tabela de Aplicação | TABE03 |
| LOC | Tabela de localizaçõ | Tabela de Aplicação | LOCALI |
| LOCALIZACOES | Localizações | Tabela de Aplicação | LOCAIS |
| MENSURACAO | Modelo de Mensuração | Tabela Interna | MODELO_MENSURACAO |
| METO | metodo | Tabela Interna | METODO |
| METODO_DEPRECIACOES_ACUMULADAS | Métod de cálculo das depreciações acumuladas | Tabela Interna | METODO_DEPRECIACOES_ACUMULADAS |
| MOD | tabela de modos | Tabela Interna | MODOOPER |
| MODM | Modelo mensuração | Tabela Interna | MODMENS |
| MOED | tabela de moedas | Tabela de Aplicação | MOEDAS |
| N32 | Método de Cálculo | Tabela Interna | METCAL |
| N36 | Formato de Ligação | Tabela Interna | FORMATO |
| N37 | Tipo de Ligação | Tabela Interna | LIGAÇÃO |
| N41 | Maior que zero | Numérica |  |
| N44 | contas sem validação | Alfanumérica |  |
| N45 | Cod Tabela em Combo | Tabela de Aplicação | CODIGO |
| N48 | Departamentos | Tabela de Aplicação | DEPART |
| N49 | Utilizadores | Tabela de Aplicação | UTILIZ |
| N51 | Num Elementos | Numérica |  |
| N52 | Num Copias | Numérica |  |
| NI | Numerico inteiro | Numérica |  |
| NOV | Novo ou Usado | Tabela Interna | NOVOUSA |
| OES | Observações especiai | Tabela de Aplicação | DESC01 |
| ORG | Grande Grupo | Tabela de Aplicação | DESCRI |
| P4 | percentagem 6 decima | Numérica |  |
| PER | Percentagem | Numérica |  |
| PERCENT4DEC | Percentagem 4 décimais | Numérica |  |
| PORTDM | Portaria Coeficientes | Tabela de Aplicação | PORTDM |
| RAM | Ramo de Seguro | Tabela Interna | RAMOS |
| REG | regime | Tabela Interna | REGIME |
| REI | reinvestimento | Tabela Interna | REINVEST |
| RESP | Responsáveis | Tabela de Aplicação | RESPO |
| RUB | Rubricas | Tabela de Aplicação | RUBRIC |
| S/N | Sim ou Não | Sim/Não |  |
| SEC | Sectores | Tabela de Aplicação | TABE02 |
| SECCOES | Secções | Tabela de Aplicação | SECCAO |
| SEDE | Sede | Tabela Interna | SEDE |
| SEM | Ajustes fiscais | Tabela de Aplicação | AJUSTE |
| SIMMETODO | Simulação - Método | Tabela Interna | SIMMETODO |
| SIMTX | Simulação - Tipo de taxa | Tabela Interna | SIMTX |
| SIMU | Tipo Simulação | Tabela Interna | TPSIMULA |
| SN | S/N Tabela | Tabela Interna | SN |
| SNCM | Código do Movimento | Tabela Interna | MOVIMENT |
| SNC_POC | SNC ou POC | Tabela Interna | SNC_POC |
| SO1 | So aceita digito 1 | Numérica |  |
| TAB | Tipo de Abate | Tabela Interna | ABATES |
| TAJ | Tipo de Ajuste | Tabela Interna | TIPOAJUS |
| TAX | Indicador de taxa | Tabela Interna | IDTX |
| TIMO | Tipo de Imobilizado | Tabela Interna | IMOBILIZ |
| TIPO_BEM | Tipos de Bens | Tabela de Aplicação | TBEM |
| TIPO_IMPU | Tipo de Imputação | Tabela Interna | TIPO_IMPUTACAO |
| TPAC | Tipos de Activos | Tabela Interna | TPACTIVO |
| TPOP | Tipo Operação | Tabela Interna | TPOPER |
| TPTE | Tipo de Terceiro | Tabela Interna | TPTERC |
| V20 | Naturezas jurídicas | Tabela de Aplicação | NATJUR |
| V92 | Codigo de Tabela | Alfanumérica |  |
| VALOR2DEC | Valor 2 Decimais | Numérica |  |
| VALOR3DEC | Valor 3 Decimais | Numérica |  |
