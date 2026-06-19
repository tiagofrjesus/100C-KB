# Dicionario de Dados 1GEP (Sage Salarios) — Catalogo de Tabelas
> Versão 3211. Uma linha por tabela de aplicacao. Faz grep por nome ou descricao.
> Schema completo (colunas, tipos, chaves): `Sage 100c Docs/DD/1GEP/<TABELA>.txt`

Total: 267 tabelas de aplicacao.

| Tabela | Descricao | Cols | Chave Primaria |
|---|---|---|---|
| ABONODES | Desc.Assoc.Abon. | 2 | CABONO+CDESC |
| ABONOS_PERIODOS_EXTRA | Abon.Period.Extraor. | 2 | CODIGO_ABONO+CODIGO_PERIODO |
| ABSENCEREASONS | Motivo das horas não trabalhadas | 2 | REFERENCE |
| ACCOES_CONSULTA | Acções de consulta | 5 | NFUNC+DATA+ACCAO |
| ACCOES_FORMACAO | Acções de formação | 5 | NFUNC+DATA+ACCAO |
| ACCOES_IMUNIZACAO | Acções de imunização | 5 | NFUNC+DATA+VACINA |
| ACCOES_INFORMACAO | Acções de informação | 5 | NFUNC+DATA+ACCAO |
| ACCOES_PROMOCAO | Acções de promoção | 5 | NFUNC+DATA+ACCAO |
| ACERTO_SOBRETAXA | Acerto da sobretaxa I.R.S. | 6 | NFUNC+DATA+ORIGEM+TIPO_RECIBO+RENDIMENTOS_SUJEITOS_IRS |
| ACTIVITIESSITUATION | Situação perante a atividade | 3 | REFERENCE |
| ACTIVITYREASONS | Motivo da situação de atividade | 2 | REFERENCE |
| ACTIVITYTYPE | Tipo de código atividade | 2 | REFERENCE |
| ACTMED | Act. Medicina Trabal | 6 | NFUNC+DATA |
| ADDIA | Abonos e desontos diários | 3 | NFUNC+CODABDES |
| ADF | ADF | 54 | COD |
| ADFIX | Valores fixos | 4 | NFUNC+CODABDES |
| ADFXDEF | Expressões A.D.F. | 3 | ADF |
| ADMISSIONREASONS | Motivo da Entrada na Entidade Empregadora | 2 | REFERENCE |
| AGRFAM | Agregado Familiar | 25 | NFUNC+NOME |
| APPLICABILITYIRCT | Aplicabilidade do IRCT | 2 | REFERENCE |
| ASSPAT | Associações Patronai | 2 | COD |
| AVISOS_VERSOES | Avisos de Versões | 4 | VERSAO |
| AVISO_FUNCIONALIDADES | Avisos de funcionalidades | 8 | CODIGO+ORDEM |
| BALCOES | Balcoes | 6 | BANCO+CODBAL |
| BANCOS | Bancos | 8 | COD |
| BICIDENTIFIER | Códigos BIC | 3 | REFERENCE |
| BIOLOGICALRISKAGENTGROUPS | Factores de Risco Biológico - Grupos | 2 | REFERENCE |
| BIOLOGICALRISKAGENTS | Factores de Risco Biológico | 4 | REFERENCE |
| BIOLOGICALRISKPREVENTIONMEASURES | Risco biológico - medidas de prevenção adoptadas | 2 | REFERENCE |
| CABIND | Cabeçalho Processame | 25 | IDPROC+OUTPRO+DATA |
| CABM10 | Cabeçalho MOD10 | 16 | TIPOM+ANODEC+TPDECL |
| CABPROC | Cab. Processamento | 39 | ANO+NFUNC+DATA+TPREC+NORDEMRE |
| CAE | Códigos CAE | 2 | CODIGO |
| CALEND | Calendário | 2 | COD |
| CARGOS | Cargos | 2 | COD |
| CATPRO | Categ. Profissionais | 2 | COD |
| CCUST | Centros de Custo | 13 | COD |
| CHARGESORIGIN | Origem do encargo | 2 | REFERENCE |
| CHEMICALRISKAGENTS | Factores de Risco Químico | 3 | REFERENCE |
| CHEMICALRISKPHRASES | Menção ou frase de risco | 2 | REFERENCE |
| CHEMICALRISKPREVENTIONMEASURES | Risco químico - medidas de prevenção adoptadas | 2 | REFERENCE |
| CHEQUES | Emissão Cheques | 11 | ORDEM |
| CIRS | C.I.R.S. | 2 | REFERENCE |
| CNTDES | Parametrização contabilística das despesas | 9 | TIPODESPESA+ESPACOFISCAL+REGIMEIVA |
| CNTESP | Contas Especificas | 18 | RUB+TPFUNC+TPMES |
| CNTGLO | Contas Gerais | 21 | NUMREG |
| CNTIND | Param. Contab. Indep | 9 | CODTAR+TPTAR+TPREND |
| CNTTPFUN | Contas tipo funcioná | 8 | CODIGO+TPMES |
| CODPOST | Codigos Postais | 2 | COD |
| COMPETENCYACHIEVED | Tipo de certificado / Diploma | 3 | REFERENCE |
| COMPETENCYLEVELS | Nível de qualificação da formação | 3 | REFERENCE |
| COMPLEMENTARYTESTSPERFORMED | Exames Complementares Realizados-Exame | 2 | REFERENCE |
| COMPLEMENTARYTESTSPERFORMEDRISKAGENTS | Exames Complementares Realizados-Factor de risco | 2 | REFERENCE |
| CONCELHO | Concelhos | 3 | CDDISTR+COD |
| CONFIGURACAO_MAPAS | Configuração dos mapas | 4 | MAPA |
| CONSULTATIONACTIVITIES | Acções de consulta | 2 | REFERENCE |
| CONTAS | Contas | 8 | BANCO+CODBAL+NCONTA |
| CONTB | Tabela de Contas | 2 | COD |
| CONTR | Contratos | 5 | COD |
| CONTRACTTYPES | Tipo de contrato | 3 | REFERENCE |
| DEPARTAMENTOS | Departamentos | 2 | REFERENCE |
| DESHOR | Horários | 2 | COD |
| DESPESAS | Despesas | 20 | NFUNC+REGISTO |
| DESTACAMENTOS | Destacamentos | 5 | NFUNC+DATAINI |
| DEVELOPEDACTIVITIES | Atividade desenvolvida | 2 | REFERENCE |
| DIASOCIO | Dias de Ócio | 3 | COD+NUMERO+DATA |
| DIAS_BAIXA_PROLONGADA | Situações de ausência prolongada | 8 | NFUNC+DATA_INICIO+DATA_FIM+CODIGO_SITUACAO |
| DISMISSALREASONS | Motivo da saída na Entidade Empregadora | 2 | REFERENCE |
| DISTR | Distritos | 2 | COD |
| DOENCASPROFISSIONAIS | Doenças Profissionais | 6 | NFUNC+DATA |
| EMISSAORECIBOS | Emissão de recibos | 10 | ANO+MES+NFUNC+TPREC+NORDEMRE |
| EMPRESA | Identificação Emp. | 65 | NUMREG |
| ENTIDADERUAS | Dados Entidade Empregadora | 25 | ANO |
| ENTIDADESEXTERNAS | Entidades Externas | 19 | CODIGO |
| ESTAB | Estabelecimentos | 29 | COD |
| ESTABSITACT | Estabelecimento situação perante a atividade | 5 | ESTABELECIMENTO+DATAINI |
| EXAMES_COMPLEMENTARES | Exames complementares | 4 | NFUNC+DATA+EXAME |
| EXAMES_COMPLEMENTARES_FACTORES | Exames complementares - Factores de risco | 4 | NFUNC+DATA+EXAME+FACTOR_RISCO |
| EXPSEG | Exportação Seguro | 9 | CODSEG+DATA+NFUNC |
| FCALDED | Lista de faltas cujos dias são descontados ao valor fixo | 2 | ABONO+FALTA |
| FCALEXC | Lista de abonos ou faltas cuja existência exclui o valor fixo | 2 | ABONO+FALTA |
| FCAND | Ficha Candidatos | 21 | NCAND |
| FINDEP | Tabela de prestadores de serviços | 87 | COD |
| FORPRO | Formação Profissional | 15 | NFUNC+DATA+HORA+TIPO |
| FRCGA | Folha Resumo CGA | 10 | ANO+MES |
| FSSMAG | Ficha S.S.Mag. | 9 | ANO+MES+MES_REAL+ESTAB+SEGSOC+ANO_REAL |
| FTAREF | Tipos de serviços | 9 | COD |
| FUNC | Funções | 2 | COD |
| FUNC1 | Funcionário | 152 | NFUNC |
| FUNCGA | Func. C.G.A. | 6 | NFUNC |
| FUNC_POR | Funcionário (Portal) | 25 | NFUNC |
| FUNDAMENTOS | Fundamentos | 2 | CODIGO |
| FUNXDEF | Expressões de Func. | 4 | NFUNC+ADF |
| GENDERS | Sexo | 2 | REFERENCE |
| GUIA | Guia | 19 | ANO+MES+ESTAB+CODSS |
| HABESC | Habilitações Escolar | 3 | COD |
| HIGSEG | Higiene Segurança | 9 | NFUNC+DATA |
| HISCGA | Hist. CGA | 19 | ANO+MES+NFUNC+CODSIT+ESTORN+DATAEF |
| HISTACIDIND | Histórico de Acidentes prestadores de serviços | 4 | OP+DATA |
| HISTACIDTEMP | Histórico de Acidentes de Trabalhadores Temporários | 4 | CODIGO+DATA |
| HISTADM | Histórico de Admissões | 4 | NFUNC+DATA |
| HISTADMCESTEMP | Histórico Entradas e Saídas Trabalhadores Temporários | 6 | CODIGO+DATAADM |
| HISTCES | Hist. cessação contr | 4 | NFUNC+DATA |
| HISTPRO | Histório promoções | 4 | NFUNC+DATA |
| HISTSS | Histórico Seg.Social | 15 | ANO+MES+ESTAB+TAXA+LINHA |
| HORPOR | Horas para processam | 4 | NFUNC+DATA |
| INDICE_ECDU | Índice para subscritores abrangidos pelo ECDU | 5 | REFERENCE |
| INFORMATIONACTIVITIES | Acções de informação | 2 | REFERENCE |
| INTHOR | Intervalo Horário | 5 | COD+DIASEM+IDX |
| IREGCOL | Instrumento de regul | 6 | COD |
| IRSDIF | Diferenças de IRS | 5 | NFUNC |
| ISEGSOC | Inst. Seg. Social | 7 | COD |
| ISO3166_1_A2_COUNTRY | Código do País conforme norma ISO 3166-1 Alpha2 | 4 | CODIGO |
| LABORSITUATIONS | Situação na Profissão | 2 | REFERENCE |
| LIGCONT | Lig. à Contabilidade | 16 | ANO+MES+ID |
| LIGCONT2 | Lig. Contabilidade D | 7 | ANO+MES+IDX |
| LINANEXOF | Preparação Anexo F | 13 | ANO+NIF+DATAINI |
| LININD | Linhas Processamento | 17 | IDPROC+OUTPRO+DATAT+TAREFA+ORIG |
| LINM10 | Linhas MOD10 | 14 | TIPOM+ANODEC+TPDECL+ANOREP+TPALT+NFISC+TPREND |
| LOG | Alterações de campos | 15 | ANO+MES+IDX+DIA+CAMPO |
| LOGDIARIOS | Histórico de abonos / descontos diários | 5 | ANO+MES+NFUNC+CODABDES |
| LOGFIXOS | Histórico de abonos/ Descontos fixo | 6 | ANO+MES+NFUNC+CODABDES |
| LOGLIMITES | Histórico limites isenção | 20 | ANO+MES |
| LOGPROC | Histórico de processamento | 111 | ANO+MES+NFUNC |
| MACUST | Mont. Aj. Custo | 3 | TIPO |
| MAPASEGUROS | Declaração remunerações seguradoras | 14 | ANO+MES+NFUNC |
| MCCUSI | Multiplos C. Custo I | 5 | OP+ANO+MES+CENTR |
| MCCUST | Multiplos C. Custo | 5 | NFUNC+ANO+MES+CENTR |
| MENSAGENS | Mensagens para os recibos | 4 | ANO+MES+NFUNC |
| MKMS | Montantes Kms | 3 | TIPO |
| MOD43 | Modelo 43 | 21 | ANO+MES |
| MODELOS_FISCAIS | Modelos Fiscais | 6 | CMODTYPE+CMODYEAR+CYEAR+CVERS |
| MOEDAS | Moedas | 9 | CODIGO |
| MOV | Mov. Processamento | 40 | ANO+MES+TPREC+NORDEMRE+NFUNC+CDALT+ORIG |
| MOVMANUA | Mov. Manuais | 29 | NFUNC+DTALT+GRP+AUX+CDALT |
| MOV_DETALHE | Movimentos (Detalhe) | 19 | ANO+MES+TPREC+NORDEMRE+NFUNC+CDALT+ORIG+LINHA |
| MSALI | Mont. Sub.Alim. | 3 | TIPO |
| MSG | Mensagens | 3 | TAB+IDX |
| MUSCULOSKELETALRISKAGENTS | Factores de Risco Relacionados com a Atividade | 2 | REFERENCE |
| MUSCULOSKELETALRISKPREVENTIONMEASURES | Risco músculo-esquelético - medidas de prevenção adoptadas | 2 | REFERENCE |
| NATJUR | Naturezas Jurídicas | 2 | COD |
| NORMALABSENCEREASONS | Motivo das horas normais não remuneradas | 2 | REFERENCE |
| NOTAS | Notas | 4 | ANO+MES+VALOR |
| NOTMOE | Notas e Moedas | 2 | COD |
| OBRIGACOES | Obrigações | 4 | ID_TIPO+PERIODO |
| OBRIGACOES_EXECUCAO | Execução de Obrigações | 6 | ID_TIPO+PERIODO+ID_FASE |
| OBRIGACOES_FASES | Fases de Obrigações | 3 | ID_TIPO+ID |
| OBRIGACOES_TIPOS | Tipos de Obrigações | 3 | ID |
| OPERATINGCOMPANIES | Entidade formadora | 3 | REFERENCE |
| OTHERRISKAGENTS | Outros Factores de Risco | 2 | REFERENCE |
| OTHERRISKPREVENTIONMEASURES | Outros factores de risco - medidas de prevenção adoptadas | 2 | REFERENCE |
| OUTENT | Outras Entidades | 18 | COD |
| PAGAMENTODESPESAS | Pagamento de despesas | 11 | NFUNC+REGISTO |
| PAISES | Países | 5 | COD |
| PALETES | Paletes de cores para as listagens | 10 | CODIGO |
| PARAMAPL | Parâmetros de configuração da aplicação | 115 | NUMREG |
| PARAMETROS_GERAIS | Parâmetros gerais da aplicação | 2 | CODIGO |
| PARAMSS | Parâmetros S.Social | 2 | NFUNC |
| PARISHES | Freguesias | 4 | DISTRICT+MUNICIPALITY+REFERENCE |
| PCCFAL | Proc. Conta Corrente | 7 | NFUNC+DATA+TPFALT |
| PENSIONPOLITIES | Regime de Reforma Aplicado | 2 | REFERENCE |
| PENSIONPOLITIESREDUCED | Regime de reforma aplicado (reduzido) | 2 | REFERENCE |
| PERFER | Periodos de Férias | 6 | NFUNC+PERIODO |
| PERIODOS | Per. Extraordinários | 3 | CODIGO |
| PERPAG | Periodos Pagamento | 5 | OP+MES+DIA |
| PESSOALSERVICOS | Pessoal serviços | 23 | ANO+ESTAB |
| PHYSICALRISKFACTOR | Factores de Risco Físico | 2 | REFERENCE |
| PHYSICALRISKPREVENTIONMEASURES | Risco Físico - medidas prevenção adoptadas | 2 | REFERENCE |
| PROF | Profissões | 2 | COD |
| PROFESSIONALDISEASERISKAGENTS | Doenças Profissionais Factores de risco | 2 | REFERENCE |
| PROFESSIONALDISEASES | Doenças Profissionais de Participação Obrigatória | 3 | PROFESSIONALDISEASERISKAGENT+REFERENCE |
| PROMAN | Processamentos Manua | 7 | NFUNC+CDALT |
| PSYCHOSOCIALORGANIZATIONALRISKAGENTS | Factores de Risco Psicossociais | 2 | REFERENCE |
| PSYCHOSOCIALORGANIZATIONALRISKPREVENTIONMEASURES | Risco psicossocial - medidas de prevenção adoptadas | 2 | REFERENCE |
| QPESS | Quadro de Pessoal | 13 | ANO+MES+NFUNC |
| QPESSP | Q.Pessoal - Folha Su | 13 | MES |
| QUALIFICATIONCATEGORIES | Habilitações literárias Categorias | 2 | REFERENCE |
| QUALIFICATIONLEVELS | Nível de Qualificação | 2 | REFERENCE |
| REGIMES_TRIBUTACAO | Regimes de tributação | 2 | CODIGO |
| RELAT | Relatório genérico | 6 | FICH+TPMSG+IDXMSG+ID |
| RELIMP | Relatório Importação | 4 | IDX |
| RELM10 | Relatório Mod. 10 | 7 | NFISC+TPREND |
| RELPRO | Relat. Processamento | 5 | NFUNC+ID |
| RELPS2 | Relatório PS2 | 6 | NFUNC+ORIG |
| RELSS | Relat. Seg. Social | 6 | NFUNC+NAT+ID |
| REPFIN | Rep. de Finananças | 4 | COD |
| RGPD_CATALOGO | Catalogo | 5 | TABELA+CAMPO |
| RGPD_CONFIGURACAO | Configuração | 3 | ENTIDADE+FINALIDADE+CAMPO |
| RGPD_CONSENTIMENTO | Consentimento para tratamento de dados | 7 | ENTIDADE+CAMPO+CHAVE+FINALIDADE |
| RGPD_FINALIDADE | Finalidade | 5 | ID |
| RGPD_REGISTOENVIO | Registo de envio de Consentimento | 7 | ENTIDADE+REGISTO |
| RGPD_TEMPLATE | Template para o documento de consentimento | 3 | ID |
| RISCO_BIOLOGICO | Risco biológico | 5 | NFUNC+DATA+FACTOR_RISCO |
| RISCO_BIOLOGICO_MEDIDAS | Risco biológico - Medidas de prevenção | 4 | NFUNC+DATA+FACTOR_RISCO+MEDIDA_PREVENCAO |
| RISCO_FISICO | Risco físico | 5 | NFUNC+DATA+FACTOR_RISCO |
| RISCO_FISICO_MEDIDAS | Risco físico - Medidas de prevenção | 4 | NFUNC+DATA+FACTOR_RISCO+MEDIDA_PREVENCAO |
| RISCO_MUSCULO_ESQUELETICO | Risco músculo-esquelético | 5 | NFUNC+DATA+FACTOR_RISCO |
| RISCO_MUSCULO_ESQUELETICO_MEDIDAS | Risco músculo-esquelético - Medidas de prevenção | 4 | NFUNC+DATA+FACTOR_RISCO+MEDIDA_PREVENCAO |
| RISCO_OUTROS | Outros factores de risco | 5 | NFUNC+DATA+FACTOR_RISCO |
| RISCO_OUTROS_MEDIDAS | Outros factores de risco - Medidas de prevenção | 4 | NFUNC+DATA+FACTOR_RISCO+MEDIDA_PREVENCAO |
| RISCO_PSICOSSOCIAL | Risco psicossocial organizacional | 5 | NFUNC+DATA+FACTOR_RISCO |
| RISCO_PSICOSSOCIAL_MEDIDAS | Risco psicossocial organizacional - Medidas de prevenção | 4 | NFUNC+DATA+FACTOR_RISCO+MEDIDA_PREVENCAO |
| RISCO_QUIMICO | Risco químico | 6 | NFUNC+DATA+FACTOR_RISCO |
| RISCO_QUIMICO_MEDIDAS | Risco químico - Medidas de prevenção | 4 | NFUNC+DATA+FACTOR_RISCO+MEDIDA_PREVENCAO |
| RMMG | Retribuição mínima mensal garantida | 2 | DATA |
| RUBCTB | Rubricas | 2 | RUB |
| SECCOES | Secções | 3 | DEPARTAMENTO+REFERENCE |
| SECTORES | Setores | 3 | COD |
| SEGSOC | Segurança Social | 17 | COD |
| SEGUROS | Seguros | 12 | COD |
| SEGUROS_ISP | Companhias de seguros (ISP) | 4 | REFERENCE |
| SERVICEPROVIDERS | Tipo de prestador | 2 | REFERENCE |
| SERVICEPROVIDERTYPES | Tipo de empresa prestadora | 2 | REFERENCE |
| SERVICOSEXTERNOS | Atividades / Serviços | 6 | ANO+ESTAB+ENTIDADE+DATA |
| SIMACERTO_SOBRETAXA | Simulação - Acerto da sobretaxa I.R.S. | 6 | NFUNC+DATA+ORIGEM+TIPO_RECIBO+RENDIMENTOS_SUJEITOS_IRS |
| SIMADD | Simulação - Ab. Desc | 3 | NFUNC+CODABDES |
| SIMADFIX | Simulação - Valores fixos | 4 | NFUNC+CODABDES |
| SIMALT | Simulação - Alterações | 29 | NFUNC+DTALT+GRP+AUX+CDALT |
| SIMCAB | Simulação - Cab. Pro | 38 | NFUNC+DATA+NORDEMRE+TPREC |
| SIMCCF | Simulação - Conta Corrente faltas | 7 | NFUNC+DATA+TPFALT |
| SIMFUN | Simulação - Dados funcionário | 147 | NFUNC |
| SIMHORPOR | Simulação - Horas para processamento | 4 | NFUNC+DATA |
| SIMMOV | Simulação - Moviment | 39 | NFUNC+DATA |
| SINDIC | Sindicatos | 7 | COD |
| SITCGA | Situação CGA | 9 | COD+TPREL |
| SITFUNC | Situação Funcionário | 4 | COD |
| SSEURO | Hist. Seg. Social (E | 14 | ANO+MES+NFUNC |
| SUBTUR | Subsídios de Turno | 3 | COD |
| TAB1 | Tab IRS 1 | 11 | ANO+TAB+LIMSUP+DOMFIS+DATA |
| TAB10 | Tab IRS 10 | 11 | ANO+TAB+LIMSUP+DOMFIS+DATA |
| TAB7 | Tab IRS 2 | 8 | ANO+TAB+LIMSUP+DOMFIS+DATA |
| TABST | Tabela I.R.S. sobretaxa | 6 | ANO+DATA+TAB+LIMSUP |
| TAREFAS | Tarefas | 20 | OUTPRO+DATA+ORIG+CODTAR |
| TAXAS_IVA | Taxas de I.V.A. | 10 | DTINICIOVIGORTAXAS |
| TECNICOS | Técnicos | 19 | CODIGO |
| TECNICOS_ACTIVIDADES | Atividades técnicos | 5 | ANO+ESTAB+TECNICO |
| TIPODESPESAS | Tipo de despesas | 9 | CODIGO |
| TIPOFUNC | Tipos de funcionário | 3 | CODIGO |
| TIPOS_ACCAO | Tipos de acções | 4 | REFERENCE |
| TIPOS_DOCUMENTO | Tipos de documento | 3 | REFERENCE |
| TIPOS_RENDIMENTOS_AT | Tipos de rendimentos para a declaração de remunerações mensal | 3 | REFERENCE |
| TIPOS_RENDIMENTOS_DRF | Tipos de rendimentos (Declaração retenção na fonte) | 2 | REFERENCE |
| TIPOS_RENDIMENTOS_INDEP | Tipos de rendimentos (Prestadores de serviços) | 10 | REFERENCE |
| TIPOS_RENDIMENTOS_M10 | Tipos de rendimentos (Modeo 10) | 2 | REFERENCE |
| TIPOS_RENDIMENTOS_M39 | Tipos de rendimentos (Modelo 39) | 2 | REFERENCE |
| TIPO_RENDIMENTOS | Tipos de rendimentos (Modelo 30 NR) | 2 | REFERENCE |
| TRABTEMP | Trabalhadores Temporários | 24 | CODIGO |
| TRAININGACTIONS | Área de Educação/Formação da Acção | 2 | REFERENCE |
| TRAININGACTIVITIES | Acções de formação | 2 | REFERENCE |
| TRAININGINITIATIVES | Iniciativa de formação | 2 | REFERENCE |
| TRAININGPERIODS | Periodo de Referência da Formação | 2 | REFERENCE |
| TRAININGSITUATIONS | Situação Face à Frequência de Formação Profissional | 2 | REFERENCE |
| TRAININGTIMETABLES | Horário da formação | 3 | REFERENCE |
| TRAININGTYPES | Modalidade de formação | 2 | REFERENCE |
| TRANSF | Emissão Transferenci | 21 | ORDEM |
| UPDATES | Registo de Updates | 2 | ID |
| VACCINES | Vacina | 2 | REFERENCE |
| WORKTIME | Regime de Duração do Trabalho | 3 | REFERENCE |
| WORKTIMEDURATIONS | Duração do Tempo de Trabalho | 3 | REFERENCE |
| WORKTIMESTRUCTURES | Organização do Tempo de Trabalho | 3 | REFERENCE |
| XDEFAL | Def.Alertas | 5 | REF |
| XDEFCOND | Def.Condições | 3 | REF |
| XDEFEC | Def.Expr.Condicionai | 7 | REF |
| XDEFK | Def.Constantes | 3 | REF |
| XDEFQ | Def.Queries | 4 | REF |
| XDEFT | Def.Tarefas | 6 | REF |
| XDEFVAR | Def.Variáveis | 3 | REF |
