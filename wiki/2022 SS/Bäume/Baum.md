## Eigenschaften
- Zwischen zwei Knoten gibt es genau einen Weg
- Es gibt immer eine Kante weniger als Knoten
- Der Graph ist minimal zusammenhängend (?)
- Keine Zyklen

- Entfernt man eine Kante, entstehen zwei Teilbäume (**Wald**)
- Verbindet man die Wurzeln zweier gerichteter Bäume, entsteht ein neuer Baum

### Ungerichtete Bäume
- Zusammenhängender, kreisfreier ungerichteter [[Graph]]
- Knoten mit Grad 1 heißen **Blätter**

### Gerichtete Bäume
- Gerichteter kreisfreier [[Graph]]
- Genau eine **Wurzel** mit Eingangsgrad 0
- Knoten mit Ausgangsgrad 0 heißen **Blätter**

### Wald
- Mehrere Bäume/Wurzeln

### Höhe/Tiefe eines Baums
- **Leerer Baum** hat keine Wurzel, Höhe 0
- Wurzel hat Tiefe 0, Höhe 1

### Binärer Baum
- Ein leerer Baum
- Sind *L* und *R* zwei binäre Bäume, lassen sie sich durch einen einzelnen Knoten zu einem neuen binären Baum zusammenfügen

#### Binärer Suchbaum
- Beide Unterbäume sind binäre Suchbäume
- Werte des linken Baums sind kleiner als Wurzelbeschriftung
- Werte des rechten Baums sind größer als Wurzelbeschriftung

#### Voller (saturierter) Baum
- Jeder Knoten besitzt 0 oder 2 Kinder

#### Vollständiger Baum
- Alle Blätter haben dieselbe Tiefe

#### Vollständiger Binärbaum (Höhe *h*)
- $2^h-1$ Knoten
- $2^{h-1} - 1$ innere Knoten
- $2^t$ Knoten in Tiefe *t* ($0 \leq t \leq h-1$)
- $2^{h-1}$ Blätter