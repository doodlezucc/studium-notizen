# Imperative Programmierung
Imperative Programme besitzen sogenannte dynamische **Programmzustände** und heißen auch *zustandsorientiert*.Programmzustände können innerhalb des Programms zugewiesen oder als Werte genutzt werden. Zu Programmzuständen gehören zum Beispiel die Attribute eines Objekts oder die hochzählende Variable einer `for`-Schleife.

Die Grundidee der imperativen Programmierung ist, dass man die Funktionsaufrufe der [[Funktionale Programmierung|funktionalen Programmierung]] durch die **Erzeugung von Objekten** und durch das **Zuweisen von Programmzuständen** ersetzt.

In der imperativen Programmierung entscheidet man zwischen zwei Arten von **Operationen**:

1. **Abfrage** - Es wird ein Programmzustand zurückgeliefert.
2. **Aktion** - Es wird ein Programmzustand verändert oder zugewiesen.
	- Jede Ausführung eines Befehls ändert den Zustand des Programms.
	  Zum Beispiel kann mehrmals der Befehl `i = i + 1` ausgeführt werden, und der Zustand der Variable `i` ändert sich jedes Mal.

Ein imperatives Programm ist nichts weiteres als eine Abfolge von Abfragen und Aktionen.

## Nebeneffekte

Ein **Nebeneffekt** ist eine Aktion, die neben der Hauptoperation ausgeführt wird. Ein Programmzustand wird also verändert, ohne, dass das die beabsichtigte Operation war.

```cpp
int a = 5;
int b = a++; // Hauptoperation: b = 5      Nebeneffekt: a++
```

Hier ist die Hauptoperation die Aktion `b = a`. Der Nebeneffekt besteht darin, dass in der zweiten Zeile die Variable `a` um 1 erhöht wird.
