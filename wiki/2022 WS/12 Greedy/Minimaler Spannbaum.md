# Minimaler Spannbaum
**Spannbaum** - Eine [[Bäume|Baum]]-Struktur, die aus einem *gewichteten* [[Graphen]] entsteht.

Ein **Spannbaum** heißt "minimal", wenn er alle Knoten beinhaltet und die Kanten mit dem kleinstmöglichen Gesamtgewicht überträgt.

## Kruskal-Algorithmus
Kanten von kleinstem zu größtem Gewicht sortieren und der Reihenfolge nach in einen **Baum** übertragen.

1. Alle Kanten des Graphen von kleinstem zu größtem Gewicht sortieren
2. *Schleife: alle Kanten der Reihenfolge nach*
	1. Überprüfen, ob die beiden Knoten der Kante schon in Verbindung stehen ("**Find-Union**")
	2. Falls **nicht**: Kante eintragen

Zyklen müssen explizit durch **Find-Union** vermieden werden.

- Alle Knoten besitzen am Anfang eine **Menge**, die nur den einzelnen Knoten beinhaltet.
- Mit jeder eingetragenen Kante werden die **Mengen** beider Knoten *vereint*.
- Eine Kante wird übersprungen, falls beide Knoten *dieselbe* **Menge** besitzen (sonst würde ein Zyklus entstehen).


![[Kruskal.png]]

## Prim-Algorithmus
1. Ein **Startknoten** wird gewählt und als *besucht* markiert
2. *Schleife: bis alle Knoten besucht sind*
	1. Erreichbare Kanten = Alle Kanten, die von allen *besuchten* Knoten ausgehen und zu *unbesuchten* Knoten führen
	2. Aus den erreichbaren Kanten wird die mit dem **kleinsten Gewicht** gewählt
	3. Die gewählte Kante wird eingetragen und der neue Knoten als *besucht* markiert

![[Prim.png]]

