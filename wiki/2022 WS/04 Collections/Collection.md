# Collection
Collection Interface besitzt Funktionen:
- einfügen eines Elements
- löschen eines Elements
- löschen aller Elemente
- abfragen, ob `x` Teil der Collection ist
- abfragen, ob leer
- durchlaufen aller Elemente

```java
interface Collection<E> {
	boolean add(E o);
	boolean remove(Object o);
	void clear();
	int size();
	boolean isEmpty();
	Object[] toArray();
	Iterator<E> iterator();
}
```

Siehe [[Iterator]].
Implementiert durch [[List]] und [[Set]].

#### Vergleich von Listen und Mengen (Laufzeitkomplexität)
| Klasse       | add()       | remove() | get() | contains() | Durchlauf-Reihenfolge |
| ------------ | ----------- | -------- | ----- | ---------- | --------------------- |
| `ArrayList`  | O(1)        | O(n)     | O(1)  | O(n)       | Einfügung             |
| `LinkedList` | ^ (schnell) | ^        | O(n)  | ^          | Einfügung             |
|              |             |          |       |            |                       |
| `TreeSet`    | O(log n)    | O(log n) |       | O(log n)   | Ordnung               |
| `HashSet`    | O(1)        | O(1)     |       | O(1)       | unspezifisch          |
