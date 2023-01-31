# Weitere Listen
Verschiedene Typen von Listen.

## Linked List
Eine Linked List beinhaltet nur eine Referenz auf das **erste** Element ("*head*"). Dieses Element kann dann auf den **nächsten** Eintrag in der Liste verweisen.

#### Doppelte Linked List
Eine [[#Linked List]], wobei jedes Element der Liste beinhaltet eine Referenz auf das nächste Element **und das vorherige** Element.

#### Circular Linked List
Eine Circular Linked List ist ein geschlossener "Ring" von Elementen.
- Das letzte Element der Liste zeigt wieder auf das erste Element
- Kann mit [[#Linked List]] oder [[#Doppelte Linked List]] umgesetzt werden

## Stack
Implementiert LIFO ("*Last in, first out*").
- `push(<ELEMENT>)` - Element auf den Stack *legen*
- `pop()` - Oberstes Element aus dem Stack *entnehmen*
- `peek() / top()` - Oberstes Element aus dem Stack *zurückgeben*, aber **nicht entnehmen**

## Queue
Implementiert FIFO ("First in, first out").
- `enqueue(<ELEMENT>)` - Element an das Ende der Queue *anhängen*
- `dequeue()` - Vorderstes Element aus der Queue *entnehmen*
- `front()` - Vorderstes Element *zurückgeben*, aber **nicht entnehmen**
- `rear()` - Hinterstes Element *zurückgeben*