Von einem Wurzelknoten ausgehend hat ein **Baum** untergeordnete Kinderknoten.

## Traversierung
```
   M
 /   \
L     R
```

- **Breadth-First** (Breiten-Traversierung)
	- Realisiert durch [[Weitere Listen#Queue|Queue]]
- **Depth-First** (Tiefen-Traversierung)
	- In Order ( **L M R** )
	- Pre Order ( **M L R** )
	- Post Order ( **L R M** )
	- Realisiert durch [[Weitere Listen#Stack|Stack]]

## Binärer Suchbaum (BST)
Ein binärer Suchbaum hat folgende Eigenschaften:
- Jeder Knoten hat maximal 2 Kinder ("links" und "rechts")
- Für einen Knoten mit Wert ***N*** gilt
	- Alle untergeordneten Knoten auf der *linken* Seite haben einen **Wert ≤ *N***
	- Alle untergeordneten Knoten auf der *rechten* Seite haben einen **Wert ≥ *N***
	- Dadurch bleibt ein binärer Suchbaum immer *sortiert*

