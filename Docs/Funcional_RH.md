# Recursos Humanos / Salários (1GEP) — Referência Funcional

> Fonte: `Sage 100c Docs/Manuais/Sage100C-RecursosHumanos.txt` (manual Sage 100c — Recursos Humanos).
> Base de dados: `<SIGLA>_1GEP`, schema `dbo`. Nomes de tabela citados confirmados em `Docs/DD_Catalog_1GEP.md`.
> **Regra:** antes de escrever SQL que toca numa tabela, lê `Sage 100c Docs/DD/1GEP/<TABELA>.txt`.

---

## 1. Objetivos e conceitos

Aplicação para processamento de salários, gestão de pessoal e emissão de mapas oficiais. Cobre: ficha de pessoal, faltas/absentismo, vencimento, subsídios de férias/Natal, cessação de contrato, trabalhadores sazonais, descontos legais (Seg. Social, IRS, sindicato, seguro, CGA, ADSE), pagamento por transferência/cheque/caixa, declarações fiscais e Relatório Único.

Conceitos-chave:
- **Retribuição horária** = `(VENCIMENTO * 12) / (HORAS_SEMANA * 52)` — base para horas extra e faltas.
- **Base de processamento** (ficha do funcionário): Mensal, Quinzenal, Semanal, Diária, Hora, Sazonal — determina a fórmula de extrapolação do vencimento mensal.
- **Código de remuneração** = rubrica de processamento (abono / desconto / falta), com uma **tipificação** fixa que rege o cálculo.
- **Tipo de recibo**: Normal, Subsídio de férias, Subsídio de Natal, Extraordinário, Parcelar, Agregado, Acumulado.

---

## 2. Tabelas mestras e configuração

### Funcionários e prestadores
| Conceito | Tabela 1GEP | Notas |
|---|---|---|
| Ficha do funcionário | `FUNC1` (chave `NFUNC`, 152 cols) | Geral, Identificação, Caraterização, Contrato, IRS, Descontos, Pagamento, Subsídios, Salário, Outros, Lig. contabilidade |
| Ficha do funcionário — simulação | `SIMFUN` | Réplica de `FUNC1` para simulação (147 cols) |
| Ficha do funcionário (portal) | `FUNC_POR` | |
| Candidatos a funcionários | `FCAND` (`NCAND`) | Pode gerar ficha de funcionário |
| Prestadores de serviços (trab. independentes) | `FINDEP` (`COD`, 87 cols) | Inclui regime de acumulação com funcionário |
| Agregado familiar | `AGRFAM` | |
| Func. CGA / config. CGA | `FUNCGA`, `FUNCGA`/grep | Escalão, nível remuneratório, índice ECDU |

A ficha de funcionário está organizada por separadores: **Geral** (contactos, estabelecimento, departamento/secção), **Identificação** (BI/CC/NIF/NISS, estado civil, naturalidade), **Caraterização** (situação na profissão, profissão, categoria, função, nível qualificação — campos RUAS), **Contrato** (admissão, tipo contrato, IRCT, horas semanais, horário, regime/duração/organização do tempo de trabalho), **IRS** (tabelas/taxa fixa, domicílio fiscal, nº titulares/dependentes/deficientes, sócio gerente, regime tributação mod.30), **Descontos** (Seg. Social, CGA, ADSE, sindicato, seguradora, fundo de compensação), **Pagamento** (forma, banco/IBAN/SWIFT, cartão refeição), **Subsídios** (dias e modo de pagamento de férias/Natal), **Salário** (base de processamento, vencimento base, diuturnidades, subs. turno, subs. alimentação).

