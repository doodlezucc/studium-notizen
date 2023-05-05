# Datentypen
## Einfache Datentypen
Einfache, eingebaute oder primitive Typen sind Datentypen, die in allen [[Programmiersprachen der Vorlesung]] **vordefiniert** sind. Dazu gehören unter anderem die Typen `int`, `float`, `boolean` und `char`.

Einfache Datentypen haben bestimmte **Wertebereiche**. Zum Beispiel kann eine Variable vom Typen `int` in Java einen Zahlenwert zwischen $-2^{31}$ und $2^{31}$ haben. In manchen Sprachen (C++, Python) ist der Wertebereich **plattformabhängig**.

### Hüllenklasse (Java)
In Java gibt es zu primitiven Datentypen die jeweiligen "Hüllenklassen" `Integer`, `Float` und `Boolean`.

Diese Hüllenklassen besitzen
1. Konstanten des Datentyp-Wertebereichs (z.B. `Integer.MIN_VALUE`, `Integer.MAX_VALUE`)
2. statische Methoden zum Konvertieren von einem String in den jeweiligen Datentyp (z.B. `Integer.parseInt(...)`).

## Abstrakte Datentypen
Ein **abstrakter Datentyp** ist in den [[Programmiersprachen der Vorlesung]] durch **Klassen** umgesetzt.

Abstrakte Datentypen (Klassen) können Attribute, Konstruktoren und Methoden beinhalten. Sie dienen als **Vorlage für abstrakte Datenstrukturen**.

Abstrakte Datenstrukturen sind einzelne **Objekte** oder **Instanzen** von abstrakten Datentypen. Sie besitzen Kopien der Methoden und Attribute, die in der Klasse definiert sind.