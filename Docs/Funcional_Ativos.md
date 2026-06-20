# Gestão de Ativos (1GAT) — Referência Funcional

> Fonte: `Sage 100c Docs/Manuais/Sage100C-GestãoAtivos.txt` (Manual da aplicação, Sage Jun/2017).
> Mapa funcional para programador. Nomes de tabela citados a partir de `Docs/DD_Catalog_1GAT.md`;
> para schema completo (colunas/tipos) lê `Sage 100c Docs/DD/1GAT/<TABELA>.txt`.
> Base de dados: `<SIGLA>_1GAT`, schema `dbo`. Não inventar nomes — confirmar sempre no DD.

---

## 1. Objetivos

- Controlo **administrativo, contabilístico e fiscal** do ativo + gestão económica dos ativos fixos.
- Cadastro completo (substitui fichas manuais); historial por ativo (aquisições, depreciações, reavaliações).
- **Processamento automático** de depreciações e reavaliações, com ordenação/agrupamento conforme os mapas oficiais.
- **Criação automática** de lançamentos contabilísticos (ligação à contabilidade).
- Modos de processamento: **Anual** (31-12-AAAA) ou **Duodecimal** (mês a mês). Definido nos Parâmetros.
- Referencial **POC** (anos < Ano SNC) vs **SNC** (anos >= Ano SNC) condiciona grupos de ativos e funcionalidades.

---

## 2. Tabelas e configuração

### Tabelas fiscais
| Conceito | O que é | Tabela DD |
|---|---|---|
| Títulos dos mapas de depreciações | Títulos impressos nos mapas oficiais (alteração só por mudança legal) | `DESCRICO` / `DESCONTA` (grep DD_Catalog_1GAT.md) |
| Códigos de tabela | Código anexo ao DR 2/90 ou 25/2009 + taxas 737/81, 2/90, 25/2009; descrição individual nos mapas. Obrigatória | `CODTAB` |
| Ajustes fiscais | Correções fiscais: % ou excesso sobre limite; sobre depr. contab. ou fiscal. Código 99 reservado (mais-valias art.32º g) CIRC) | `AJFISC` |
| Coeficientes de desvalorização monetária | Portarias + coeficientes anuais (mais-valias fiscais) | `PORTDM` (portaria), `COEFDM` (coef. por ano) |
| Coeficientes de reavaliação | Índices por ano | `COEFREAV` |
| Decretos de reavaliação | Decretos autorizados (sigla, ano reporte, portaria, fator, % depr. aceite, vida útil mín., refs de mapas) | `DECRETOS` |
| Observações especiais | Legendas para situações especiais nos mapas (turnos, PEDIP...) | `DESESPEC` |
| Taxas de IVA | Codificação IVA (aquisições/ligação CTB) | `IVA` |

### Localização, responsáveis, empresa
| Conceito | Tabela DD |
|---|---|
| Localizações de bens | `LOCALIZA` (e `LOCAIS`) |
| Responsáveis por bens | `RESPO` |
| Empresa (identificação, dados fiscais, CAE, conservatória) | `EMPRESA` |
| Estabelecimentos | `ESTAB` |
| Secções (pertencem a um estabelecimento) | `SECCAO` |
| Clientes (só nas alienações) | `CLIENTES` |
| Fornecedores de ativo (aquisições/reparações; Nº contabilístico + Tipo de terceiro) | `FORNEC` |
| Códigos postais | `CODPOST` |
| Classificações de ativos | `CLASSIFI` / `TPIMO` (classificação de ativos) |
| Grupos homogéneos | `GRUPOS_HOMOGENEOS` |
| Naturezas jurídicas | `NATJUR` |
| Parâmetros gerais da aplicação | `PARAMAPL`, `PARAMETROS_GERAIS` |

### Configuração da ligação à contabilidade
| Conceito | Detalhe | Tabela DD |
|---|---|---|
| Grupo de ativos | Tipos de ativo p/ ligação CTB; referencial POC ou SNC | `GRUPO_ACTIVOS` |
| Contas gerais por grupo de ativos | Parametrização por exercício+tipo+grupo (aquisição, depr. acum., imparidades acum.…) | `PARAMETRIZACAO_CONTABILISTICA` |
| Contas gerais por ativo | Igual mas por ativo; **prevalece** sobre a config. por grupo | `PARAMETRIZACAO_ACTIVO` |
| Descrição das contas | Radical da conta + descrição + flag Reavaliável | `DESCONTA` |
| Centros de custo (até 4 tabelas; 2ª-4ª só Gestexper); rateios >999999 | `CENCU`, `CENCU1..4`; centros de imóveis `IMOCC` |
| Distribuição de custos | % por conta/sinal D/C de um ativo | `DISTCUST`, `DISTRIBUICAO_CUSTOS` |
| Sectores | `SECTORES`; repartição `REPSECTO` |

