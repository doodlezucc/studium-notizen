## Java
In Java unterscheidet man zwischen **Klassen**-Methoden (`static`) und **Objekt/Instanz**-Methoden.

## Python
**3** Kategorien von Methoden.

#### Instanz-Methoden
- erstes Argument: `self`
- gehören zur konkreten Instanz

#### Klassen-Methoden
- erstes Argument: `cls`
- Aufruf durch `Klasse.methode()` oder `instanz.methode()`

#### Statische Methoden
- kein implizites Argument
- direkt in der Klasse definiert
- Aufruf durch `Klasse.methode()` oder `cls.methode()`

```python
class Math:
	@classmethod
	def version(cls):
		return "1.0"
	
	@staticmethod
	def add(a, b):
		return a + b
	
	@classmethod
	def rechne(cls):
		return cls.add(22, 20)
```