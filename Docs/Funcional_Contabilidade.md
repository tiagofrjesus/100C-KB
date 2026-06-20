# Contabilidade (1GCO) — Referência Funcional

> Mapa funcional destilado do manual `Sage 100c Docs/Manuais/Sage100C-Contabilidade.txt`.
> A Contabilidade partilha a base de dados da Gestão Comercial (`<SIGLA>_1GCO`, schema `dbo`).
> Para colar conceito→tabela física, confirma sempre em `Docs/DD_Catalog_1GCO.md` e lê o `.txt` da tabela antes de escrever queries.

---

## 1. Conceitos fundamentais

- **Integração com a gestão**: a classificação contabilística está *associada* às operações comerciais/financeiras (compras, vendas, cobranças, pagamentos). Documentos lançados na Gestão Empresarial repercutem-se automaticamente na Contabilidade. Não há "reflexão" de movimentos — a classificação adicional preenche atributos no mesmo registo. Tabela base dos movimentos: `MOVCTB`.
- **Dimensões analíticas múltiplas**: cada movimento pode ser classificado em várias dimensões, todas facultativas e estruturadas por um *plano de enquadramento* (em árvore, como o POC):
  - Financeira (POC) → `POC`; enquadramento de razões em `RAZOES`.
  - IVA → `PLAIVA`.
  - Fluxos de caixa → `PLFLUX`.
  - Gestão (analítica): **Setor** (`SECTORES`), **Rubrica** de gestão (`RUBRORC`), **Centro de custo** (`CCUSTO`), **Custeio** (`CUSTEIO`).
  - O sistema desmultiplica o registo quando a classificação exige vários códigos (ex.: 1 movimento financeiro repartido por vários centros de custo) sem afetar a leitura noutras perspetivas. Dispensa a classe 9.
- **Tratamento do IVA**: sistema autónomo — desliga a conta financeira do tipo/taxa de IVA, evitando subcontas no POC. Cada conta base de IVA aponta a sua conta de IVA correspondente e taxa (cálculo automático). Tipos: Não aplicável, Suportado, Dedutível, Liquidado, Regularizações a favor do estado/empresa. Suporta auto-liquidação, % não dedutível, pró-rata e Regime de IVA de Caixa (contas Exigível / Não exigível).
- **Fluxos de caixa**: dimensão aplicável a entradas/saídas de fundos. Natureza (Exploração/Financiamento/Investimento), sentido Entrada/Saída e tipo de entidade. Associam-se às contas de **contrapartida** das contas de tesouraria.
- **Planos A / B** (`PLCORA`, `PLCORB`): a cada conta do POC pode corresponder uma conta em dois planos externos, para reportes com nomenclatura/agregação distinta. Balancetes Plano A / Plano B em paralelo.
- Exercício contabilístico independente do ano civil; aplicação plurianual (vários anos em-linha).

---

## 2. Tabelas mestras

| Conceito | Descrição (1 linha) | Tabela |
|---|---|---|
| Código de Contas (POC) | Plano de contas SNC; contas integradoras vs movimento; tipo auxiliar (Cliente/Forn/Tesouraria), nº dígitos terceiros, associações IVA/Fluxo/Rubrica/Custeio/Taxonomia, reconciliação bancária | `POC` |
| Plano de IVA | Códigos de IVA: conta de IVA correspondente, taxa, tipo, mercado, posições para declarações (DPIVA, anexos 40/41, DA) | `PLAIVA` |
| Plano de fluxos | Códigos de fluxo de caixa (natureza, sentido, tipo de entidade) | `PLFLUX` |
| Planos de enquadramento | Estrutura hierárquica (árvore) por dimensão de gestão — Setores / Rubricas / Centros de custo / Custeios | `ENQSEC` / `ENQRUB` / `ENQCUS` / `ENCUST` |
| Tipos de documento | Distingue operações; só Tipificação "Contabilidade"; tipo de IVA, tipo de operação (Recebimento/Pagamento), modelo de movimentação, séries | `TPDOC` (séries em `NOMSERIE`) |
| Diários | Numeração (Direta/Mensal/Geral por mês/Anual), origem, tipo (Abertura/Normal/Regularizações/Apuramentos/Fecho), controlo mensal | `DIARIO` (numeradores `NUMDIAR`; equivalência `NXTCTBDI`) |
| Descritivos automáticos | Descrições tipificadas para acelerar lançamentos (mnemónicas @T/@R/@D) | `DESAUT` |
| Movimentos automáticos | Definição de apuramentos (resultados, IVA) e outros movimentos: conta origem/destino, tipo de valor (saldo/saldo acumulado/valor débito/crédito) | grep `DD_Catalog_1GCO.md` (sem correspondência única clara; ver `APCAB`/`APLIN` para apuramentos gerados) |
| Modelos de movimentação | "Protótipos" de documento; mnemónicas de data (@HH…@HU), contas com `*`/`?`, fórmulas entre linhas (@n) | `MODELOS` |

