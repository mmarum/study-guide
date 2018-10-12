# LIST
`list1=[1,2,3,4,5,6,7,8]`
  * A list is mutable

  * Access a single item from list
    - `list1[3]`
    - `list1[-2]`

  * Slicing a List
    - `list1[1:4]`

* Deleting a List
    - `del list1[3]`
    - `del list1`

# TUPLE
`colors=('Red','Green','Blue')`
  * Like a list but is immutable

# SET
`myset={3,1,2}`
  * Like a list but does not hold duplicate values and is unordered
  * Can do union and intersection, difference
```
    A = {0, 2, 4, 6, 8};
    B = {1, 2, 3, 4, 5};
    print("Union :", A | B)
    print("Intersection :", A & B)
    print("Difference :", A - B)
    print("Symmetric difference :", A ^ B)
```
  * to create an empty set you have to use set(), not {}

# DICTIONARY
`mydict={1:2,2:4,3:6}`
```
for key, val in mydict.iteritems(): # or items()
    print "the {} and {}".format(key, val)
```
  * The dict() constructor builds dictionaries from sequences of key-value pairs
```
    dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    {'sape': 4139, 'guido': 4127, 'jack': 4098}
```
  * Show index and value
```
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
```

# Generators
`yield`

  * returns only next item in list
  * saves memory; good for huge lists

# List Comprehensions
`[x**2 for x in range(10)]`
`[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]`
`[abs(x) for x in vec]`
`[(x, x**2) for x in range(6)]`
```
from math import pi
[str(round(pi, i)) for i in range(1, 6)]
```
```
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
[[row[i] for row in matrix] for i in range(4)] #OR
list(zip(*matrix))
```

# Set Comprehensions
`a = {x for x in 'abracadabra' if x not in 'abc'}`

# Dict Comprehensions
`{x: x**2 for x in (2, 4, 6)}`
