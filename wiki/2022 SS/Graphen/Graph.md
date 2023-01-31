# Graph
- Graph $G = (V, E)$
	- $V = \set{1,2, ..., |V|}$ - Menge von Knoten
	- $E \subseteq V \times V$ - Menge von Pfeilen/Kanten

## Gerichtet/Ungerichtet
- Ein gerichteter Graph besteht aus Pfeilen von $v$ nach $v'$.
- Ein ungerichteter Graph besteht aus Kanten, sodass $(v,v') \in E \implies (v', v) \in E$.


## Darstellung - Adjazenzmatrix
- Speichert für alle Kanten entweder 0 (`false`) oder 1 (`true`) in zweidimensionalem Array
- Benötigt $|V|^2$ Bits/Booleans
- Ungünstig, wenn die Anzahl an Verbindungen klein ist

## Darstellung - Adjazenzliste
- Gut für das Verfolgen von Pfaden
- Schlecht für das Hinzufügen oder Entfernen von Knoten
- Jeder Knoten wird mit einer zusätzlichen Liste von Endknoten gespeichert
- Knoten in Array (**statisch**) oder in doppelt verketteter Liste (**dynamisch**)


## Traversierung
- Algorithmus mittels Stack und Markierung
	- weiß - neu
	- grau - eingereiht
	- schwarz - besucht
- Startknoten $v_0$ auf Stack/Queue
- *Solange Stack/Queue nicht leer:*
	- Einen Knoten entnehmen und schwarz markieren
	- Alle weißen Nachbarknoten grau markieren und in Stack/Queue einreihen

- **Breitensuche** - Queue
- **Tiefensuche** - Stack
