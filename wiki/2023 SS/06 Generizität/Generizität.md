# Generizität
Das objektorientierte Konzept der **Generizität** erlaubt es, den Typen einer Klasse anzugeben und innerhalb des Codes wiederzuverwenden. Zum Beispiel sagt eine **generische Liste** aus, dass alle Elemente der Liste von einem bestimmten Typ sind.

In Java ist die Generizität mit sogenannten **parametrisierten Typen** umgesetzt. In spitzen Klammern `<...>` kann man nach einem Methodenname oder Klassenname einen spezifischen Typen angeben. Um das Konzept näher zu erklären, werden die Klassen und Vererbungen aus dem Kapitel [[2023 SS/03 Objektorientierung/Polymorphie|Polymorphie]] wiederverwendet.

```
			Lebewesen
			    |
			   Tier
			    |
			 Haustier
		________|________
		|               |
	  Katze            Hund
```

Jede Klasse in dem Schaubild kann als **Typ** genutzt werden. Eine generische Liste kann so definiert werden, dass sie z.B. nur Elemente vom Typ *Hund* enthält.

```java
ArrayList<Hund> hunde = new ArrayList<Hund>();

hunde.add(new Hund()); // Objekt vom Typ "Hund" kann hinzugefügt werden

hunde.add(new Katze()); // Objekt vom Typ "Katze" kann NICHT hinzugefügt werden
              ^^^^^
```

Weil eine *Katze* nicht von der Klasse *Hund* erbt, kann sie nicht in die generische Liste eingefügt werden. Die Schreibweise `ArrayList<Hund>` funktioniert, weil die Klasse `ArrayList` *generisch* ist und einen parametrisierten Typ annimmt.

Um eine Klassendefinition generisch zu machen, können Typ-Parameter mit einem Namen angegeben werden. Normalerweise ist dieser Name `T` ("type") oder im Falle von Kollektionsklassen `E` ("element").

```java
public class MyList<E> { // <E> macht diese Klasse zu einer generischen Klasse

	private E[] elements; // Der Typ-Parameter E kann in der Klasse genutzt werden
	
	public E get(int index) {
		return elements[index];
	}
}
```

### Generizität in C++

In C++ können Klassen und Methoden auf die gleiche Weise umgesetzt werden, allerdings unterscheidet sich die Notation. Anstatt den Typ-Parameter in spitzen Klammern hinter den Klassennamen zu schreiben, wird `template <typename ...>` **vor den Klassennamen** geschrieben. Ähnlich wie in Java kann auch hier eine beliebige Bezeichnung für den Typ-Parameter ausgesucht werden, normalerweise `T` oder für Listen- und Mengen-Datenstrukturen `E`.

Die Definition der generischen Klasse `MyList` von oben sieht in C++ zum Beispiel folgendermaßen aus.

```cpp
// "template <typename E>" macht diese Klasse zu einer generischen Klasse
template <typename E> class MyList {  
	private:
		E elements[]; // Der Typ-Parameter E kann in der Klasse genutzt werden
	
	public:
		E get(int index) {
			return elements[index];
		}
};
```


## Eingeschränkte Generizität

Wenn die Generizität einer Klasse oder einer Methode **auf bestimmte Typen beschränkt** wird, spricht man von eingeschränkter Generizität. Das ist nützlich, wenn man die Attribute und Methoden einer bestimmten Klasse verwenden will.

In Java wird dafür die Notation `<T extends ...>` genutzt, wobei hinter dem Wort extends der eingeschränkte Typ geschrieben wird. Im folgenden Beispiel wird die generische Klasse `Tierbesitzer` auf den Typ-Parameter *Haustier* eingeschränkt.

```java
public class Tierbesitzer<T extends Haustier> {
	private T haustier;
	
	public Tierbesitzer(T haustier) {
		this.haustier = haustier;
	}
	
	public String getHaustierName() {
		// Die Methode "getName()" ist in der Klasse "Haustier" definiert und
		// kann hier wegen der Einschränkung <T extends Haustier> genutzt werden
		return haustier.getName();
	}
}
```

Beim Erzeugen eines `Tierbesitzer`-Objekts kann als generischer Typ *Haustier* oder eine Unterklasse von *Haustier* angegeben werden.

```java
Katze katze = new Katze();

Tierbesitzer<Katze> katzenBesitzer = new Tierbesitzer<>(katze); ✔

Tierbesitzer<Haustier> haustierBesitzer = new Tierbesitzer<>(katze); ✔


Tierbesitzer<Lebewesen> lebewesenBesitzer = new Tierbesitzer<>(katze);
             ^^^^^^^^^
// ❌ Der Typ "Lebewesen" kann NICHT als Typ-Parameter genutzt werden,
//    da ein Lebewesen keine Unterklasse von "Haustier" ist.
```

Im Gegensatz zu Java gibt es in C++ **keine eingeschränkte Generizität**. Es ist also nicht möglich, den Typ-Parameter einer Klasse oder einer Methode auf einen bestimmten Typen zu beschränken.
