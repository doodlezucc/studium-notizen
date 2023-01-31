# Zeiger/Pointer
Alle Pointer haben dieselbe Größe.

### Heap-Speicher in C
Speicher im Heap reservieren: `malloc(<size in bytes>)`

- siehe [[sizeof]]
- *return*: Pointer auf Speicheraddresse

Reservierten Speicher freigeben: `free(POINTER)`

```c
// Liegt auf Stack
int a = 18;



// Liegt auf Heap
int *b = &a; // *b == &a == Pointer auf a

int d = *b; // dereferenzieren

// *&a <=> a

// NICHT möglich, keine Addresse zugewiesen.
int *f;
*f = 7; 


int alpha(void) {...}
int *ptr_a(void) = alpha


struct Punkt {
	int x;
	int y;
}

struct Punkt* p = malloc(sizeof(struct Punkt));
if (p == NULL) {
	return NULL;
}

p->x = 1;
p->y = 2;

free(p)

```
