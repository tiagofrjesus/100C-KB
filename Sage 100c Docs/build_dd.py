#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Constroi os indices do Dicionario de Dados Sage 100c no estilo X3-KB.
Saida:
  C:/100C-KB/Docs/DD_Catalog_<schema>.md       (catalogo: tabela -> desc, #cols, PK)
  C:/100C-KB/Docs/Vistas_<schema>.md            (catalogo de vistas SQL)
  C:/100C-KB/Docs/Validacoes_<schema>.md        (listas de valores / lookups)
  C:/100C-KB/Sage 100c Docs/DD/<schema>/<T>.txt (schema completo por tabela)
"""
import re, html, os

SRC = r"D:\Git\Sage100C\DicionarioDados"
KB  = r"C:\100C-KB"
DOCS = os.path.join(KB, "Docs")
DDDIR = os.path.join(KB, "Sage 100c Docs", "DD")

SCHEMAS = {
    "1GAT": "Sage Gestao de Ativos",
    "1GCO": "Sage Gestao Empresarial / Comercial",
    "1GEP": "Sage Salarios",
}

def clean(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s).replace("﻿", "").replace("\xa0", " ")
    return re.sub(r"\s+", " ", s).strip()

def section_regions(t):
    """Devolve {nome_seccao: (ini, fim)} a partir dos titulos titletable."""
    titles = ["Tabelas de Aplicação", "Tabelas Internas", "Vistas", "Formatos", "Validações"]
    pos = {}
    for name in titles:
        m = re.search(r'class="titledata">\s*' + re.escape(name) + r'\s*</td>', t)
        if m:
            pos[name] = m.start()
    ordered = sorted(pos.items(), key=lambda kv: kv[1])
    regions = {}
    for i, (name, start) in enumerate(ordered):
        end = ordered[i + 1][1] if i + 1 < len(ordered) else len(t)
        regions[name] = (start, end)
    return regions

# ---- tabelas de aplicacao -------------------------------------------------
TBL_RE = re.compile(
    r'<a name="ancoraVistTA[^"]*">\s*<td class="TA_N1_ROW">(.*?)</td>\s*</a>\s*'
    r'<td class="TA_N1_ROW">(.*?)</td>', re.S)
FIELD_RE = re.compile(
    r'<td class="TA_N2_ROW">(.*?)</td>\s*<td class="TA_N2_ROW">(.*?)</td>\s*'
    r'<td class="TA_N2_ROW">(.*?)</td>\s*<td class="TA_N2_ROW">(.*?)</td>\s*'
    r'<td class="TA_N2_ROW">(.*?)</td>', re.S)
# linha de indice: img-cell, Nº, Nome, Primario, Unico
IDX_RE = re.compile(
    r'<td class="TA_N2_ROW"><IMG[^>]*></IMG></td>\s*<td class="TA_N2_ROW">(.*?)</td>\s*'
    r'<td class="TA_N2_ROW">(.*?)</td>\s*<td class="TA_N2_ROW">(.*?)</td>\s*'
    r'<td class="TA_N2_ROW">(.*?)</td>', re.S)
IDXFLD_RE = re.compile(
    r'<td class="TA_N3_ROW">.*?</td>\s*<td class="TA_N3_ROW">(.*?)</td>', re.S)

def parse_tables(t, ini, fim):
    region = t[ini:fim]
    ms = list(TBL_RE.finditer(region))
    out = []
    for i, m in enumerate(ms):
        name = clean(m.group(1)); desc = clean(m.group(2))
        if not name:
            continue
        seg = region[m.end(): ms[i + 1].start() if i + 1 < len(ms) else len(region)]
        idx_pos = seg.find(">Índices<")
        campos_seg = seg[:idx_pos] if idx_pos != -1 else seg
        idx_seg = seg[idx_pos:] if idx_pos != -1 else ""
        # campos
        fields = []
        for f in FIELD_RE.finditer(campos_seg):
            fn = clean(f.group(2))
            if fn:
                fields.append((fn, clean(f.group(3)), clean(f.group(4)), clean(f.group(5))))
        # indices: cada IDX seguido do bloco de campos N3 ate ao proximo IDX
        idxs = []
        idx_ms = list(IDX_RE.finditer(idx_seg))
        for j, im in enumerate(idx_ms):
            iname = clean(im.group(2)); prim = clean(im.group(3)); uniq = clean(im.group(4))
            blk = idx_seg[im.end(): idx_ms[j + 1].start() if j + 1 < len(idx_ms) else len(idx_seg)]
            iflds = [clean(x.group(1)) for x in IDXFLD_RE.finditer(blk) if clean(x.group(1))]
            idxs.append((iname, prim == "Sim", uniq == "Sim", iflds))
        out.append((name, desc, fields, idxs))
    return out

# ---- vistas ---------------------------------------------------------------
VIEW_RE = re.compile(
    r'<a name="ancoraVistVist[^"]*">\s*<td class="VISTAS_N1_ROW">(.*?)</td>\s*(?:</a>\s*)+'
    r'<td class="VISTAS_N1_ROW">(.*?)</td>', re.S)

def parse_views(t, ini, fim):
    out = []
    for m in VIEW_RE.finditer(t[ini:fim]):
        name = clean(m.group(1)); desc = clean(m.group(2))
        if name:
            out.append((name, desc))
    return out

# ---- validacoes ------------------------------------------------------------
VAL_RE = re.compile(
    r'<a name="ancoraVistVal[^"]*">\s*<td class="VALIDACOES_N1_ROW">(.*?)</td>\s*</a>\s*'
    r'<td class="VALIDACOES_N1_ROW">(.*?)</td>\s*<td class="VALIDACOES_N1_ROW">(.*?)</td>', re.S)

def parse_validations(t, ini, fim):
    region = t[ini:fim]
    ms = list(VAL_RE.finditer(region))
    out = []
    for i, m in enumerate(ms):
        code = clean(m.group(1)); desc = clean(m.group(2)); tipo = clean(m.group(3))
        seg = region[m.end(): ms[i + 1].start() if i + 1 < len(ms) else len(region)]
        # tabela alvo (se "Tabela Interna")
        tgt = re.search(r'href="#ancoraVal\w+">([^<]+)</a>', seg)
        target = clean(tgt.group(1)) if tgt else ""
        if code:
            out.append((code, desc, tipo, target))
    return out

def fmt_type(tipo, comp):
    return f"{tipo}({comp})" if comp else tipo

def write_table_txt(schema, name, desc, fields, idxs):
    d = os.path.join(DDDIR, schema)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, f"{name}.txt"), "w", encoding="utf-8") as w:
        w.write(f"{name} — {desc}  [{schema} · {SCHEMAS[schema]}]\n\n")
        if idxs:
            w.write("Keys / Indices:\n")
            for iname, prim, uniq, iflds in idxs:
                tags = []
                if prim: tags.append("primary")
                if uniq: tags.append("unique")
                tag = f" [{', '.join(tags)}]" if tags else ""
                w.write(f"  {iname}{tag}: {'+'.join(iflds)}\n")
            w.write("\n")
        w.write(f"Columns ({len(fields)}):\n")
        wn = max([len(f[0]) for f in fields] + [4])
        wt = max([len(fmt_type(f[2], f[3])) for f in fields] + [4])
        for fn, fd, ft, fc in sorted(fields):
            w.write(f"  {fn.ljust(wn)}  {fmt_type(ft, fc).ljust(wt)}  {fd}\n")

def pk_of(idxs):
    for iname, prim, uniq, iflds in idxs:
        if prim:
            return "+".join(iflds)
    for iname, prim, uniq, iflds in idxs:
        if uniq:
            return "+".join(iflds)
    return ""

def main():
    os.makedirs(DOCS, exist_ok=True)
    for sch in SCHEMAS:
        t = open(os.path.join(SRC, f"100C.Cat.Base.{sch}.html"), encoding="utf-8", errors="replace").read()
        ver = re.search(r"<h2>(Vers[^<]*)</h2>", t)
        ver = clean(ver.group(1)) if ver else ""
        reg = section_regions(t)
        tabs = parse_tables(t, *reg["Tabelas de Aplicação"]) if "Tabelas de Aplicação" in reg else []
        views = parse_views(t, *reg["Vistas"]) if "Vistas" in reg else []
        vals = parse_validations(t, *reg["Validações"]) if "Validações" in reg else []

        # per-table txt
        for name, desc, fields, idxs in tabs:
            write_table_txt(sch, name, desc, fields, idxs)

        # catalogo de tabelas
        with open(os.path.join(DOCS, f"DD_Catalog_{sch}.md"), "w", encoding="utf-8") as w:
            w.write(f"# Dicionario de Dados {sch} ({SCHEMAS[sch]}) — Catalogo de Tabelas\n")
            w.write(f"> {ver}. Uma linha por tabela de aplicacao. Faz grep por nome ou descricao.\n")
            w.write(f"> Schema completo (colunas, tipos, chaves): `Sage 100c Docs/DD/{sch}/<TABELA>.txt`\n\n")
            w.write(f"Total: {len(tabs)} tabelas de aplicacao.\n\n")
            w.write("| Tabela | Descricao | Cols | Chave Primaria |\n|---|---|---|---|\n")
            for name, desc, fields, idxs in sorted(tabs):
                w.write(f"| {name} | {desc} | {len(fields)} | {pk_of(idxs)} |\n")

        # catalogo de vistas
        with open(os.path.join(DOCS, f"Vistas_{sch}.md"), "w", encoding="utf-8") as w:
            w.write(f"# Vistas {sch} ({SCHEMAS[sch]})\n")
            w.write("> Vistas da aplicacao. Muitas correspondem a views SQL queryaveis.\n\n")
            w.write(f"Total: {len(views)} vistas.\n\n")
            w.write("| Vista | Descricao |\n|---|---|\n")
            for name, desc in sorted(views):
                w.write(f"| {name} | {desc} |\n")

        # catalogo de validacoes (listas de valores / lookups)
        with open(os.path.join(DOCS, f"Validacoes_{sch}.md"), "w", encoding="utf-8") as w:
            w.write(f"# Validacoes {sch} ({SCHEMAS[sch]})\n")
            w.write("> Regras de validacao de campos. 'Tabela Interna' -> lookup noutra tabela; "
                    "fixas -> lista de valores. Equivalente aos local menus do X3.\n\n")
            w.write(f"Total: {len(vals)} validacoes.\n\n")
            w.write("| Codigo | Descricao | Tipo | Tabela alvo |\n|---|---|---|---|\n")
            for code, desc, tipo, target in sorted(vals):
                w.write(f"| {code} | {desc} | {tipo} | {target} |\n")

        print(f"{sch}: {len(tabs)} tabelas, {len(views)} vistas, {len(vals)} validacoes")

main()
