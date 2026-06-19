# Sage 100c — Módulos, Bases de Dados e Estrutura

Sage 100c é um ERP português da Sage, sobre **SQL Server**. Cada módulo tem a sua base de dados.

## Módulos

| Código | Módulo | Base de dados SQL | Conteúdo |
|---|---|---|---|
| `1GCO` | Sage Gestão Empresarial / Comercial | `<SIGLA>_1GCO` | Clientes, fornecedores, artigos, documentos comerciais, contabilidade, tesouraria |
| `1GAT` | Sage Gestão de Ativos | `<SIGLA>_1GAT` | Fichas de ativos, depreciações, abates, reavaliações |
| `1GEP` | Sage Salários | `<SIGLA>_1GEP` | Processamento de salários, funcionários |

`<SIGLA>` = código da empresa. A base de dados chama-se `SIGLA_MODULO`, ex.: `DEMO_1GCO`, `MODELO_1GAT`.
Empresas de exemplo fornecidas: **DEMO** e **MODELO** (backups em `D:\Git\Sage100C\DB-Demo-Modelo\*.bak`).

## Tipos de entidade no dicionário de dados

| Entidade | O que é | Onde |
|---|---|---|
| **Tabela** | Tabela física SQL Server (schema `dbo`) | `DD_Catalog_<MOD>.md` + `DD/<MOD>/<T>.txt` |
| **Vista** | View da aplicação; muitas são views SQL queryáveis | `Vistas_<MOD>.md` |
| **Validação** | Regra de valores de um campo (lista fixa ou lookup a tabela interna) — equivalente aos *local menus* do X3 | `Validacoes_<MOD>.md` |

## Camadas de desenvolvimento

1. **SQL direto** (SQL Server) — leitura/relatórios/mapas. Escrita só em tabelas do cliente.
2. **SDK 100C** (`C100SDK.exe`, automação COM/ActiveX) — VBScript/VBA; objeto `Aplicacao`.
3. **API .NET** (`Sage1GCOApi`) — lógica de negócio completa para documentos/entidades.

## Documentação de origem (em `D:\Git\Sage100C`)

| Pasta | Conteúdo |
|---|---|
| `DicionarioDados/` | Catálogos HTML do dicionário de dados (1GAT/1GCO/1GEP) |
| `ApiGestao/ApiDocumento/` | `Sage.1GCO.Api.Documentação.pdf` (guia da API) |
| `ApiGestao/ApiHelpHTML/` | Help HTML da API (classes e métodos) |
| `ApiGestao/ApiSage100cConnectCSharp/` | Exemplo C# — integrador por XML (ApiService.Ini) |
| `ApiGestao/ApiSage100cLaunchCSharp/` | Exemplo C# — formulários (artigos, clientes, documentos) |
| `100C SDK/` | `C100SDK.exe`, Help do modelo de objetos, explorador de catálogos |
| `DB-Demo-Modelo/` | Backups SQL Server das empresas DEMO e MODELO |
