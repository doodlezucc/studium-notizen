# Komponenten und Anwendungen
Als **Komponente** wird ein Teil eines Programms bezeichnet, der ausschließlich einen einzigen, spezifischen Zweck erfüllt. Die einzelnen Komponenten, die in einer Software existieren, sind "abgeschlossene Systeme", also unabhängig voneinander. In anderen Worten: die Implementierung einer Komponente hat keinen Einfluss auf die Implementierung der anderen Komponenten.

> [!example] Beispiel
> Zum Beispiel könnte es ein Programm geben, in dem es die zwei folgenden Komponenten gibt:
> 1. *Zahlengenerator* - erfüllt den Zweck, zufällige Zahlen zurückzugeben.
> 2. *Zahlensortierer* - erfüllt den Zweck, eine Liste von Zahlen zu sortieren.
> 
> Diese beiden Komponenten funktionieren unabhängig voneinander und erfüllen komplett unterschiedliche Zwecke.
> 
> Allerdings können sie im Programm kombiniert werden, sodass beim Ausführen des Programms erst ein paar zufällige Zahlen generiert werden (Komponente 1) und diese danach sortiert werden (Komponente 2).

Die Aufteilung einer Software in mehrere Komponenten ist wichtig, um eine bessere Übersicht und eine bessere Softwarequalität zu erhalten.

## Werkzeugkastenkomponente

Eine **Werkzeugkastenkomponente** ist eine Komponente, die mehrere, eng verwandte Methoden zur Verfügung stellt, die von anderen Teilen des Programms verwendet werden können. Wie aus einem Werkzeugkasten können die Methoden der Komponente dann als Hilfsmittel im Code angewandt werden. Eine Werkzeugkomponente kann zum Beispiel eine Klasse sein, in der mehrere verschiedene Sortieralgorithmen implementiert sind.

```java
public class ToolsetSort {
	public void bubbleSort(int[] array) {
		// ...
	}
	
	public void quickSort(int[] array) {
		// ...
	}
	
	public boolean isSorted(int[] array) {
		// ...
	}
}
```

## Generische Komponenten

Mithilfe von [[Generizität]] ist es möglich, einen Algorithmus für unterschiedliche Datentypen zu verwenden. So kann man zum Beispiel einen Sortieralgorithmus entwerfen, der nicht nur Integer, sondern auch Strings und andere Typen sortieren kann. Durch die Nutzung von Generizität muss man also nur **eine einzige Implementierung** des Algorithmus schreiben, die für alle möglichen Datentypen funktioniert. Damit spart man nicht nur an Schreibarbeit, sondern erhöht auch die Softwarequalität, weil der Algorithmus genau an einer bestimmten Stelle im Code zu finden ist.

Sehr praktisch kann es sein, eine ganze Werkzeugkastenkomponente generisch zu machen. Auf diese Weise können alle darin enthaltenen Methoden auf den parametrisierten Typen [[Generizität#Eingeschränkte Generizität|eingeschränkt]] werden.

Im folgenden Beispiel wurde die Sortier-Werkzeugkastenkomponente um einen  generischen Typ-Parameter `<E extends Comparable<E>>` erweitert. Die Algorithmen `bubbleSort`, `quickSort` und `isSorted` nutzen diesen Typen in ihrer Signatur und funktionieren jetzt also auf allen möglichen vergleichbaren Datentypen (`Comparable`).

```java
public class ToolsetSort<E extends Comparable<E>> {
	public void bubbleSort(E[] array) {
		// ...
	}
	
	public void quickSort(E[] array) {
		// ...
	}
	
	public boolean isSorted(E[] array) {
		// ...
	}
}
```
