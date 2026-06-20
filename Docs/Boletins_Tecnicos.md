# Boletins Técnicos — Histórico de Versões

> Fontes: `Sage 100c Docs/Manuais/BT_Sage_100cloud_2026.txt`,
> `Sage 100c Docs/Manuais/BT_Sage_100cloud_2023.txt`,
> `Sage 100c Docs/Manuais/Sage_100c_V2018.01.07.txt`.
> Objetivo: ver que funcionalidades/correções existem em cada versão e desde quando.
> A lista completa de correções está nas fontes — aqui resume-se o essencial para dev/integração.

---

## 2026 (2026.01.x / 2026.02.x)

### 2026.02.02 (Build 213) — 21 mai 2026
- **RH:** Relatório Único — atualização do validador para o ano 2025.

### 2026.02.01 (Build 212) — 12 mai 2026
- **Plataforma:** EULA unificada com Termos & Condições (documento legal único); novas cláusulas sobre **Inteligência Artificial**, Cookies e Customer Services; opção no menu Ajuda para consulta permanente dos T&C (aceitação obrigatória na instalação). Tratamento de prémios de produtividade/desempenho, participações nos lucros e gratificações de balanço (Portaria 289/2025/1; art. 115.º CIRS, OE2025).
- **RH:** Atualização da tabela de freguesias (nova codificação INE) — rever ficha de empresa e estabelecimentos. **Segurança Social** — novo campo em *Entidades e taxas > Centros regionais de SS* para código de enquadramento do regime; comunicação de vínculo de trabalhadores por **webservice** passa a incluir o enquadramento.
- **Gestão:** Validação de **tipos de IVA** à entrada da aplicação (taxa, tipo de imposto, região, motivo de isenção); assistente para marcar tipos com taxas inválidas como expirados; sugestão de taxas por espaço fiscal. **Motivos de isenção SAF-T** com data limite e validação do tipo de imposto (TaxType "Não sujeito" → só M99). Na movimentação de vendas, bloqueio de motivos expirados; **M31** só com cliente sujeito passivo de IVA; aviso informativo no **M09** (só pequenos retalhistas). **Guias de Transporte — comunicação à AT via API** (substitui mecanismos antigos).
- **Correções (dev/integração):** sugestão 132654 (API comunicar documentos à AT, ex.: GTs); 146530 (API permitia linha com taxa IVA ≠ 0 com motivo de isenção); 125994 (introdução automática SAF-T vendas não arredonda). Lista completa na fonte.

### 2026.01.06 (Build 211) — 24 mar 2026
- **Contabilidade:** Modelo 22 e Modelo 3 (e suporte magnético) atualizados para entrega em 2025. Correções Bizdocs (ligação a documentos da GC; pesquisa e-fatura).

### 2026.01.05 (Build 210) — 17 mar 2026
- **Gestão:** **Sistema de Depósito e Reembolso** (depósito sobre embalagens de bebidas não reutilizáveis até 3 L; símbolo *Volta* a partir de mar 2026).
- **Plataforma/Conta Sage:** nova app de autenticação 2FA **Sage Verify** (push em vez de código de 6 dígitos; opcional; preferencial para novos utilizadores e reset de 2FA).

### 2026.01.04 (Build 209) — 23 fev 2026
- **RH:** **DMR-AT** atualizada para entrega em 2026 (Portaria 69/2026/1); novo código **A34** (compensações a bombeiros) e revisão da descrição do **A41** (prémios/gratificações).
- **Contabilidade:** correção DPIVA (ano 2026 na relação de fornecedores). Correção 146862 (erro 100 ao comunicar cessação de vínculo à SS).

### 2026.01.03 (Build 208) — 23 fev 2026
- **RH:** Cálculo do número de dias de tempo trabalhado a declarar à SS (Decreto Regulamentar 7/2025: 1 dia por cada 5 horas, máx. 30 dias/mês).
- **Correções:** 141040 e 146778 (API — transferências entre armazéns e `objContabDoc.cab.Referencia` no movimento contabilístico); reconciliação bancária.

