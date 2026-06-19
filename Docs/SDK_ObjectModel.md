# SDK 100C — Modelo de Objetos (C100SDK)
> Automacao COM/ActiveX da aplicacao 100C. Exemplos em VBScript/VBA. Ponto de entrada: objeto **Aplicacao**.

## Classes

- **Aplicacao** — Ponto de entrada do SDK. SQL, vistas, listas, iteradores, Crystal e mensagens. (15 membros)
- **Empresa** — Dados da empresa ativa (sigla, designacao, versao). (4 membros)
- **Utilizador** — Utilizador autenticado (login, nome). (2 membros)
- **Contexto** — Contexto de um registo: ler/escrever campos, gravar, criar iteradores. (12 membros)
- **Campo** — Campo de um contexto: valor, texto, descricao, foco, validacao. (8 membros)
- **Iterador** — Percorre registos de SQL ou vista (LerRegisto, Fim, Campo). (5 membros)

---

## Aplicacao

Ponto de entrada do SDK. SQL, vistas, listas, iteradores, Crystal e mensagens.

| Membro | Assinatura | Descricao |
|---|---|---|
| AbrirLista | Public Sub AbrirLista(ByVal NomeVista As String) | Abre a lista para a vista indicada |
| AbrirVista | Public Sub AbrirVista(ByVal NomeVista As String) | Abre a manutenção de uma vista indicada |
| CriarIteradorSql | Public Function CriarIteradorSql(ByVal Sql As String) As Iterador | Devolve um objecto iterador para navegação nos registos seleccionados a partir de uma instrução SQL |
| CriarIteradorVista | Public Function CriarIteradorVista(ByVal NomeVista As String, ByVal Where As String) As Iterador | Devolve um objecto iterador para navegação nos registos seleccionados numa determinada vista |
| EmitirCrystal | Public Sub EmitirCrystal(ByVal NomeMapa As String, Optional ByVal Destino As Integer = 0) | Abre a emissão do mapa crystal com nome para o Destino: 0 = Ecrãn, 2 = Impressora |
| ExecutarSql | Public Function ExecutarSql(ByVal Sql As String) As Boolean | Executa uma instrução SQL sobre a base de dados em utilização Normalmente usado para inserir ou alterar dados em outras tabelas criadas pelo utilizador no âmbito da costumização. |
| Get.Descricao | Public Property Get Descricao() As String | Descrição da aplicação |
| Get.Empresa | Public Property Get Empresa() As Empresa | Representa informação sobre a empresa em uso na 100C |
| Get.Nome | Public Property Get Nome() As String | Nome da aplicação |
| Get.Utilizador | Public Property Get Utilizador() As Utilizador | O objecto utilizador representa o utilizador que está no momento no sistema |
| Get.hWnd | Public Property Get hWnd() As Long | A janela representada na propriedade hWnd deve ser utilizada como pai para todas as janelas construidas em componentes externos à 100C. |
| Mensagem | Public Function Mensagem(ByVal Texto As String, Optional ByVal Botoes As Integer = vbOKOnly + vbInformation, Optional ByVal Titulo As String = "") As Integer | Envia uma mensagem ao utilizador da aplicação |
| Operacao | Public Sub Operacao(ByVal Operacao As Long) | Executa uma operação SDK definida pelo utilizador ao nível da aplicação. |
| SqlValor | Public Function SqlValor(ByVal Sql As String) As String | Esta função é normalmente utilizada para obter resultados de uma soma de registos de outra tabela ou de um valor especifico de um campo para um registo. |
| SqlValores | Public Function SqlValores(ByVal Sql As String, Campos As Variant) As Boolean | Esta função é normalmente utilizada para obter resultados do acesso a um determinado registo |

## Empresa

Dados da empresa ativa (sigla, designacao, versao).

| Membro | Assinatura | Descricao |
|---|---|---|
| Get.Designacao | Public Property Get Designacao() As String | Designação da empresa em utilização |
| Get.Sigla | Public Property Get Sigla() As String | Código da empresa em utilização |
| Get.Versao | Public Property Get Versao() As Integer | Versão do catálogo de dados da empresa em utilização |
| Get.VersaoX | Public Property Get VersaoX() As Integer | Versão do catálogo do projecto SDK associado à aplicação em utilização |

