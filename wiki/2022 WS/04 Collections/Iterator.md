# Iterator
Ein Iterator bewegt sich über eine Sequenz, ohne die unterliegende Datenstruktur zu kennen.
- leicht herzustellen
- bewegen sich in nur eine Richtung

```java
interface Iterator<E> {
	boolean hasNext();
	E next();
	void remove();
}
```

## Iterable
`for-each`-Schleifen sind eine einfachere Schreibweise, die `iterator()`-Methode von `Iterable`-Objekten (alle Collections sind `Iterable`) zu nutzen.

```java
void cancelAll(Collection<TimerTask> c) {
	for (TimerTask t : c) {
		t.cancel(); // Aktion auf einzelnem Element
	}
}
```

```java
void cancelAll(Collection<TimerTask> c) {
	for (Iterator<TimerTask> i = c.iterator(); i.hasNext();) {
		TimerTask t = i.next();
		t.cancel(); // Aktion auf einzelnem Element
	}
}
```
