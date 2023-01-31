In Java gibt es 3 Standard-Datenströme für die Ein-/Ausgabe von Nachrichten in der **Konsole**.

## Input
Der Standard-Datenstrom **`System.in`** kann Nachrichten verarbeiten, die in der Konsole *eingegeben* werden.

## Output
Die normale *Ausgabe* von `println`-Befehlen funktioniert über den Datenstrom **`System.out`** in Java.

Fehlernachrichten und Ausnahmen werden über einen weiteren Datenstrom namens **`System.err`** ausgegeben. Diese Nachrichten werden in der Konsole in **roter Farbe** angezeigt.

```java
// EINGABE
System.in.read(...);

// AUSGABE (NACHRICHTEN)
System.out.println("Hello World");

// AUSGABE (FEHLER)
System.err.println("Fehler!!!");
```