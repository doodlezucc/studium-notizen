# Set
Sets/Mengen beinhalten keine doppelten Elemente.

### HashSet
Implementiert Element-Eindeutigkeit mithilfe Hashings.
- Vorteil: schnelles Einfügen, Löschen und Suchen
- Nachteil: Speicherverbrauch

## SortedSet
Sortieren mithilfe von [[Comparable]]-Schnittstelle.
- Elemente sind [[Comparable]]
- **oder** expliziten [[Comparable#Comparator|Comparator]] im Konstruktor übergeben

### TreeSet
Sortierung mithilfe eines balancierten binären Suchbaums.
