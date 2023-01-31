Schnittstelle, um Objekte vergleichbar zu machen.
- `< 0`, falls `a < b`
- `== 0`, falls `a == b`
- `> 0`, falls `a > b`

```java
interface Comparable<T> {
	int compareTo(T other);
}

class Integer implements Comparable<Integer> {
	public int compareTo(Integer other) {
		return 3 - 7; < 0
	}
}
```

## Comparator
[[Generics|Typ-Generische]] Schnittstelle, die zwei Objekte desselben Typs

```java
interface Comparator<T> {
	int compare(T a, T b);
}
```
