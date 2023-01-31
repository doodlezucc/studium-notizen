# Algorithmus
Ein Algorithmus beschreibt, wie ein konkretes Problem gelöst werden soll – und zwar exakt. Er besteht aus einer endlichen Abfolge von Anweisungen.

**Erforderliche Eigenschaften**

1. **Finit** - Mit endlichem Text eindeutig beschreibbar
2. **Dynamisch finit** - Endlicher Speicherbedarf
3. **Ausführbar** - Jeder Schritt muss ausführbar sein
4. **Terminierend** - Es werden nur endliche Schritte benötigt

**Weitere mögliche Eigenschaften**

1. **Determiniertheit** - Gleiche Eingabe liefert immer das gleiche Ergebnis
2. **Deterministisch** - Der nächste Programmschritt ist immer eindeutig definiert

## Strategien
Algorithmen nach Strategien kategorisiert.

1. *Brute Force* - Alle möglichen Lösungen unintelligent generieren und alle versuchen
2. **[[Backtracking]]** - Systematisch und schrittweise (vor und zurück) mögliche Lösungen generieren
3. *Divide and Conquer* - Problem rekursiv in **unabhängige** Unterprobleme teilen und dann zusammenfügen
4. *Dynamische Programmierung* - Optimierungsproblem rekursiv in **überlappende** Unterprobleme teilen und dann zusammenfügen
5. **[[Greedy]]** - Immer den nächstbesten Schritt **ohne zurückzugehen**
6. *Branch and Bound* - Backtracking bei Optimierungsproblemen
7. *Hill Climbing* - Optimierungsproblem durch evolutionäre Verbesserungen lösen
8. *Particle Swarm* - Dezentalisierte "Partikel", die organisiert auf unterschiedliche Weise eine Lösung suchen