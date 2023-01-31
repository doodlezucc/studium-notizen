# Graphen
Siehe [[Graph]].

Weitere Eigenschaften eines Graphen:
- **Grad/Valenz** - Anzahl der verbundenen Kanten an einem Knoten
	- Gerichtete Graphen haben dabei *Eingangsgrad* und *Ausgangsgrad*
- Ein Graph heißt "*regulär*", wenn **alle** Knoten **denselben Grad** haben
- **Gewichtete Graphen**

## Untergraphen und Teilgraphen
Sei ***G*** ein Graph. ***G*** kann als "Obergraph" bezeichnet werden. Wenn Knoten oder Kanten aus diesem Obergraph *entfernt* werden, bildet sich ein neuer **Teilgraph von *G***.

Spezieller Fall "**Untergraph**" - Es werden Knoten aus dem Obergraphen entfernt, aber so viele Kanten wie möglich beibehalten.

## Wege und Pfade
Ein **Weg** ist eine Aneinanderreihung von Knoten, die jeweils durch Kanten verbunden sind.

Spezieller Fall "**Pfad**" - Es gibt keine doppelten Knoten in der Aneinanderreihung.
Spzieller Fall "**Eulerscher Weg**" - Es werden **alle** Kanten verwendet. Falls der Endknoten gleichzeitig auch der Startknoten ist, spricht man von einem "**Eulerschen Kreis**".

## Traversierung
Graphen können im Gegensatz zu [[Bäume|Bäumen]] sogenannte **Zyklen** enthalten.

- **Breitensuche** - Umgesetzt durch [[Weitere Listen#Queue|Queue]]
- **Tiefensuche** - Umgesetzt durch [[Weitere Listen#Stack|Stack]]

## Umsetzung
- **Adjazenzliste** - Pro Knoten werden die verbundenen Endknoten gespeichert
	- **Statische Adjazenzliste** - Nutzung von Arrays
	- **Dynamische Adjazenzliste** - Nutzung von [[Weitere Listen#Linked List|Linked Lists]]
- **Adjazenzmatrix** - 2-dimensionelles Array (abbildende "Tabelle") zur Beschreibung von Kanten

