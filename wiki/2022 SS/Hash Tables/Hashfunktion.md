# Hashfunktion
## Kriterien für gute Hashfunktionen
Geringe Wahrscheinlichkeit von Kollisionen
- Möglichst gleichmäßige Verteilung der Hashwerte auf erwartete Eingabewerte

Chaos
- Ähnliche Eingabewerte sollen zu möglichst verschiedenen Hashwerten führen
- Idealfall: Ändern eines Eingabe-Bits = Ändern der Hälfte aller Hash-Bits

Surjektivität
- Kein Hashwert soll unmöglich sein

Effizienz
- Funktion muss schnell berechenbar sein
- Funktion muss ohne großen Speicherverbrauch auskommen

Lösung: Kryptographische Hashfunktionen (md5, sha1)