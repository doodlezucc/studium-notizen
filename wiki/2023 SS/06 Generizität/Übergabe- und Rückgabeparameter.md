# Übergabe- und Rückgabeparameter
In Programmieren von Methoden ist es möglich, beliebig viele Parameter in der Signatur anzugeben. Ab einer gewissen Anzahl von Parametern in einer Methode wird das allerdings unübersichtlich und führt zu unleserlichem Code. Die folgende Methode nimmt zum Beispiel 5 unterschiedliche Parameter an.

```java
public void createPerson(String firstName, String lastName, int age, int height, String eyeColor) {
	// ...
}
```

Um den Code übersichtlich zu halten, wird es empfohlen, statt einer großen Anzahl von primitiven Parametern nur **einen einzigen abstrakten Datentyp** als Parameter in die Signatur zu schreiben.

```java
class PersonDetails {
	String firstName;
	String lastName;
	int age;
	int height;
	String eyeColor;
}

public static void createPerson(PersonDetails details) {
	// ...
}
```

Dieses Verfahren hat neben der Übersichtlichkeit außerdem den Vorteil, dass die Parameter in einer **beliebigen Reihenfolge** angegeben oder sogar vollständig ausgelassen werden können.

```java
public static void main(String[] args) {
	PersonDetails detailsRoland = new PersonDetails();
	
	details.eyeColor = "Brown";
	details.firstName = "Roland";
	details.age = 50;
	
	createPerson(detailsRoland);
}
```

Dieses Konzept ist auch für den **Rückgabewert** einer Methode anwendbar. Eine Methode kann nur einen einzigen Rückgabewert zurückgeben. Falls eine Methode zum Beispiel also zwei Integer zurückgeben will, ist es **notwendig**, einen abstrakten Datentyp für dieses Ergebnis zu erzeugen.

```java
class Range {
	int minValue;
	int maxValue;
}

// Gibt den kleinsten und den größten Wert des Array "array" zurück.
public static Range getArrayValueRange(int[] array) {
	int min = array[0];
	int max = array[0];
	
	for (int value : array) {
		if (value < min) {
			min = value;
		} else if (value > max) {
			max = value;
		}
	}
	
	Range result = new Range();
	result.minValue = min;
	result.maxValue = max;
	
	return result;
}
```