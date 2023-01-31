# Generics
Siehe [[Typisierung]].

## Generische Datentypen
Man will
- beliebige Elementtypen zulassen
- beim Aufrufen von Container-Operationen einen konkreten Typ nutzen

#### Lösung 1 - Polymorphe Behälter
- alle Elemente als `Object` behandelt
- manuelles [[Upcast und Downcast#Downcast (Spezifizieren)|Downcasting]]
- keine Typsicherheit

#### Lösung 2 - Generische Datentypen
- Deklaration einer Collection erhält Elementtyp als **generischen Typ-Parameter**
- seit Java 5
- `List<E>` = generischer Typ, `E` = Typ-Parameter
```java
interface List<E> {
	void add(int index, E element);
}

class ArrayList<E> extends List<E> {
	public void add(int index, E element) { ... }
}

// Liste von Strings erzeugen
ArrayList<String> myList = new ArrayList<String>();

// seit Java 7 kürzer durch Typ-Inferenz
ArrayList<String> myList = new ArrayList<>();
```
