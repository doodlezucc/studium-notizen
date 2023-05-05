# Assertions
Assertions (auch "Annahmen" und "Zusicherungen" genannt) können **im Quellcode** geschrieben werden, um sicherzustellen, dass das Programm zu einem gewissen Zeitpunkt (z.B. beim Aufrufen einer Methode) in einem **erwarteten Zustand** ist.

In Java geht das beispielsweise mit einer **`assert`-Zeile**:

```java
public static float getAverageOfArray(float[] array) {
	assert array != null: "The array parameter must not be null.";
	assert array.length > 0: "The array parameter must not be empty.";
	
	// ...
}
```

Hier wird *zugesichert* ("asserted"), dass beim Start der Methode der übergebene Array-Parameter `array` nicht `null` ist und mindestens ein Element enthält (Länge > 0). Jedes Mal, wenn die Methode aufgerufen wird, werden diese Bedingungen (`array != null` und `array.length > 0`) überprüft. Falls man der Methode einen leeren Array überliefert, wird das Programm an dieser Stelle durch eine Exception abgebrochen.

Es ist möglich, beim Ausführen eines Java-Programms über die [[Kommandozeile]] die Assertions an- oder auszuschalten. Durch ein [[Kommandozeile#Befehle mit Argumenten ausführen|Argument]] namens `-enableassertions` wird entschieden, ob das Programm bei fehlgeschlagenen *Assertion-Bedingungen* abbricht oder nicht.

