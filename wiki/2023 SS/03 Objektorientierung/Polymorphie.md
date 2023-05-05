# Polymorphie
Polymorphie ("Vielgestaltigkeit") heißt bei objektorientierten Sprachen, dass ein Objekt mehr als nur einer festen Klasse angehören kann. Durch Vererbung ist es möglich, ein Objekt zu verallgemeinern oder zu spezifizieren.

Wenn man zum Beispiel einen *Hund* oder eine *Katze* betrachtet, können beide auch als *Haustier* oder noch weiter als *Tier* und *Lebewesen* verallgemeinert werden.

```
			Lebewesen
			    |
			   Tier
			    |
			 Haustier
		________|________
		|               |
	  Katze            Hund
```

Eine Katze wird kann in dieser Klassenhierarchie *polymorph* genannt werden. Sie kann in mehreren Formen oder Gestalten beschrieben werden: Als *Lebewesen*, als *Tier*, als *Haustier* oder am präzisesten als *Katze*.

## Vererbung

Angenommen, in der Klasse *Haustier* steht ein `name`-Attribut und in der Klasse *Lebewesen* gibt es ein `alter`-Attribut. Dann werden diese Attribute an die Klassen *Katze* und *Hund* **vererbt**, sodass jede Katze und jeder Hund jeweils ein eigenes Alter und einen bestimmten Namen hat.

```
			  Lebewesen - - - - - - [alter] (int)
			      |
			     Tier
			      |
			   Haustier - - - - - - [name] (String)
		__________|__________
		|                   |
	  Katze                Hund
    /       \            /      \
 [alter]  [name]      [alter] [name]
```

Die Vererbung und die Polymorphie sind in der objektorientierten Programmierung ein allgegenwärtiges Konzept.

Durch die Polymorphie kann man z.B. in der Programmiersprache Java ein Objekt der Klasse *Katze* erstellen und als eine andere "Gestalt" behandeln. In diesem Beispiel wird eine Katze als allgemeines *Lebewesen* behandelt. Deshalb kann hier nicht das `name`-Attribut der spezifischeren Klasse *Haustier* verwendet werden.

```java
Lebewesen lebewesen = new Katze(2, "Mark");

int alter = lebewesen.alter;  //  ✔ Keine Fehler

String name = lebewesen.name; // ❌ Fehler, weil nicht jedes LEBEWESEN einen Namen hat
                        ^^^^
```
