# API Sage 1GCO (.NET / COM) — Catalogo de Classes
> Logica de negocio da Gestao Comercial. Faz grep por classe ou conceito.
> Membros completos (assinatura, input/output, proposito): `Sage 100c Docs/API/<Classe>.txt`

Total: 90 classes.

Tipos de membro: **Sub** (acao) · **Function** (devolve valor) · **Get/Let/Set** (propriedade).

| Classe | Proposito | Membros |
|---|---|---|
| AjudaCompra | Entidade AjudaCompra. Manutenção directa á tabela. | 16 |
| Aprovisionamento | Entidade Aprovisionamento. Manutenção directa á tabela. | 29 |
| Artigos | Entidade Artigos. Manutenção directa á tabela. | 31 |
| ArtigosArmazens | Entidade ArtigosArmazens. Manutenção directa á tabela. | 16 |
| Balcoes | Entidade Balcoes. Manutenção directa á tabela. | 16 |
| Bancos | Entidade Bancos. Manutenção directa á tabela. | 1 |
| BancosReader | Ligação ao módulo de bancos. Leitura de definições para ligação de documentos comerciais a bancos. | 0 |
| BancosRules | Ligação ao módulo de bancos. Não usado. Regras de negócio | 0 |
| BancosWriter | Ligação ao módulo de bancos. Não usado. Acesso a dados para escrita | 0 |
| BaseBusiness | BACKBONE da Api, tem as propriedades de ligação, efectua a ligação e termina a Api | 0 |
| CamposLivresDocumentos | Campos livres associados ao documento comercial, manutenção directa da entidade | 12 |
| CeC_Compostos | Compostos e Componentes - nível mais alto, Composto | 0 |
| CeC_Factores | Compostos e Componentes - nível mais baixo, componente | 0 |
| CeC_Operacoes | Compostos e Componentes - componentes associados a cada operação do composto | 0 |
| Clientes | Entidade Clientes. Manutenção directa á tabela. | 17 |
| ClsNovoPCM | Gestão da actualização de stocks para todo o tipo de movimentações comerciais | 0 |
| CompostosRules | Compostos e componentes - Regras de negócio | 0 |
| ConfiguracaoUtilizador | Implementa as Configurações Utilizador (Responsável de Sistema) | 0 |
| ContabilidadeReader | Ligação á contabilidade de documentos comerciais e financeiros, acesso a dados para leitura | 0 |
| ContabilidadeRules | Ligação á contabilidade de documentos comerciais e financeiros, regras de negócio | 0 |
| ContabilidadeWriter | Ligação á contabilidade de documentos comerciais e financeiros, acesso a dados para escrita | 0 |
| ContasBancarias | Entidade Contas Bancarias. Manutenção directa á tabela. | 16 |
| DadosEmpresa | Implementa os dados da empresa (tabela EMPRESA na base de dados) | 0 |
| DataAccessDatabase | Não usada | 0 |
| DataAccessInterface | Estrutura básica dos erros | 0 |
| DataAccessXML | Classe gestora do registo de erros e warnings da API. Usa MSXML2 | 0 |
| DescontosPagamento | Entidade Descontos de pagamento, manutenção directa | 16 |
| Diarios | Entidade Diarios. Manutenção directa á tabela. | 19 |
| DiariosControlo | Entidade Controlo de Diarios. Manutenção directa á tabela. | 16 |
| DocsOriginais | Documentos comerciais - actualização dos documentos originais qudo se faz importação de documentos | 0 |
| DocumentoComercial | Documentos comerciais Principal (clientes, fornecedores, internos), (orçamentos, encomendas, guias, facturas, devoluções, notas de crédito) | 131 |
| DocumentoContabilistico | Documentos contabilisticos - Principal (classificação de comerciais e financeiros) | 26 |
| DocumentoFinanceiro | Documentos financeiros - Principal | 35 |
| DocumentosEcoValores |  | 15 |
| DocumentosGcLin | Documentos Comerciais - Linhas | 224 |
| EcoValLinha | Ecovalores - Linha de dados de ecovalores assciada a cada linha de documento, cada linha de documento pode ter várias destas associadas | 1 |
| EcoValRules |  | 2 |
| EcoValWriter | Ecovalores - Acesso a daos para escrita | 0 |
| EncargosCompras | Classe partilhada com a camada de dados Sage.1GCO.Data, usada pelo documento comercial para conter os dados associados aos encargos (compras) | 0 |
| Especificos | must have. Interface com framework | 0 |
| Etiquetas | Biblioteca de funções de geração e iompressão de etiquetas, usada pelo documentocomercial | 0 |
| ExcepDescComInterface | Não usada | 0 |
| ExcepDescontosComissoes | Classe que implementa a grelha de desconto e comissões | 0 |
| ExcepcaoComissao | Não usada | 0 |
| ExcepcaoDesconto | Não usada | 0 |
| ExtraDocumentoComercial | Campos Extra associados a cada documento (cabeçalho). Situações específicas. | 0 |
| FormulasMovLinha | Formulas de movimentação - Entidade associada a cada linha de documento com artigo com formulas de movimentação configuradas, também faz acesso a dados para escrita | 0 |
| FormulasMovReader | Formulas de movimentação - Acesso a dados para leitura | 0 |
| FormulasMovRules | Formulas de movimentação - Regras de negócio | 0 |
| FormulasMovWriter | Formulas de movimentação - Acesso a dados para escrita | 0 |
| FormulasMovimentacao | Entidade Formulas de Movimentacao. Manutenção directa á tabela. | 16 |
| Fornecedores | Entidade Fornecedores. Manutenção directa á tabela. | 16 |
| GrelhasTamanhoCores | Grelhas de tamanhos e cores - Acesso a dados, armazenamento memória, contentor principal | 0 |
| GrelhasTerceiros | Entidade Grelhas de Terceiros. Manutenção directa á tabela. | 15 |
| InfoCredito | Implementação da informação de crédito que aparece no introdutor de vendas | 1 |
| InibeReservas | Reservas de Stocks - Implementação da grelha de inibição de reservas | 0 |
| LotesLinha | Lotes, dados de cada linha de lotes que está associada a cada linha de documento também faz acesso a dados para escrita | 0 |
| LotesReader | Lotes, acesso a dados para leitura | 0 |
| LotesRules | Lotes, regras de negócio, usado nos documentos comerciais | 0 |
| LotesWriter | Lotes, acesso a dados para escrita | 0 |
| MeiosPagamento | Entidade Meios de Pagamento. Manutenção directa á tabela. | 16 |
| Moedas | Entidade Moedas. Manutenção directa á tabela. | 17 |
| MoradasAlternativas | Entidade Moradas Alternativas. Manutenção directa á tabela. | 16 |
| MovCTBCab | Ligação á contabilidade, classe que tem os dados da contabilidade geral que são comuns a todas as linhas de movimento do documento | 0 |
| MovimentosCtb2 | Ligação á contabilidade, classe que tem os dados da contabilidade geral e analitica (collection LinhasAnalitica) | 0 |
| MovsAnalitica | Ligação á contabilidade, classe que tem os dados da contabilidade analitica durante o processo de reclassificação de um documento | 0 |
| NomesSeries | Entidade Nomes das Series. Manutenção directa á tabela. | 15 |
| NumSerieLinha | Numeros de serie, Linha de numero de serie associada a linha de documento comercial 1 1 | 0 |
| NumSerieReader | Numeros de serie, implementação da leitura de informação da camada de dados | 0 |
| NumSerieRules | Numeros de serie, implementação das regras de negócio de numeros de serie | 0 |
| NumSerieWriter | Numeros de serie, todas as rotinas que vão escrever dados de numeros de serie, associados a determinado documento comercial | 0 |
| Paises | Entidade Paises. Manutenção directa á tabela. | 16 |
| Pendentes | Entidade Pendentes. Manutenção directa á tabela. | 16 |
| PlanodeContas | Entidade Plano de Contas. Manutenção directa á tabela. | 22 |
| RecContas | Usada na ligação á contabilidade (contabilidaderules.cls) contas com erros de classificação. | 0 |
| RecMoedaTerceiro | Usada na ligação á contabilidade (contabilidaderules.cls) classificação de documentos da área financeira | 0 |
| RegimesIva |  | 16 |
| RegrasVencimento | Entidade Regras de vencimento. Manutenção directa á tabela. | 16 |
| Sage1GCOApi |  | 1 |
| Sectores | Entidade Sectores. Manutenção directa á tabela. | 16 |
| TaxasAdicionais | Entidade Taxas Adicionais. Manutenção directa á tabela. | 16 |
| TerceirosVdi | Entidade Terceiros VDI. Manutenção directa á tabela. | 12 |
| TiposDocumento | Entidade Tipos de documento. Manutenção directa á tabela. | 16 |
| Totais | Classe que armazena os totais de documento durante o processo de recalculo dos mesmos, tem os totais do interface e outros subtotsid usados em calculos intermédios | 0 |
| Unidades | Entidade Unidades. Manutenção directa á tabela. | 21 |
| Vendedores |  | 16 |
| ZonasGeograficas |  | 16 |
| gtcReader | Grelhas de tamanhos e cores - Acesso a dados para leitura, contem coleccção com todas as medidas associadas a um artigo | 0 |
| gtcRules | Grelhas de tamanhos e cores - Regras de negócio | 0 |
| gtcWriter | Grelhas de tamanhos e cores - acesso a dados para escrita | 0 |