Tabelas de configuração relacionadas: Bancos `BANCOS`, Balcões/Naturezas `NATBAN`, Grupos de bancos `GRPBAN`, Contas bancárias da empresa `CNTBAN` (+ `CONTAS`), Contas com analítica `CNTANA`, Contas de resultados `CNTRES`, Repartição setores/centros `REPSECTO`, Taxas pró-rata `TXPRO`, Distribuição séries/setor `DISSSEC`. Restrições (auxiliam a movimentação quando a conta não tem o código preenchido): IVA `RESIVA`, Rubricas `RESRUB`, Fluxos `RESFLUX`, Custeios `RESCUS`, Descritivos `RESDES`. Notas/auditoria: `NTCNT`, `AUDCNT`, `AUDDOC`.

---

## 3. Movimentação

- **Introdução por documento** / **por diário**: dois ecrãs com o mesmo significado operacional; lançamento baseado no Tipo de documento. Movimentos gravados em `MOVCTB`. Ações: Saldar documento, Documentos digitais, Documentos em aberto, Origem do IVA (nº pedido anexos 40/41), Notas cabeçalho/linhas.
- **Movimentos de gestão**: lançamentos diretos na contabilidade de gestão sem mexer na financeira.
- **Análise de movimentos**: grelha por critérios (Diário, Tipo doc, datas, Extrato por conta/centro/IVA/custeio/fluxo, Pesquisa, Excluídos).
- **Introdução automática** (assistente, 7 passos): 1) ficheiro a importar; 2) formato (outros formatos — datas, separadores, perfil, posição/tamanho campos); 3) status (Suspensos/Efetivos/Extra contabilísticos) e tipo de numeração; 4) tabelas associadas (IVA/Fluxos/Custeios/Rubricas); 5) códigos a usar (regras da contabilidade vs já indicados); 6) rubricas; 7) formato (só novos / atualizar existentes / interromper em erro → `IAERRO.TXT`).
- **Abertura de exercício**: gera movimentos de transferência de saldos do exercício anterior; ignora Contas de resultados (`CNTRES`). Não obrigatória (cálculo plurianual). Sem IVA/Fluxos/Rubricas/CC/Custeios.
- **Apuramento de IVA**: salda contas de IVA contra a conta de apuramento (parametrização em Movimentos automáticos, tipo "Apuramento IVA", mensal/trimestral). Definição das contas em `IVAPAG`. **IVA a pagar / a recuperar / reembolsar**: gera documento conforme saldo.
- **Fecho de exercício**: Regularizações (manual) → Apuramentos (resultados: Operacionais/Correntes/Extraordinários/Financeiros/Antes de impostos) → Final (Imposto, Resultados líquidos). Parametrização em Movimentos automáticos, tipo "Apuramento resultados".
- **Sage reconciliações bancárias** (assistente): por conta de tesouraria configurada como "Conta de reconciliação" (tipo Ficheiro/Papel, período semanal/quinzenal/mensal, dias de tolerância). Reconciliação automática (valor + data ± tolerância + sinal contrário) ou manual. Não permite alterar/anular documentos já reconciliados. Tabelas: cabeçalhos `BANRECON`, movimentos do extrato `BANMVEMP`, movimentos do banco `BANMVBAN`, saco temporário `BANMVTMP`, data de fecho `DTFRECON`, documentos bancários `DOCBAN`/`BANCABDP`.

