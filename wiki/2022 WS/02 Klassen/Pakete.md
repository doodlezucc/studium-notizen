# Pakete
Pakete erlauben die hierarchische **Strukturierung** von Code.

## Java
- Klassen mit demselben Namen können in mehreren Packages definiert sein.
- Pakete entsprechen normalerweise auch individuellen Ordnern im Projektverzeichnis.
- `java.lang` ist das "Default-Paket" und muss nicht extra importiert werden.

```java
// Package aller Klassen, die in dieser Datei definiert werden
package mypackage;

// Ermöglicht das Nutzen aller Klassen aus dem java.util Package
import java.util.*;

// Ermöglicht das Nutzen der Klasse OtherClass aus dem Package otherpackage
import otherpackage.OtherClass;
```

```java
// Nutzt die Klasse OtherClass ohne Import
otherpackage.OtherClass instanz = new otherPackage.OtherClass();
```

## Python
Python unterscheidet zwischen Modulen und Paketen.

#### Modul
- entspricht einer einzelnen Python-Datei (`my_module.py`)
- importieren mit `import my_module`

#### Paket
- entspricht einem Ordner
- Ordner muss eine Datei namens `__init__.py` beinhalten