# Innere Klassen
## Vorteile von inneren Klassen
- logische Gruppierung vereinfacht die Pakete
- erhöhte Verkapselung (kann private Felder der äußeren Klasse nutzen und verändern)
- Code besser lesbar und wartbar (*good practice*)

### Statische Klassen
- Können von überall verwendet werden mithilfe von `A.B`

```java
public class Account {
	private int userId;
	private Permissions perm;
	
	public Account(int userId) {
		this.userId = userId;
		perm = new Permissions();
	}
	
	public static class Permissions {
		public boolean canRead;
		public boolean canWrite;
		public boolean canDelete; 
	}
	
	public Permissions getPermissions() { return perm; }
}
```

```java
Account.Permissions = new Account.Permissions();
```

### Instanzklassen
- Können auf alle Eigenschaften einer Instanz zugreifen

```java
public interface Selector<T> {
	Iterable<T> getItems();
}

public class Sequence<T> {
	private List<T> items;

	private class SequenceSelector implements Selector {
		@Override
		public Iterable<T> getItems() {
			return items; // Private member of Sequence
		}
	}

	public Selector selector() {
		return new SequenceSelector();
	}
}
```

### Lokale Klassen

```java
class Math {
	public static void calculate() {
		// Lokale innere klasse
		class Differntial {
			...
		}
		
		var diff = new Differential();
	}

}
```

### Anonyme Klassen

```java
interface Callback {
	void call();
}

class Delay {
	public final Callback callback;

	public Delay(Callback callback) {
		this.callback = callback;
	}
}

public static void main(String[] args) {
	var delay = new Delay(new Callback() {
		@Override
		void call() {
			System.out.println("Done");
		}
	});
}
```



### Python

```python
class Outer():
	class Inner():
		def __init__(self, name):
			self.name = name

	def __init__(self):
		self.construct = Outer.Inner("Construct")

	def __str__(self):
		return f"Outer '{self.construct.name}'"
```
