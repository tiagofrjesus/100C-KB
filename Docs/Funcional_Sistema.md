# Sistema — Referência (Administração / Plataforma)

Mapa de administração e plataforma do Sage 100c, destilado de
`Sage 100c Docs/Manuais/Sage100C-Sistema.txt` (manual da Área de Sistema, Sage Jun 2017).
Foco: programador/administrador. Para o configurador de mapas/documentos ver também `Docs/Mapas_Crystal.md`.

> O acesso a todas as funções de administração faz-se na janela de arranque (Sage.BINI.exe),
> botão **Sistema** → área **Responsável de Sistema** (`Sage.BSIS.exe`).

---

## 1. Arquitetura e bases de dados

- ERP em **Microsoft SQL Server**; cliente/servidor (instalação Servidor, Posto ou Monoposto).
- O componente **Servidor** detém a *directoria de ficheiros comuns* (partilhada na rede, permissões totais aos postos). Guarda registo, scripts T-SQL, logs, configs, caches.
- Por defeito: dados em `C:\Sage Data\Main`; postos em `C:\Program Files\Sage\Applications`.
- **Conta SQL única**: todos os postos acedem com uma conta SQL Server (não Windows Auth) com role **sysadmin** — a app usa-a para criar/remover BDs. Instância criada pela app: nome `Sage`, conta `sa` / senha `sage2008+`.
- **Collation** recomendada/instalada: `Latin1_General_CI_AS`; linguagem `English (United States)` (define o formato de inserção de datas `mdy`). Alterar BD: `ALTER DATABASE <bd> COLLATE Latin1_General_CI_AS`.
- **Multiempresa**: uma empresa = sigla única (máx. 15 caracteres) + 3 bases de dados possíveis. Nome da BD = `<Sigla>_<Aplicação>`:

| Aplicação | Sigla interna | BD |
|---|---|---|
| Gestão / Contabilidade | `1GCO` | `<Sigla>_1GCO` |
| Recursos Humanos / Salários | `1GEP` | `<Sigla>_1GEP` |
| Gestão de Ativos | `1GAT` | `<Sigla>_1GAT` |

- **Grupos de Empresa**: agrupam as várias BDs (1GCO, 1GEP, 1GAT) de uma mesma entidade; só uma BD por aplicação por grupo. Têm Sigla, Descrição e NIF.
- Empresas de demonstração (DEMO/MODELO) sempre disponíveis; não editáveis para trabalho real.

---

## 2. Utilizadores e segurança

- **Senha de Sistema** (responsável de sistema): protege a área de administração. Sugerida após licenciamento; configurável em `Sistema → Senha de Sistema`. Remover = senha actual + os dois campos novos vazios. Versão demo não tem limite de acesso.
- **Utilizadores** (`Utilizadores → Novo`/F2): separadores **Identificação** (Login, Nome, senha), **Módulos** (acessos), **Empresas** (quais empresas vê).
- Senha do utilizador define-se na janela de arranque (Identificação → *Alterar senha*); admin pode **Limpar Senha**.
- Por defeito um utilizador novo tem acesso total. Restrições no separador Módulos, em 4 grupos:

| Grupo | Granularidade |
|---|---|
| **Tabelas** | por tabela: Aceder / Anular / Novo / Alterar |
| **Menus** | Global (menu inteiro) ou Particular (opção específica) |
| **Funções** | funções intrínsecas (ex.: alterar taxas de IVA) |
| **Consultas** | Global ou Particular (ex.: margens de artigos) |

- **Perfis**: copiar acessos de um utilizador existente ao criar outro.
- **Copiar Parâmetros** (`Utilizadores → Copiar Parâmetros`): copia parâmetros utilizador/empresa para outros utilizadores/empresas.
- **Estado dos Utilizadores**: quem está ligado (login, nome, posto); refresh 30s.
- Acessos por empresa específicos (só Gestão/Contabilidade): **Acesso por Sectores**, **Sage Search** (entidades pesquisáveis), **Sectores\Séries**, **Parâmetros Gestão**, **Parâmetros Contabilidade**, **Movimentação Sugerida**, **Modelo Impressão**.

---

## 3. Parâmetros e estado da aplicação

