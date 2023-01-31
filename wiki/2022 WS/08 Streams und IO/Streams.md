# Streams
Ein Stream ist eine Datenstruktur ähnlich wie eine **Queue**/Warteschlange.

Streams besitzen zwei Seiten:
1. **Quelle**: Hier werden Daten in die Queue *hinzugefügt*.
2. **Senke**: Hier werden Daten aus der Queue *entfernt*.

![[Stream.png]]

In Java werden Streams für verschiedene Operationen verwendet.

1. Ein-/Ausgabe über die Konsole ([[Standard-Datenströme]] `System.in`/`System.out`/`System.err`)
2. Laden/Speichern von [[Dateien]] (`FileInputStream`, `FileOutputStream`)