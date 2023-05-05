# Begrifflichkeiten
In dem Konzept [[Spezifikation durch Vertrag]] können verschiedene Bedingungen festgelegt werden, die im "Vertrag" eines Dienstes beachtet werden müssen.

## Vorbedingung

Eine Vorbedingung beschreibt, was **vor dem Aufrufen** einer Methode oder eines *Dienstes* gelten muss. Um zum Beispiel die Quadratwurzel einer Zahl zu berechnen, muss vorher gelten, dass die Zahl nicht negativ ist. Der eingegebene Parameter hat also einen festgelegten **Wertebereich** zwischen 0 und $\infty$.

## Nachbedingung

Nachdem ein Dienst fertig bearbeitet ist, wird sein Ergebnis zurückgeliefert. Für dieses Ergebnis stehen in der Spezifikation immer eine oder mehrere Nachbedingungen. Sie bestimmen, was zurückgegeben wird - den **Rückgabetyp** und den **Wertebereich** des Ergebnisses.

## Invariante

Mit einer Invariante in einem Vertrag wird festgelegt, dass sich bestimmte Zustände einer Software während des Aufrufen eines Dienstes **nicht ändern** und konsistent bleiben. Falls zum Beispiel eine Methode `arrayToString` die Elemente eines Arrays in einem String zurückgeben soll, kann in der Spezifikation dieser Methode die folgende **Invariante** stehen:
- *"Die Länge und der Inhalt des überlieferten Arrays wird durch den Dienst `arrayToString` nicht verändert."*

```java
public static String arrayToString(int[] array) {
	return // ...
}
```