## Utilizador

Utilizador autenticado (login, nome).

| Membro | Assinatura | Descricao |
|---|---|---|
| Get.Login | Public Property Get Login() As String | Código do utilizador da aplicação 100C |
| Get.Nome | Public Property Get Nome() As String | Nome do utilizador da aplicação 100C |

## Contexto

Contexto de um registo: ler/escrever campos, gravar, criar iteradores.

| Membro | Assinatura | Descricao |
|---|---|---|
| Campo | Public Function Campo(Optional ByVal Nome As String = "") As Campo | Instância do objecto que representa um campo da vista |
| CriarIterador | Public Function CriarIterador(Optional ByVal Where As String = "") As Iterador | Devolve um objecto iterador para navegação nos registos seleccionados para a vista referida no objecto contexto |
| Fechar | Public Sub Fechar() | Fecha a janela da vista em edição (O mesmo que carregar no botão Fechar) |
| Get.Api | Public Property Get Api() As Object | Devolve um objecto API da aplicação em causa |
| Get.Descricao | Public Property Get Descricao() As String | Descrição da vista actual ou da aplicação |
| Get.Nome | Public Property Get Nome() As String | Nome da vista actual ou da aplicação |
| Get.NomeBase | Public Property Get NomeBase() As String | Nome da tabela base associada ao contexto |
| Get.Valor | Public Property Get Valor(ByVal Nome As String) As String | Obtém o Valor do campo de uma vista indicado no parâmetro nome |
| Gravar | Public Sub Gravar() | Provoca a gravação do registo em edição (O mesmo que carregar no botão Confirmar) |
| Let.Valor | Public Property Let Valor(ByVal Nome As String, ByVal Valor As String) | Escreve um valor no campo da vista |
| Mensagem | Public Function Mensagem(ByVal Texto As String, Optional ByVal Botoes As Integer = vbOKOnly + vbInformation, Optional ByVal Titulo As String = "") As Integer | Envia uma mensagem ao utilizador da aplicação |
| Valido | Public Function Valido() As Boolean | Provoca a validação do registo actual na vista (A mesma validação executada ao carregar em confirmar) |

## Campo

Campo de um contexto: valor, texto, descricao, foco, validacao.

| Membro | Assinatura | Descricao |
|---|---|---|
| Get.Descricao | Public Property Get Descricao() As String | Representa a descrição do campo |
| Get.Nome | Public Property Get Nome() As String | Representa o nome do campo |
| Get.NomeBase | Public Property Get NomeBase() As String | Representa o nome do campo na tabela base |
| Get.Texto | Public Property Get Texto() As String | Devolve o texto associado ao elemento |
| Get.Valor | Public Property Get Valor() As String | Devolve o valor armazenado no campo |
| Let.Valor | Public Property Let Valor(ByVal Value As String) | Escreve um valor no conteúdo do objecto campo |
| PoeFoco | Public Sub PoeFoco() | Coloca o Focus (Posiciona o cursor) no campo |
| Valido | Public Function Valido() As Boolean | Verifica a validade do valor no campo |

## Iterador

Percorre registos de SQL ou vista (LerRegisto, Fim, Campo).

| Membro | Assinatura | Descricao |
|---|---|---|
| Campo | Public Function Campo(ByVal Nome As String) As String | Retorna o conteúdo do campo passado como parâmetro |
| Fechar | Public Sub Fechar() | Fecha o cursor para a base de dados relativo ao iterador em uso |
| Fim | Public Function Fim() As Boolean | Move o cursor para o próximo registo e retorna False se não estiver no último, retorna True se estiver no último. |
| Get.TemRegistos | Public Property Get TemRegistos() As Boolean | Indica se o cursor contém pelo menos um registo |
| LerRegisto | Public Function LerRegisto(Campos As Variant) As Boolean | Copia para um array de strings passado por referência os valores dos campos do registo actual |

