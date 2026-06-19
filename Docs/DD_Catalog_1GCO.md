# Dicionario de Dados 1GCO (Sage Gestao Empresarial / Comercial) — Catalogo de Tabelas
> Versão 3234. Uma linha por tabela de aplicacao. Faz grep por nome ou descricao.
> Schema completo (colunas, tipos, chaves): `Sage 100c Docs/DD/1GCO/<TABELA>.txt`

Total: 403 tabelas de aplicacao.

| Tabela | Descricao | Cols | Chave Primaria |
|---|---|---|---|
| ACARTANO | Acumul. Artigo Ano | 10 | ARTIGO+ANO+CODEST+ARMAZEM |
| ACARTMES | Acumul. Artigo Mês | 11 | ARTIGO+ANO+MES+ESTATIST+ARMAZEM |
| ACFLUX | Acumulados Fluxos | 9 | ANO+MES+STATUS+CODFLUX+CODBNC+CONTA |
| ACGES | Acumulados Gestão | 11 | ANO+MES+STATUS+SECTOR+RUB+CCUS+CUSTEIO+CONTA |
| ACIVA | Acumulados IVA | 12 | ANO+MES+STATUS+CONTA+CODIVA+TPIVA+TPTERC+TERC+NCONT |
| ACPIVA | Ac. Plano IVA | 5 | ANO+MES+CODIVA |
| ACPOCSEC | Acumulados POC por sector | 11 | ANO+MES+STATAC+NAT+CONTA |
| ACTERLIN | Acumulados Terceiros Lin | 17 | TPTERC+ANO+TERCEIRO+ARGEST+TPOPER+MES |
| ACTIVIDADE | Actividades | 3 | CODIGO |
| ACUMFAM | Acumulados Familia | 8 | ANO+MES+GRUPO+FAMILIA |
| ACUMGRP | Acumulados Grupo | 7 | ANO+MES+GRUPO |
| ACUMPOC | Acumulados POC | 10 | ANO+MES+STATAC+NAT+CONTA |
| ACUMPOCCL9 | Acumulados POC Classe 9 | 9 | ANO+MES+STATAC+NAT+CONTA |
| ACUMPOCTODAS | Acumulados Contas (Todas as contas) | 10 | ANO+MES+STATAC+NAT+CONTA |
| ACUMPOC_CACHE | Acumulados POC (Cache) | 10 | EXERCICIO+ANO+MES+STATAC+NAT+CONTA |
| ACUMPREV | Acumulados prevision | 9 | ARTIGO+ANO |
| ACUMSUBF | Acumulados SubFamili | 9 | ANO+MES+GRUPO+FAMILIA+SUBFAMIL |
| ACUMTERC | Acumulados Terceiros | 17 | TPTERC+ANO+TERCEIRO+ARGEST+TPOPER+MES |
| ACUMULADOS_TERCEIRO_ARTIGOS | Acumulados por terceiro e artigos | 12 | TPTERC+TERCEIRO+ANO+MES+ARTIGO |
| ACUMVEND | Acumulado Vendedores | 9 | ANO+VENDEDOR+MES |
| AEXECUTA | Produção a Executar | 14 | PROCESSO+ARTIGO+TIPODOC+ANO+NUMDOC+SERIE+OPERACAO+FACTOR+CCOMPOST+DATAENTR |
| AJUDACMP | Ajuda à Compra | 21 | ARTIGO+FORNECED |
| AJUDAVND | Ajuda à Venda | 11 | ARTIGO+CLIENTE |
| ANEXOIVA | Anexo I perio. iva | 7 | ANO+MES+NIF+TPOPER |
| ANEXOS | Anexos | 8 | COD_ORC+COD_FASE+URL |
| APCAB | Apuramentos Cab | 4 | CODAP+TIPO_PLANO |
| APLIN | Apuramentos Linhas | 6 | CODAP+TIPO_PLANO |
| ARMAZEM_OBRA | Reservas de obra por armazém | 4 | ARTIGO+ARMAZEM+OBRA |
| ARMAZENS | Armazens | 19 | CODIGO |
| ARTARM | Artigos por Armazém | 31 | ARTIGO+ARMAZEM |
| ARTCT | Artigos CT | 2 | SIGLA |
| ARTIDIOM | Artigo por Idiomas | 4 | ARTIGO+IDIOMA |
| ARTIGOS | Artigos | 150 | CODIGO |
| ARTIGOS_IVA | Historico de tipos de IVA | 4 | ARTIGO+TIPO_IVA+DATA_LIMITE |
| ARTLOT | Artigos Lotes | 15 | ARTIGO+CODLOTE+ARMAZEM+VOSSLOTE |
| ARTOPERA | Operações por Artigo | 6 | ARTIGO+OPERACAO+SEQ |
| AUDCNT | Notas Conta | 4 | ANO+MES+CONTA |
| AUDDOC | Auditoria Doc | 6 | ANO+TPDOC+SERIE+NDOC+NLIN |
| AUTOS | Autos | 25 | COD_ORC+TIPO_AUTO+ORC_SE+AUTO+NOME |
| AUTOS_CONTROL | Controlo de Autos | 49 | COD_ORC+TIPO_AUTO+ORC_SE+SITUACAO |
| AUTOS_IMPORTACAO | Importação de Autos | 9 | COD_ORC+ORC_SE+SITUACAO+TIPO_TRABALHO |
| AVENCAB | Avenças Cabecalhos | 30 | CLIENTE+TIPOCNTR+NUMCNTR+ANO |
| AVENCNTR | Avenças Contratos | 5 | CODIGO |
| AVENLIN | Avenças Linhas | 13 | TIPOCNTR+NUMCNTR+ANO+LINHA |
| AVENNUM | Avenças Numeração | 3 | TIPOCNTR+ANO |
| AVENPROC | Avenças Processa | 11 | CLIENTE+TIPOCNTR+NUMCNTR+ANOCNTR+DATAPROC |
| AVISOS_VERSOES | Avisos de Versões | 4 | VERSAO |
| AVISO_FUNCIONALIDADES | Avisos de funcionalidades | 8 | CODIGO+ORDEM |
| BALCOES | Balcões | 14 | BANCO+CODIGO |
| BALORC | Balancetes Orçamenta | 11 | EXERC+MES+SECTOR+RUBRICA+CCUSTO+CUSTEIO+CONTA |
| BANASSOC | Bancos Associados | 7 | ASSOCIAD+LINHA |
| BANCABDP | Cabeçalhos Talões | 14 | TPDOCBAN+NUMDBAN |
| BANCOS | Bancos | 10 | CODIGO |
| BANLINDP | Linhas Talões | 12 | TIPODBAN+NUMDBAN+NUMLIN |
| BANMVASS | Bancos Mov Assoc | 7 | CHVPRIM+LINHA |
| BANMVBAN | Movimentos Banco | 12 | CHVPRIM |
| BANMVEMP | Extracto Banco | 31 | CHVPRIM |
| BANMVTMP | Movs Banco Temp | 20 | BANCO+BALCAO+CONTA+NDOCBAN+TPDOCBAN |
| BANORIG | Banco Docs Originais | 10 | BANCO+BALCAO+CONTA+TPDOCBAN+NDOCBAN |
| BANPERIODICMV | Movimentos Periódicos | 18 | CODIGO |
| BANRECON | Reconciliações | 8 | BANCO+BALCAO+CONTA+CODEXTBA |
| BANSCHEDULEMV | Movimentos Programados | 17 | CODIGO |
| BASEANOS | Bases Dados Anos Fec | 3 | BDANO+BDNOME |
| BICIDENTIFIER | BIC do banco | 3 | REFERENCE |
| CADASTROEQUIPAMENTO | Cadastro de equipamento | 24 | CODIGO+TP_EQUIP |
| CARTEIRA | Carteiras | 3 | CODIGO |
| CATEGORIAS_LOTES | Categorias de lotes | 6 | CATEGORIA |
| CATEGORIAS_NUMSERIE | Categorias de números de série | 5 | CATEGORIA |
| CAUC_GARANT | Cauções e Garantias | 15 | COD |
| CBARRAS | Códigos de Barras | 8 | ARTIGO+IMPRIME+CODIGO |
| CCCAB2 | Cópia de DocCcCab | 44 | ANO+TPDOC+SERIEPGT+NUMDOC |
| CCLIN2 | Cópia de DocCcLin | 33 | TIPOD+SERIED+NUMD+NUMLIN |
| CCUSTO | Centros Custo | 3 | COD |
| CFGPARAM | Parametros Config. U | 5 | CODIGO |
| CFGUTIL | Configuração Utiliza | 6 | UTIL+PARAM+CHAVE |
| CLART | Campos Livres artigo | 11 | CODIGO |
| CLASSE_RETENCAO | Classes de Retenção | 2 | CODIGO |
| CLASSIFICACAO_CP | Classificação das alterações no Capital Próprio | 4 | EXERCICIO+CODIGO |
| CLCCCAB | Campos Livres CC Cab | 14 | ANO+TIPODOC+SERIE+NDOC |
| CLCLIE | Campos Livres Client | 11 | CODIGO |
| CLCONF | Configuração Clivres | 14 | CHAVE+NCAMPO |
| CLDOCGC | Campos Livres GC Cab | 24 | ANO+TIPODOC+SERIE+NDOC |
| CLFORN | Campos Livres Fornec | 11 | CODIGO |
| CLIENTES | Clientes | 123 | CODIGO |
| CLLOTES | Campos Livres Lotes | 14 | ARTIGO+CODLOTE+ARMAZEM+VOSSLOTE |
| CNTANA | Contas Analitica | 2 | EXERCICIO+CONTA |
| CNTBAN | Contas Bancos | 1 | CONTAPOC |
| CNTRES | Contas Resultados | 2 | EXERCICIO+CONTA |
| COBRA | Custos de obra | 10 | NUM_LANC |
| CODPOST | Códigos Postais | 2 | COD |
| CODTAB | Codigos de tabelas | 5 | CODIGO |
| COMISSOES_LINHA | Comissões de vendedores por linha | 13 | ORGANO+ORGTPDOC+ORGSERIE+ORGNUMDOC+LIQANO+LIQTPDOC+LIQSERIE+LIQNUMDOC+VENDEDOR+TIPO_COBRANCA+ESTADO |
| COMPLRTF | Texto das notas comp | 4 | CODIGO+TIPO+NOTA |
| COMUN | Comunidades | 2 | COD |
| CONCELHO | Concelhos | 3 | CDDISTR+COD |
| CONSULTA | Consulta a fornecedores | 15 | REQUIS_NUM+COD_OBRA+DESTINO+COD_ENT |
| CONSULTA_VENDEDORES | Consulta de Vendedores | 8 | ANO+MES+VENDEDOR |
| CONTAS | Contas Bancárias | 23 | BANCO+AGENCIA+NUMCONTA |
| CONTENC | Contencioso | 11 | CLIENTE+NPROC |
| CRMNOTES | Notas CRM | 11 | CODIGO |
| CRMTHEMES | Temas CRM | 2 | CODIGO |
| CTBORC | Contab. Orçamental | 8 | EXERC+MES+SECTOR+CONTA+RUBRICA+CCUSTO+CUSTEIO |
| CTBTAG | CTB Tag | 19 | ANO |
| CUSTEIO | Custeio | 3 | CUSTEIO |
| CUSTOSCOMUNS | Custos Comuns | 8 | NUM_LANC |
| DEFREC | Definição Reconstr | 11 |  |
| DEPARTAMENTOS | Departamentos | 2 | CODIGO |
| DESAUT | Descritivos Automáti | 3 | DESAUT |
| DESCPGT | Descontos de Pagamen | 15 | CODIGO |
| DESCRIT | Descritores | 9 | COD |
| DESPEQUIPCAB | Despesas de equipamento cab. | 24 | NUMERO |
| DESPEQUIPLIN | Despesas de equipamento lin. | 9 | NUMERO+REF |
| DESPESAS | Despesas | 7 | ANO+TPDOC+SERIE+NUMDOC |
| DIAGTEMP | Diagnósticos GA | 10 | IDDIAG+ANO+TPDOC+SERIE+NUMDOC |
| DIARIO | Diários | 13 | CODIGO |
| DIARLIN | Diários- Controlo | 5 | DIARIO+EXERC+NMES |
| DISSSEC | Dist. Séries/Sector | 3 | SECTOR+TPDOC |
| DISTR | Distritos | 2 | COD |
| DISTRIBUICAOCUSTOS | Distribuição de Custos | 6 | ID+COD_OBRA |
| DOCBAN | Documentos Bancários | 11 | CODIGO |
| DOCCABDRF | Documentos rectificativos de facturas/compras | 40 | ANO+TPDOC+SERIE+NUMDOC |
| DOCCCCAB | Documentos CC Cab | 70 | ANO+TPDOC+SERIEPGT+NUMDOC |
| DOCCCLIN | Documentos CC Lin | 37 | ANO+TIPOD+SERIED+NUMD+NUMLIN |
| DOCGCCAB | Documentos GC Cab | 215 | ANO+TPDOC+SERIE+NNUMDOC |
| DOCGCCAB_SUBEMP | Documentos Subempreitadas | 7 | TPDOC+NNUMDOC+SERIE+ANO |
| DOCGCECO | Documentos EcoValore | 20 | ID |
| DOCGCLIN | Documentos GC Lin | 84 | ANO+TPDOCUM+SERIE+NNUMDOC+NUMLINHA |
| DOCGCLIN_AUTOS | Ligação Documentos - Autos | 10 | TPDOC+ANO+SERIE+NUMDOC+NUMERO_LINHA |
| DOCIMP | Documentos Imp | 5 | TPDOC+SERIE+IDIOMA |
| DOCLINDRF | Linhas dos documentos rectificativos de facturas/compras | 32 | ANO+TPDOC+SERIE+NUMDOC+NUMLIN |
| DOCNEXTC | Equivalência Documen | 2 | DOCNEXT |
| DOCOBCAB | Documentos Obras Cab | 105 | ANO+TPDOC+SERIE+NNUMDOC |
| DOCOBLIN | Documentos Obras Lin | 40 | ANO+TPDOCUM+SERIE+NNUMDOC+NUMLINHA |
| DOCUMENTSUBMISSIONLOG | Log de submissão de documentos | 10 | TPDOC+SERIE+NNUMDOC+ANO+SUBMISSIONDATE |
| DPIVAANEXO40 | DP iva anexo 40 | 9 | ANO+TPDOC+SERIE+NNUMDOC+ANONC+MESNC+ARTIGO |
| DTFRECON | Data Fecho Recon | 1 | DATA |
| ECOCATEG | Categorias | 3 | ECOTAXA+CODIGO |
| ECOEXCEP | Excepção de Taxas | 7 | GRUPO+FAMILIA+SUBFAM+ARTIGO+ECOVALOR |
| ECONIVEL | Níveis | 2 | CODIGO |
| ECOTIPO | Tipos de Taxas | 3 | CODIGO |
| EDC_CAB | Dados do Encontro de Contas | 6 | EXERCICIO+NUMERO |
| EDC_CONFIGURACAO | Configuração de Encontro de Contas | 25 | CODIGO |
| EDC_ENTIDADES | Tabela de entidades (Clientes e Fornecedores) | 4 | NIF |
| EDC_LN | Documentos Gerados do Encontro de Contas | 6 | EXEREDC+NUMEDC+TPDOC+SERIE+EXERCICIO+NUMERO |
| EDC_NUM | Numerador de encontro de contas | 2 |  |
| EDILOCAL | EDI Locais | 8 | CENTRO |
| EFATMOV | Movimentos eFatura | 23 |  |
| EMPRESA | Dados da Empresa | 74 | NUMREG |
| ENCARGOS | Encargos | 13 | ANO+TPDOC+SERIE+NUMDOC+LINHA |
| ENCOMEND | Preparação de encomendas | 43 | NOME |
| ENCUST | Plano Enq.Custeio | 3 | ENCUST |
| ENQCUS | Plano Enq. C.Custo | 3 | ENQCUS |
| ENQRUB | Plano Enq. Rúbricas | 4 | ENQRUB |
| ENQSEC | Plano Enq. Sectores | 4 | ENQSECT |
| EQUIVALENCIA_FLUXOS | Equivalências entre planos de fluxos | 3 | EXERCICIO+FLUXO_EXERCICIO+FLUXO_EXERCICIO_ANTERIOR |
| EQUIVALENCIA_PLANO_CONTAS | Equivalências entre planos de contas | 3 | EXERCICIO+CONTA_EXERCICIO+CONTA_EXERCICIO_ANTERIOR |
| ERROSL10 | Erros Ligação L100 | 6 | ANO+TPDOC+SERIE+NUMDOC |
| ESTATIST | Codigos Estatistica | 2 | COD |
| ESTIMATECONFIG | Orçamentação | 11 | ANO+SECTOR+CLIENTE+TIPOORCAMENTO+ARTIGO+GRUPO+MES+FAMILIA+SUBFAMILIA |
| ETIQUETA | Etiquetas | 5 | ARTIGO |
| ETPDOC | Tipo Doc. Electrónic | 12 | ETPDOC+GLN |
| EXCEPDES | Excepção Descontos | 27 | GRUPO+FAMILIA+SUBFAM+ARTIGO+GRPCLI+CLIENTE |
| EXCEPLOT | Excepções de Lotes | 9 | GRUPO+FAMILIA+SUBFAM+ARTIGO |
| EXCEPRSV | Inibição de Reservas | 8 | CLIENTE+GRUPO+FAMILIA+SUBFAMIL+ARTIGO |
| EXECUTAD | Produçao Executada | 13 | PROCESSO+ARTIGO+TIPODOC+ANO+NUMDOC+SERIE+OPERAÇÃO+FACTOR+CCOMPOST+DATAENTR |
| EXEPCOMI | Excepção Comissões | 21 | GRUPO+FAMILIA+SUBFAM+ARTIGO+GRPCLI+CLIENTE |
| EXERC | Exercicios | 4 | EXERC |
| EXPEDIR | Modo expedicao | 4 | CODIGO |
| EXTHIS | Extracto histórico | 19 | UTIL+NUM |
| EXTRASLI | Dados Complemtares d | 7 | ANO+TPDOC+SERIE+NNUMDDO+LINHA+TIPEXTRA |
| FACTORES_ENCARGO | Factores de Encargo | 3 | CODIGO |
| FAMILIA | Familia | 8 | GRUPO+COD |
| FASES | Fases | 2 | CODIGO |
| FEDOCIDS | F.E. Identificadores do documento | 7 | ANO+TPDOC+SERIE+NUMDOC+LINHA |
| FEDOCIN | F.E. Docs Entrada | 11 | TPDOC+ANO+SERIE+NUMERO |
| FEDOCOUT | F.E. Docs Saída | 8 | MSGREFID |
| FEDOCTRF | F.E. Docs Transforma | 12 | TPDOC+ANO+SERIE+NUMERO+ORTPDOC+ORANO+ORSERIE+ORNUMERO |
| FEREGRAS | F.E. Regras Conversã | 4 | CODIGO |
| FE_CONFIGURACAO_IDS | Configuração de Identificadores F.E. | 6 | ID_ELECTRONICO |
| FE_CONFIGURACAO_IDS_CAMPOS | Configuração dos campos dos IDs F.E. | 5 | ID_ELECTRONICO+TIPO_DOCUMENTO+CAMPO_NEXT+CAMPO_XML |
| FE_CONFIGURACAO_IDS_CAMPOS_XML | Campos XML para config. dos IDs F.E. | 2 | TIPO_DOCUMENTO+XPATH_XML |
| FORMRECON | Formatos de reconciliação | 2 | CODIGO |
| FORNEC | Fornecedores | 72 | CODIGO |
| FREGUESI | Freguesias | 4 | CDDISTRI+CDCONC+COD |
| FUNCIONARIOS | Cadastro Funcionários | 35 | CODIGO |
| FUNCIONARIOSSERVICOS | Serviços de Funcionários | 18 | NUM_LANC |
| GCCAB2 | Cópia de DocGcCab | 113 | ANO+TPDOC+SERIE+NNUMDOC |
| GCLIN2 | Cópia de DocGcLin | 37 | ANO+TPDOCUM+SERIE+NNUMDOC+NUMLINHA |
| GENERALLEDGERDOCUMENTLOG | Movimentos detalhe da contabilidade | 15 | CONTA+ORIGEM_ANO+ORIGEM_TPDOC+ORIGEM_SERIE+ORIGEM_NUMDOC+LIQUIDACAO_ANO+LIQUIDACAO_TPDOC+LIQUIDACAO_SERIE+LIQUIDACAO_NUMDOC+DATA+TIPO_IVA+TIPOOPERACAO |
| GESTDOC | Gestão Documental | 5 | ANO+TPDOC+SERIE+NUMDOC |
| GESTEQUIPFIXOCAB | Gestão de equipamento fixo cab. | 21 | TRANSF_NUM+TRANSF_COD |
| GESTEQUIPFIXOLIN | Gestão de equipamento fixo lin. | 19 | DATA+DOC_REF+REF+CODIGO+AUX |
| GRCONTMV | Grelha Contab. Mov. | 13 | EXERCICIO+TPDOC+TERCCT+COMPRART+REGIME_IVA+TIPO_IVA |
| GREGIVA | Grelha Geral IVA | 8 | EXERCICIO+TPOPER+TPBEM+REGIVA+TXIVA |
| GRELHA_NATUREZAS | Grelha de naturezas bancárias | 5 | EXERCICIO+NATUREZA |
| GRELHA_RETENCAO | Grelha de Retenção | 6 | EXERCICIO+CLASSE+TIPO_OPERACAO+TIPO_SUJEITO |
| GRPBAN | Grupos Bancos Empre | 2 | CODIGO |
| GRPCONTA | Grupos Contas | 10 | EXERCICIO+CARTEIRA+TPDOC+MERCADO |
| GRUPOS | Grupos | 7 | COD |
| GRUPOS_EMPRESA | Grupos de Empresas | 2 | CODIGO |
| GRUPO_OBRAS | Grupos de obras | 2 | CODIGO |
| HABILITACOES | Habilitações | 2 | CODIGO |
| HORAS_EXTRA_MAO_OBRA | Horas Extra de Mão-de-Obra | 4 | ARTIGO+NUMERO |
| IDIOMAS | Idiomas | 3 | CODIGO |
| IMO | Tabela de Imobilizad | 32 | ANO+TPDOC+SERIE+NUMDOC+NUMLINHA |
| IMOPI_DISTRITOS | Distritos para revisão de preços | 4 | COD |
| IMOPI_FORMULAS | Fórmulas para revisão de preços | 7 | COD |
| IMOPI_INDICES | Índices para revisão de preços | 9 | ANO+MES+COD_MATERIAL+COD_FORMULA+COD_DISTRITO |
| IMOPI_MATERIAIS | Materiais para revisão de preços | 6 | COD |
| IMOPI_PARAMETROS | Parâmetros para revisão de preços | 6 | COD_FORMULA+COD_MATERIAL |
| IMPRESSA | Impressao | 8 | CHAVE |
| IMPUTACOES_DIVER | Imputações custos diversos | 4 | NUM_LANC+COD_ORC+NOME |
| IMPUTACOES_EQUIP | Imputações equipamento | 4 | NUM_LANC+COD_ORC+NOME |
| IMPUTACOES_MAO | Imputações mão de obra | 4 | NUM_LANC+COD_ORC+NOME |
| IMPUTACOES_MAT | Imputações materiais | 8 | TPDOC+NNUMDOC+SERIE+ANO+NUMLINHA+COD_ORC+NOME |
| IMPUTACOES_SERV | Imputações serviços | 8 | TPDOC+NNUMDOC+SERIE+ANO+NUMLINHA+COD_ORC+NOME |
| IMPUTACOES_SUBEMP | Imputações subempreiteiros | 8 | TPDOC+NNUMDOC+SERIE+ANO+NUMLINHA+COD_ORC+NOME |
| INDIC | Indicadores | 2 | COD |
| INDTERC | Indicadores Terc | 5 | TERC+TIPOIND |
| INVENT | Inventario | 16 | ARMAZ+DTINV+CODART |
| INVENTAR | Inv. Preparados | 14 | DATAINV+ARMAZEM |
| ISO3166_1_A2_COUNTRY | Tabela dos Países conforme norma ISSO 3166-1 Alpha2 | 2 | CODIGO |
| ISO4217 | Tabela das Moedas conforme norma ISO4217 | 3 | CODIGO |
| IVANAODE | Iva Nao Dedutível | 3 | SECTOR+GRPARTIG |
| IVAPAG | IVA Pagar | 5 |  |
| IVAREMA | IVA-Reemb. Manut | 8 | ANO+MES+NIF |
| IVAREPAR | IVA-Reemb. Param | 5 | MASCARA+CONTA+TPDOC |
| LIGIMO | Contas Lig. Imobiliz | 3 | EXERCICIO+CONTA+TPDOC |
| LINPRC | Nomes de linhas de p | 3 | LINHA |
| LISTANEGRA | Lista SCCI | 5 | TIPODOC+NUMDOC |
| LOTEMOVS | Lotes Movs | 20 | ANO+TPDOCUM+SERIE+NNUMDOC+NUMLINHA+CODLOT+VOSSLOTE |
| LOTESSCC | Lotes - SSCC | 2 | IDLOTE+IDSSCC |
| MEDIDAS | Medidas | 15 | COD |
| MEDTAMCO | Medidas Grelha Taman | 4 | CODTIPOM+CODMED |
| MEIOIMP | Meios Imp | 5 | MEIOPGT+BANCO |
| MEIOTRAN | Meios Transporte | 2 | COD |
| MODELOS | Modelos | 23 | CODMOD+NOLIN |
| MODELOSIMPRESSAO | Modelos de impressão crystal (VCON) | 4 | GRUPO+ORDEM |
| MODELOS_FISCAIS | Modelos Fiscais | 6 | CMODTYPE+CMODYEAR+CYEAR+CVERS |
| MODOPGT | Modo Pagamento | 16 | CODIGO |
| MOEDAS | Moedas | 13 | CODIGO |
| MORADAS | Moradas Alternativas | 16 | TPTERC+TERCEIRO+CDMORADA |
| MOTIVOSANULACAO | Motivos de anulação de documentos | 2 | CODIGO |
| MOTIVOS_DRF | Motivos dos documentos rectificativos de facturas/compras | 3 | CODIGO |
| MOTIVO_ISENCAO_IVA | Motivos de Isenção de IVA | 4 | CODIGO |
| MOVCT | Movimentos Contabili | 23 | ANO+TPDOC+SERIE+NUMDOC+NUMLINHA |
| MOVCTB | Movimentos CTB | 54 | ANO+TPDOC+SERIE+NUMDOC+NUMLINHA |
| MSEXERC | Meses Exercicio | 5 | EXERC+NMES |
| NATBAN | Naturezas Bancárias | 11 | CODIGO |
| NATJUR | Naturezas Jurídicas | 2 | COD |
| NAT_CUSTO | Naturezas de Custos | 2 | CODIGO |
| NC2000 | Pautal Intrastat | 3 | NC |
| NIFEMAIL | Nifs e respectivos emails para envio de fatura eletrónica Sage | 2 | NIF |
| NOMSERIE | Nome das Séries | 35 | TIPODOC+SERIE |
| NOTASAX | Notas Anexo ao Balan | 4 | CODIGO+TIPO+CODANEXO |
| NOTASRTF | Texto das notas | 5 | CODIGO+TIPO+NOTA |
| NSEREXEP | NumSer Excepcoes | 7 | GRUPO+FAMILIA+SUBFAM+ARTIGO |
| NSEREXIS | NumSer Existencias | 5 | ARTIGO+NUMSER+ARMAZEM |
| NSERMOVS | NumSer Movimentos | 16 | ANO+TIPDOC+SERIE+NUMDOC+LINHA+NUMSER |
| NTCNT | Notas Plano Contas | 3 | EXERCICIO+CONTA |
| NUMDIAR | Numerador Diários | 4 | DIARIO+ANO+MES |
| NUMDOC | Numeradores Docum. | 6 | DOC+ANO+SERIE |
| NXTCTBDI | Equivalência Diários | 2 | DIARIONE |
| OBRIGACOES | Obrigações | 4 | ID_TIPO+PERIODO |
| OBRIGACOES_EXECUCAO | Execução de Obrigações | 6 | ID_TIPO+PERIODO+ID_FASE |
| OBRIGACOES_FASES | Fases de Obrigações | 3 | ID_TIPO+ID |
| OBRIGACOES_TIPOS | Tipos de Obrigações | 3 | ID |
| OPERACOE | Operações de Produçã | 6 | CODIGO |
| OPERAFAC | Operações por Factor | 7 | ARTIGO+OPERACAO+SEQ+FACTOR |
| ORCAM | Orçamentos | 59 | COD_ORC+NOME |
| ORCAMCARGA | Carga de Orçamentos | 5 | COD_ORC+ARTIGO+TIPOPRECO |
| ORCAMENCARGOS | Encargos de Obra | 13 | COD_ORC+NOME |
| ORCAMSUBEMP | Orçamentos de Sub Empreiteiro | 11 | COD_ORC+COD |
| ORCAMSUBEMPDETALHES | Detalhes de Orçamentos de Sub Empreiteiro | 4 | COD_ORC+COD+NOME |
| ORC_ADIT | Aditamento de Orçamentos | 6 | COD_OBRA+SIT_TRABALHOS+COD_ORC |
| ORC_DATA | Datas associadas a processos | 3 | COD_ORC+ID |
| ORC_DATA_TIPIFIC | Tipificação de datas de processo | 10 | ID |
| ORC_LIST | Lista de Processos | 185 | COD_ORC |
| ORC_SE | Orçamentos de Subempreiteiro Adjudicados | 15 | COD_OBRA+COD_SE+NR_ORCAM |
| ORC_SECURE | Segurança de Orçamentos | 3 | COD_ORC+UTILIZ |
| ORC_SE_ADIT | Aditamentos de Orçamentos de Subempreiteiro Ajudic | 7 | COD_OBRA+COD_SE+NR_ORCAM+D_ADIT |
| PAINEL | Painel | 8 | CM1 |
| PAISES | Países | 5 | COD |
| PALETCAB | Paletes Cabeçalho | 12 | SSCC |
| PALETLIN | Paletes Linhas | 13 | SSCC+LINHA |
| PARAMAPL | Parametros Aplicação | 264 | NUMREG |
| PARAMETRIZACOES_CTB | Parametrizações Contabilísticas | 7 | ENTIDADE+CHAVE1+CHAVE2+CHAVE3+EXERCICIO+CAMPO |
| PARAMETROS_GERAIS | Parâmetros gerais da aplicação | 2 | CODIGO |
| PAREFAT | Parametros do e-Fatura | 12 | EXERCICIO+CODIGO |
| PDOCUM | Painel Empresa Documentos | 6 | ANO+MES+OPERADOR |
| PENDENTE | Pendentes | 39 | ANO+TPDOC+SERIE+NNUMDOC |
| PERIODO_ADESAO_WS_AT | Período de adesão ao Webservice da AT | 4 | TIPO+DATA+ATIVO |
| PERIOD_OF_VALIDITY_RIC | Período de vigência do Regime de IVA de caixa | 3 | REFERENCE |
| PLAIVA | Plano IVA | 39 | EXERCICIO+CODIVA |
| PLANOREQUISICOES | Plano de Requisições | 14 | COD_ORC+NOME |
| PLANOTRABALHO | Plano de Trabalhos | 7 | COD_ORC+NOME |
| PLCORA | Correspondente A | 2 | CONTA |
| PLCORB | Correspondente B | 2 | CONTA |
| PLFLUX | Plano Fluxos | 7 | EXERCICIO+CODFLUX |
| PLFLUXSNC | Plano Fluxos SNC | 7 | EXERCICIO+CODFLUX |
| POC | Plano Contas | 29 | EXERCICIO+CONTA |
| PREAPR | Aprovisionamentos pr | 25 | NUMER+LINHA |
| PRECOS | Preços | 19 | ARTIGO+MOEDA+LINPRC |
| PRECOSPREPARADOS | Preços preparados para correr com o SageIva | 5 | ARTIGO+PRECO+TIPO |
| PS2EXP | PS2 EXPORTADOS | 1 | CHAVE |
| PVENANOM | PosVen Anomalias | 2 | CODIGO |
| PVENBASE | PosVen Base | 13 | ARTIGO+NUMSER |
| PVENDESG | PosVen Artigos Desga | 4 | GRUPO+FAMILIA+SUBFAM+ARTIGO |
| PVENDIAS | PosVen Dias Garantia | 3 | CODIGO |
| PVENPEDI | PosVen Pedidos | 2 | CODIGO |
| PVENSTAT | PosVen Status | 2 | CODIGO |
| PVENTECN | PosVen Tecnico | 6 | CODIGO |
| RAZOES | Razoes | 1 | RAZAO |
| RECAPI | Recapitulativos | 15 | ANO+TPDOC+SERIE+NUMDOC+NTERC+NCONT |
| RECON | Indica se existem artigos para reconstruir depois de uma importacao | 1 | RECON |
| RECONBANCAB | Reconciliação Bancária Cabeçalho | 12 | ANO+CONTA+PERIODO |
| RECONBANLIN | Reconciliação Bancária Linhas | 13 |  |
| RECURSOS | Recursos | 2 | CODIGO |
| REEXPCNT | Reexpressão de conta | 4 | ANO+ORIGEM+DESTIN |
| REFANEXO | Referencia do Anexo | 9 | CODIGO+TIPO+REF |
| REFVIS | Referencias Visiveis | 3 | REF+CODTIPOM+MEDIDA |
| REGISTOS | Registo de Acções | 6 | IDENTIFICADOR |
| REGRVCT | Regras de Vencimento | 5 | CODIGO |
| RELATORI | Registo dos relatori | 9 | TIPO+EMPRESA+EXERCICI+VERSAO |
| RELATORIO_CONVERSAO | Relatório da Conversão de documentos | 13 | UTIL+DATA+SESSAO |
| REPORTMANAGEMENT_LOG | Gestão de envio e impressão de documentos | 12 | ANO+TPDOC+SERIE+NUMDOC+DATA |
| REPSECTO | Rep. Sect Custo | 5 | RUBRICA+SECTOR+CCUSTO |
| RESCLASSIFICACAO_CP | Restrição classificação das alterações no Capital Próprio | 3 | EXERCICIO+CONTA |
| RESCUS | Restrição Custeio | 3 | EXERCICIO+CONTA+CUSTEIO |
| RESDES | Restrição Descritivo | 4 | EXERCICIO+CONTA+TPDOC+CODAUT |
| RESFLUX | Restrição Fluxos | 4 | EXERCICIO+CONTA+TPDOC+CODFLUX |
| RESIVA | Restrição IVA | 9 | EXERCICIO+CONTA+TPDOC+MERC |
| RESREFLEX | Restrição Reflexões | 6 | EXERCICIO+CONTA |
| RESRUB | Restrição Rubricas | 3 | EXERCICIO+CONTA+RUB |
| REVISAO_AUTOS | Autos para revisão de preços | 9 | CODIGO |
| REVISAO_PAGAMENTOS | Plano de pagamentos para revisão de preços | 4 | COD_OBRA+ANO+MES |
| REVISAO_SITUACOES | Situações de trabalho para revisão de preços | 4 | COD_OBRA+DATA+TIPO_TRABALHO |
| RGIVA | Tipos de IVA | 19 | CODIGO |
| RGPD_CATALOGO | RGPD Catalogo | 5 | TABELA+CAMPO |
| RGPD_CONFIGURACAO | Configuração | 3 | ENTIDADE+Finalidade+CAMPO |
| RGPD_CONSENTIMENTO | Consentimento para tratamento de dados | 7 | ENTIDADE+CAMPO+CHAVE+Finalidade |
| RGPD_FINALIDADE | Finalidade | 5 | ID |
| RGPD_REGISTOENVIO | Registo de envio de Consentimento | 7 | ENTIDADE+REGISTO |
| RGPD_TEMPLATE | Template para o documento de consentimento | 3 | ID |
| ROTAS | Rotas Por Terminal | 5 | CODROT+VENDEDOR+ORDVIS |
| RUBRORC | Rubricas Orçamentais | 4 | COD |
| SECTORES | Sectores | 22 | CODIGO |
| SEGURADORAS | Seguradoras | 5 | CODIGO |
| SEQUENCIAS | Números de Sequência | 2 | SEQUENCIA |
| SERVICOSEQUIPAMENTO | Serviços de equipamento | 15 | NUM_LANC |
| SIMULCAB | Simulação Cabecalho | 9 |  |
| SIMULLIN | Simulação Linhas | 10 | COMPONEN |
| SLDMED | Saldos Medios | 16 |  |
| STATCAB | Cab Proc Intrastat | 14 | TPDOC+NNUMDOC+SERIE+ANO |
| STATENTR | CONDIÇÕES ENTREGA IN | 2 | CODIGO |
| STATIN | TRANSAÇÕES INTRASTAT | 4 | CODIGOA+CODIGOB |
| STATLIN | Lin Proc Intrastat | 7 | TPDOC+SERIE+ANO+NNUMDOC+NUMLIN |
| STATPAIS | PAÍSES INTRASTAT | 2 | CODIGO |
| STATPORT | PORTOS AEROPORTOS IN | 3 | CODIGO |
| STATREGI | REGIÕES INTRASTAT | 2 | CODIGO |
| STATTRAN | MODO DE TRANSPORTE I | 2 | CODIGO |
| STATUNID | UNIDADES SUPLEMENTAR | 2 | CODIGO |
| SUBACTIVIDADE | Subactividades | 4 | COD_ACTIV+CODIGO |
| SUBEMPIMPORT | Importação de sub-empreiteiros | 6 | COD_ORC+ORC_SE+AUTO_DESTINO+AUTO_ORIGEM+NOME |
| SUBFAMIL | Sub-Familia | 9 | GRUPO+FAMILIA+COD |
| SUBUTDECLFISC | Sub-utilizadores de Declarações Fiscais | 5 | TPDECLARACAO |
| TABLIV01 | Tabela Livre 1 | 2 | CHAVE |
| TABLIV02 | Tabela Livre 2 | 2 | CHAVE |
| TABLIV03 | Tabela Livre 3 | 2 | CHAVE |
| TABLIV04 | Tabela Livre 4 | 2 | CHAVE |
| TABLIV05 | Tabela Livre 5 | 2 | CHAVE |
| TABLIVCF | Config Tab Livres | 7 | CHAVE |
| TAG | Tag File | 12 | TPFAC+DATA+CLIENTE+NUMERO |
| TAXDETAIL | Movimentos detalhe do I.V.A. | 18 | ORIGEM_ANO+ORIGEM_TPDOC+ORIGEM_SERIE+ORIGEM_NUMDOC+LIQUIDACAO_ANO+LIQUIDACAO_TPDOC+LIQUIDACAO_SERIE+LIQUIDACAO_NUMDOC+TIPOBEM+TAXAIVA+TIPOOPERACAO+ARTIGO_DESCRITOR |
| TAXEXEMPTIONDETAIL | Movimentos detalhe do I.V.A. isento | 14 | ORIGEM_ANO+ORIGEM_TPDOC+ORIGEM_SERIE+ORIGEM_NUMDOC+LIQUIDACAO_ANO+LIQUIDACAO_TPDOC+LIQUIDACAO_SERIE+LIQUIDACAO_NUMDOC+TIPOBEM+TAXAIVA+TIPOOPERACAO+ARTIGO_DESCRITOR+MOTIVO_ISENCAO |
| TAXEXEMPTIONREASON | Tabela de motivos de isenção | 2 | CODIGO |
| TAXONOMIAS | Codigo das Taxonomias | 5 | ANO+TIPOEMPRESA+CONTA+TAXONOMIA |
| TERCCT | Terceiros Ct | 2 | SIGLA |
| TERCVDI | Terceiros VDI | 10 | ANO+TPDOC+SERIE+NUMDOC |
| TEREFAT | Parametrização dos fornecedores | 15 | EXERCICIO+NIF |
| TIPMED | Tipo de Medidas GTC | 2 | TIPOMED |
| TIPOS_ANEXO | Tipos de Anexo | 2 | CODIGO |
| TIPO_FALTAS | Tipos de faltas | 3 | CODIGO |
| TIPTERA | Tipo Terceiro A | 2 | CODIGO |
| TIPTERB | Tipo Terceiro B | 2 | CODIGO |
| TPDESPESAS | Tipos de despesas | 8 | CODIGO |
| TPDOC | Tipos Documento | 70 | CODIGO |
| TPMORADA | Tipos Moradas | 2 | CODIGO |
| TRBANCAB | Tranf Ban Cab | 14 | TPDOC+NUMDOC+SERIE+ANO |
| TRBANLIN | Tranf Ban Lin | 19 | TPDOC+NUMDOC+SERIE+ANO+LINHA |
| TRFPAG | Transferência Pagamentos | 7 |  |
| TXPRO | Taxas Pro-Rata | 2 | EXERC |
| UNID | Unidades | 4 | COD |
| UNITEMPO | Unidades de Tempo | 3 | CODIGO |
| UPDATES | Registo de Updates | 2 | ID |
| VENDEDOR | Vendedores | 23 | CODIGO |
| VERSAO | Versao | 2 | TIPOREG |
| VLMEDIDA | Valor Medida Linhas | 11 | ANO+TPDOC+SERIE+NUMDOC+LINHA |
| XDEFAL | Alertas | 6 | REF |
| XDEFQ | SQL | 4 | REF |
| XDEFT | Tarefas | 7 | REF |
| ZONAGEO | Zonas geográficas | 6 | ZONA |
| ZONAS | Zonas Vendas | 2 | CODIGO |
