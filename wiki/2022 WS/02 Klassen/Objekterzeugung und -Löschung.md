Objekte werden aus Klassen (Objekt-Vorlagen) mit dem Aufrufen eines **Konstruktors** erzeugt. Wenn das Objekt nicht mehr gebraucht wird, muss der belegte Speicher freigegeben werden.

## Java
**Erzeugen**
```java
public class MyObject {
	private int id;
	
	public MyObject(int id) {
		this.id = id;
	}
}

MyObject mo = new MyObject(123);
```

**Löschen**
Automatisch durch Garbage Collector.

## Python
**Erzeugen**
```python
class MyObject():
	def __init__(self, id):
		self.id = id

mo = MyObject(123)
```

**Löschen**
```python
del mo
```
