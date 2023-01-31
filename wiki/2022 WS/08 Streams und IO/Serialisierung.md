Das Konvertieren von einem **Objekt --> Bytes**, die z.B. auf der Festplatte gespeichert werden können.

Die gelagerten Bytes können danach wieder *deserialisiert* werden (**Bytes --> Objekt**).

### Algorithmus der Serialisierung
Algorithmus, um ein bestimmtes Objekt in Bytes zu verwandeln.

1. Erzeuge und Schreiben einer **ID** ("eindeutige Seriennummer") für das Objekt
2. Schreiben der **Klasseneigenschaften** (Klassenname, Attributnamen und -typen)
3. Schreiben der **Attributwerte**
	1. Falls es sich um einen **primitiven Typen** handelt, schreibe ihn direkt
	2. Falls es sich um eine **Referenz** handelt...
		1. Falls die Referenz noch nicht serialisiert ist: **Serialisiere** die Referenz (*rekursiv!*)
		2. Falls die Referenz bereits geschrieben wurde, schreibe ihre **ID**

Eine Klasse ist **nur** serialisierbar, wenn...
1. Sie das [[Interfaces|Marker-Interface]] `Serializable` implementiert
2. In ihren Attributen ausschließlich [[Datentypen#Primitive Datentypen|primitive Datentypen]] und serialisierbare Objekte stehen

### (De-)Serialisierung mit Datenstrom
In Java können serialisierbare Objekte mithilfe von `ObjectOutputStream` in einen Byte-Datenstrom konvertiert werden.

```java
class ObjectOutputStream {
	// Konstruktor
	ObjectOutputStream(OutputStream stream) throws IOException {...}
	
	// Schreibt "obj" in den Strom
	void writeObject(Serializable obj) throws IOException {...}
	
	// Setzt alle Referenzen zurück, die bereits geschriebenen wurden
	void reset() throws IOException {...}
}
```

Zum *Deserialisieren* kann die Klasse `ObjectInputStream` benutzt werden.

```java
class ObjectInputStream {
	// Konstruktor
	ObjectInputStream(InputStream in) throws IOException {...}
	
	// Liest das nächste Objekt aus dem Byte-Datenstrom und gibt es zurück
	Object readObject() throws IOException {...}
}
```

Beispiel:
```java
// Speichert einen Studenten in die Datei "savefile.ser"
public void writeStudentToFile() {
	ObjectOutputStream objectStream;
	
	try {
		Student s = new Student("Hugo", "Test", 12345678);
		s.setNote(1.3);
		
		FileOutputStream fileStream = new FileOutputStream("savefile.ser");
		objectStream = new ObjectOutputStream(fileStream);
		objectStream.writeObject(s);
	} finally {
		objectStream.close();
	}
}

// Liest das erste Objekt aus der Datei "savefile.ser" und gibt es zurück
public Student readStudentFromFile() {
	ObjectInputStream objectStream;
	
	try {
		FileInputStream fileStream = new FileInputStream("savefile.ser");
		objectStream = new ObjectInputStream(fileStream);
		
		Object deserialized = objectStream.readObject();
		return (Student) deserialized; // Explizites Downcasting
	} finally {
		objectStream.close();
	}
}
```

### Grenzen der Serialisierung
- Wenn der Quellcode einer Klasse **abgeändert** wird, können vorher gespeicherte Bytes **nicht mehr** in die Klasse konvertiert werden.
- Aus gespeicherten Bytes können andere Anwendungen nur **sehr schwer** die Daten importieren.
