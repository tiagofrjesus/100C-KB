# Gestão (1GCO) — Referência Funcional

Resumo destilado do manual oficial **Sage 100c – Gestão** (Gestão Empresarial / Comercial). Mapa funcional para ligar conceitos a tabelas/API; fonte completa em `Sage 100c Docs/Manuais/Sage100C-Gestão.txt`. Nomes de tabela citados foram confirmados em `DD_Catalog_1GCO.md` — quando não há correspondência clara, indica-se "grep DD_Catalog_1GCO.md".

## 1. Objetivos e ciclos

A aplicação relaciona encomendas (a fornecedores / de clientes) com entradas/saídas de armazém, mantendo o histórico para reposição da situação original em caso de alteração/anulação.

| Ciclo | O que cobre |
|---|---|
| **Aprovisionamento** (compras) | Orçamentos/encomendas a fornecedores → guias de transporte/entrada → faturas de compra / compras a dinheiro → notas débito/crédito |
| **Entregas** (vendas) | Orçamentos/encomendas de clientes → guias de transporte/remessa → faturas / vendas a dinheiro → notas débito/crédito |
| **Controlo de stocks** | Inventário permanente: cadastro de artigos, existência física por armazém, justificação por movimentos, valorização, imputação a centros de custo, estatística |
| **Financeiro de pagamentos** | Carteiras a pagar (fornecedores): conta corrente, registo de pagamento, títulos a pagar, transferências entre carteiras, registo bancário |
| **Financeiro de cobranças** | Carteiras a receber (clientes): conta corrente, recebimentos, títulos a receber (letras/pré-datados: emissão, desconto, reforma), transferências, registo bancário |

## 2. Entidades e tabelas mestras

| Entidade | O que é | Tabela / pastas |
|---|---|---|
| **Clientes** | Entidades compradoras (efetivo ou potencial; flag inativo) | `CLIENTES`. Pastas: Informação, Vendas, Recebimentos, Contabilidade, Observações, Contactos, Livres, Crédito, Faturação Eletrónica Saphety. Campos livres: `CLCLIE` |
| **Fornecedores** | Entidades vendedoras | `FORNEC`. Pastas: Informação, Compra, Pagamento, Observações, Contactos, Faturação Eletrónica, Livres. Campos livres: `CLFORN` |
| **Artigos** | Cadastro de produtos/serviços (base do inventário permanente) | `ARTIGOS`. Pastas: Informação, Operações, Contabilidade, Existências, Gestão, Observações, Venda, Compra. Descrições por idioma: `ARTIDIOM`; campos livres: `CLART`; códigos de barras: `CBARRAS` |
| **Descritores** | "Artigos" sem stock (serviços/rúbricas de faturação) | `DESCRIT`. Pastas: Informação, Operações, Contabilidade, Observações, Preços base |
| **Avenças** | Contratos de faturação periódica por cliente | Tipos: `AVENCNTR`; cabeçalho por cliente: `AVENCAB`; linhas: `AVENLIN`; numeradores: `AVENNUM`; processamento: `AVENPROC` |
| **Serviço pós-venda** | Folhas de obra / reparações: anomalias, tipos de pedido, técnicos, status, dias de garantia | Folhas de obra: `DOCOBCAB`/`DOCOBLIN`. Tabelas de apoio: `PVENANOM`, `PVENPEDI`, `PVENTECN`, `PVENSTAT`, `PVENDIAS`, `PVENDESG` |
| **Números de série** | Rastreio individual de artigos | Existências: `NSEREXIS`; movimentos: `NSERMOVS`; exceções: `NSEREXEP`. Definições por artigo → grep DD_Catalog_1GCO.md |
| **Tamanhos e cores** | Variantes de artigo (matriz tamanho×cor) | Medidas: `MEDIDAS`, `MEDTAMCO`; referências visíveis: `REFVIS`; tipos de medida: `TIPMED` |
| **Lotes** | Controlo por lote | Lotes por artigo: `ARTLOT`; movimentos de lote: `LOTEMOVS`; controlo: `EXCEPLOT` |
| **Compostos / componentes** | Estrutura de composição (BOM); operações e unidades de tempo | Operações por artigo: `ARTOPERA`; produção a executar: `AEXECUTA`; produção executada: `EXECUTAD`; simulação: `SIMULCAB`/`SIMULLIN` |
| **Taxas adicionais** | Taxas/impostos extra por nível e grelha | grep DD_Catalog_1GCO.md (taxas, tipos, níveis, grelha) |

