Alle Klassen, Methoden und Variablen in Java haben eine "Sichtbarkeit".

| UML-Symbol | Sichtbarkeit                  | Selbes Package | Unterklassen | Außerhalb des Package |
| ---------- | ----------------------------- | -------------- | ------------ | --------------------- |
| `-`        | `private`                     |                |              |                       |
| `~`        | `default ("package-private")` | x              |              |                       |
| `#`        | `protected`                   | x              | x            |                       |
| `+`        | `public`                      | x              | x            | x                     |

## Sichtbarkeit von Klassen
- mehrere Klassendefinitionen pro Datei möglich
- genau eine Klasse muss `public` sein und dem Dateinamen gleichen
- Klassen ohne `public` sind nur innerhalb des Datei-[[Pakete|Packages]] nutzbar

```java
package mypackage;

public class Klasse1 { // public
	...
}

class Klasse2 { // package-private
	...
}
```
