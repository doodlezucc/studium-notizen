# Balancierte Bäume
## Eigenschaften
- Alle Äste (fast) gleich lang
- Kann in binären Suchbäumen nicht erzwungen werden
- Nicht-balancierte Bäume nennt man **entartete Bäume**

## Rot-Schwarz-Baum
1. Jeder Knoten ist entweder schwarz oder rot
2. (Die Wurzel ist schwarz)
3. Alle Blätter sind schwarz
4. Die Kinder eines roten Knoten sind schwarz
5. Jeder Pfad von Knoten zu allen Blättern enthält gleich viele schwarze Knoten

- Laufzeitkomplexität bei Einfügen und Löschen **höher** als bei binären Suchbäumen
- Suche ist für alle Eingabesequenzen garantiert `O(lg n)`











https://www.happycoders.eu/de/algorithmen/rot-schwarz-baum-java/

### Einfügen
- Eingefügte Knoten sind immer rot
- Falls Vater schwarz: fertig
- Falls Vater rot:
	- Umfärben (Vater, Onkel, Großvater)
	- *Schleife: Hoch traversieren*
		- Falls Onkel schwarz:
			- Falls rechtes Kind
				- Rotate-Left (Vater)
			- Falls linkes Kind
				- Rotate-Right (Großvater)
				- Umfärben (Vater, Großvater)

![[Pasted image 20220717163327.png]]

### Löschen
![[Pasted image 20220717163356.png]]

### Rotate
- rotate-left
	- parent becomes left child
	- left child becomes parent's right child
- rotate-right
	- parent becomes right child
	- right child becomes parent's left child

```sh
  20                [40]                       40                [20]
 /  \               /  \                      /  \               /  \  
10 [40]    -->    20    50                  [20]  50    -->    10    40
   /  \          /  \                       /  \                    /  \     
  30  50        10  30                     10  30                  30  50    
```
