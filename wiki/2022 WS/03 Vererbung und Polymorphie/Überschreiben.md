Eine Subklasse kann geerbte Methoden der Superklasse **überschreiben** (override), d.h. neu implementieren.

## Java
Methode muss die gleiche Signatur wie in der Superklasse haben und mit `@Override` gekennzeichnet werden.

**Konstruktoren**
- Der Konstruktor einer Unterklasse führt immer zuerst einen Konstruktor der Oberklasse aus.
- Erste Zeile des Sub-Konstruktors: `super( Argumente... )`

```java
class SuperClass {
	private int id;

	public SuperClass(int id) {
		this.id = id;
	}
	
	public void print(String msg) {
		System.out.println(msg);
	}
}

class SubClass extends SuperClass {
	private String prefix;

	public SubClass(String prefix, int id) {
		super(id);
		this.prefix = prefix;
	}

	@Override
	public void print(String msg) {
		super.print(prefix + msg);
	}
}

// darf vom Typ SuperClass oder SubClass sein
SuperClass instanz = new SubClass("Printing: ", 0);
instanz.id; // 0
instanz.print("Hallo"); // "Printing: Hallo"
```

