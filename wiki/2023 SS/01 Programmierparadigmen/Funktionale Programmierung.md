# Funktionale Programmierung
Die funktionale Programmierung ist ähnlich wie das Umformen und Lösen von mathematischen Ausrücken. Jeder Ausdruck kann so lange aufgelöst werden, bis am Ende nur ein einziger konstanter Wert da steht.

$$f(x) = -x^3$$
$$g(x) = x + 5$$

Die beiden Funktionen $f(x)$ und $g(x)$ können ineinander oder unabhängig voneinander zu einem Ergebnis umgeformt werden.

$$
\begin{align}
f(g(2)) &= f(2 + 5)\\
&= f(7)\\
&= -7^3\\
&= -343
\end{align}
$$

Hier wird der mathematische Ausdruck $f(g(2))$ zu einem konstanten Ergebnis $-343$ aufgelöst.

In der funktionalen Programmierung werden keine Variablen definiert oder zugewiesen - es gibt keine Variablen. Stattdessen gibt es ausschließlich Konstanten und Funktionen. Jede Funktion liefert auf eine Eingabe immer eine vorhersehbare Ausgabe. Funktional geschriebene Programme sind *zustandlos* und können deswegen keine [[Imperative Programmierung#Nebeneffekte|Nebeneffekte]] haben.

Obwohl die [[Programmiersprachen der Vorlesung]] objektorientierte Sprachen sind, ist es trotzdem möglich, das Programmierparadigma der funktionalen Programmierung umzusetzen. Entscheidend für das Paradigma ist die folgende Eigenschaft: Es dürfen keine Variablen angelegt werden - nur die **Parameter** und die **Rückgabe** einer Funktion dienen als **Werte**. Deshalb werden in der funktionalen Programmierung Algorithmen nur in [[Rekursiv und Iterativ#Rekursiv|rekursiver Form]] formuliert.

```java
public static float f(float x) {
	return -(x * x * x); // -x³
}

public static float g(float x) {
	return x + 5;
}


public static void main(String[] args) {
	System.out.println(  f(g(2))  );  // Gibt "-343" in der Konsole aus
}
```

Hier wurden die oberen Funktionen $f(x)$ und $g(x)$ in Java umgesetzt. Der funktionale Ansatz bleibt dabei erhalten, da die Funktionen ausschließlich daraus bestehen, einen Wert zurückgeben.