**Tabelas de terceiros/apoio:** Vendedores `VENDEDOR`, Zonas geográficas `ZONAGEO`, Áreas de venda `ZONAS`, Comunidades `COMUN`, Modos de expedição `EXPEDIR`, Meios de pagamento `MODOPGT`, Regras de vencimento `REGRVCT`, Regimes de IVA `RGIVA`, Códigos postais `CODPOST`, Países `PAISES`, Moedas `MOEDAS`, Idiomas `IDIOMAS`, Tipos de morada `TPMORADA`, Descontos de pagamento `DESCPGT`, Classe de descontos `TIPTERA`, Classe de comissões `TIPTERB`, Moradas alternativas `MORADAS`.

**Tabelas de artigos:** Armazéns `ARMAZENS`, Artigos por armazém `ARTARM`, Unidades `UNID`, Grupos `GRUPOS`, Famílias `FAMILIA`, Sub-famílias `SUBFAMIL`, Linhas de preços / Preços `PRECOS`, Grelhas de descontos `DESAUT`, Grelhas de comissões `EXEPCOMI`, Fórmulas de movimentação `MODELOS`.

**Bancos/tesouraria:** Bancos `BANCOS`, Balcões `BALCOES`, Documentos bancários `DOCBAN`, Naturezas bancárias `NATBAN`, Grupos de contas bancárias `GRPBAN`, Contas bancárias da empresa `CONTAS`.

## 3. Tipos de documento e ciclo de documentos

- **Tipos de documento** em `TPDOC` (configuração da tipificação: comercial, financeiro, stock); modelos de impressão por idioma/série em `DOCIMP`. Cada tipificação determina comportamento (reserva de stock, cálculo de comissões, gera pendente "Documento a crédito", obriga vosso nº, nota crédito/débito financeira, etc.).
- **Séries** em `NOMSERIE` (até 100 por documento). Origem: Assinado Interno / Não assinado Interno / Externo / Auto-faturados / Recuperação / Movimentos internos. Numeração Automática ou Manual; numeradores em `NUMDOC`. Série pode forçar linha de preços, regime de IVA e diário próprios.
- **Transformação / conversão de documentos:** Diferida (status "Não convertido" até invocado), Imediata (após gravação), Específica (numeração direta, ex.: guia 50 → fatura 50). Define-se documento/série de conversão na série. Fluxos típicos: orçamento→encomenda→guia/remessa→fatura.
- **Cabeçalhos/linhas:** comerciais em `DOCGCCAB`/`DOCGCLIN`; financeiros em `DOCCCCAB`/`DOCCCLIN`; dados extra de linha `EXTRASLI`; equivalência de documentos `DOCNEXTC`.
- **Emissão por lista** ("Gestão de emissão de documentos"): emite em lote para Papel, E-mail (PDF) ou EDI conforme a forma de envio da série; opção Arquivo Digital. Faturação e remessas diferidas convertem em lote.

> **Regra de ouro:** documentos criam-se/alteram-se pela **API .NET** (lógica de negócio), nunca por SQL direto.

## 4. Fluxos principais