**Parâmetros (separadores):** Diversos (Data de ativos, datas de tributação, Método de cálculo Anual/Duodecimal, Ano SNC, códigos de barras, englobar depr. meses anteriores, Exercícios `EXERC`/`MSEXERC`); Mapas Fiscais (subtotais por conta POC / grande grupo / código tabela / subgrupo; excluir totalmente depreciados/abatidos); Contabilidade (tipo de ligação Business / 50 Business / Gestexper, máscaras Conta Fornecedor `2711TNNNN` e Conta IVA `24322IT`, Conta Caixa); Centros de Custo.

---

## 3. Ficha de ativo (`ACTIVOS` — cabeçalho; `IMO` = Ficha de Activos)

Campos chave: Código, Estado (Ativo / Inativo / Desreconhecido / Abatido), Descrição, Data início/fim, Data aquisição, Classificação, Número de elementos, fotografia. Valores calculados em `ACTIVOS_CALCULADOS`.

| Separador | Conteúdo |
|---|---|
| **Geral** | Decreto próxima reavaliação; Valor de aquisição (original, imutável em reav.); Depreciação período tributação; Depr. acumuladas (não reav.) e atualizadas; Taxa depr. acumuladas; Quotas perdidas acumuladas; Imparidades acum.; Revalorizações acum.; Valor aquisição atualizado; Quantia escriturada; Vida útil restante; ajustes (valor depr./aquisição/líquido ajustado) |
| **Fiscal** | Método (Quotas constantes / decrescentes); Depreciação anual (depreciação total no 1º ano); Grupo homogéneo; **Regime** (Não processa / 737/81 / 2/90 / 25/2009); Indicador da taxa (Código de tabela / Especial); Código da tabela; Ajuste fiscal 1/2; Taxa depreciação (p/ Especial); Valor estimado final; % residual (não depreciável) / Valor residual (mutuamente exclusivos); flag "depr. acima da quota máxima aceites fiscalmente"; Vida fiscal; Vida real |
| **Caracterização** | Grande grupo; Sub-grupo; Observações especiais; Novo/Usado; Vida adicional / Vida adicional atribuída; Modelo de mensuração (Custo / Revalorização / Justo Valor); Associado ao ativo; flags: Ativo de reinvestimento, Obras em edifícios alheios, Descrição individual nos mapas, Excluído de reavaliações, Ativo de reduzido valor, Incluir no mapa 31, Grande reparação/beneficiação e terreno/edifício, Bem em regime intensivo, Reportar menos-valia fiscal no modelo 31 |
| **Leasing** | Contrato locação financeira p/ Modelo 40 (contratos até 31-12-1993) | `LEASING` |
| **Seguro** | Apólice, data, ramo, valor | `SEGURO`, `APOLI`/`APOLB`, `SEGUR` |
| **Avaliação** | Avaliações extra-contabilísticas (data/valor/obs) | `AVALIACA` |
| **Mais/menos Valias** | Ano/valor de mais-valia não tributada associada (reinvestimento, art.44º CIRC) | `MAISVALI` |
| **Contabilidade** | Tipo de ativo SNC (Fixo tangível / Intangível / Ativo biológico de produção / Investimento financeiro / Propriedade de investimento / Não corrente detido para venda); Grupo de ativo; Sector contab. (só Business); flags lig. CTB desreconhecimento/reclassificação |
| **Gestão** | Fornecedor/Cliente, NIF cliente, fatura venda, data e tipo de abate (Alienação/Sinistro/Abate/Outros), valor alienação, estabelecimento, secção, localização, código barras, utilizador/responsável |
| **Associados** | Ativos associados ao ativo em edição |
| **Observações / Bloco de notas** | Notas livres | `MSG` |
| **Centros de Custo** | Imputação das depr. do período por CC |
| **Dados bem** | Marca, modelo, referência, dimensões, peso, descrição extensa | `BEM`, `BEMPC`, `BEMTI` |
| **Depreciações** | Histórico de depreciações | `REINTEGR` (Depreciação), `PREVISAO`/`PREVISAO_SNC` |
| **Reavaliações** | Decretos aplicáveis (ano >= início utilização) + vida útil adicional | `REAVALIA` |

