# Zeichenketten in C
In C können Zeichenketten (Strings) mit dem Typ `char*` definiert werden. Es handelt sich bei `char*` um einen [[Zeiger]] auf das *erste Zeichen* eines Strings.

```cpp
char *adresse = "Hello World!";

char zeichen1 = *adresse;       // H
char zeichen2 = *(adresse + 1); // e
char zeichen3 = *(adresse + 2); // l
```

Die Variable `adresse` ist in diesem Beispiel eine **Referenz** auf den ersten Buchstaben "H".

```
*adresse

H e l l o   W o r l d !
^
```

Die einzelnen Zeichen des Strings `"Hello World"` können durch [[Zeiger#Dereferenzierung|Dereferenzierung]] der Speicheradresse erhalten werden. Im Speicher liegen die Zeichen eines Strings direkt nebeneinander.

Durch Addition kann deshalb mit `adresse + 2` zum Beispiel der dritte Buchstabe des Strings erhalten werden.

```
*(adresse + 2)

H e l l o   W o r l d !
    ^
```

## Länge eines Strings

Da nur die Speicheradresse des ersten Zeichens von einem String gespeichert wird, ist nicht offensichtlich, welche Länge ein String tatsächlich hat.

Dieses Problem wird gelöst, indem die letzte Speicheradresse eines Strings mit dem speziellen Zeichen `\0` markiert wird. Das Symbol bedeutet, das hier das Ende des Strings erreicht ist.

```
H e l l o   W o r l d ! \0
                         ^
```
