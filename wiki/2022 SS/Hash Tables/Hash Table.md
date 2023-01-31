# Hash Table
- Kombination aus Array und Liste
- Elemente werden in Array nicht von links nach rechts, sondern durch [[Hashfunktion]] zugewiesen

## Einfügen
- Hash des Element-Schlüssels (z.B. Student-Matrikelnummer)

## Suchen
- Index = Hash des Element-Schlüssels
- Solange mit implementierter Strategie Index erhöhen, bis der Schlüsselwert übereinstimmt
- Suchen anhand anderer Attribute (außer Schlüssel) **nicht** optimiert, stattdessen lineare Suche

## Löschen
- Element auf `NULL` zu setzen nicht möglich, weil eventuell Elemente desselben Hashes eingefügt wurden
- Mögliche Algorithmen
	1. Platzhalter
		- Einfach zu realisieren
		- Keine Änderungen an anderen Funktionen notwendig
	2. Neuberechnung nachfolgender Einträge
		- Aufwendig bei großem Cluster
		- Beschleunigt die Suche

## Strategien
- **Kollision** - Fall, dass zwei unterschiedliche Einträge auf denselben Hash/Index eines Arrays zeigen
- Betrachte Array als Ring (modulo)
- Erzwungener Abbruch, nachdem alle Felder durchsucht wurden

### Linear Probing
- $h(k, i) = (k + i) \mod m$
- Index um 1 erhöhen
- *Problem:*
	- Kollisionsballung verschlechtert Laufzeitverhalten

### Quadratic Probing
- $h(k, i) = (k + c_1 * i + c_2 * i^2) \mod m$
- Lege $c_1$ und $c_2$ für ein Hash Table **konstant** an
- Nimmt immer größer werdende Sprünge

### Double Hashing
- $h(k, i) = (k + i * h_2(k)) \mod m$
- Hängt von einer unterschiedlichen Hashfunktion $h_2(k)$ ab
- Sprungweite hängt vom Schlüssel ab

### Chaining
- Jeder Hashwert ist im Array eine verkettete [[Liste]] von Einträgen
- Dynamisch