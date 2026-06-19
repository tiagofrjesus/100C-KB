# Mapas (Crystal Reports) no Sage 100c

Os mapas/relatórios do 100C são **Crystal Reports** (`.rpt`) cuja fonte de dados são queries SQL
sobre as tabelas e vistas do dicionário de dados.

## Fluxo para criar/alterar um mapa

1. **Modelar os dados** — identifica as tabelas/vistas no catálogo (`DD_Catalog_<MOD>.md`) e lê os
   `.txt` (`DD/<MOD>/<TABELA>.txt`) para colunas, tipos e chaves.
2. **Query** — escreve e valida a query que alimenta o mapa segundo as regras de SQL da skill
   (base `<SIGLA>_<MODULO>`, nomes exatos, validações para campos de estado, JOINs com chaves confirmadas).
3. **Desenhar o .rpt** — no Crystal Reports, ligar a query/tabelas e desenhar o layout.
4. **Emitir** — pela aplicação, ou por código via SDK.

## Emitir por código (SDK)

```vbscript
' obj é o objeto Aplicacao do SDK 100C
obj.EmitirCrystal "NomeDoMapa", 0   ' Destino: 0 = ecrã, 2 = impressora
```

Assinatura: `Public Sub EmitirCrystal(ByVal NomeMapa As String, Optional ByVal Destino As Integer = 0)`
(ver `SDK_ObjectModel.md`, classe `Aplicacao`).

## Notas

- Para listagens ad-hoc sem desenhar `.rpt`, usar `Aplicacao.AbrirLista`/`AbrirVista` ou um
  iterador SQL (`Aplicacao.CriarIteradorSql`) e tratar os dados no script.
- Confirma sempre o nome interno do mapa na instalação do cliente antes de o emitir por código.
