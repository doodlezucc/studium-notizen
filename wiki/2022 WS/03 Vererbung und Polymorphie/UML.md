UML-Diagramme sind Projektentwürfe.
- Klassen
	- Attribute
	- Methoden
- Klassenbeziehungen
	- [[Datentypen]] der Attribute
	- Signaturen der Methoden

| **Duck**               |     |
|:---------------------- | --- |
|                        |     |
| `- name : string`      |     |
| `- color : int`        |     |
|                        |     |
| `+ Duck(string, int)`  |     |
| `+ getName() : string` |     |
| `~ getColor() : int`   |     |

## Klassendiagramm
- **Klassenname**: zentriert und in Fettschrift
	- Überschrift ggf. `<<interface>>`, `<<abstract>>` oder `<<enumeration>>`
- Liste von Attributen `<-|~|#|+> <name>: <type>`
	- [[Sichtbarkeit]]
	- Name
	- Typ
- Liste von Methoden/Operationen `<-|~|#|+> <name>(<param-type ...>): <return-type>`
	- Sichtbarkeit
	- Name
	- Argumententypen
	- Rückgabetyp

#### Besonderheiten
- abstrakte Klassen und Methoden *kursiv* oder \<abstract>
- statische Attribute und Methoden <u>unterstrichen</u> oder \<static>

## Generalisierung
- Pfeil von Unterklasse auf Oberklasse
- `extends` = durchgezogen
- `implements` = gestrichelt

![[UML Generalisierung.png]]