- **Abrir empresa**: expõe configurações ocultas conforme o tipo de BD.
- Parâmetros de negócio por empresa em **Parâmetros Gestão / Contabilidade** (acesso por utilizador, ver §2).
- **Estado do Sistema** (`Sistema → Estado do Sistema`): marca o sistema **Indisponível** (bloqueia entrada de todos os postos) com mensagem; repor para **Disponível** para reabrir. Usar antes de manutenção/backup.
- **Informação do Sistema**: relatório HTML (servidor SQL, utilizadores, empresas).

---

## 4. Administração da base de dados (`Sistema`)

| Opção | O que faz |
|---|---|
| **Criar empresa** | Ficha (Identificação/Dados Fiscais), escolha do Servidor SQL, BD modelo (ex.: MODELO), e cria as 3 BDs. Liga a utilizadores e a Grupo de Empresa. |
| **Adicionar BDs** | a empresa existente (editar empresa → *Seguinte* → BDs em falta). |
| **Registar BD** | associa uma BD já existente no servidor a uma empresa (BD deve chamar-se `<Sigla>_<Aplicação>`). |
| **Desregistar dados** | desassocia a BD da empresa **sem** a apagar fisicamente. |
| **Apagar dados** | elimina a BD do disco — **irreversível**. |
| **Alterar sigla** | muda a sigla (identificação única) da empresa. |
| **Compactar BD** | otimiza espaço ocupado. |
| **Backup** | cópia por BD → ficheiro `.bak`; sem outros postos a trabalhar. Não escrever por cima de cópias antigas. |
| **Restore** | repõe a partir de `.bak`. |
| **Reposição de tabelas** | copia tabelas de empresa origem→destino: *Copiar* (acrescenta, opção *Substituir registo se existir*) ou *Substituir* (integral). |
| **Importar** | cópia integral de uma BD para outra (origem semelhante; primeira empresa → base MODELO). |
| **Compatibilizar** | compatibiliza (upgrade) o schema das BDs. |
| **Executar SQL** | corre instruções T-SQL sobre uma BD sem Enterprise Manager (segue regras de ficheiro). |
| **Agendar** | tarefas de manutenção (ver §6). |

**SQL-Server** (sub-área): `Servidores` (propriedades/diagnóstico), `Empresas` (propriedades das BDs), `Adicionar/Remover` servidores, **Processos no servidor** (matar ligações — necessário antes de apagar uma BD), **Desligar/Ligar base de dados** (detach/attach: mover `*.mdf`/`*.ldf` entre servidores; ao ligar pode registar como Empresa 100C).

---

## 5. Customização

- **Personalizar** (barra superior, também na Responsável de Sistema):
  - **Menu Principal** e **Barra de Navegação Lateral** — atalhos/pastas/separadores; personalização **por utilizador**, **comum a todas as empresas**. Novo Atalho pode apontar a opção de menu ou funcionalidade externa.
  - **Área de Trabalho** (working area) — painéis (atalhos, indicadores, notícias RSS); grelha 2×8 (máx. 16 painéis). Personalização **pelo administrador**, **por empresa** (não por utilizador, mas com permissão de ver por utilizador/grupo). Caches de dados em ficheiros encriptados na pasta de rede.
  - É aqui que se **colocam no menu** os mapas/consultas criados (incl. Crystal).
- **Configurador de Mapas / Documentos / Cheques / Etiquetas** (`SageMap.exe`, pasta *Sage Tools*) — cria/altera mapas e modelos de impressão. Inclui SQL especial, campos calculados (Fórmulas, funções `Func_*`), quebras, ordenação, totais. Detalhe em `Docs/Mapas_Crystal.md`.
- **Crystal Reports**: mapas `.rpt` à medida (licença adicional); colocados no menu via *Personalizar*.

---

## 6. Ferramentas / utilitários de sistema

- **Agendar** (tarefas na Responsável de Sistema). Tipos: **Backup**, **Executar SQL**, **Compactar**, **Compatibilizar**. Periodicidade: Diária / Semanal / Mensal / **Externa**. Campo *Alertar após x dias* (máx. 365) → ao exceder, bloqueia entrada até executar a tarefa.
  - Execução pelo **Task Scheduler do Windows** sem a RS aberta:
    `Sage.BSIS.exe /Tasks` (verifica e corre pendentes) · `Sage.BSIS.exe /Task=BACKUP1 /Task=BACKUP2` (corre tarefas nomeadas).
