# Paging
Im Normalfall werden alle Ressourcen, die ein Programm im [[#Stack]] oder im [[#Heap]] speichert, physikalisch im **Arbeitsspeicher (RAM)** angelegt.

Die Größe an Daten, die ein Rechner in seinem Arbeitsspeicher haben kann, ist physikalisch eingeschränkt. Wenn auf einem Rechner mehrere Programme gleichzeitig laufen, kann es sein, dass sie gemeinsam die Größe des RAMs überschreiten würden.

Um den Arbeitsspeicher nicht zu überlasten, kommt das sogenannte **Paging** zum Einsatz: Der reservierte Speicher ("Page") von Programmen, die an einem gewissen Punkt keine Rechenleistung verbrauchen, wird _vom **RAM** auf die **Festplatte**_ verschoben. Der **RAM** wird immer für die Programme verwendet, die im Moment viel Rechenleistung benötigen.

Wenn ein inaktives Programm jetzt wieder auf seine Daten zugreifen will, muss die **Page** des Programms wieder zurück in den Arbeitsspeicher geladen werden. Das Verschieben von Daten zwischen **RAM** und **Festplatte** nennt man Paging.

## Virtueller Adressraum
Es ist auch gut zu wissen, dass das Programm selbst nichts von dem Verschieben seiner Daten mitbekommt. Für das Programm bleiben die Speicheradressen seiner Variablen immer gleich, egal ob sie sich gerade auf dem RAM oder auf der Festplatte befinden. Die eigentlichen physischen Adressen sind also **unabhängig** von den Adressen, die innerhalb eines Programms genutzt werden. Deshalb spricht man bei den Speicheradressen, die ein einzelnes Programm reservieren kann, auch von seinem **virtuellen Adressraum**.