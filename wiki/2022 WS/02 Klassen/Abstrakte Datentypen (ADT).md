# Abstrakte Datentypen (ADT)

Wenn Attribute nur über Methoden verändert werden können, spricht man von "Abstrakten Datentypen".

- ADT sollten bei objektorientierter Programmierung immer genutzt werden
	- **Aktionen** (`SETTER`) verändern Objekt-Attribute ohne Rückgabe
	- **Abfragen** (`GETTER`) liefern Aussagen über aktuelle Attributwerte
- Abstrakte Datentypen [[Datenkapselung|kapseln]] die Attribute nach außen hin

## Java
In Java realisierbar durch `private` und `protected`.

## Python
Python erlaubt immer direkten Zugriff auf Attribute
- strukturell lassen sich ADT nicht erzwingen
- private Attribute normalerweise mit Unterstrich kennzeichnen (`_attribut`)
- siehe [[Getter und Setter]]
