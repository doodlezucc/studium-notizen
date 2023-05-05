# Kompilationseinheiten
Ein Programmierprojekt besteht meist aus mehreren selbstgeschriebenen und importierten Quellcode-Dateien, die alle gemeinsam in Maschinencode übersetzt werden müssen, um das Programm auszuführen.

In Java kann man durch die Nutzung von `import` Klassen aus anderen Dateien verwenden, zum Beispiel die Standardimplementierung einer `ArrayList`:

```java
import java.util.ArrayList;
```

Diese Zeile ist wichtig für den **Compiler**, damit er weiß, welche Dateien alle für das Programm relevant sind. Während dem Kompilieren werden alle relevanten Klassendateien übersetzt, sodass man ausführbaren Code erhält.

### Code-Aufteilung in C/C++
In den Programmiersprachen C/C++ ist dieses Konzept noch etwas verfeinert: Zu jeder Klasse gibt es klar getrennt eine **Schnittstellendatei** und eine **Implementationsdatei**.

In der **Header-/Schnittstellendatei** (Dateiendung `.h` oder `.hpp`) stehen nur die Signaturen von Methoden und Konstruktoren der Klasse. Diese Datei wird vom **Compiler** verwendet, um generell zu wissen, welche Klassen und Methoden in verschiedenen Projektdateien existieren.

Die **Implementationsdatei** (Dateiendung `.c`, `.cc` oder `.cpp`) definiert den "Body" oder die Implementierung der einzelnen Methoden, die in der zugehörigen Headerdatei stehen.

Eine Projektstruktur kann dann zum Beispiel so aussehen:
```yaml
projektordner/
  - circle.hpp
  - circle.cpp
```

```cpp
// circle.hpp

class Circle
{
  float x;
  float y;
  float radius;

public:
  Circle(float x, float y, float radius);
  float getArea();
};
```

```cpp
// circle.cpp

#include "circle.h"

Circle::Circle(float x, float y, float radius)
{
  this.x = x;
  this.y = y;
  this.radius = radius;
}

float Circle::getArea()
{
  float PI = 3.14159;
  return PI * radius * radius;
}
```