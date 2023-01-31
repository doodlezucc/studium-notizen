# Mehrfachvererbung
Eine Klasse kann (prinzipiell) von mehreren Basisklassen erben ("Mehrfachvererbung"). In Java ist der Übersicht halber **nur Einfachvererbung** möglich.

#### Interfaces mit Default-Methoden
Java 8+ erlaubt **default**-Methoden innerhalb von Interfaces, welche eine Standard-Implementierung vorgeben.

 ```java
interface MyInterface {
	void firstMethod();
	void secondMethod();
	
	default void callAllMethods() {
		firstMethod();
		secondMethod();
	}
}
```

Damit ist *Mehrfachvererbung* auch in Java möglich.

```java
interface Printer {
	default void printName() {
		System.out.println("Unknown");
	}
}

interface InputReceiver {
	default void handleInput(char keyPressed) {
		System.out.println("Pressed key " + keyPressed);
	}
}

class Game implements Printer, InputReceiver {}

Game game = new Game();
game.printName(); // "Unknown"
game.handleInput('a'); // "Pressed key a"
```

##### Doppelte Methoden
**Fehler**, falls zwei implementierte Interfaces eine Methode mit **gleichem Namen** und **gleichen Argumenten** definieren.

```java
interface Bob1 {
	default void bob() {
		System.out.println("Bob1::bob");
	}
}

interface Bob2 {
	default void bob() {
		System.out.println("Bob2::bob");
	}
}

class Bob implements Bob1, Bob2 {}
```

Kann behoben werden durch **Disambiguation**.

```java
class Bob implements Bob1, Bob2 {
	@Override
	public void bob() {
		Bob2.super.bob();
	}
}
```