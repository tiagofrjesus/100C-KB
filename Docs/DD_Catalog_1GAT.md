# Dicionario de Dados 1GAT (Sage Gestao de Ativos) — Catalogo de Tabelas
> Versão 3207. Uma linha por tabela de aplicacao. Faz grep por nome ou descricao.
> Schema completo (colunas, tipos, chaves): `Sage 100c Docs/DD/1GAT/<TABELA>.txt`

Total: 162 tabelas de aplicacao.

| Tabela | Descricao | Cols | Chave Primaria |
|---|---|---|---|
| ABATE | Ficha de Abate | 4 | FICHA |
| ACTIVOS | Activos | 83 | CODIGO |
| ACTIVOS_CALCULADOS | Valores calculados | 39 | CODIGO |
| ACTIVOS_CONTAGEM | Activos na contagem | 11 |  |
| ACTIVOS_DEPRECIACAO | Activos no cálculo de depreciações | 47 | CODIGO |
| ACTIVOS_DESRECONHECIMENTO | Activos no desreconhecimento | 6 | CODIGO |
| ACTIVOS_EMISSAO_ETIQUETAS | Activos na emissão de etiquetas | 10 |  |
| ACTIVOS_INTRODUCAO_DECRETO | Activos na introdução de decreto | 21 |  |
| ACTIVOS_PREPARACAO_EMISSAO | Activos na preparação da emissão de decreto | 21 |  |
| ACTIVOS_REAVALIA_ESPECIAL | Activos no cálculo de reavaliações especiais | 13 |  |
| ACTIVOS_REAVALIA_FISCAL | Activos no cálculo de reavaliações fiscais | 19 |  |
| ACTIVOS_RECLASSIFICACAO | Activos na reclassificação | 18 |  |
| ACUMPOC | Acumulados Poc | 9 | ANO+MES+STATAC+NAT+CONTA |
| AJFISC | Ajustes Fiscais | 6 | CODIGO |
| ALERT | Alertas Programados GEST | 21 | NREG |
| APOLB | Bens das Apólices (Linhas) GEST | 5 | CAPO+CBEM |
| APOLI | Ficha de Apólices (Cabeçalhos) GEST | 14 | CAPO |
| AQUISICO | Aquisicoes | 12 | REGISTO+FICHA |
| AVALIACA | Tabela de avaliacao | 4 | FICHA+DATA |
| AVISOS_VERSOES | Avisos de Versões | 3 | VERSAO |
| AVISO_FUNCIONALIDADES | Avisos de funcionalidades | 8 | CODIGO+ORDEM |
| BEM | Bens GEST | 26 | CBEM |
| BEMPC | Bens - Peças GEST | 7 | CBEM+NSERIE |
| BEMTI | Bens - Tipos de Informação GEST | 9 | CBEM+CTINF |
| CBARRAS | Código de Barras da | 7 | FICHA+CBARRAS |
| CENCU | Tabelas de Centros de Custo | 14 | TCECU+CCECU |
| CENCU1 | Tabelas de Centros de Custo 1 | 3 | CCECU |
| CENCU2 | Tabelas de Centros de Custo 2 | 3 | CCECU |
| CENCU3 | Tabelas de Centros de Custo 3 | 3 | CCECU |
| CENCU4 | Tabelas de Centros de Custo 4 | 3 | CCECU |
| CFGEXTER | Configurações GEST | 6 | CCFG+CAUX1+CAUX2+CAUX3+CAUX4 |
| CLASSIFI | Classificacao | 2 | CODIGO |
| CLIENTES | Clientes | 114 | CODIGO |
| CNTANA | Contas com analitica | 1 | CONTA |
| CODPOST | Código Postal | 2 | COD |
| CODTAB | Codigos de tabelas | 6 | CODIGO |
| COEFDM | Coeficientes de desvalorização monetária | 3 | CPORT+ANO |
| COEFREAV | Coeficientes de desv | 2 | ANO |
| CONSERVA | Conservacao/Reparaca | 8 | NLINHA+FICHA |
| CONTAGEM | Tabela de Contagem | 3 | FICHA+LOCALIZA |
| CONTCAB | Contagem Cabeçalho | 10 | DATAREF |
| CONTLIN | Contagem Linhas | 6 | DATAREF+CODBARRA |
| COPCTB | Ctb Compactado | 20 | CONTADOR |
| CORRFISC | CorrecoesFiscais | 6 | SITUACAO+FICHA |
| CUSTEIO | Custeio | 3 | CUSTEIO |
| DECRETOS | Tabela de Decretos | 15 | CODIGO |
| DEPART | Departamentos | 2 | CODIGO |
| DESCONTA | Descrição de Contas | 5 | CODIGO |
| DESCRICO | Descrições | 2 | CODIGO |
| DESESPEC | Descricoes especiais | 2 | CODIGO |
| DF_MAPA_31 | Dossier fiscal - Mapa 31 | 14 | EXERCICIO+CODIGO+NATUREZA |
| DF_MAPA_32 | Dossier fiscal - Mapa 32 | 22 | LINHA+NATUREZA+METODO+EXERCICIO |
| DF_MAPA_RESUMO | Mapa resumo | 13 | EXERCICIO+LINHA+NATUREZA |
| DISTCUST | Distribuicao de Cust | 5 | REGISTO |
| DISTRIBUICAO_CUSTOS | Distribuição de Centros de Custo | 4 | CODIGO+CONTA_9 |
| EMPRESA | Empresa | 34 | NUMREG |
| ESTAB | Estabelecimentos | 10 | CEST |
| ESTADO_APLICACAO | Estado da aplicação | 4 | EXERCICIO+ACCAO |
| EVENT | Eventos Existentes GEST | 9 | CEVE |
| EXERC | Exercício | 3 | EXERC |
| EXPCB | Listagens configuradas - Cabeçalhos GEST | 28 | CEXP |
| EXPFD | Listagens configuradas - Campos GEST | 10 | CEXP+TFUN+NLIN |
| EXPTB | Listagens configuradas - Tabelas GEST | 5 | CEXP+NLIN |
| FORNEC | Fornecedores | 59 | CODIGO |
| GRINF | Grupos de Informação | 5 | CGINF |
| GRUPO | Tabela de grupos de operadores GEST | 3 | CGR |
| GRUPOS_HOMOGENEOS | Grupos Homogeneos | 5 | CODIGO |
| GRUPO_ACTIVOS | Grupo de Activos | 3 | CODIGO+SNC |
| HISTCORF | historico de correcc | 7 | FICHA+SITUACAO+ANO |
| IMO | Ficha de Activos | 78 | FICHA |
| IMOCC | Centros de Custo de Imóveis | 5 | TCECU+CIMO+DATA+CCECU |
| INFMV | Recolha de Informação de Bens GEST | 6 | CBEM+DATA+CTINF |
| IVA | Tabela de Iva | 3 | CODIGO |
| LEASING | Ficha de Leasing | 6 | FICHA |
| LIGCTB | LigacaoContabilidade | 14 | NUMLINHA |
| LOCAIS | Localizações | 7 | CLOC |
| LOCALIZA | Localizações de Bens | 2 | CODIGO |
| LOCMV | Movimentos de Localizações de Bens | 6 | CBEM+DATA |
| LSCFG | Configuração de listagens GEST | 4 | LISTAGEM+NREG |
| M321 | Mapa 32.1 | 23 | LINHA+ANO |
| M322 | Mapa 32.2 | 24 | LINHA+ANO |
| M331 | Mapa 33.1 | 20 | LINHA+ANO |
| M3310 | Mapa 33.10 | 24 | LINHA+ANO |
| M3311 | Mapa 33.11 | 22 | LINHA+ANO |
| M3312 | Mapa 33.12 | 24 | LINHA+ANO |
| M3313 | Mapa 33.13 | 23 | LINHA+ANO |
| M3314 | Mapa 33.14 | 22 | LINHA+ANO |
| M3315 | Mapa 33.15 | 24 | LINHA+ANO |
| M3316 | Mapa 33.16 | 23 | LINHA+ANO |
| M3317 | Mapa 33.17 | 22 | LINHA+ANO |
| M3318 | Mapa 33.18 | 24 | LINHA+ANO |
| M3319 | Mapa 33.19 | 23 | LINHA+ANO |
| M332 | Mapa 33.2 | 21 | LINHA+ANO |
| M333 | Mapa 33.3 | 24 | LINHA+ANO |
| M334 | Mapa 33.4 | 24 | LINHA+ANO |
| M335 | Mapa 33.5 | 24 | LINHA+ANO |
| M336 | Mapa 33.6 | 24 | LINHA+ANO |
| M337 | Mapa 33.7 | 24 | LINHA+ANO |
| M338 | Mapa 33.8 | 24 | LINHA+ANO |
| M339 | Mapa 33.9 | 24 | LINHA+ANO |
| M341 | Mapa 34.1 | 18 | LINHA+ANO |
| M342 | Mapa 34.2 | 21 | LINHA+ANO |
| M343 | Mapa 34.3 | 18 | LINHA+ANO |
| M344 | Mapa 34.4 | 20 | LINHA+ANO |
| M345 | Mapa 34.5 | 18 | LINHA+ANO |
| M346 | Mapa 34.6 | 20 | LINHA+ANO |
| MAISVALI | Mais valias | 3 | FICHA+ANO |
| MAPA31 | Mais ou Menos Valias | 21 | FICHA+ANO |
| MAPOBS | Observações dos Mapa | 12 | NUMERO+ANO |
| METAC | Definição dos campos. Usado nos limites GEST | 13 | CTAB+CCOL |
| METAP | Tabela com as permissões existentes GEST | 10 | CTAB+CLS+CPAR |
| METAT | Meta-Tabela. Definição das tabelas GEST | 4 | CTAB |
| MODELOS_FISCAIS | Modelos Fiscais | 6 | CMODTYPE+CMODYEAR+CYEAR+CVERS |
| MOEDAS | Moedas | 8 | CODIGO |
| MOVIMENTOS_ACTIVO | Movimentos do Activo | 54 | CODIGO+DATA_OCORRENCIA+TIPO_MOVIMENTO+NUMERO_ORDENA |
| MRESUMO | Mapa Resumo | 16 | LINHA+ANO |
| MSEXERC | Meses Exercicio | 5 | EXERC+NMES |
| MSG | BlocoNotas | 3 | TAB+IDX |
| MSGBX | Lista de mensagens do sistema para utilizadores GEST | 3 |  |
| NATJUR | Naturezas Jurídicas | 2 | COD |
| OBRIGACOES | Obrigações | 4 | ID_TIPO+PERIODO |
| OBRIGACOES_EXECUCAO | Execução de Obrigações | 6 | ID_TIPO+PERIODO+ID_FASE |
| OBRIGACOES_FASES | Fases de Obrigações | 3 | ID_TIPO+ID |
| OBRIGACOES_TIPOS | Tipos de Obrigações | 3 | ID |
| PARAMAPL | PARAMAPL | 56 | NUMREG |
| PARAMETRIZACAO_ACTIVO | Parametrização contabilística do activo | 19 | EXERCICIO+ACTIVO |
| PARAMETRIZACAO_CONTABILISTICA | Parametrização por grupos de activos | 20 | EXERCICIO+TIPO_ACTIVO+GRUPO_ACTIVOS |
| PARAMETROS_GERAIS | Parâmetros gerais da aplicação | 2 | CODIGO |
| PERGR | Tabela com as permissões de cada grupo GEST | 3 | CGR+CPER |
| PFINACEI | Plano Financeiro | 7 | NLINHA+FICHA |
| PORTDM | Portaria de Coeficientes | 2 | CPORT |
| PREVISAO | Previsao de depreciações | 8 | FICHA+ANO |
| PREVISAO_SNC | Previsao de depreciações SNC | 10 | FICHA+ANO |
| PROREAVA | Provisorio de reaval | 18 | FICHA |
| PROREINT | provisorio de reinte | 41 | CONTADOR |
| REAVALIA | Reavaliacoes | 9 | REGISTO+FICHA |
| REINTEGR | Depreciação | 7 | FICHA+ANO+CONTADOR |
| REINVESTIMENTO_VALORES | Reinvestimento de Valores | 9 | ANO_REALIZACAO |
| REPSECTO | Reparticao Sector Ce | 5 | RUBRICA+SECTOR+CCUSTO |
| RESPO | Responsáveis | 14 | CRES |
| RGIVA | Regime de Iva | 7 | CODIGO |
| RGPD_CATALOGO | RGPD Catalogo | 5 | TABELA+CAMPO |
| RGPD_CONFIGURACAO | Configuração | 3 | ENTIDADE+FINALIDADE+CAMPO |
| RGPD_CONSENTIMENTO | Consentimento para tratamento de dados | 7 | ENTIDADE+CAMPO+CHAVE+FINALIDADE |
| RGPD_FINALIDADE | Finalidade | 5 | ID |
| RGPD_REGISTOENVIO | Registo de envio de Consentimento | 7 | ENTIDADE+REGISTO |
| RGPD_TEMPLATE | Template para o documento de consentimento | 3 | ID |
| RUBRORC | Rubricas Orcamentais | 4 | COD |
| SECCAO | Secções | 3 | CSEC |
| SECTORES | Tabela de Sectores | 18 | CODIGO |
| SEGUR | Seguradoras GEST | 16 | CSEG |
| SEGURO | Ficha de Seguro | 7 | FICHA+NAPO+DATA |
| SEPRC | Caracterização de Produtos de Seguradoras GEST | 6 | CCOB+CPRO+CSEG |
| SEPRO | Produtos de Seguradoras GEST | 3 | CPRO+CSEG |
| SIMULACAO | Simulação de Activos | 27 |  |
| STATUSPR | Status dos provisori | 7 | PROV |
| TBEM | Tipos de Bens GEST | 20 | CTBEM |
| TBEMTI | Tipos de Bens - Tipos de Informação GEST | 7 | CTBEM+CTINF |
| TPIMO | Classificação de Activos | 7 | TIMO |
| TPINF | Tipos de Informação GEST | 33 | CTINF |
| UPDATES | Update Via Web | 2 | ID |
| UTILIZAD | Utilizadores | 4 | CODIGO |
