# List
```java
interface List<E> extends Collection<E> {
	void add(int index, E o);
	boolean addAll(int index, Collection<E> c);
	E get(int index);
	int indexOf(Object o);
	int lastIndexOf(Object o);
	E remove(int index);
	E set(int index, E o);
}
```

## ArrayList
- realisiert durch internen *Array*, wessen Größe bei `add()` und `remove()` automatisch angepasst wird
- falls Platz für neue Elemente benötigt ist, *Array* um ca. 50% vergrößern
- Initiale Größe `10` Elemente (falls nicht im Konstruktor anders angegeben)

## LinkedList
- realisiert durch *(doppelt) verkettete Liste*
- kann als Stack und als Queue gleichzeitig verwendet werden
- zusätzliche Operationen `addFirst(), getFirst(), removeFirst()` und `addLast(), getLast(), removeLast()`
