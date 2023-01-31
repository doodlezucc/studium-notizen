## Java
Durch simple Methoden `getID()`, `setID()` ohne Besonderheit umgesetzt.

## Python
Auf zwei mögliche Weisen implementierbar.
```python
class MyObject:
	def __init__(self, id):
		self._id = id
	
	def getid(self):
		return self._id
	
	def setid(self, value):
		self._id = value
	
	def delid(self):
		del self._id
	
	id = property(getid, setid, delid, "Property description.")
```

```python
class MyObject:
	def __init__(self, id):
		self._id = id
	
	@property
	def id(self):
		"""Property description."""
		return self._id
	
	@id.setter
	def id(self, value):
		self._id = value
	
	@id.deleter
	def id(self):
		del self._id
```
