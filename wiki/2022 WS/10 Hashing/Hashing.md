Hashfunktionen und deren Anwendung.

**Anwendungen**
- **Prüfsummen** - Schnelles Überprüfen der Richtigkeit von ISBN oder Kontonummern durch Modulorechnung
- **Kryptologie** - Einseitiges Verschlüsseln von Passwörtern

**Kriterien für einen guten Hashalgorithmus**
1. **Streuung** - Möglichst gleichverteilte Hashwerte für erwartete Eingaben (weniger Kollisionen)
2. **Datenreduktion** - Ein Hashwert soll weniger Speicher verbrauchen als die Eingabe
3. **Chaos** - Möglichst verschiedene Hashwerte für ähnliche Eingaben
	- Ändern eines einzigen Eingabe-Bits sollte durchschnittlich die Hälfte aller Hashwert-Bits verändern
4. **Surjektivität** - Möglichst viele theoretische Hashwerte
5. **Effizienz** - Möglichst schnell zu berechnen
6. **Ordnungserhaltend** - Bei sortiertem Zugriff auf Hashtabelle

