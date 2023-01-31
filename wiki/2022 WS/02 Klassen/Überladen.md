## Java
Es können mehrere Methoden mit dem gleichen Namen aber unterschiedlicher *Signatur* deklariert werden.
```java
public int max(int a, int b) {
	return a < b ? b : a;
}

public double max(double a, double b) {
	return a < b ? b : a;
}
```

(auch mit Konstruktoren möglich)

## Python
Nicht möglich, weil Methoden wie *Attribute* behandelt werden. Weitere Deklarationen desselben Namens überschreiben die vorherige Definition.

Stattdessen können **Default**-Werte für Argumente definiert werden.

```python
def refresh_page(delete_cache = False):
	# Implementierung...

refresh_page() # delete_cache = False

refresh_page(True) # delete_cache = True

refresh_page(delete_cache=True) # expliziter Parameter
```
