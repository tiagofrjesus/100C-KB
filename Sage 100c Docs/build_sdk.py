#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Constroi o modelo de objetos do SDK 100C (C100SDK, automacao COM).
Saida: C:/100C-KB/Docs/SDK_ObjectModel.md
Fonte: D:/Git/Sage100C/100C SDK/Help/*.html  (cp1252)
"""
import re, html, os, glob
from collections import defaultdict

SRC = r"D:\Git\Sage100C\100C SDK\Help"
DOCS = r"C:\100C-KB\Docs"

CLASSES = ["Aplicacao", "Empresa", "Utilizador", "Contexto", "Campo", "Iterador"]
CLASS_DESC = {
    "Aplicacao": "Ponto de entrada do SDK. SQL, vistas, listas, iteradores, Crystal e mensagens.",
    "Empresa": "Dados da empresa ativa (sigla, designacao, versao).",
    "Utilizador": "Utilizador autenticado (login, nome).",
    "Contexto": "Contexto de um registo: ler/escrever campos, gravar, criar iteradores.",
    "Campo": "Campo de um contexto: valor, texto, descricao, foco, validacao.",
    "Iterador": "Percorre registos de SQL ou vista (LerRegisto, Fim, Campo).",
}

def to_lines(path):
    s = open(path, "rb").read().decode("cp1252", errors="replace")
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", s, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", "\n", s)
    s = html.unescape(s).replace("\xa0", " ")
    return [re.sub(r"[ \t]+", " ", l).strip() for l in s.splitlines() if l.strip()]

def parse_member(path):
    lines = to_lines(path)
    base = os.path.basename(path)[:-5]
    cls = base.split(".")[0]
    member = ".".join(base.split(".")[1:])
    sig_start = None
    for i, l in enumerate(lines):
        if re.match(r"^(Public|Private|Friend)\b", l):
            sig_start = i; break
    title_token = base.split(".")[-1]
    desc = []
    for l in lines[2:sig_start if sig_start else len(lines)]:
        if l in (f"{cls}: {member}", member, title_token, cls):
            continue
        desc.append(l)
    sig = ""
    if sig_start is not None:
        sg = []
        for l in lines[sig_start:]:
            if l in ("Parameters", "Return Values", "Remarks", "See Also"):
                break
            sg.append(l)
        sig = re.sub(r"\s+\)", ")", re.sub(r"\s+\(\s+", "(", " ".join(sg)))
        sig = re.sub(r"\s+,", ",", sig)
    return cls, member, sig, " ".join(desc).strip()

def main():
    os.makedirs(DOCS, exist_ok=True)
    members = defaultdict(list)
    for f in glob.glob(os.path.join(SRC, "*.html")):
        base = os.path.basename(f)
        if base.count(".") < 2:
            continue
        if base.split(".")[0] not in CLASSES:
            continue
        cls, member, sig, desc = parse_member(f)
        members[cls].append((member, sig, desc))
    out = os.path.join(DOCS, "SDK_ObjectModel.md")
    with open(out, "w", encoding="utf-8") as w:
        w.write("# SDK 100C — Modelo de Objetos (C100SDK)\n")
        w.write("> Automacao COM/ActiveX da aplicacao 100C. Exemplos em VBScript/VBA. "
                "Ponto de entrada: objeto **Aplicacao**.\n\n")
        w.write("## Classes\n\n")
        for c in CLASSES:
            w.write(f"- **{c}** — {CLASS_DESC[c]} ({len(members.get(c, []))} membros)\n")
        w.write("\n---\n\n")
        for c in CLASSES:
            w.write(f"## {c}\n\n{CLASS_DESC[c]}\n\n")
            w.write("| Membro | Assinatura | Descricao |\n|---|---|---|\n")
            for member, sig, desc in sorted(members.get(c, [])):
                w.write(f"| {member} | {sig.replace('|','/')} | {desc.replace('|','/')} |\n")
            w.write("\n")
    print(f"-> Docs/SDK_ObjectModel.md ({sum(len(v) for v in members.values())} membros)")

main()
