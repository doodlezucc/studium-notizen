# Komplexitätsberechnung
Es gibt drei Methoden zur Komplexitätsberechnung bei Rekursionen.

## Substitution (Induktion)
Aus den Laufzeit-Komponenten eines Algorithmus wird eine rekursive Funktion gebildet. Aus dieser Funktion wird eine Komplexität eingeschätzt und dann induktiv bewiesen.

- Rekursive Formel: z.B. $T(n) = 2T(n/2) + n$
- **Geschätzte** Komplexität der Formel: $\Theta(n \log{n})$
- Induktion: Beweisen von $T(n) \leq c * n \log{n}$ (Komplexität multipliziert mit einer Konstante)

## Rekurrenzbaum
Darstellung der Teilprobleme als einzelne Knoten eines [[Bäume|Baums]]. Jeder Teilproblem-Knoten ist beschriftet mit seinem "Arbeitsaufwand" (Komplexität).

- Die Komplexität von Blättern ist $\Theta(1)$
- **Gesamtkomplexität** durch Addition aller Knoten

![[Rekurrenzbaum.png]]

## Master-Theorem
Diese Methode kann nur genutzt werden, falls der rekursive Algorithmus die folgende Form.
$$T(n) = a * T(n/b) + f(n)$$
Komponenten seien dabei
- Anzahl der Teilprobleme pro Rekursionsschritt: $a \geq 1$
- Teilung des Inputs pro Teilrekursion: $b > 1$

Dann wird zwischen drei Fällen unterschieden, abhängig von der Komplexität von $f(n)$.
$$f(n) = \Theta(n^c)$$
1. $c < \log_b a \implies T(n) = \Theta(n^{\log_b a})$
2. $c = \log_b a \implies T(n) = \Theta(n^c * \log{n})$
3. $c > \log_b a \implies T(n) = f(n)$

