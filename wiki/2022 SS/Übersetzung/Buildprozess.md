# Buildprozess
- Programme sind in Hochsprachen geschrieben und müssen in [[Maschinensprache]] übersetzt werden.
- In Hochsprachen können Funktionen (und andere Teile des Codes) sowie Funktionsbibliotheken (wieder-)verwendet werden.
- In Hochsprachen kann umfangreicher Code aus Lesbarkeit in viele Dateien unterteilt werden, die bei Übersetzung zusammengebündelt werden.

**> Code**
`quelltext.c` enthält Präpozessor-Anweisungen (z.B. `#include`, `#ifdef` usw.)

**> Präprozessor/Compiler**
Von C zu [[Assembler]]-Code zu Objektdateien (`quelltext.o`)

**> Linker**
Ausführbare Anwendung (`quelltext.exe`)