### 2026.01.02 (Build 207) — 22 jan 2026
- **Gestão:** novos mapas de **Existências à consignação** (Stocks > Relatório de stocks > Existências).
- **Correções:** anulação de REC/NC corrompia assinatura; recibo de adiantamento não exportado para SAF-T; reconciliação bancária automática.

### Plataforma — 3 dez 2025 (aplicável à 2018.01.01, setup completo)
- **Plataforma:** **Sage Self-Service** — loja de aplicações/add-ons nativos Sage e de terceiros.
- **Contabilidade:** **Bank Feeds** (Sage Banking Service via GoCardless/AISP, Open Banking — recolha automática de extratos para reconciliação). **Arquivo Digital Cloud** (associação do documento físico ao movimento contabilístico).

---

## 2023 (2023.01.x / 2023.02.x)

### Novidades por área

**Plataforma**
- 2023.02.01: Rebranding; consola de estado/reenvio de documentos à AT passa a guardar no arquivo digital; validação do código de comunicação AT introduzido manualmente (só consoantes maiúsculas e algarismos, exceto 0 e 1).

**Gestão / Faturação e AT**
- 2023.01.01 (Build 148): Controlo da **data de carga/descarga** e do **SystemEntryDate** (faturação e recebimentos); Documentos Internos com parâmetro para não movimentar encomendas de cliente; tabela de **motivos de isenção** atualizada (M03 e M08 deixam de ser aplicáveis); **Sage Inventários** sugere ficheiro v2.01 (Portaria 126/2019); validação da impressão de **ATCUD** nos modelos; **controlo de incoerências nos diários**; **comunicação à AT por webservice** alargada aos *WorkingDocuments* (OR, NE, FC, CC) e *Payments* (RC — IVA de caixa); importação SAF-T de faturação valida NIF do ficheiro contra o da empresa; Backup/Restore com checksum Sage.
- 2023.01.02 (149): assistente de "Nova Série" cobre Orçamentos, Encomendas e Recibos; FE AP/Generix com campo **ATCUD**.
- 2023.01.03 (150): **comunicação em lote de séries à AT**.
- 2023.01.04 (151): FE AP/Generix com **QRCode Text**; melhorias à comunicação de séries (data/número sugeridos).
- 2023.01.05 (153): **comunicação de séries e de documentos de autofaturação à AT via webservice**; recibos com discriminação da taxa de IRS (`GepVenReciboA4.lst`, `GepVenReciboA4-OriginalDuplicado.lst`, `SQLRecibos Por Email.rpt`, `NGEP_Recibo.rpt`).
- 2023.01.07 (155): séries de **"Autofaturação sem acordo"** (ex-"Fornecedor Genérico").
- 2023.01.10 (160): utilitário **Sage IVA 2023 — Cabaz de alimentos** (alteração do regime de IVA dos artigos).
- 2023.02.02 (162): FE AP/Generix inclui **Motivo de isenção** no ficheiro.
- 2023.02.07 (168): ação para marcar documento como "Já comunicado" (status -10 Invoices / -22 WorkingDocuments) em Consulta de estado/reenvio e em Vendas.

**Contabilidade**
- 2023.01.08 (158): novo Jar de comunicação SAF-T (`FACTEMICLI-2.5.26-44872-cmdClient.jar`); Modelo 3 (período 2022); Relatório Único v14 (dados 2022).
- 2023.01.04 (151): Modelo 39, Modelo 10 e **IES** versão 2023 (dados 2022).
- 2023.01.07 (155): Modelo 22 para entrega em 2023; alerta de movimentos Suspensos na criação de declarações fiscais.
- SVAT/2023.01.01: registo de alterações de lançamentos (auditoria), controlo de incoerências nos movimentos, regras de status Suspenso/Efetivo, diários para status extra contabilístico, SAF-T global anual em exercícios fechados.

