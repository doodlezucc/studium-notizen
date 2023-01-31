# Interfaces
Interfaces = Schnittstellen

Interfaces können von anderen Interfaces erben (`extends`).

#### Implementierungs-Beziehung
- Attribute innerhalb eines `interface` sind implizit `static final` (also *konstant*)
- **leere** Interfaces heißen "Marker"-Schnittstellen

#### Java 8+
- mögliche [[Mehrfachvererbung]] durch `default` Methoden
- Definition von "Utilities" durch `static` Methoden

#### Vergleich zu abstrakten Klassen
|                     | Interface                                           | Abstrakte Klasse                     |
| ------------------- | --------------------------------------------------- | ------------------------------------ |
| instanziierbar      |                                                     |                                      |
| Erb-Notation        | `class Klasse implements Interface1, Interface2 {}` | `class Klasse extends OberKlasse {}` |
| mehrfach verwendbar | x                                                   |                                      |
