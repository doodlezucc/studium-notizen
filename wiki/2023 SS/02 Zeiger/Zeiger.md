# Zeiger
Alle Variablen eines Programms müssen an einem bestimmten Ort im Rechner gelagert werden. Jedes Mal, wenn im Ablauf eines Programms eine neue Variable deklariert wird, wird *Speicher* reserviert.

```cpp
int a = 5;
int b = 10;
```

Hier werden zwei Integer definiert. Für beide Variablen werden im Speicher neue Adressen extra für die jeweiligen Integer reserviert. Es gibt jetzt also einen festen Ort im Speicher, an dem die Werte 5 und 10 eingetragen sind.

Die Werte, die an diesen Speicheradressen eingetragen sind, können durch Zuweisungen verändert werden.

```cpp
int a = 5;
int b = 10;

a = 7;
b = a + 1;
```

Nach Ablauf des Codes stehen im Speicher an den jeweiligen Adressen von `a` und `b` jetzt die Zahlen 7 und 8. Die vorherigen Werte werden also durch die Zuweisungen überschrieben. Es muss hier kein weiterer Speicher reserviert werden, weil keine neue Variable angelegt wird.

## Referenzierung

In C/C++ ist es möglich herauszufinden, an welcher Speicheradresse der Wert einer Variable gespeichert ist.

Ein *Zeiger* oder *Pointer* ist eine Speicheradresse. Zeiger sind keine Daten - stattdessen geben sie an, *wo Programmdaten im Speicher* zu finden sind. Mit anderen Worten, ein Zeiger ist eine **Referenz** auf Daten.

```cpp
int a = 5;

int* a_speicher_adresse = &a; // REFERENZIERUNG
```

Der Ausdruck ` &a ` bedeutet "Speicheradresse von `a`". An genau dieser Adresse liegt im Speicher jetzt die Zahl 5.

Man sagt hier, dass *`a_speicher_adresse`* ein **Pointer auf `a`** oder eine **Referenz auf `a`** ist und auf den Integerwert 5 "zeigt".

Durch das Symbol `*` nach dem Typ `int` wird angegeben, dass es sich um einen Zeiger auf einen Integer handelt.

## Dereferenzierung

Umgekehrt ist es auch möglich, aus einer gegebenen Speicheradresse die darin gelagerten Daten zu lesen. Diesen Vorgang nennt man **Dereferenzierung**.

```cpp
int a = 5;

int* a_speicher_adresse = &a; // REFERENZIERUNG

int b = *a_speicher_adresse; // DEREFERENZIERUNG
```

Der Ausdruck ` *a_speicher_adresse ` bedeutet "Gespeicherter Wert von `a_speicher_adresse`".

Hier wird die Referenz auf `a` wieder aufgelöst, sodass die neue Variable `b` schließlich auch genau den Wert 5 hat, welcher an der Speicheradresse von `a` gespeichert war.

## Verkettete Listen
Verkettete Listen werden in C/C++ mit Zeigern umgesetzt:
- Eine Liste besteht nur aus einem Zeiger auf das erste *Element* (Head) der Liste.
- In jedem *Element* ist ein `*next` Zeiger auf das nächste *Element* der Liste.
- Auf diese Weise sind alle *Elemente* vom Anfang bis zum Ende der Liste miteinander verkettet.

