# CPU
#### Vorgang
- Kommando wird aus dem Speicher/Heap in **Kommandoregister** geladen
- **Kommandologik** führt aktuelles Kommando aus
	- **Programmzähler** manipulieren (z.B. jmp-Befehl)
	- Daten lesen/schreiben (zwischen einem Rechenregister AX, BX, CX, DX und dem Speicher/Heap oder **Stackpointer** SP)
	- Rechne/Vergleiche (arbeitet auf Rechenregistern)
- Programmzähler wird um 1 erhöht (falls nicht manipuliert)
