# Exceptions
### Hierarchie
- `Error` = Problem in der _JVM_
	- **sollten nicht** gecatcht werden
- `Exception` = Problem im _Java-Code_
	- `RuntimeException`: Laufzeitfehler (**können** gecatcht werden)
	- Andere: **sollten** gecatcht werden

```java
try {
	int ergebnis = 5 / 0; // wird Ausnahme werfen
}
catch (ArithmeticException e) {
	System.out.println("Kann nicht durch 0 dividieren.");
	throw e; // rethrow
}
finally {
	// "Aufräumarbeiten"
}
```

