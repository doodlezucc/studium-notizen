# Klassen und Objekte
## Klassenbeziehungen

Die wichtigsten Beziehungen zwischen zwei Klassen sind
1. Die **Benutzungs-Beziehung** - In jeder Klasse stehen Methoden, die von anderen Klassen verwendet werden können.
2. Die **Vererbungs-Beziehung** - Jede Klasse kann als Oberklasse für ihre erbenden Unterklassen dienen.

## Klassendaten und -operationen

Klassendaten sind Attribute, die nicht einem **Objekt**, sondern einer ganzen **Klasse** gehören. In den Sprachen C++, C# und Java sind Klassendaten mit `static` gekennzeichnet.

Zusätzlich spricht man von **Klassenoperationen**, wenn eine Klasse statische Methoden enthält.

Beispiel in Java:
```java
public class Circle {
	private static final float PI = 3.14159; // Statisches Klassenattribut

	// ...

	public static float getPI() { // Statische Klassenoperation
		return Circle.PI;
	}
}
```


## Abstrakte Klassen

Von abstrakten Klassen können keine Objekte erzeugt werden. Sie dienen sozusagen nur als Gruppierung oder **Vorlage** für spezifischere Unterklassen.