- **Atualizações via web**: descarrega tabelas oficiais da Sage (taxas IRS, coeficientes…) e aplica a empresas escolhidas; fazer backup antes.
- **Solução de Customização**: regista/desregista soluções SDK (a Sage distribui um exemplo por aplicação).
- **Configurar → Percursos (Editor de Configurações)** (`EditWin.exe`): directorias (Catálogos, Aplicação, Imagens web, Ficheiros comuns) e apps de exportação (Excel/Word/PDF…).
- **Configurar → SMTP**: servidor de correio para envio por e-mail (alternativa ao Outlook); `PorEMail.exe`.
- **Licenciamento** (`Licenciar`): por aplicação ou todas (RS). Registo via Internet (código+palavra-passe) ou via ficheiro (portal My Sage → Chave de Cliente/Chave de Ativação). Ativar até **30 dias** após registo, senão volta a demo.
- **Exportação de listas**: Texto, Excel (incl. Pivot), Word, RTF, JPEG, PDF; máx. 3 envios e-mail em simultâneo.

---

## 7. Notas para developers

**Ficheiros na directoria partilhada (servidor)** — relevantes para integração/automação:

| Ficheiro | Conteúdo |
|---|---|
| `UI 100C.dat` | personalizações de menus/barras/áreas de trabalho |
| `INFRS.Tasks.dat` | tarefas agendadas da Responsável de Sistema |
| `Sage.Licenses.Manifest.dat` | dados de licenciamento (apps/módulos licenciáveis) |
| (registo XML encriptado) | empresas + utilizadores + senhas/níveis/aplicações por empresa |
| `<Sigla>.LK?` | ficheiros temporários de acessos concorrentes (locks) |
| `<Utilizador>.up2.xml` | preferências globais do utilizador (servidor) |
| `<Utilizador>.up1.xml` | preferências locais do utilizador (posto) |

**Executáveis-chave (posto)**: `Sage.BINI.exe` (arranque, comum à linha 100C) · `Sage.BSIS.exe` (Responsável de Sistema; aceita switches `/Tasks`, `/Task=`) · `SageMap.exe` (configurador) · `EditWin.exe` (editor de configurações) · `<Aplicação>.exe` = `SAGE.1GCO` / `SAGE.1CTB` / `SAGE.1GAT` / `SAGE.1SLR`.

**Formatos de ficheiro de configuração** (citados no manual):

| Extensão | Conteúdo |
|---|---|
| `.rpt` | mapas/documentos em **Crystal Reports** |
| `.mps` | mapas no formato SageMap (todos num ficheiro) |
| `.lst` | configuração de **um** mapa SageMap (`<Nome>.LST`) |
| `.tls` | índice/títulos de todos os mapas SageMap (`<Aplicação>.TLS`) |
| `.anl` | configurações de documentos e consultas (SageDoc) |
| `.cat` / `100C.<Aplicação>.cat` | definições da base de dados (catálogo) |
| `.cba` | definições da BD (formato antigo) |
| `.jnl` | desenho das janelas |
| `.lig` | atalhos para funções |
| `.cal` | campos calculados de mapas/consultas |
| `.fnd` | formatos de mapas |
| `.def` | fórmulas dos mapas de Contabilidade/RH |

> No configurador, **Criar LST** explode o `.mps` distribuído em `.lst` individuais; **Criar TLS** regenera o índice `<Aplicação>.TLS`. Usar sempre `.lst` novo para não substituir o original.

**Integração / camadas** (ver `Docs/Modulos.md`): SQL direto só leitura/escrita em tabelas do cliente; documentos sempre via **API .NET** (`Sage1GCOApi`); automação via **SDK COM** (objeto `Aplicacao`, ver `Docs/SDK_ObjectModel.md`). A app fala com SQL Server pela conta sysadmin única; credenciais SMTP em `Configurar → SMTP`. Não citar nomes de tabelas sem confirmar em `Docs/DD_Catalog_<MOD>.md`.
