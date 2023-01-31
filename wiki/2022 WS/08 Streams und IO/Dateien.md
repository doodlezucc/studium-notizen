**Datei**: Generell eine (unstrukturierte) Folge von Bytes.
**Dateizeiger**: Byte-Position, an der aktuell gelesen/geschrieben wird.

### Operationen
Dateien müssen "geöffnet" sein, um Daten lesen und schreiben zu können. Danach müssen sie wieder "geschlossen" werden.

- **Öffnen** - "*open*"
	- Es wird ein sogenannter **Dateipuffer** eingerichtet, um schneller auf die Daten einer Datei zugreifen zu können
- **Lesen** - "*read*" (Bytes werden aus einer Datei geladen)
	- Es ist nicht möglich, den **Dateizeiger** über das Ende der Datei (**EOF** = End-of-File) hinaus zu schieben.
- **Schreiben** - "*write*" (Bytes werden in einer Datei verändert)
	- Wenn der **Dateizeiger** hinter **EOF** positioniert ist, werden Daten an eine Datei *angehängt*.
- **Suchen** - "*seek*" (Die Position des **Dateizeigers** wird verändert)
- **Schließen** - "*close*"
	- Speichert die geänderten Daten schließlich auf der Festplatte.

### In Java
Datei-Operationen werden durch zwei spezielle [[Streams]] ermöglicht.

1. `FileInputStream` - Aus dem Strom können Daten **entnommen/gelesen** werden
2. `FileOutputStream` - In den Strom können Daten **hinzugefügt/geschrieben** werden.

Bei [[Textdateien]] sollten bestimmte Klassen genutzt werden.

```java
public static void main(String[] args) throws IOException {
	// "open"
	// DATEISTRÖME für die EIN- und AUSGABE werden erzeugt.
	FileInputStream in = new FileInputStream("datei.txt");
	FileOutputStream out = new FileOutputStream("kopierte_datei.txt");

	// "read"
	// Der erste Byte wird aus der Warteschlange des EINGABE-STROMS entnommen.
	int dataByte = in.read();

	while (b != -1) {
		// "write"
		// Der gelesene Byte wird in die Warteschlange des AUSGABE-STROMS hinzugefügt.
		out.write(b);
	
		// "read"
		// Der nächste Byte wird aus dem EINGABE-STROM entnommen.
		b = in.read();
	}

	// "close"
	// Dateioperationen sind fertig - Alle Streams sollten GESCHLOSSEN werden.
	in.close();
	out.close();
}
```
Beispiel: Die Datei "datei.txt" wird in eine andere Datei "kopierte_datei.txt" **kopiert**.

