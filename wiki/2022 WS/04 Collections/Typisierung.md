# Typisierung
## Typsicherheit
Werden Typfehler spätestens zur Laufzeit erkannt, spricht man von **typsicheren Sprachen**.

- keine Typverletzungen
- Typsicherheit zugestellt durch Compiler bzw. Interpreter

## Typprüfung
- Verwendung von Datentypen innerhalb des **Typsystems** prüfen
- Zuweisungen müssen nicht dem exakten Typ entsprechen (z.B. `float zahl = 4;`)
- **statisch typisiert**: Typprüfung während Kompilierung
- **dynamisch typisiert**: Typprüfung primär zur Laufzeit

## Sprachen
#### Java
- **statisch**: Typsicherheit von primitiven Datentypen bereits vom Bytecode-Compiler `javac` geprüft
- **dynamisch**: lässt dynamische Typprüfungen durch `instanceof`-Operator zu

#### Python, JavaScript, PHP, Ruby
- vollständig **dynamisch typisiert**