| Fluxo | Conteúdo |
|---|---|
| **Vendas** | Orçamentos → encomendas (com aprovação) → remessas → faturação; vendas a dinheiro; descontos (comercial/artigo); documentos não satisfeitos; importação EDI de encomendas; folhas de obra; reenvio AT |
| **Compras** | Orçamentos → encomendas → guias de entrada → compras / compras a dinheiro; sugere último preço líquido; abre janela de contabilidade na fatura |
| **Cobranças** | Recebimentos, registo bancário, lançamento de pendentes (`PENDENTE`), alteração de data de pagamento, transformações/títulos, transferência de carteiras, operações de financiamento (desconto/recâmbio/regularização), ajustamento cambial, gestão e histórico de cobranças |
| **Pagamentos** | Pagamentos (e por lista), transferência bancária, emissão de cheques, preparação ("Bom para pagar" / marcação), pendentes a pagar, lançamento bancário, operações de carteira, ajustamento cambial, gestão/histórico |
| **Stocks / inventário** | Inventário inicial, sobras/quebras, saídas de consumos, entradas de produção, transferências entre armazéns, ajustamento em valor; inventariação (preparação `INVENTAR`, contagem `INVENT`, mapa de diferenças, ajustamento); inventário permanente (diagnóstico, valorização detalhe/resumo), zerar stock |
| **Avenças** | Avenças por cliente; processamento (atualização avenças/calendário, simulação, processamento definitivo, renovação antecipada, ativação, copiar) |
| **Bancos / tesouraria** | Extractos bancários (`BANMVEMP`, movimentos do banco `BANMVBAN`, saco `BANMVTMP`), talões de depósito (`BANCABDP`/`BANLINDP`), reconciliações (`BANRECON`, datas `DTFRECON`), transferências entre contas, posição de tesouraria, saldos médios, controlo de tesouraria |
| **Ligação à contabilidade** | Movimentos contabilísticos `MOVCTB`; descarga diferida, exportação/importação, correção contabilística, fecho de datas. Estados (campo `Ligado`): 1 Integrado, 2 Não exportável, 3 Exportado, 4 A substituir, 90 A exportar, 99 Erro de integração |

## 5. Faturação eletrónica e AT

| Mecanismo | Resumo |
|---|---|
| **Comunicação à AT via WebService** | Alternativa ao SAF-T para Fatura, Fatura-Recibo, Fatura Simplificada, Nota de Débito/Crédito em séries Assinada Interna / Externa / Recuperação. Credenciais `<NIF>/<Subutilizador AT>` nos parâmetros (separador "Webservice AT Faturas"); envio Imediato ou Após 1/2/3 dias. Envio automático na finalização; estados no separador "Faturação Eletrónica" e em "Consulta e Reenvio AT de documentos". Após adesão não se pode voltar ao SAF-T no mesmo ano civil (DL 198/2012) |
| **Faturação Eletrónica Sage** | Envio por e-mail de PDF assinado (Certificado Digital Sage ou do utilizador) com link de descarga. Exige séries dedicadas (forma de envio "Faturação Eletrónica Sage", Arquivo Digital obrigatório), cliente com forma de envio e "E-mail para envio" preenchidos. Estado de sucesso: "Processado (-1000)" |
| **Faturação Eletrónica Saphety** | Pasta dedicada na ficha de cliente (operador externo de faturação eletrónica) |
| **Documentos criados indiretamente** | NC automáticas, finalização em lote, transformação de guias, conversão de folhas de obra, descontos financeiros, avisos de lançamento, processamento de avenças → submissão **manual** em "Consulta e Reenvio AT" |
| **Fitofarmacêuticos** | DL 26/2013 (contratos Plus/Premium). Exige nº autorização de exercício de atividade (empresa/cliente/fornecedor) e nº autorização de venda (artigo); modelos `SQLFACTFORRTF.RPT` (compras) / `SQLFACTCLIRTF.RPT` (vendas) |

> CIUS-PT: o manual não usa o termo literal; a faturação eletrónica estruturada é tratada via EDI (Generix/Indra) e operadores (Saphety/Sage). Confirmar versão antes de assumir suporte CIUS-PT.

## 6. Integração

