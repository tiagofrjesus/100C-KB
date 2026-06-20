# -*- coding: utf-8 -*-
"""Parse all DD/<MOD>/<TABLE>.txt into {table: {desc, pk, uniques, idx, cols}} and
build an inverted index col -> [tables]. Used to derive table relationships
heuristically (no native FKs in the Sage 100c dictionary)."""
import os, re, json, sys

DD = r"C:\100C-KB\Sage 100c Docs\DD"
MODS = ["1GCO", "1GAT", "1GEP"]

def parse_table(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        lines = f.read().splitlines()
    name = os.path.splitext(os.path.basename(path))[0]
    desc = ""
    m = re.match(r"^\S+ — (.*?)\s+\[", lines[0]) if lines else None
    if m: desc = m.group(1)
    pk, uniques, idxs, cols = [], [], [], []
    mode = None
    for ln in lines:
        s = ln.strip()
        if s.startswith("Keys / Indices"): mode = "keys"; continue
        if s.startswith("Columns"): mode = "cols"; continue
        if not s: continue
        if mode == "keys":
            # "  NAME [tags]: A+B+C"
            km = re.match(r"^(\S+)\s*(\[[^\]]*\])?\s*:\s*(.+)$", s)
            if km:
                tags = (km.group(2) or "")
                flds = km.group(3).split("+")
                if "primary" in tags: pk = flds
                elif "unique" in tags: uniques.append((km.group(1), flds))
                else: idxs.append((km.group(1), flds))
        elif mode == "cols":
            cm = re.match(r"^(\S+)\s+\S", s)
            if cm: cols.append(cm.group(1))
    return name, {"desc": desc, "pk": pk, "uniques": uniques,
                  "idx": idxs, "cols": cols}

def load(mod):
    d = os.path.join(DD, mod)
    tables = {}
    for fn in os.listdir(d):
        if fn.endswith(".txt"):
            n, info = parse_table(os.path.join(d, fn))
            tables[n] = info
    return tables

def main():
    want = sys.argv[1] if len(sys.argv) > 1 else "diag"
    allmods = {m: load(m) for m in MODS}
    json.dump(allmods, open(os.path.join(os.path.dirname(__file__), "schema.json"), "w", encoding="utf-8"))
    for m in MODS:
        tables = allmods[m]
        inv = {}
        for t, info in tables.items():
            for c in info["cols"]:
                inv.setdefault(c, []).append(t)
        if want == "diag":
            # report presence counts for candidate FK column names
            cands = ["CLIENTE","FORNEC","FORNECEDOR","TERCEIRO","TPTERC","ARTIGO",
                     "DESCRITOR","DESCR","CONTA","VENDEDOR","VEND","ARMAZEM","MOEDA",
                     "PAIS","BANCO","TPDOC","TPDOCUM","TIPODOC","SERIE","NNUMDOC",
                     "ACTIVO","ATIVO","FUNC","FUNCION","CODFUNC","SECCAO","SECTOR",
                     "CCUSTO","RUBRICA","CODIGO","COD","NUMDOC","PROCESS"]
            print(f"\n===== {m}: {len(tables)} tabelas =====")
            for c in cands:
                if c in inv:
                    print(f"  {c:12} -> {len(inv[c])} tabelas")
        if want == "report":
            outp = os.path.join(os.path.dirname(__file__), f"rel_{m}.md")
            w = open(outp, "w", encoding="utf-8")
            w.write(f"# Material bruto de relações — {m}  ({len(tables)} tabelas)\n\n")
            # 1) CAB/LIN pairs
            w.write("## Pares Cabeçalho/Linha (CAB/LIN) — chaves\n\n")
            for t in sorted(tables):
                for suf_c, suf_l in [("CAB","LIN"),("CABEC","LINHA")]:
                    if t.endswith(suf_c):
                        partner = t[:-len(suf_c)] + suf_l
                        if partner in tables:
                            w.write(f"- `{t}` ({tables[t]['desc']}) PK={'+'.join(tables[t]['pk'])}  <->  "
                                    f"`{partner}` ({tables[partner]['desc']}) PK={'+'.join(tables[partner]['pk'])}\n")
            # 2) single-column-PK masters
            w.write("\n## Masters (tabelas com PK de coluna única)\n\n")
            for t in sorted(tables):
                if len(tables[t]['pk']) == 1:
                    w.write(f"- `{t}` PK=`{tables[t]['pk'][0]}` — {tables[t]['desc']}\n")
            # 3) inverted index for curated FK column names
            FK = {"1GCO": ["CLIENTE","FORNEC","FORNECEDOR","TERCEIRO","TPTERC","ARTIGO",
                           "CONTA","VENDEDOR","ARMAZEM","MOEDA","PAIS","BANCO","TPDOC",
                           "TIPODOC","TPDOCUM","SERIE","NNUMDOC","SECTOR","CCUSTO","CARTEIRA",
                           "RUBORC","CODFLUX","CUSTEIO","GRUPO","FAMILIA","LOTE","NOMSERIE"],
                  "1GAT": ["CODIGO","FICHA","CONTA","SECTOR","CCUSTO","CLIENTE","FORNECEDOR",
                           "MOEDA","PAIS","GRUPO","CODTAB","DECRETO"],
                  "1GEP": ["NFUNC","CONTA","PAIS","BANCO","SECCAO","SECTOR","CCUSTO","TAB",
                           "CODEMP","CATEG","SITPRO","ADF","ADD","TPREC"]}[m]
            w.write("\n## Índice invertido — coluna FK -> tabelas que a contêm\n\n")
            for c in FK:
                ts = sorted(inv.get(c, []))
                w.write(f"### {c}  ({len(ts)} tabelas)\n")
                for t in ts:
                    w.write(f"- `{t}` — {tables[t]['desc']}\n")
                w.write("\n")
            w.close()
            print(f"wrote {outp}  ({os.path.getsize(outp)} bytes)")

main()
