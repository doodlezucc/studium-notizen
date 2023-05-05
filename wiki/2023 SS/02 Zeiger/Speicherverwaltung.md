# Speicherverwaltung
Daten eines ausgeführten Programms werden an unterschiedlichen Orten im Rechner gespeichert.

Bei der Ausführung eines Programms liegen an einem festen Ort:
- (Maschinen-)Code des Programms
- Statische Variablen und Konstanten

## Stack

Der Stack eines Programms wird bei der Ausführung *dynamisch verwaltet*. Das heißt, die Größe des Stacks verändert sich während des Programmablaufs.

Wenn innerhalb einer Methode Variablen definiert werden, wird Speicher auf dem Stack reserviert (der Speicher *wächst*). Sobald die Methode durchlaufen ist, werden die reservierten Speicheradressen wieder freigegeben (der Speicher *nimmt ab*).

Der Stack wird für **lokale Variablen** genutzt, die z.B. nur innerhalb einer for-Schleife verwendet werden.

> [!NOTE] Wertsemantik
> Primitve Datentypen wie zum Beispiel `int` oder `float` werden normalerweise auf dem Stack gespeichert und als *Wert* behandelt: Wenn eine Methode einen *Wert* als Parameter annimmt, wird eine **Kopie** des Werts in der Methode verwendet.
> 
> Der Wert kann also innerhalb der Methode verändert werden, ohne das er sich außerhalb der Methode ändert.

## Heap
Der Heap wird von allen Programmen des Rechners gleichzeitig genutzt. Durch das "Allokieren" kann Speicher auf dem Heap für das eigene Programm reserviert werden.

> [!NOTE] Referenzsemantik
> Erweiterte Datentypen wie zum Beispiel ein Array oder ein Objekt werden normalerweise auf dem Heap angelegt und mit einem [[Zeiger]] als *Referenz* behandelt: Wenn eine Methode einen Zeiger als Parameter annimmt, wird kann dieser [[Zeiger#Dereferenzierung|dereferenziert]] werden.
> 
> Auf diese Weise wird ein Array oder Objekt global - also auch außerhalb der Methode - verändert.