Barra lateral: Movimentos (`MOVIMENTOS_ACTIVO`), Arquivo Digital, Código de Barras (`CBARRAS`), assistentes de reclassificação/desreconhecimento, geração automática de movimentos (de abertura/históricos). **Desagrupar ficha** divide elementos por várias fichas (divide o histórico).

---

## 4. Tratamento contabilístico / movimentos do exercício

Todos os movimentos podem ser criados no menu próprio ou no ecrã único **Movimentos** (data sugerida = Data de ativos). Só o **último** movimento de um ativo é editável/anulável. Movimentos: `MOVIMENTOS_ACTIVO`.

| Operação | Notas | Tabela DD |
|---|---|---|
| **Aquisições** | Fatura, fornecedor, valor custo, IVA dedutível/não dedutível, quotas perdidas, Ano/Valor Mais Valia (reinvestimento). Aquisição < ano corrente → pergunta criar histórico | `AQUISICO` |
| **Depreciações — manual** | Taxa, Depr. não reav. e Depr. (reavaliada); garante quantia escriturada >= valor estimado final | `REINTEGR` |
| **Simulador de depreciações** | Filtros (classificação, grupo homogéneo, novo/usado, método); altera taxa global ou ativo-a-ativo; pode gravar método/taxa na ficha (passa Indicador a Especial) | `SIMULACAO` |
| **Geração de depreciações** | Cálculo automático mensal/anual. Tipos: pela taxa do ativo / metade da taxa base / taxa específica / por ativo. Recalcula (apaga e regera). Exclui: desreconhecidos, Não corrente p/ venda, Regime "Não processa", data fim < ano proc., início > proc., totalmente depreciados | `ACTIVOS_DEPRECIACAO` |
| Métodos | **Quotas constantes** = Taxa × Valor aquisição reav. **Quotas decrescentes** = (V.aq − depr.acum.)×taxa×fator (1,5 <5 anos; 2,0 = 5-6; 2,5 >6); exige Vida fiscal. **Quotas perdidas** quando taxa < metade da base | |
| **Imparidades** | Quantia recuperável < quantia escriturada e > valor estimado final. Nova taxa = (100/anos vida estimada)×(quantia recuperável/valor aquisição). Só anos >= SNC, sem excedente revalorização, ativo não abatido/não totalmente depreciado | (movimentos em `MOVIMENTOS_ACTIVO`) |
| Reversão de imparidade | Valor <= imparidade revertível | |
| **Revalorizações** (SNC) | Excedente de revalorização revertível = anterior − (inicial/vida útil estimada) | |
| Reversão de revalorização | | |
| **Reavaliações fiscais** | Por **decreto** (atualização monetária). Valor reav. = V.aq.anterior × coeficiente + acerto. Marcação de ativos a reavaliar por decreto; gera linha por ativo. Mapas separados por totalmente depreciados / decreto | `ACTIVOS_REAVALIA_FISCAL`, `PROREAVA`, `STATUSPR`, `PROREINT` |
| **Reavaliações especiais** | Ajustamento registado em campos próprios (Ajuste valor aquisição/depreciações, Valor líquido ajustado), não afeta bases de cálculo | `ACTIVOS_REAVALIA_ESPECIAL` |
| Introdução/preparação de decreto | | `ACTIVOS_INTRODUCAO_DECRETO`, `ACTIVOS_PREPARACAO_EMISSAO` |
| **Reparações / Conservações** | Informativo; fornecedor, fatura, descrição, valor, classe | `CONSERVA` |
| **Plano financeiro** | Leasing: capital em dívida, renda, juros, amortização (p/ Modelo 40) | `PFINACEI` |
| **Ajustes fiscais (movimento)** | Código de ajuste + valor; correções fiscais | `CORRFISC`, `HISTCORF` |
| **Alienações / sinistros / abates** | Valor de realização, prometido reinvestir, tipo de abate (determina conta), data, cliente. Estado→Abatido, Data fim preenchida. **Abate parcial** gera 3 fichas (original Inativa, abatida, ativa) | `ABATE` |
| **Depreciações recuperadas** | Depr. acima quota máxima recuperáveis em exercícios seguintes (art.20º DR 25/2009); lançadas só a 31-12; coluna 16 mapa 32; só se flag "acima quota máxima aceites" **não** marcada | |
| **Imparidades recuperadas** | Imparidades não aceites recuperáveis (art.35º nº4 CIRC); limite = quota máxima − depr. exercício − depr. recuperadas | |
| **Reinvestimento de valores de realização** | Distribui valor a reinvestir pelas aquisições (ordem de lançamento); só ativos com flag "Ativo de reinvestimento". Análise + automático + consulta. Pré-2001 vs legislação atual (art.44º CIRC) | `REINVESTIMENTO_VALORES` |