### Tabelas de funcionários / caraterização
| Conceito | Tabela 1GEP |
|---|---|
| Habilitações literárias | `HABESC` |
| Tipos de contrato | `CONTR`, validação `CONTRACTTYPES` |
| Tipos de funcionário (classificação contabilística) | `TIPOFUNC` |
| Situação do funcionário | `SITFUNC` |
| Cargos / Categorias profissionais / Funções | `CARGOS` / `CATPRO` / `FUNC` |
| Subsídios de turno / alimentação | `SUBTUR` / `MSALI` |
| Ajudas de custo / Quilómetros | `MACUST` / `MKMS` |
| Horários / Intervalos / Calendário / Dias de ócio | `DESHOR` / `INTHOR` / `CALEND` / `DIASOCIO` |
| Períodos extraordinários | `PERIODOS` (+ `ABONOS_PERIODOS_EXTRA`) |
| Fundamentos horas extra | `FUNDAMENTOS` |
| Departamentos / Secções / Setores / Centros de custo | `DEPARTAMENTOS` / `SECCOES` / `SECTORES` / `CCUST` |

### Empresa e estabelecimentos (tabelas RUAS)
| Conceito | Tabela 1GEP |
|---|---|
| Identificação da empresa | `EMPRESA` |
| Dados entidade empregadora (RUAS) | `ENTIDADERUAS` |
| Estabelecimentos | `ESTAB`; situação atividade `ESTABSITACT` |
| Parâmetros da aplicação | `PARAMAPL` (115 cols), `PARAMETROS_GERAIS` |
| Códigos postais / Países / Distritos / Concelhos / Freguesias | `CODPOST` / `PAISES` / `DISTR` / `CONCELHO` / `PARISHES` |
| Naturezas jurídicas / Associações patronais | `NATJUR` / `ASSPAT` |
| Profissões / Categorias prof. / Instrumentos regul. coletiva | `PROF` / `CATPRO` / `IREGCOL` |
| Códigos CAE | `CAE` |

### Códigos de remuneração (abonos / descontos / faltas)
Tabela mestra das rubricas de processamento: **`ADF`** (chave `COD`, 54 cols), descrição `ABONODES`, expressões `ADFXDEF`. A **tipificação** (não alterável) define o comportamento. Valores fixos do funcionário em `ADFIX` (simulação `SIMADFIX`); abonos/descontos diários em `ADDIA` (simulação `SIMADD`). Listas de faltas que descontam/excluem valor fixo: `FCALDED`, `FCALEXC`.

Separadores da ficha do código de remuneração: **Geral** (recibos afetados, impressão), **Valores fixos** (modo de lançamento), **Incidências** (descontos que incidem), **Apuramento taxa IRS** (apurada/fixa/autónoma/não aplicável), **Horas suplementares** (% acréscimo, descanso compensatório, classificação RU), **Faltas** (unidade, complemento de doença, afeta turno/absentismo/férias), **Mapas** (DMR-AT, Seg. Social, CGA, Modelo 30, mapa resumo art.119, Relatório Único anexo A).

Cálculos-chave documentados no manual:
- Subsídio de férias = `(Vencimento * Dias de férias) / 22`
- Subsídio de Natal = `(Nº dias Natal * Vencimento) / 30`
- Abono nos meses especiais = `Valor abono * Dias férias / 22` (Natal: `/ 30`)
- Abono para falhas: parte sujeita = excede 5% do vencimento.
- Seg. Social: incidência limitada a 12× salário mínimo (sócio-gerente).

### Entidades e taxas (descontos)
| Conceito | Tabela 1GEP |
|---|---|
| Segurança Social (centros/regimes, taxas beneficiário/contribuinte) | `SEGSOC` |
| Instituições de Segurança Social | `ISEGSOC` |
| Outras entidades (CGA, ADSE, FCT/FGCT/ME) | `OUTENT` |
| Sindicatos | `SINDIC` |
| Seguradoras / Companhias ISP | `SEGUROS` / `SEGUROS_ISP` |
| Bancos / Balcões / Contas | `BANCOS` / `BALCOES` / `CONTAS` |
| Repartições de finanças | `REPFIN` |
| Entidades externas | `ENTIDADESEXTERNAS` |