| Integração | Resumo |
|---|---|
| **EDI** | Importa encomendas; exporta faturas, notas de débito e vendas a dinheiro. Localizações EDI configuráveis. Tradutores suportados: **INFLUE** e **TSVA** (ficheiros de ligação com estrutura fixa — não modificar). Forma de envio da série: "EDI (Generix ou Indra)" |
| **Conversor Genérico** | Assistente que importa dados de Excel para a Gestão (`...\Sage\100C\ConversorGenerico`). Layout fixo (folhas/colunas nomeadas, obrigatórias a azul); assistente em 7 passos (conversor, origem, destino SQL, processos, diagnóstico, execução, finalização). Criar empresa destino a partir da MODELO |
| **Sage Exchange** | Troca de informação entre apps Sage via Cloud; nesta fase, envio do SAF-T de faturação ao contabilista (Gestão \ Check-up SAF-T (PT) \ Exportação). Requer subscrição ativa |
| **Intrastat** | Mapa de chegadas/expedições. Tabelas: cabeçalho `STATCAB`, linhas `STATLIN`, condições entrega `STATENTR`, transações `STATTRAN`, regiões `STATREGI`, países `STATPAIS`, portos `STATPORT`, unidades `STATUNID`, modos transporte `MEIOTRAN`, códigos pautais `NC2000` |

## 7. Mapas / consultas

- **Vendas:** planeamento, carteira de encomendas, preparação, controlo, análise, margens, comissões, IVA, avenças, serviço pós-venda, números de série, tamanhos/cores, lotes.
- **Compras:** preços, planeamento, carteira de encomendas, preparação, controlo, análise, IVA, nºs de série, tamanhos/cores, lotes.
- **Cobranças/Pagamentos:** carteira de valores, gestão de financiamentos, comissões, provisões, diferenças cambiais, gestão e histórico.
- **Stocks:** existências, encomendas internas, extracto de artigo, inventário contabilístico.
- **Bancos:** extractos, posição de tesouraria, posição por código de banco, estatística de naturezas, saldos médios, talões em curso, controlo de tesouraria.
- **Gerais:** análise contabilística, custo das vendas, extracto de movimentos, extracto histórico de clientes/fornecedores, Inventário AT.
- **Painéis (consultas):** empresa, clientes, fornecedores, documentos, vendedores, centros de custo, setores, contas, bancos, referências, armazéns, compostos/componentes (controlo de obra, simulação de produção).

## 8. Glossário

| Termo | Significado |
|---|---|
| **Avença** | Contrato de faturação periódica/recorrente a um cliente (`AVENCAB`/`AVENLIN`) |
| **Descritor** | Linha de faturação sem stock (serviço/rúbrica), alternativa ao artigo (`DESCRIT`) |
| **Carteira** | Classificação dos valores em conta corrente (Conta corrente, Letras, Pré-datados, Contencioso, Em desconto). Até 5 por cliente/fornecedor; carteira 1 não desativável (`CARTEIRA`) |
| **Pendente** | Valor em aberto a receber/pagar; gerado por documento "a crédito" (`PENDENTE`) |
| **Setor** | Departamento/secção que organiza os movimentos; condiciona série/numeração e centro de custo. Distribuição séries/setores: `DISSSEC`; repartição setores/centros de custo: `REPSECTO`; tabela mestra de setores → grep DD_Catalog_1GCO.md |
| **Série** | Sequência de numeração de um tipo de documento, com origem e regras próprias (`NOMSERIE`) |
| **Conversão / transformação** | Passagem de um documento a outro no ciclo (orçamento→encomenda→guia→fatura); diferida, imediata ou específica |
| **Grelha de movimentação** | Regras que ligam tipo de documento + grupos contabilísticos de artigos/terceiros às contas de movimento (`GRCONTMV`); fórmulas/modelos de movimentação em `MODELOS` |
| **Grupo contabilístico** | Classificação de artigos/descritores (`ARTCT`) e de terceiros (`TERCCT`/`GRPCONTA`) para a parametrização contabilística |
| **Tipificação** | Categoria funcional de um tipo de documento (ex.: Fatura de Venda, Encomenda de Cliente) que ativa comportamentos específicos |
| **Vosso número** | Referência do documento atribuída pelo terceiro (ex.: nº de encomenda do cliente) |
| **Título** | Valor transformado (letra, cheque pré-datado) na carteira de cobranças/pagamentos |
| **Inventário permanente** | Existências sempre valorizadas em tempo real a partir dos movimentos |
| **Acumulados** | Tabelas de totais por dimensão: artigo/mês `ACARTMES`, IVA `ACIVA`, terceiros `ACUMTERC`, vendedores `ACUMVEND`, plano de contas `ACUMPOC`, fluxos `ACFLUX` |
