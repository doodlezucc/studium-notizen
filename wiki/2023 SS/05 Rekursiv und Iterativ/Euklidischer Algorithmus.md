# Euklidischer Algorithmus
Betrachtet man die Zahlen 44 und 12, dann sieht man, dass sie **beide** durch 2 teilbar sind. 2 ist also ein **gemeinsamer Teiler** der beiden Zahlen. Ein weiterer gemeinsamer Teiler ist die Zahl 4, da sowohl die Division $44 : 4 = 11$ als auch $12 : 4 = 3$ eine Ganzzahl ergibt.

Der **Euklidische Algorithmus** berechnet den **größten gemeinsamen Teiler** ("ggT") von zwei Zahlen $a$ und $b$. Der größte gemeinsame Teiler ist die höchste Zahl, durch die sowohl $a$ als auch $b$ geteilt werden kann.

In der folgenden Abbildung wird veranschaulicht, wie der Algorithmus funktioniert. In jedem Schritt wird die kleinere Zahl so oft wie möglich von der größeren Zahl subtrahiert. Das wird so oft wiederholt, bis die kleinere von beiden Zahlen komplett von der anderen subtrahiert werden kann und das Ergebnis der Subtraktion 0 ist. Ab diesem Fall ist der Algorithmus fertig und die verbleibende Zahl wird zurückgegeben.

![](https://upload.wikimedia.org/wikipedia/de/f/fb/Euklidischer_Algorithmus.png)