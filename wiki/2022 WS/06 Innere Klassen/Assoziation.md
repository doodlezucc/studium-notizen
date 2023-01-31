## Beziehungen zwischen [[UML]]-Klassen
- ungerichtet (kein Pfeil): "nicht definiert"
- gerichtet (1-2 Pfeilenden)
- reflexiv (auf sich selbst gerichtet)

![[Assoziation.png]]

## Spezielle Typen von Assoziation

![[Aggregation Komposition.png]]

### Aggregation
```java
public class Foo {
	private Bar bar;
	Foo(Bar bar) {
		this.bar = bar;
	}
}
```

#### Komposition
- starke Form der Aggregation
- Teil-Objekt kann nicht ohne sein Komposit-Objekt existieren
	- darf also nicht nach außen weitergegeben werden
```java
public class Foo {
	private Bar bar = new Bar();
	private class Bar{
		...
	}
}
```

```java
public class Foo {
	private Bar bar;
	public Foo() {
		bar = new Bar(this);
	}
}

class Bar {
	private Foo foo;
	public Bar(Foo foo) {
		this.foo = foo;
	}
}
```
