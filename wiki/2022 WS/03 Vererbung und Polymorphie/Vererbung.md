Klassen können von anderen Klassen "abgeleitet" werden.

Abgeleitete Klassen
- erben **alle *Attribute* und *Methoden*** der Basisklasse
- können Attribute und Methoden **ergänzen**
- können Methoden **modifizieren/überschreiben**

Prinzipiell erlauben Programmiersprachen [[Mehrfachvererbung]].

#### Nomenklatur
- Vererbung = Erweiterung = Ableitung
- Basisklasse = Oberklasse = Elternklasse = Superklasse $\Rightarrow$ **Verallgemeinerung**
- abgeleitete Klasse = Unterklasse = Kindklasse = Subklasse $\Rightarrow$ **Spezialisierung**

```java
class Shape {
	private int color;
	
	public Shape(int color) {
		this.color = color;
	}
}

class Circle extends Shape {
	private double radius;

	public Circle(int color, double radius) {
		super(color);
		this.radius = radius;
	}
}
```

```python
class Shape:
	def __init__(self, color):
		self.color = color

class Circle(Shape):
	def __init__(self, color, radius):
		super(Circle, self).__init__(color)
		self.radius = radius
```
