- Klassen, von denen keine konkreten Objekte/Instanzen erzeugt werden können
- werden als **Schnittstellen** verwendet (mit teilweiser Standardimplementierungen)
- können **abstrakte** Methoden(-Signaturen) beinhalten, welche erst in Unterklassen einen Körper bekommen
- falls die Unterklasse einer abstrakten Oberklasse auch als `abstract` markiert ist, müssen die abstrakten Methoden der Oberklasse **nicht** implementiert werden

```java
abstract class Shape {
	private int color;
	
	public Shape(int color) {
		this.color = color;
	}
	
	public abstract double getArea();
}

class Circle extends Shape {
	private double radius;

	public Circle(int color, double radius) {
		super(color);
		this.radius = radius;
	}

	@Override
	public double getArea() { // MUSS überschrieben werden, weil zuvor abstract
		// area = πr²
		return Math.PI * radius * radius;
	}
}
```
