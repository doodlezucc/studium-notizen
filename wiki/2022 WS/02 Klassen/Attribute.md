# Attribute
## Klassen-Attribute
- auch **statische** Attribute genannt
- *Java*
	- durch `static` veränderbar von überall, abhängig von der Sichtbarkeit
		- deshalb populäre Fehlerquelle
	- durch `static final` wird das Attribut zu einer **Konstante**.
- *Python*
	- direkt in Klasse deklariert
	- wird in Instanzen als Objekt-Attributen kopiert

## Objekt-Attribute
- auch **Instanz**-Attribute genannt

```python
class Dog:
	kind = "canine" # KLASSEN-ATTRIBUT
	
	def __init__(self, name):
		self.name = name # OBJEKT-ATTRIBUT

d = Dog("Rookie")
d.kind # "canine" (KOPIERTER Wert)
d.name # "Rookie"

Dog.kind # "canine" (statisch)
```