### Tabelas de IRS e escalões
| Conceito | Tabela 1GEP |
|---|---|
| Tabelas de retenção IRS | `TAB1`, `TAB7`, `TAB10` (chave inclui `ANO+TAB+LIMSUP+DOMFIS+DATA`) |
| Tabela sobretaxa IRS | `TABST` |
| Códigos C.I.R.S. | `CIRS` |
| RMMG (retribuição mínima) | `RMMG` |
| Regimes de tributação (mod.30) | `REGIMES_TRIBUTACAO` |

### Configuração contabilística
| Conceito | Tabela 1GEP |
|---|---|
| Contas gerais / por tipo func. / específicas | `CNTGLO` / `CNTTPFUN` / `CNTESP` |
| Param. contab. independentes (prestadores) | `CNTIND`, despesas `CNTDES` |
| Tabela de contas / Rubricas / Setores / Centros custo | `CONTB` / `RUBCTB` / `SECTORES` / `CCUST` |
| Múltiplos centros de custo (rateio %) | `MCCUST` (func.), `MCCUSI` (independentes) |

> Para valores válidos de campos de estado/tipo, consulta `Docs/Validacoes_1GEP.md` (tabelas `REFERENCE` como `GENDERS`, `WORKTIME`, `CONTRACTTYPES`, etc.).

---

## 3. Processamento

**Lançamentos de alterações** (por funcionário ou em lote): alterações mensais, valores fixos, períodos de férias, situações de ausência. Tabelas: movimentos `MOV` / `MOVMANUA` / `MOV_DETALHE`, processamentos manuais `PROMAN`, períodos de férias `PERFER`, ausências prolongadas `DIAS_BAIXA_PROLONGADA`, horas para processamento `HORPOR`, conta corrente faltas `PCCFAL`.

**Geração de alterações de cessação de contrato**: calcula proporcionais de férias/Natal e indemnização; funcionário passa de "Cessação de contrato" a "Inativo". Histórico: `HISTCES`, `HISTADM`, `HISTPRO`.

**Processamento de vencimentos** — função central. Filtra por **base de processamento** e intervalo de funcionários/estabelecimentos. Cria cabeçalho + linhas:
- Cabeçalho de processamento (interno): `CABIND`; linhas `LININD`; tarefas `TAREFAS`.
- Recibo (cabeçalho/movimentos): `CABPROC` (39 cols), `MOV` / `MOV_DETALHE`.
- Histórico de processamento: `LOGPROC` (111 cols), logs diários `LOGDIARIOS`, fixos `LOGFIXOS`, limites isenção `LOGLIMITES`, alterações de campos `LOG`.

**Tipos de processamento** (checkboxes): Normal, Férias (só subs. férias do período seguinte), Natal, Períodos Extraordinários (só base Mensal/Hora; só abonos/faltas manuais marcados na ligação a períodos extra). Subsídio de Natal/férias paga-se na totalidade, por tranches/duodécimos ou misto 50/50.

**Ordem de cálculo**: Salário hora → Faltas → Abonos → Descontos → IRS → TSU (Seg. Social) → Sindicato → Seguro → Subs. alimentação → Complemento doença → Horas extra → Abonos para falhas. Alterações manuais têm prioridade sobre definições da ficha.

**Simulação de processamento** (`SIM*`: `SIMFUN`, `SIMCAB`, `SIMMOV`, `SIMALT`, `SIMADD`, `SIMADFIX`, `SIMCCF`, `SIMHORPOR`, `SIMACERTO_SOBRETAXA`): simula recibo, permite **cálculo inverso** (do líquido para o bruto) e simulação de cessação. "Copiar dados p/aplicação" para gravar.

**Multiempresa**: operações em várias empresas (parâmetro Sistema Multi Empresa). **Importação de alterações** a partir de ficheiro ASCII de códigos de remuneração.

---

## 4. Obrigações legais e declarações

