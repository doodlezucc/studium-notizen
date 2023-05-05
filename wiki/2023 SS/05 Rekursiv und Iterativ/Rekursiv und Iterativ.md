# Rekursiv und Iterativ
Ein Algorithmus kann rekursiv oder iterativ geschrieben werden. Als Beispiel-Algorithmus wird in der Vorlesung der [[Euklidischer Algorithmus|Euklidische Algorithmus]] erklärt und in sowohl rekursiver als auch iterativer Form dargestellt.

## Iterativ

Ein iterativer Algorithmus nutzt eine **Schleife** (z.B. `while`-Schleife oder `for`-Schleife), um zu einer Lösung zu kommen. Es gibt in einer Schleife immer eine **Abbruchbedingung**, die dafür sorgt, dass die Schleife nicht unendlich weiterläuft.

Da es sich bei Schleifen um ein *zustandsorientiertes*, nicht-funktionales Konzept handelt, ist dieser Ansatz nur in der [[Imperative Programmierung|imperativen Programmierung]] umsetzbar.

Der Euklidische Algorithmus lässt sich *iterativ* auf die folgende Weise implementieren.

```python
def ggT(a, b):
	while a != 0: # GEGENTEIL der Abbruchbedingung
	
		if a > b:
			a = a - b
		else:
			# (Die Variablen werden miteinander vertauscht, damit die
			# Abbruchbedingung funktioniert)
			previous_a = a
			
			a = b - a
			b = previous_a
	
	return b
```

## Rekursiv

Der rekursive Ansatz eines Algorithmus besteht aus einer Methode, die **sich selbst aufruft**. Auch in jeder rekursiven Methode muss es eine Abbruchbedingung geben, damit jene nicht unendlich lang weitere Aufrufe tätigt. Erst, sobald die Abbruchbedingung erfüllt ist, wird ein Wert zurückgegeben.

In der [[Funktionale Programmierung|funktionalen Programmierung]] ist **ausschließlich** die rekursive Umsetzung eines Algorithmus möglich, da hier keine Programmzustände zugewiesen werden müssen.

Der Euklidische Algorithmus lässt sich *rekursiv* auf die folgende Weise implementieren.

```python
def ggT(a, b):
	if a == 0: # Abbruchbedingung
		return b
	else:
		if a > b:
			return ggT(a - b, b) # Rekursiv: die Methode "ggT" ruft sich selbst auf.
		else:
			return ggT(b - a, a)
```

Hier wird solange die kleinere Zahl von der größeren subtrahiert, bis die Zahl 0 erreicht ist. Als Abbruchbedingung dient hier die obere Zeile `if a == 0`. Im folgenden Block werden alle Aufrufe dargestellt, die durch die ursprüngliche Methode `ggT(44, 12)` rekursiv entstehen.

```python
ggT(      44, 12) # a > b
 ggT(     32, 12) # a > b
  ggT(    20, 12) # a > b
   ggT(    8, 12) # b ≤ a
    ggT(   4,  8) # b ≤ a
     ggT(  4,  4) # b ≤ a
      ggT( 0,  4) # a == 0 (Abbruchbedingung ist erfüllt)
       return 4
```

### Endrekursiv

Eine rekursive Methode wird *endrekursiv* genannt, wenn die Methode direkt nach dem rekursiven Selbstaufruf an ihrem Ende angelangt ist und danach kein Code mehr in der Methode ausgeführt werden muss.

```python
def f(x):
	if x == 0:
		return 0
	
	f(x - 1) # Rekursiv: die Methode "f" ruft sich selbst auf.
	
	# NICHT ENDREKURSIV: die Methode führt weiteren Code
	# nach dem rekursiven Aufruf aus.
	print(x)


def g(x):
	if x == 0:
		return 0
	
	# ENDREKURSIV: die Methode "g" ruft sich selbst auf und
	# ist danach am Ende angelangt.
	return g(x - 1)
```


## Umwandlung von Rekursiv zu Iterativ

Jeder [[#Endrekursiv|endrekursiv]] formulierte Algorithmus kann auch [[#Iterativ|iterativ]] formuliert werden. Dafür muss man verstehen, wo in dem gegebenen endrekursiven Algorithmus die folgenden 3 Dinge stehen:

1. Das Abbruchkriterium
2. Die Rückgabe beim Abbruch
3. Die Aktion eines Rekursionsaufrufs

```python
def ggT(a, b):
	if a == 0: # ABBRUCHKRITERIUM / Abbruchbedingung
		return b # RÜCKGABE BEIM ABBRUCH
	else:
		if a > b:
			return ggT(a - b, b) # REKURSIONSAUFRUF 1
		else:
			return ggT(b - a, a) # REKURSIONSAUFRUF 2
```

Diese Teile des Codes können dann in eine iterative Form mit einer `while`-Schleife umstrukturiert werden. Dafür sind die folgenden Schritte nötig:

1. Das *Gegenteil* des Abbruchkriteriums wird als **Bedingung** für die `while`-Schleife verwendet.
2. Die Rückgabe beim Abbruch wird **hinter** die `while`-Schleife gesetzt.
3. Die Aktion eines Rekursionsaufrufs wird **innerhalb** der `while`-Schleife geschrieben.

```python
# SCHRITT 1

def ggT(a, b):
	while a != 0: # GEGENTEIL DES ABBRUCHKRITERIUMS
		...
```

```python
# SCHRITT 2

def ggT(a, b):
	while a != 0:
		...
	
	return b # RÜCKGABE BEIM ABBRUCH
```

```python
# SCHRITT 3

def ggT(a, b):
	while a != 0:
	
		if a > b:
			a = a - b # AKTION VON REKURSIONSAUFRUF 1
		
		else:
			# AKTION VON REKURSIONSAUFRUF 2
			
			# (Die Variablen werden miteinander vertauscht, damit die
			# Abbruchbedingung funktioniert)
			previous_a = a
			
			a = b - a
			b = previous_a
	
	return b
```