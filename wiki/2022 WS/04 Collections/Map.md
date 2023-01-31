# Map
Map = Dictionary = Abbildung
- Gruppe von Schlüssel-Werte-Objektpaaren
- realisiert **assoziativen Speicher** (Zugriff über individuelle Schlüssel *statt Index*)

## Eigenschaften
- jeder Schlüssel hat entweder **gar keinen** oder **genau einen** Wert
- falls der Schlüssel beim Einfügen schon vorhanden ist, wird der Wert überschrieben
- löschen eines Schlüssels löscht das ganze Paar
- Sortierung beliebig

```java
interface Map<K, V> {
	void clear();
	int size();
	boolean isEmpty();
	V put(K key, V value);
	V get(Object key);
	V remove(Object key);
	boolean containsKey(Object key);
	boolean containsValue(Object value);
}
```

## TreeMap
- Schlüsselmenge in binärem Suchbaum
- funktioniert mit [[Comparable]]

## HashMap
- Schlüsselmenge durch Hashing
