# -*- coding: utf-8 -*-
"""Ubica en los PDF de revisión cada mención de una norma o dato legal: documento, página y frase.
Uso: python3 citas_legales.py <carpeta pdf> <prefijo de curso>  → tabla Markdown."""
import re, sys, glob, os
import pymupdf

PATRONES = [
    ('Ley 1034/83 (arts. 74-76) y Ley 4924/2013', r'1034|4924|autorización judicial|Registro Público de Comercio'),
    ('Ley 7593/2025 (datos personales)', r'7593'),
    ('Ley 6534/2020 (datos crediticios)', r'6534'),
    ('Ley 1334/98 (consumidor)', r'1334'),
    ('Ley 7143/2023 (DNIT)', r'7143'),
    ('Ley 7158/2023 (MEF)', r'7158|Ministerio de Economía'),
    ('Ley 6380/2019 (IRE: SIMPLE, RESIMPLE, obligaciones 700-702)', r'6380|\b70[012]\b|RESIMPLE'),
    ('Salario mínimo (Decreto 6225/2026)', r'6225|salario mínimo|3\.044\.000'),
    ('IPS 9 % / 16,5 %', r'16,5 ?%|aporte obrero'),
    ('RG DNIT 41/2025', r'41/2025'),
    ('RG DNIT 49/2026 y obligación 948', r'49/2026|\b948\b'),
    ('RG DNIT 52/2026', r'52/2026'),
    ('RG DNIT 54/2026', r'54/2026'),
    ('e-Kuatia / e-Kuatia\'i (RG 21/2024)', r"e-Kuatia|21/2024"),
    ('SIFEN: plazo de 72 h, DE/DTE, KuDE, XML al receptor', r'72 horas|KuDE|\bDTE\b'),
    ('IVA 10 % y 5 %', r'IVA.{0,40}(10|5) ?%|tasa reducida'),
]


def frases(texto, rx):
    t = ' '.join(texto.split())
    for m in re.finditer(rx, t):
        a = max(0, t.rfind('. ', 0, m.start()) + 2); b = t.find('. ', m.end()); b = len(t) if b < 0 else b + 1
        yield t[a:b][:220]


if __name__ == '__main__':
    carpeta = sys.argv[1]
    print('| Norma / dato | Documento | Página del PDF | Frase (recortada) |')
    print('|---|---|---|---|')
    for nombre, rx in PATRONES:
        for f in sorted(glob.glob(os.path.join(carpeta, '*.pdf'))):
            doc = os.path.basename(f).split('_BTC_')[1].rsplit('_', 1)[0]
            vistos = set()
            for i, p in enumerate(pymupdf.open(f)):
                for fr in frases(p.get_text(), rx):
                    if (fr[:80]) in vistos:
                        continue
                    vistos.add(fr[:80])
                    print('| %s | %s | %d | %s |' % (nombre, doc, i + 1, fr.replace('|', '/')))
