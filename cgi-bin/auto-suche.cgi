#!/usr/bin/python3
import cgi
import html

print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()
generation = html.escape(form.getvalue("generation", ""))
preis_str = html.escape(form.getvalue("preis", "0"))
leistung = html.escape(form.getvalue("leistung", ""))

try:
    preis = int(preis_str)
except:
    preis = 0

autos = [
    {"modell": "318i", "generation": "E30", "preis": 8500, "leistung": "bis100"},
    {"modell": "325i", "generation": "E30", "preis": 12000, "leistung": "150-200"},
    {"modell": "318i", "generation": "E36", "preis": 4500, "leistung": "bis100"},
    {"modell": "328i", "generation": "E36", "preis": 7800, "leistung": "150-200"},
    {"modell": "320i", "generation": "E46", "preis": 3500, "leistung": "100-150"},
    {"modell": "330i", "generation": "E46", "preis": 6500, "leistung": "150-200"},
]

ergebnisse = []
for auto in autos:
    if generation and auto["generation"] != generation:
        continue
    if preis > 0 and auto["preis"] > preis:
        continue
    if leistung and auto["leistung"] != leistung:
        continue
    ergebnisse.append(auto)

print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("<meta charset='UTF-8'>")
print("<title>Suchergebnisse</title>")
print("<link rel='stylesheet' href='../style.css'>")
print("</head>")
print("<body>")
print("<div class='container'>")
print("<h1>Suchergebnisse</h1>")

if not ergebnisse:
    print("<p>Keine Autos gefunden.</p>")
else:
    for auto in ergebnisse:
        print("<div class='car-card'>")
        print("<strong>BMW " + auto["modell"] + "</strong><br>")
        print("Preis: " + str(auto["preis"]) + " €<br>")
        print("Generation: " + auto["generation"] + " | Leistung: " + auto["leistung"] + " PS")
        print("</div>")

print("<p><a href='../index.html'>Neue Suche</a></p>")
print("<footer><a href='https://github.com/Abdulai3002/Projekt-semsterabgabe-'>GitHub Repository</a></footer>")
print("</div>")
print("</body>")
print("</html>")