---

## 5. Mapas fiscais e consultas

**Determinam o tipo de mapa:** Regime; Método; Decreto da última reavaliação; Vida adicional; Novo/Usado (abatidos); Conta de aquisição SNC.

- **Mapas de depreciações** (modelos oficiais por ano): ativo fixo tangível, intangível, não totalmente depreciados, totalmente depreciados, abatidos no exercício, quotas decrescentes, outros tipos. Mapas 32.x → `M321`/`M322`; mapa resumo → `MRESUMO`, `MAPOBS` (observações). Dossier fiscal: `DF_MAPA_31`, `DF_MAPA_32`, `DF_MAPA_RESUMO`, `MODELOS_FISCAIS`.
- **Ordenação/subtotais (4 níveis):** conta de aquisição (I), grande grupo (II), código da tabela (III), subgrupo (IV). Agregação por ano de início de utilização; ativos usados no fim; reduzido valor numa linha; reinvestimento individualizado.
- **Mapas de reavaliações:** totalmente / não totalmente depreciados.
- **Mais/menos valias:** mapa 31 → `MAPA31`. Mais-valias impressas se anteriores a 2001 (duodecimal: só no último mês). Mapa de menos-valias dedutíveis (viaturas cód. tabela 2375; modelo 31/32).
- **Suporte magnético:** ficheiro dossier fiscal modelos 31 e 32 (Portaria 92-A/2011).
- **Consultas:** ativos, aquisições/depreciações/reavaliações/abates por exercício, listagem de fichas, mapa de gestão interna (por utilizador/responsável/localização/departamento → `DEPART`), valores de ativos, mapa de depreciações, listagem de aquisições.

---

## 6. Ligação à contabilidade (`LIGCTB`, `COPCTB` = ctb compactado, `ACUMPOC`)

- **Gerar movimentos de ligação** por tipo: aquisições, depreciações, mais/menos valias, reavaliações fiscais/especiais, perdas por imparidade, reversão de perdas, revalorizações, reversão de revalorizações, reclassificações, desreconhecimento.
- Informação do documento: descrição, diário/série/código, número (Série só Business). **Reclassificar movimentos gerados** regera por intervalo de datas.
- **Prioridade de contas:** Contas Gerais por Ativo (`PARAMETRIZACAO_ACTIVO`) > Contas Gerais por Grupo (`PARAMETRIZACAO_CONTABILISTICA`).
- Aquisições: conta fornecedor (se houver) ou conta caixa; IVA conforme máscara dos Parâmetros.
- Consultar / Retificar movimentos de ligação; Conferência de movimentos; Mapas de depreciações / reavaliações / depreciações-reavaliações (confronto com a CTB).
- **Exportação para contabilidade:** ficheiro p/ Contabilidade 50 Business / Business / Gestexper (duodecimal → exportar mês a mês). Estruturas em secção 7.

---

## 7. Utilitários e importação

