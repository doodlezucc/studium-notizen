# Lambda
Lambda = Anonyme Funktion

### Java 7
```java
StateOwner stateOwner = new StateOwner();
stateOwner.addStateListener(new StateChangeListener() {
	public void onStateChange(State oldState, State newState) {
		System.out.println("State changed");
	}
});
```

### Java 8+
```java
StateOwner stateOwner = new StateOwner();
stateOwner.addStateListener(
	(oldState, newState) -> System.out.println("State changed")
);
// ODER
stateOwner.addStateListener((oldState, newState) -> {
	System.out.println("State changed");
});
```

### Python
```python
lambda ARGS : COMPUTATION

def anonymous(ARGS):
	COMPUTATION
```
