Argumente eines Methoden-Aufrufs haben verschiedenes Verhalten, abhängig davon, ob es sich um einen **primitiven** Datentyp oder um eine **Referenz** handelt. ([[Datentypen]])

**call by value** (_primitiver Datentyp / immutable_)
- Argument wird für die Methode "kopiert"
- verändert sich deshalb nicht außerhalb der Methode

**call by reference** (_Referenz / mutable_)
- Argument wird nicht kopiert
- Intern wird also die Speicheradresse übergeben