**Recursos Humanos**
- 2023.01.01–.04: **DMR-AT** versão 2023 (Portaria 307/2022); Modelo 10 (Portaria 8/2023); IRS Jovem ajustado ao OE2023; redução de retenção para titulares de crédito à habitação (art. 155.º OE2023).
- 2023.01.05 (153): redução para metade da retenção autónoma de IRS no trabalho suplementar a partir da 101.ª hora.
- 2023.02.01 (161): novas tabelas de retenção IRS 2.º semestre 2023 (Despacho 14043-B/2022 e 4930/2023); alterações ao Código do Trabalho (compensação por cessação); fim do desconto FCT/FGCT; **comunicação da DMR SS por webservice**.
- 2023.02.05 (166): processamento conforme Ofício Circulado 20258 (tabelas de retenção desde jul/2023).
- 2023.02.06 (167): funcionário **residente não habitual** (taxa fixa 20%, art. 99.º n.º 8 CIRS); fator de multiplicação para dependentes com incapacidade ≥ 60% (Despacho 7673-B/2023); importação de relógio de ponto marca faltas em dias de ócio; faltas em horas em dias de descanso/feriado.
- 2023.01.03 (150): comunicação de **vínculos à SS, FCT e ACT** (consulta de contratos, cessação, alterações, comprovativos); comunicação de novos períodos de rendimento.

### Alterações/correções relevantes para dev/integração (amostra)

| # | Área | Tema |
|---|---|---|
| 129278 | Gestão/API | Inserir recibo via API não preenche linhas |
| 143317 | Gestão/API | Documento em preparação não respeita data das linhas |
| 142402 | Gestão/API | Anular CCF não faz estorno do movimento CTB |
| 142006 / 138887 | Gestão/API | API não insere financeiros; documento "em uso noutro posto" |
| 141666 / 141818 | Gestão/API | SELECT à tabela PENDENTES; não herda relação empresa do -1 |
| 140387 | Gestão/API | API integra movimentos em diários fechados |
| 127146 / 141865 | SAF-T | Erro validação SAF-T 1.04 (TaxPercentage); CreditAmount no simplificado |
| 142068 | SAF-T | Submissão com valores calculados pela AT diferentes |
| 143387 / 143372 / 141601 | CIUS-PT | GLN do local de mercadoria; nº de conservatória; extensão `.xmlxml` |
| 143623 | CIUS-PT | Erro de motivo de isenção ao validar |
| 142913 | CIUS-PT | `InvoiceDocumentReference` mal preenchido |
| 140917 | CIUS-PT | Regenerar/substituir ficheiro existente no arquivo digital |
| 142013 / 142000 | Séries/AT | Série externa e autofaturação não aceitam código/ATCUD AT |
| 142032 | Ligação CTB | Documento anulado passa à contabilidade como suspenso |
| 142235 | Ligação CTB | Alterar documento de compra elimina a contabilidade |
| 141085 | Ligação CTB | NC sobre FR coloca movimento CTB como excluído |
| 141761 | SDK | Importação elimina campos SDK / do introdutor |
| 140594 | Crystal | `SQLFACTLOT.RPT` não imprime |
| 137177 | Crystal | `SQLFACTCLIRtf.rpt` soma 1.ª linha na página seguinte |
| 141241 | Crystal | `TALAO.RPT` só imprime até 3 linhas de artigo |
| 143212 | Crystal | mensagem em `NGCO_PrepExpedicaoCli.rpt` |
| 141958 | Crystal | `SQLFACTFORRTF.RPT` usa morada errada |
| 128786 | Export | Exportação PDF com dupla extensão (`.pdf .pdf`) |

> Lista completa de correções (centenas de linhas "NNNNNN : descrição") na fonte `BT_Sage_100cloud_2023.txt`.
> Versão do **Crystal Reports Runtime 13.0.34** introduzida na 2023.02.09 (Build 170); a build corrige conflito de instalação com Sage X3 em Crystal 30.

---

## 2018.01.07 — Customização de menus (out 2017)

