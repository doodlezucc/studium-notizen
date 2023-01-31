# Upcast und Downcast
Nur in Java relevant, weil es eine **streng typisierte Sprache** ist.

## Upcast (Verallgemeinern)
Instanz einer Unterklasse wird als eine ihrer Oberklassen behandelt.

- immer erlaubt
- nur Methoden und Attribute der Superklasse verwendbar
- beim Aufrufen einer Methode wird dennoch die "unterste" überschriebene Variante aufgerufen (**dynamisches Binding / late binding**)

## Downcast (Spezifizieren)
Instanz einer Oberklasse wird als eine ihrer Unterklassen behandelt.

- **Casting Exception**, falls die Instanz nicht der gecasteten Unterklasse entspricht
- erlaubt das Nutzen von ergänzten Methoden und Attributen

```java
// Upcast
Shape shape = new Circle(...);

// Downcast
Circle circle = (Circle) shape;
```
