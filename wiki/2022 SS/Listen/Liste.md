# Liste
- Lassen sich zur Laufzeit dimensionieren - Höhere Flexibilität bedeutet verringerte Zugriffsgeschwindigkeit
- Einfügen von Elementen
- Suchen von Elementen
- Löschen von Elementen
- (Ändern der Reihenfolge)

### Einfach verkettete Liste
- "Horizontales Stapeln" durch Aneinanderhängen
- Elemente (bis auf das letzte) verweisen auf Nachfolger
- Erstes Element (**Head**) muss gespeichert werden
- Zeiger auf `NULL` gilt als Ende der Liste

#### Mit zusätzlichem Ende der Liste
- Erleichtert das Einfügen neuer Elemente am Ende der Liste (**Tail**)

#### Doppelt verkettete Liste
- Erleichtert das Löschen von Elementen

#### Ring
- Letztes Element zeigt auf **Head**

### Stapel / Kellerspeicher (**Stack**)
- Erlaubt nur zwei Grundoperationen:
	- Ablegen (*push*)
	- Entnehmen des obersten Elements (*pop*)
- Last-in-first-out (**LIFO**)

### Schlange (**Queue**)
- Erlaubt nur zwei Grundoperationen:
	- Einfügen an den Anfang (*enqueue*)
	- Entnehmen am Ende (*dequeue*)
- First-in-first-out (**FIFO**)