| Obrigação | Tabela(s) 1GEP | Notas |
|---|---|---|
| DMR-AT (declaração mensal remunerações) | `MOD43`, tipos de rendimento `TIPOS_RENDIMENTOS_AT` | Categoria A; opção DRAT vs Modelo 10 ao nível da empresa |
| Modelo 10 (rendimentos/retenções residentes) | `CABM10` / `LINM10`, relatório `RELM10`, tipos `TIPOS_RENDIMENTOS_M10` | Preparação + Emissão; "Auto Declaração" recalcula |
| Modelo 30 (não residentes) | tipos `TIPO_RENDIMENTOS` (NR), regimes `REGIMES_TRIBUTACAO` | Exige regime tributação + país residência |
| Modelo 39 (taxas liberatórias) | `TIPOS_RENDIMENTOS_M39` | |
| Declaração retenção na fonte IRS/IRC/IS | `TIPOS_RENDIMENTOS_DRF` | Inclui sobretaxa IRS |
| Sobretaxa IRS | `ACERTO_SOBRETAXA`, `TABST` | 3,5% sobre o que excede a RMMG (após IRS e contrib. obrigatórias) |
| Segurança Social (folha de remunerações) | `HISTSS`, `GUIA`, `SSEURO`, `FSSMAG`, `RELSS` | Webservice/suporte magnético; agrupa por estab./taxa |
| Quadro de pessoal | `QPESS`, `QPESSP` | |
| Fundo de Compensação do Trabalho (FCT/FGCT/ME) | entidades em `OUTENT`; códigos remun. em `ADF` | Obrigatório p/ admissões ≥ 01-10-2013 (Lei 70/2013) |
| Declaração remunerações seguradoras | `MAPASEGUROS`, exportação `EXPSEG` | |
| Caixa Geral de Aposentações | `HISCGA`, `FRCGA`, `SITCGA`, `FUNCGA`, índice ECDU `INDICE_ECDU` | Preparação + suporte magnético |
| Relatório Único | anexos via `QPESS`, `PESSOALSERVICOS`, `SERVICOSEXTERNOS`, `TECNICOS*` | Diagnóstico por anexo; campos RUAS na ficha |
| Recibos de vencimento | `EMISSAORECIBOS`, mensagens `MENSAGENS` | Emissão por lista/filtros; papel ou e-mail |

Regularizações: **Gerar regularizações de IRS** (`IRSDIF`) recalcula com novas taxas. **Atualização RMMG** (assistente, tabela `RMMG`).

---

## 5. Mapas e consultas

- **Mapa de assiduidade / mapa de alterações** — para registo manual antes do processamento.
- **Listagem de alterações** — conferência pré-processamento.
- **Cadastro de funcionários** — extração de histórico de alterações da ficha.
- **Mapas Seg. Social**: nota de acompanhamento, carta de autorização de pagamento, folha resumo, mapa auxiliar admissões/cessações, mapa auxiliar de cálculo de dias, relatório da última exportação.
- **Declarações de funcionários**: liquidação de IRS por funcionário (valor coletável/imposto/taxa), declaração de rendimentos (abonos + descontos legais).
- **Mapas de pagamento**: mapa de cheques (`CHEQUES`), caixa, notas e moedas (`NOTAS`, `NOTMOE`).
- Config. de mapas: `CONFIGURACAO_MAPAS`; relatórios genéricos `RELAT`, `RELIMP`, `RELPRO`, `RELPS2`.

---

## 6. Integração

**Ligação à contabilidade** — gera movimentos contabilísticos a partir do processamento. Tabelas: `LIGCONT`, `LIGCONT2`. Contas configuradas em `CNTGLO`/`CNTTPFUN`/`CNTESP` (precedência: específicas > por tipo func. > gerais); contas Seg. Social patronal/encargos definidas em `SEGSOC`. Mapas de ligação: Normal/Centro de Custo, por Abonos/Descontos, por Conta/Funcionário, por Centro de Custo/Tipo de Recibo. **Descarga para a Contabilidade** cria ficheiro (data, tipo doc., diário, nº doc.) — um documento por setor.