- **Customização de menus:** o utilizador acrescenta/remove atalhos nos menus existentes para aplicações, mapas Crystal, consultas, documentos, mapas e etiquetas. Customização por utilizador, em todas as BDs a que tem acesso; o tipo **Administrador** pode tornar atalhos disponíveis para todos os utilizadores.
- **Novo Atalho** (botão do utilizador, canto superior direito): posicionar primeiro no menu/separador de destino (ex.: "Vendas"). Tipos:
  - **Executar Aplicação** — aplicação externa (`.exe`), com campo *Argumentos*.
  - **Mapa Crystal** — mapas `.rpt` criados para a empresa.
  - **Consulta/Documento** — ficheiros `.anl`.
  - **Mapa/Etiqueta** — ficheiros `.lst`.
- **Configuração:** Nome, Descrição (tooltip), Acesso (todos/próprio — só Administrador), Ficheiro, Argumentos.
- **Remover:** marca como "removida"; só desaparece após gravar.
- **Posicionamento/Favoritos:** atalhos à esquerda na barra superior e por baixo na barra lateral; podem ser arrastados para a zona de **Favoritos**.

---

## Notas para developers

- **Ficheiros `.rpt`/`.lst` mencionados:** `SQLFACTLOT.RPT`, `SQLFACTCLIRtf.rpt`, `SQLFACTFORRTF.RPT`, `TALAO.RPT`, `NGCO_PrepExpedicaoCli.rpt`, `NGEP_Recibo.rpt`, `SQLRecibos Por Email.rpt`, `GepVenReciboA4.lst`, `GepVenReciboA4-OriginalDuplicado.lst`. Modelos de impressão de documentos fiscais (desde 2023) têm de incluir o campo **ATCUD**.
- **Customização de mapas/atalhos:** extensões reconhecidas pela aplicação — `.exe`, `.rpt` (Crystal), `.anl` (consultas/documentos), `.lst` (mapas/etiquetas).
- **API (.NET / COM) — comportamentos a ter em conta:** historicamente bugs em inserção de financeiros, herança da relação de empresa do cliente/fornecedor -1, SELECT a PENDENTES vs PENDENTE, integração em diários fechados, estorno de movimento CTB ao anular, `objContabDoc.cab.Referencia` no movimento, transferências entre armazéns sem lançamento contabilístico. Desde 2026, a API permite **comunicar documentos à AT (ex.: Guias de Transporte)**; valida taxa de IVA vs motivo de isenção nas linhas.
- **SAF-T:** versões validadas SAF-T 1.04; recibos fora do regime de IVA de Caixa não geram estrutura `Tax` e `TaxPayable=0.00` (`NetTotal`=`GrossTotal`); IVA de Caixa (`PaymentType="RC"`) discrimina imposto. Jar de comunicação: `FACTEMICLI-2.5.26-44872-cmdClient.jar` (2023.01.08). Comunicação por webservice à AT alargada a *WorkingDocuments* (OR, NE, FC, CC) e *Payments* (RC).
- **CIUS-PT:** exportação para `.xml`; campos GLN do local de entrega, nº de conservatória, `InvoiceDocumentReference`; possibilidade de regenerar/substituir o ficheiro já existente no arquivo digital; FE AP/Generix inclui ATCUD, QRCode Text e Motivo de isenção.
- **Crystal Reports Runtime:** versão **13.0.34** desde 2023.02.09 (Build 170); cuidado com coexistência com Sage X3 (Crystal 30).
- **Motivos de isenção SAF-T (regras correntes):** M03/M08 descontinuados (2023); M31 exige cliente sujeito passivo; M09 só pequenos retalhistas; TaxType "Não sujeito" → M99; motivos têm **data limite** e a aplicação bloqueia os expirados (2026).
- **Segurança Social por webservice:** DMR SS (desde 2023.02.01), vínculos/FCT/ACT (2023.01.03), e enquadramento do regime no vínculo de trabalhadores (2026.02.01).
- **Integridade/auditoria (contabilidade):** controlo de incoerências em diários e movimentos, registo de alterações de lançamentos, status Suspenso/Efetivo e diários para status extra contabilístico (desde 2023.01.01 / SVAT).
- **Autenticação:** 2FA via **Sage Verify** (push) desde 2026.01.05; **Conta Sage** como camada de identidade.
