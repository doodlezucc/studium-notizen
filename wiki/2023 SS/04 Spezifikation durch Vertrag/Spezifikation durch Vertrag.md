# Spezifikation durch Vertrag
Spezifikation durch Vertrag (**SdV**) führt zu besserer Softwarequalität.

Eine Spezifikation dient als Vorlage für den Code, der in einem Programm stehen soll. In der Spezifikation ist klar beschrieben, welche Werte in eine Methode **eingegeben** und von ihr **ausgegeben** werden können. Das heißt, dass es neben dem Quellcode noch ein Dokument gibt, in dem die Anforderungen an einzelne Komponenten (Methoden, Getter, Setter) einer Software beschrieben werden.

## Client-Supplier-Modell

In dem Client-Supplier-Modell werden die einzelnen Methoden (und weiteren Komponenten) eines Programms als **Supplier** betrachtet. Sie bieten einen **Dienst** an, der an anderen Stellen des Codes genutzt werden kann.

Wenn zum Beispiel eine `sqrt(x)` Methode zum Berechnen der Quadratwurzel existiert, kann diese als ein Dienst-Angebot beschrieben werden. Es wird angeboten, die Quadratwurzel von einer Zahl `x` zu berechnen. 

```java
public static float sqrt(float x) {
	/// ...
}
```

Für dieses Angebot kann es **vertragliche Bedingungen** geben: es ist beispielsweise notwendig, dass die eingegebene Zahl `x` $\geq 0$ ist. Gleichzeitig kann auch garantiert werden, dass die ausgegebene Zahl `sqrt(x)` $\geq 0$ ist.

Angenommen, es gibt noch eine weitere Methode in dem Programm: `distance(px, py, qx, qy)`. In dieser Methode wird die Distanz zwischen zwei Punkten $(px, py)$ und $(qx, qy)$ berechnet.

> [!example] Mathematische Notation
> In mathematischer Schreibweise lässt sich die Distanzberechnung wie folgt formulieren.
> $$Distanz = \sqrt{(qx-px)^2 + (qy-py)^2}$$

```java
public static float distance(float px, float py, float qx, float qy) {
	float x = qx - px;
	float y = qy - py;
	
	return sqrt( x*x + y*y );
}
```

Es wird die oben beschriebene Methode `sqrt(x)` aufgerufen und als **Dienst** verwendet. Es gibt also zwei Seiten:

1. Der Kunde (**Client**) - Die `distance`-Methode will den Dienst `sqrt` benutzen.
2. Der Anbieter (**Supplier**) - Die `sqrt`-Methode bietet ihren Dienst an.

Um den Dienst nutzen zu können, muss ein "Vertrag" geschlossen werden. Sowohl der Supplier als auch der Client sollen den Vertrag einhalten und alle Bedingungen erfüllen. Welche Bedingungen das sind, steht jeweils in der Spezifikation der Software. In diesem Fall gibt es zwei Bedingungen:

1. Eine **Vorbedingung** - Die eingegebene Zahl `x` in `sqrt(x)` darf nicht negativ sein.
2. Eine **Nachbedingung** - Das Ergebnis von `sqrt(x)` ist die Quadratwurzel von `x`. Dieses Ergebnis kann nicht negativ sein.

Es ist durch den Vertrag klar definiert, was die `sqrt`-Methode benötigt, um ein gewünschtes Ergebnis zu liefern. Ein **Client** weiß deshalb immer genau, welches Ergebnis er von seinem **Supplier** bekommen wird, wenn der Vertrag korrekt eingehalten wird.

Mit Spezifikation durch Vertrag werden instabile Programmzustände (wie [[Imperative Programmierung#Nebeneffekte|Nebeneffekte]]) schon vor dem Schreiben des Quellcodes gezielt vermieden - die Softwarequalität verbessert sich also enorm.