**Bancos / pagamentos**:
- **Transferência bancária** (`TRANSF`): nacional/internacional; **suporte magnético** TXT segundo normas Banco de Portugal / formato configurado no banco. Valida NIB/IBAN/BIC. Inclui funcionários e prestadores ("Transferência" + sem nº documento).
- **Cheques** (`CHEQUES`) — modo pagamento "Cheque" + data de pagamento preenchida.
- **Caixa / Notas e Moedas** (`NOTAS`, `NOTMOE`) — ajuste à moeda mínima.

**Despesas de funcionários** (`DESPESAS`, tipos `TIPODESPESAS`, pagamento `PAGAMENTODESPESAS`): estados Em apreciação → Aprovada por pagar → Aprovada paga / Convertida / Reprovada. Conversão a vencimento lança abono no recibo.

**Prestadores de serviços** (`FINDEP`): tipos de serviço `FTAREF`, tipos de rendimento `TIPOS_RENDIMENTOS_INDEP`; períodos de pagamento `PERPAG`, pagamentos em lote. Retenção IRS/IRC, ligação à contabilidade própria (`CNTIND`).

**API técnica** — `Sage.BGEP.Api` (COM, `ApiLaunchSalariosVB6`): leitura de funcionários, inserção/remoção de Abonos/Descontos/Faltas. Objeto base `PayrollAPI`; objetos `Employees`, `GetSalaryTypes`, `WorkDetail`. Requer instalação local da aplicação RH (dependência `Sage.BGEP.Api.DL`). Exportação **Sage Extended Accounting XML**.

**Definições avançadas** — fórmulas/expressões para abonos/descontos (`XDEFEC`, `FUNXDEF`, `ADFXDEF`), constantes (`XDEFK`: Salario_Minimo, IAS), condições (`XDEFCOND`), SQL (`XDEFQ` — só SELECT), alertas (`XDEFAL`), tarefas (`XDEFT`). Funções: `ADFQtd`/`ADFValor`, `QtdIntro`/`ValorIntro`.

---

## 7. Glossário

| Termo | Significado |
|---|---|
| **Código de remuneração** | Rubrica de abono/desconto/falta (`ADF`); a tipificação fixa rege o cálculo |
| **Tipificação** | Classificação não alterável do código de remuneração (Vencimento, Subs. férias, Horas suplementares, Faltas, etc.) |
| **Base de processamento** | Periodicidade/fórmula do vencimento (Mensal, Quinzenal, Semanal, Diária, Hora, Sazonal) |
| **Tipo de recibo** | Normal, Subs. férias, Subs. Natal, Extraordinário, Parcelar, Agregado, Acumulado |
| **TSU** | Taxa Social Única — desconto Seg. Social (beneficiário + contribuinte) |
| **Recibo parcelar / agregado** | Parcelar = cada quinzena/semana; agregado = acumulado do mês |
| **Recibo acumulado** | Recibo introduzido manualmente para meses não processados; não reprocessável |
| **Período extraordinário** | Processamento extra no mês (prémios/comissões) com abonos manuais marcados |
| **Duodécimos** | Pagamento de 1/12 do subs. férias/Natal por mês |
| **IRCT** | Instrumento de Regulamentação Coletiva do Trabalho (`IREGCOL`) |
| **RUAS** | Tabelas de apoio ao Relatório Único de Atividade Social |
| **RMMG** | Retribuição Mínima Mensal Garantida (`RMMG`) |
| **IAS** | Indexante dos Apoios Sociais (constante do sistema) |
| **DMR / DRAT** | Declaração Mensal de Remunerações à AT (categoria A) |
| **CGA / ADSE** | Caixa Geral de Aposentações / subsistema de saúde — outras entidades (`OUTENT`) |
| **FCT / FGCT / ME** | Fundo de Compensação / Fundo de Garantia / Mecanismo Equivalente do Trabalho |
| **Complemento de doença** | Valor pago em faltas por doença = `Salário hora * Faltas * % remuneração / 100` |
| **Prestador de serviços** | Trabalhador independente (categoria B / IRC) — ficha `FINDEP` |
| **Dias de ócio** | Dias não úteis do calendário (`DIASOCIO`) |
