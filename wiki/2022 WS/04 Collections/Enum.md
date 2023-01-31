- Alternative zu `class`
- **ohne Vererbung**
- für **wenige konstante Instanzen**

Instanzmethoden:
- `ordinal()`: Index der Definition
- `compareTo()`: Index vergleichen

Klassenmethoden:
- `values()`: [[Iterator#Iterable|Iterable]] aller definierter Konstanten im Enum

## [[UML]]-Notation
| `<<enumeration>>`<br> **Weekday**   |     |
| ------------- | --- |
| `+ MONDAY`    |     |
| `+ TUESDAY`   |     |
| `+ WEDNESDAY` |     |
| `+ THURSDAY`  |     |
| `+ FRIDAY`    |     |
| `+ SATURDAY`  |     |
| `+ SUNDAY`    |     |

## `switch`-Vergleich
```java
Weekday day = Weekday.SATURDAY;
switch (day) {
	case MONDAY:
	case TUESDAY:
	case WEDNESDAY:
	case THURSDAY:
	case FRIDAY:
		System.out.println("Wochentag");
		break;
	case SATURDAY:
	case SUNDAY:
		System.out.println("Wochenende");
		break;
}
```
