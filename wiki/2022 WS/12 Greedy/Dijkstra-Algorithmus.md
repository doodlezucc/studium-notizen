Der Dijkstra-Algorithmus findet die kürzesten [[Graphen#Wege und Pfade|Pfade]] von einem gewählten **Startknoten** zu allen anderen Knoten eines [[Graphen|Graphen]].

Zu jedem Knoten werden zwei Dinge gespeichert.
- Die *Pfadlänge* zum **Startknoten** (anfangs $\infty$)
- Der *Vorläufer*-Knoten in seinem Pfad (anfangs `null`)

1. Setze die *Pfadlänge* des **Startknoten** auf 0
2. *Schleife: bis keine Knoten mehr übrig sind*
	1. Entnehme den Knoten mit der kleinsten *Pfadlänge* ("**Priority Queue**")
	2. *Schleife: für alle anschließenden Kanten des entnommenen Knoten*
		1. Sei $w$ = (*Pfadlänge* des entnommenen Knoten + *Gewicht* der Kante)
		2. *Falls* $w$ < *Pfadlänge* des anderen Knoten:
			1. Setze die *Pfadlänge* des anderen Knoten auf $w$
			2. Trage als *Vorläufer* des anderen Knoten den entnommenen Knoten ein

![[Dijkstra.png]]

| Iteration | Betrachteter Knoten | *Pfadlänge* und *Vorläufer* der jeweiligen Knoten |
| --------- | ------------------- | ------------------------------------------------- |
| 0         | -                   | `s( 0,- ) t( ∞,-) x( ∞,-) y( ∞,-) z( ∞,-)`        |
| 1         | s                   | `-------- t(10,s) x( ∞,-) y( 5,s) z( ∞,-)`        |
| 2         | y                   | `-------- t( 8,s) x(14,y) ------- z( 7,y)`        |
| 3         | z                   | `-------- t( 8,s) x(13,y) ------- -------`        |
| 4         | t                   | `-------- ------- x( 9,y) ------- -------`        |

Am Ende beinhaltet jeder Knoten des Graphen die minmale *Pfadlänge* zum **Startknoten** und den jeweiligen *Vorläufer*-Knoten seines minimalen Pfades.