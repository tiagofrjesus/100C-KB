#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Constroi o indice da API .NET Sage 1GCO no estilo X3-KB.
Saida:
  C:/100C-KB/Docs/API_Index.md                    (catalogo de classes)
  C:/100C-KB/Sage 100c Docs/API/<Classe>.txt      (membros completos por classe)
Fonte: D:/Git/Sage100C/ApiGestao/ApiHelpHTML/*.html  (cp1252)
"""
import re, html, os, glob

SRC = r"D:\Git\Sage100C\ApiGestao\ApiHelpHTML"
KB  = r"C:\100C-KB"
DOCS = os.path.join(KB, "Docs")
APIDIR = os.path.join(KB, "Sage 100c Docs", "API")

SKIP = {
    "backsdk3","backsdk4","class","const","contents","declare","enum","event",
    "filter","form","function","help","index","langref","lib","linkcss","module",
    "parchild","parlower","parmult","parspace","project","property","requirements",
    "seealso","sub","type","unknown","usercontrol","variable",
    "Sage1GCOApi_bug","Sage1GCOApi_history","Sage1GCOApi_todo",
}

def to_lines(path):
    s = open(path, "rb").read().decode("cp1252", errors="replace")
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", s, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", "\n", s)
    s = html.unescape(s).replace("\xa0", " ")
    return [re.sub(r"[ \t]+", " ", l).strip() for l in s.splitlines() if l.strip()]

def parse_blocks(lines):
    sep = re.compile(r"^=+$")
    blocks, cur = [], []
    for l in lines:
        if sep.match(l):
            if cur: blocks.append(cur); cur = []
        else:
            cur.append(l)
    if cur: blocks.append(cur)
    return blocks

def block_kv(block):
    d, cur = {}, None
    for l in block:
        m = re.match(r"^(Name|Input|Output|Purpose|Remarks|Version|Author):\s*(.*)$", l)
        if m:
            cur = m.group(1); d[cur] = m.group(2).strip()
        elif cur in ("Purpose", "Input", "Output", "Remarks") and cur in d:
            d[cur] = (d[cur] + " " + l).strip()
    return d

SIG_RE = re.compile(
    r"^(?:Public|Private)\s+(Property Get|Property Let|Property Set|Sub|Function)\s+([A-Za-z0-9_]+)", re.I)
KIND = {"Property Get": "Get", "Property Let": "Let", "Property Set": "Set",
        "Sub": "Sub", "Function": "Function"}

def parse_class(path):
    name = os.path.splitext(os.path.basename(path))[0]
    lines = to_lines(path)
    purpose = ""
    members, seen = [], set()
    for b in parse_blocks(lines):
        d = block_kv(b)
        nm = d.get("Name", "")
        if not nm:
            continue
        if nm == name and not purpose:
            purpose = re.split(r"\s*(Functions:|Properties:|Methods:)", d.get("Purpose", ""))[0].strip()
            continue
        m = SIG_RE.match(nm)
        if m:
            kind = KIND.get(m.group(1).title().replace("Property Get", "Property Get"), m.group(1))
            # normalise kind label
            for k, v in KIND.items():
                if m.group(1).lower() == k.lower():
                    kind = v; break
            mname = m.group(2)
            key = (kind, mname)
            if key in seen:
                continue
            seen.add(key)
            members.append((kind, mname, d.get("Input", ""), d.get("Output", ""), d.get("Purpose", "")))
    return name, purpose, members

def main():
    os.makedirs(DOCS, exist_ok=True)
    os.makedirs(APIDIR, exist_ok=True)
    classes = []
    for f in sorted(glob.glob(os.path.join(SRC, "*.html"))):
        base = os.path.basename(f)
        if base[:-5].count(".") >= 1:   # membro (dois pontos) -> ignora
            continue
        nm = base[:-5]
        if nm in SKIP:
            continue
        name, purpose, members = parse_class(f)
        if not members and not purpose:
            continue
        classes.append((name, purpose, members))
        # per-class txt
        with open(os.path.join(APIDIR, f"{name}.txt"), "w", encoding="utf-8") as w:
            w.write(f"{name}\n{purpose}\n\n")
            w.write(f"Membros ({len(members)}):\n")
            for kind, mname, inp, outp, pur in members:
                w.write(f"\n  [{kind}] {mname}\n")
                if inp:  w.write(f"    Input : {inp}\n")
                if outp: w.write(f"    Output: {outp}\n")
                if pur:  w.write(f"    => {pur}\n")

    with open(os.path.join(DOCS, "API_Index.md"), "w", encoding="utf-8") as w:
        w.write("# API Sage 1GCO (.NET / COM) — Catalogo de Classes\n")
        w.write("> Logica de negocio da Gestao Comercial. Faz grep por classe ou conceito.\n")
        w.write("> Membros completos (assinatura, input/output, proposito): "
                "`Sage 100c Docs/API/<Classe>.txt`\n\n")
        w.write(f"Total: {len(classes)} classes.\n\n")
        w.write("Tipos de membro: **Sub** (acao) · **Function** (devolve valor) · **Get/Let/Set** (propriedade).\n\n")
        w.write("| Classe | Proposito | Membros |\n|---|---|---|\n")
        for name, purpose, members in sorted(classes):
            w.write(f"| {name} | {purpose} | {len(members)} |\n")
    print(f"{len(classes)} classes -> Docs/API_Index.md + Sage 100c Docs/API/*.txt")

main()