| Utilitário | Função |
|---|---|
| Alteração da data de ativos | Muda data de processamento (obrigatório no duodecimal) |
| Substituição de valores | Substituição global do conteúdo de um campo (com condições; não valida obrigatoriedade) |
| Emissão de mapas fiscais revogados | Mapas em formatos antigos |
| **Passagem de ano** | Abre novo exercício (`EXERC`); opção passar abatidos/desreconhecidos (só Monoanuais/Gestexper); cria meses (`MSEXERC`) |
| **Fecho de atividade** | Cria abate tipo "Outros" em todos os ativos em funcionamento |
| **Códigos de barras / contagem** | Norma Code 39; nomenclatura `<cod>.<elem>.<seq>`. Geração/emissão de etiquetas (layout `Imo.lbl` POC / `ImoSNC.lbl` SNC). Contagem por filtros | `CBARRAS`, `CONTAGEM`, `CONTCAB`, `CONTLIN`, `ACTIVOS_CONTAGEM`, `ACTIVOS_EMISSAO_ETIQUETAS` |
| Importação ficheiro de contagem | TXT posicional `Contagem<dataref>.txt` (cód. barras 19, data 8, localização 5) + `Localizacoes.txt` |
| **Importação de fichas (XML)** | `<Fichas><Ficha Codigo=...><Fields><Field Name=.. Value=..>`. Campos: DESCRI, NELEM, CONTAPOC/RED/REC, NOVO, DTAQUISI, VALAQUIS, CTABELA, REGIME, METODO, INDTAXA, VAQACTUA, DTUTILIZ, FACTURA, FORNECED, VALORIMP, IVADEDUT/NDEDU, TAXAIVA, REGISTO… Por ativo existente: Ignorar/Atualizar (ficha) e Ignorar/Adicionar/Atualizar (aquisição) |
| **Importação de fichas (TXT)** | Formato posicional configurável (separadores, campos, posições) |
| Alteração de código de fichas | Renomeia código propagando a todas as tabelas |
| **Reclassificação de ativos** | Assistente 6 passos: POC→SNC ou p/ Não corrente detido p/ venda; define novo tipo + grupo + lig. CTB | `ACTIVOS_RECLASSIFICACAO` |
| **Desreconhecimento de ativos** | Assistente: reconhecidos no POC mas não no SNC; contrapartida conta 56; nos mapas saem como abatidos. Ativos com depr. no exercício têm de anular depr. primeiro | `ACTIVOS_DESRECONHECIMENTO` |
| Reposição de tabelas | Copia tabelas entre BDs de ativos (só Linha 50/Gestexper) |
| Arquivo digital | Anexa documentos digitalizados à ficha/empresa |

**Estruturas de ficheiro Sage** (layouts posicionais para exportação CTB):
- **Business 50:** Data, Conta, Código/Número do Diário, Código/Número do Documento, Descrição (20), Valor (11), Sinal D/C, Rubrica, Centro de Custo, Grupo/Número de Terceiro, CR+LF.
- **Business:** layout próprio da Contabilidade Business (com Série).
- **Gestexper:** layout Gestexper (até 4 tabelas de centro de custo; tipos de lançamento/documento CTB definidos nos Parâmetros).

---

## 8. Glossário

| Termo | Significado |
|---|---|
| **Depreciação** | Imputação sistemática do valor depreciável de um ativo ao longo da vida útil (quotas constantes / decrescentes; anual ou duodecimal) |
| **Reavaliação** | Atualização monetária do valor do ativo por **decreto** legal, via coeficientes de desvalorização (fiscal ou especial) |
| **Revalorização** | Ajuste do valor segundo o modelo SNC (excedente de revalorização revertível) |
| **Imparidade** | Perda de valor: redução da quantia escriturada à quantia recuperável; pode ser revertida |
| **Abate** | Saída do ativo: Alienação / Sinistro / Abate / Outros (não eliminar a ficha — necessária aos mapas) |
| **Reclassificação** | Passar um ativo de um tipo (POC) para outro (SNC) sem o desreconhecer |
| **Desreconhecimento** | Retirar do balanço ativo reconhecido em POC mas não em SNC (contrapartida 56) |
| **Mais/menos valia** | Diferença entre valor de realização e valor contabilístico no abate (mapa/modelo 31) |
| **Quotas perdidas** | Depreciação não considerada fiscalmente por taxa < metade da taxa base |
| **Depreciações/imparidades recuperadas** | Valores não aceites num exercício recuperados em exercícios seguintes (col. 16 mapa 32) |
| **Quantia escriturada** | V. aquisição − depr. acum. − depr. exercício − imparidades acum. + revalorizações acum. |
| **Valor estimado final / residual / % não depreciável** | Limites inferiores do valor depreciável (mutuamente exclusivos) |
| **Reinvestimento** | Reaplicação do valor de realização em novas aquisições (art.44º CIRC) com benefício fiscal |
| **Grupo homogéneo** | Conjunto de ativos da mesma espécie e mesmo regime de depreciação |
| **Regime** | Diploma de taxas: 737/81, DR 2/90, DR 25/2009 ou "Não processa" |
| **Ano SNC** | Ano de entrada em vigor das regras SNC; separa referencial POC de SNC |
