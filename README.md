# 100C-KB — Knowledge Base Sage 100c para Claude

Índices de referência, schemas de tabelas e uma skill Claude Code para desenvolvimento em
**Sage 100c** (SQL, mapas Crystal, SDK COM e API .NET).

Estrutura espelhada na do `C:\X3-KB` (a KB equivalente para Sage X3).

---

## O que tem dentro

| Caminho | Conteúdo |
|---|---|
| `Docs/` | Índices pré-construídos — catálogos de tabelas, vistas, validações, API, modelo SDK, mapas |
| `Docs/Funcional_*.md` | Referências funcionais por módulo (Gestão, Contabilidade, Ativos, RH, Sistema) — destiladas dos manuais oficiais |
| `Docs/Integracao_*.md` | Specs de integração — EDI (GENERIX) e faturação eletrónica UBL 2.1 (CIUS-PT) |
| `Docs/Relacoes_*.md` | Relações DERIVADAS entre tabelas (JOINs canónicos verificados) — 1GCO/1GAT/1GEP |
| `Docs/Boletins_Tecnicos.md` | Histórico de versões (novidades/correções) |
| `Sage 100c Docs/DD/<MOD>/` | Schema `.txt` por tabela (colunas, tipos, chaves) — 1GAT/1GCO/1GEP |
| `Sage 100c Docs/API/` | `.txt` por classe da API .NET (90 classes) |
| `Sage 100c Docs/Manuais/` | Texto completo dos manuais oficiais (grepável) — fonte das referências funcionais |
| `Sage 100c Docs/build_*.py` | Scripts que reconstroem os índices a partir da documentação fonte |
| `.claude/commands/sage100c.md` | A skill `/sage100c` |
| `CLAUDE.md` | Regras de desenvolvimento (carregadas quando esta pasta é o workspace) |
| `PROJECT.md` | Template — preencher por cliente/projeto |

Conteúdo: **832 tabelas**, **1097 vistas**, **932 validações** (1GAT+1GCO+1GEP), **90 classes** de API, modelo de objetos do SDK, **5 referências funcionais** por módulo, **2 specs de integração** (EDI/UBL), **3 mapas de relações entre tabelas** (1GCO/1GAT/1GEP) e histórico de versões.

---

## Instalação

A KB deve estar em **`C:\100C-KB\`** (a skill usa caminhos absolutos para esta localização).

Instalar a skill globalmente (disponível em qualquer workspace):

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\commands"
Copy-Item "C:\100C-KB\.claude\commands\sage100c.md" "$env:USERPROFILE\.claude\commands\sage100c.md" -Force
```

---

## Uso

1. Abre a pasta do teu projeto 100c no Claude Code
2. Escreve `/sage100c` — o Claude carrega as regras e lê o `PROJECT.md` do workspace
3. Trabalha normalmente — os lookups ao KB acontecem antes de escrever qualquer query/código

Para um projeto novo, copia o `PROJECT.md` para a raiz do repo do projeto e preenche a sigla da
empresa e os módulos ativos.

---

## Reconstruir os índices

Se a documentação fonte em `D:\Git\Sage100C` for atualizada, reconstrói (precisa de Python 3):

```powershell
$env:PYTHONIOENCODING = "utf-8"
cd "C:\100C-KB\Sage 100c Docs"
python build_dd.py     # dicionário de dados  -> Docs/DD_*.md, DD_*/.txt, Vistas_*, Validacoes_*
python build_api.py    # API .NET             -> Docs/API_Index.md, API/*.txt
python build_sdk.py    # modelo de objetos SDK -> Docs/SDK_ObjectModel.md
python build_relacoes.py report   # material bruto p/ relações -> rel_<MOD>.md (curado à mão em Docs/Relacoes_*.md)
```

> `build_relacoes.py` apenas gera o **material bruto** (pares CAB/LIN, masters de PK única, índice
> invertido coluna→tabelas). Como o dicionário 100c não tem FKs, os `Docs/Relacoes_*.md` são
> **curados manualmente** a partir desse material e verificados contra os `.txt`.

Codificação: os HTML do dicionário estão em UTF-8; os da API e do SDK em cp1252/ISO-8859-1
(os scripts já tratam cada caso).
