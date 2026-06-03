#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import os
import random

print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()

modell = form.getfirst("modell", "Kein Modell gewählt")
zustand = form.getfirst("zustand", "Keine Angabe")
baujahr = int(form.getfirst("baujahr", "1990"))

# --- Fahrzeugdaten ---
autos = {
    "E30": {
        "grundpreis": 12000,
        "beschreibung": "Ein klassischer BMW aus den 80er Jahren.",
        "prefix": "e30"
    },
    "E36": {
        "grundpreis": 15000,
        "beschreibung": "Sportlich, zuverlässig und ein echter Klassiker.",
        "prefix": "e36"
    },
    "E39": {
        "grundpreis": 18000,
        "beschreibung": "Luxuriös, komfortabel und zeitlos.",
        "prefix": "e39"
    }
}

# --- Preisfaktoren ---
def zustand_zuschlag(z):
    if z == "Top Zustand":
        return 3000
    if z == "Gut":
        return 1000
    if z == "Restaurationsbedürftig":
        return -2000
    return 0

def baujahr_zuschlag(b):
    if b < 1990:
        return -1000
    if 1990 <= b <= 1995:
        return 0
    if b > 1995:
        return 1500
    return 0

# --- HTML + CSS ---
print("""
<html>
<head>
<style>
    body {
        font-family: Arial;
        background-color: #F2F2F2;
        margin: 0;
        padding: 0;
    }
    .container {
        width: 85%;
        margin: 40px auto;
        background: white;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 0 20px rgba(0,0,0,0.15);
    }
    h1, h2 {
        color: #1C69D4;
    }
    .logo {
        width: 120px;
        display: block;
        margin: 0 auto 20px auto;
    }
    .gallery {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
    }
    .gallery-item {
        text-align: center;
    }
    .gallery-item img {
        width: 100%;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,0,0,0.2);
    }
    .price {
        font-size: 18px;
        font-weight: bold;
        color: #1C69D4;
        margin-top: 8px;
    }
</style>
</head>
<body>
<div class="container">
""")

print("<img src='/~sagmingo/images/bmw_logo.jpeg' class='logo'>")
print("<h1>BMW Oldtimer – Ergebnisse</h1>")
print(f"<p><strong>Ausgewähltes Modell:</strong> {modell}</p>")
print(f"<p><strong>Zustand:</strong> {zustand}</p>")
print(f"<p><strong>Baujahr:</strong> {baujahr}</p>")
print("<hr>")

# --- Bilder laden ---
bild_ordner = "/homes/students/sagmingo/html/images"

if modell in autos:

    daten = autos[modell]
    grundpreis = daten["grundpreis"]

    print(f"<h2>BMW {modell}</h2>")
    print(f"<p>{daten['beschreibung']}</p>")

    prefix = daten["prefix"]
    alle_dateien = os.listdir(bild_ordner)
    bilder = sorted([f for f in alle_dateien if f.startswith(prefix)])

    print("<div class='gallery'>")

    for bild in bilder:

        # Preisberechnung pro Bild
        preis = grundpreis \
                + zustand_zuschlag(zustand) \
                + baujahr_zuschlag(baujahr) \
                + random.randint(-300, 300)

        print("<div class='gallery-item'>")
        print(f"<img src='/~sagmingo/images/{bild}'>")
        print(f"<div class='price'>Preis: {preis} €</div>")
        print("</div>")

    print("</div>")

else:
    print("<p>Unbekanntes Modell.</p>")

print("""
</div>
</body>
</html>
""")