---

## 4. Exploração e mapas

- **Posição conta**: movimentos, saldo e saldo acumulado de uma conta financeira, por meses.
- **Balancetes**: por Natureza, Razão, Geral, Geral entre meses, Plano A, Plano B, Terceiros (Clientes/Fornecedores). Opções: Período, Acumulado, Período e acumulado, Anterior e período, Anterior+período+acumulado, Justificativo, Comparativo. Filtros: Exercício, Período, Tipo de saldo, Conta (máscaras `*`/`?`), Grau, Status, Contas a zero. (Dados em `ACUMPOC`/`ACUMPOCTODAS`/`ACPOCSEC`.)
- **Livros selados**: legalização da escrituração oficial.
- **Mapa de exploração SNC**: resultados mensal/acumulado por períodos (aproximação; cuidado com variação de existências).
- **Rácios**: Balanço (grandes classes) e análise de situação financeira/rentabilidade.
- **Declarações fiscais** (via Configurador de modelos — secção 5): Retenção na fonte, **Modelo 22** (IRC), Declaração anual **IES/DA** (IRC/IRS/IVA/IS), **Modelo 3** (IRS), **Declaração Periódica do IVA** (anexos 40/41 — nº pedido, "Origem do IVA"), Mapa de reembolso IVA (Desp. Norm. 342/93; param. `IVAREPAR`, manutenção `IVAREMA`; anexo I `ANEXOIVA`).
- **Extratos**: contabilísticos (Normal/Detalhe/Total por mês), de conferência, de contrapartida (terceiro/financeira/custeio/setorial/IVA). IVA (extratos, posição código IVA, balancetes, balancetes cruzados). Tesouraria (extratos, demonstração de fluxos de caixa, posição fluxo, balancetes cruzados Fluxo/Conta/Banco). Gestão (extratos e posição por Setor/CC/Custeio/Rubrica, balancetes cruzados). Acumulados: IVA `ACIVA`/`ACPIVA`, fluxos `ACFLUX`, gestão `ACGES`.
- **Relatórios de gestão** (interface Microsoft Word): Anexo ao balanço e à DR, relatório de gestão, atas. Modelo Word com Notas/Referências (`"…"`, `\nnn\`); referências de tabela `nnnQqllcc`; ferramentas no `ANEXO.DOC`. Notas/referências em `NOTASAX` / `REFANEXO`.
- **Mapas de gestão**: Demonstração de resultados (e art. 3º, financeiros, extraordinários), Balanço (ativo/passivo/sintético); outros desenhados em SageGES. Notas dos relatórios.

---

## 5. Configurador de modelos fiscais

- Sistema integrado para preencher mapas/páginas/quadros dos modelos oficiais. Árvore: Nível 1 = Modelo, Nível 2 = Versão (propriedades, estado), Nível 3 = imagem/anexo. Estados: **POR VALIDAR → VALIDADA → SUBMETIDA** (submetida bloqueia edição).
- **Modelos**: criar versão (período de tributação, regime, região autónoma, com base na versão, grupo de fórmulas), acrescentar/retirar anexos, validar, submeter (webservice ou suporte magnético), exportar PDF, arquivo digital.
- **Gestor de fórmulas**: grupos de fórmulas reutilizáveis por conjuntos de empresas homogéneas (página/quadro/campo/fórmula). Tipos de fórmula no Editor: **Específica deste modelo**, **Do grupo de fórmulas**, **Standard SAGE**.
- **Sintaxe de fórmulas**: `SaldoAteReg[conta]`, `SaldoAba12[241#]`, `SaldoCrédito1a12[24#]`, `SaldoFinal[88]`; referências a campos `@[09311]`, a outros anexos `@[063,DR1]`; ano N-1 `PAAnoInicioTributacao[-1]`. Mapa auxiliar de Tributações Autónomas (Modelo 22, Q10 campo 365). IES/DA por tipo de empresa (0-Normal / 1-Pequena / 2-Microentidade); anexos POC vs SNC consoante o período.
- **Taxonomias** (Portaria n.º 302/2016): tabelas de correspondência para caracterizar contas, simplificando anexos A e I da IES. Campo **Taxonomia** na pasta Configuração do Código de Contas (`POC`); só exercícios ≥ 2017 e contas de movimento. Conjunto de códigos depende do tipo de empresa (ficha em `EMPRESA`). Atribuição automática (relação unívoca) ou manual; Gestor do Plano de Contas com botão "Alterar taxonomia".

---

## 6. Integração

- **Sage Exchange**: troca direta de informação entre aplicações Sage via Cloud (ex.: SAF-T de faturação enviado pela Gestão Empresarial → notificação na Contabilidade). Botões: Importar (abre Introdução automática), Analisar (analisador SAF-T), Gravar cópia.
- **Sage Extended Accounting XML** (≥ 2017.02): formato de importação na Introdução automática; assistente estabelece equivalências obrigatórias (Diários, Setores, Rubricas, Centros de custo, Códigos de contas) com possibilidade de criar registos em falta.
- **Conversor L50**: transporta dados da Contabilidade Linha 50 (erros de ligação à L100 em `ERROSL10`).
- **Transporte de movimentos**: Exportação/Importação entre equipamentos sem rede (por suporte magnético; "incluir já importados" = reclassificar).
- **Transferência de movimentos**: desdobra uma conta em níveis inferiores (origem fica sem movimentos, vira integradora). Não transfere entre contas distintas.
- **Multiempresa**: aplica-se apenas aos modelos fiscais; ativar em Configuração de parâmetros (`PARAMAPL` / ficha `EMPRESA`). Filtros: mesma data, só multiempresa, mesma versão.
- **Outros utilitários**: Mudança de estado, Diagnósticos (valores POC/fluxos/IVA/gestão, níveis de integração, movimentos), Integridade de valores, Diagnósticos de IVA, Limpeza de valores, Anular movimentos excluídos.

---

## 7. Glossário

| Termo | Significado |
|---|---|
| **POC / Código de Contas** | Plano de contas SNC; contas integradoras (≥ grau 2 com sufixos) vs contas de movimento (`POC`). |
| **Razão** | Conta de grau 2; conta-pai criada automaticamente (`RAZOES`). |
| **Diário** | Agrupador de movimentos com numeração e tipo próprios (`DIARIO`). |
| **Descritivo (automático)** | Texto tipificado de apoio ao lançamento (`DESAUT`). |
| **Movimento automático** | Regra de geração automática de apuramentos/lançamentos (conta origem→destino). |
| **Modelo de movimentação** | Documento-protótipo com mnemónicas e fórmulas (`MODELOS`). |
| **Setor** | Dimensão analítica departamental; controla séries/numeração (`SECTORES`, enq. `ENQSEC`). |
| **Rubrica** | Agregação funcional de contas de custos/proveitos (`RUBRORC`, enq. `ENQRUB`). |
| **Centro de custo** | Dimensão analítica de estrutura organizacional (`CCUSTO`, enq. `ENQCUS`). |
| **Custeio** | Objeto de afetação (obras, contratos, viaturas) (`CUSTEIO`, enq. `ENCUST`). |
| **Fluxo de caixa** | Classificação de recebimentos/pagamentos por natureza e entidade (`PLFLUX`). |
| **Restrição** | Regra que sugere código (IVA/rubrica/fluxo/custeio/descritivo) quando a conta não o tem; procura por conta de nível inferior (`RESxxx`). |
| **Apuramento** | Geração de movimentos de fecho (resultados ou IVA) a partir de Movimentos automáticos. |
| **Auxiliar** | Conta de detalhe de cliente/fornecedor/tesouraria; prefixo (grelha terceiros) + sufixo (nº terceiro formatado pelo nº dígitos do POC). |
| **Status do movimento** | Suspenso / Efetivo / Extra contabilístico / Excluído (anulado mas não eliminado fisicamente). |
| **Taxonomia** | Código de correspondência de conta (Portaria 302/2016) para IES (anexos A/I); campo em `POC`. |
| **Modelo fiscal** | Declaração oficial preenchida no Configurador (M22, Modelo 3, DPIVA, IES/DA, retenções). |
| **Grupo de fórmulas** | Conjunto reutilizável de fórmulas para empresas homogéneas no Configurador. |
