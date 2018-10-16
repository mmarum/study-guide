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

  * methods of list objects:
    - list.append(x), list.extend(iterable), list.insert(i, x), list.remove(x), list.pop([i]), list.clear(), list.count(x), list.sort(key=None, reverse=False), list.reverse(), list.copy()

  * Return zero-based index in the list of the first item whose value is equal to x:
    - `list.index(x[, start[, end]])`

  * Use list as stacks aka "last-in, first-out"
    - `append(), pop()`

  * Sort by value:
    - `new_var = sorted(var, key=lambda x: int(x['whatevs']), reverse=True)`

# TUPLE
`colors=('Red','Green','Blue')`
  * Like a list but is immutable

# SET
`myset={3,1,2}`
  * Like a list but does not hold duplicate values and is unordered
  * Can do union and intersection, difference (membership testing)
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
    > {'sape': 4139, 'guido': 4127, 'jack': 4098}
```
  * Show index and value
```
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
```
  * list(d) on a dict returns a list of all keys
`sorted(d)`

# Generators
`yield`

  * returns only next item in list
  * saves memory; good for huge lists

# List Comprehensions
`[x**2 for x in range(10)]`
`[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]`
`[abs(x) for x in vec]`
`[(x, x**2) for x in range(6)]`
  * The following list comprehension will transpose rows and columns:
```
matrix = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], ]
[[row[i] for row in matrix] for i in range(4)]
```
or
```
list(zip(*matrix))
> [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
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
```
{x: x**2 for x in (2, 4, 6)}
> {2: 4, 4: 16, 6: 36}
```

# Fibonacci
```
a, b = 0, 1
while a < 100:
    print(a, end=' ')
    a, b = b, a+b
```

# Underscores
  * `_var` A single underscore in front of a variable name is a hint that a variable is meant for internal use only.
  * `var_` You can append a single underscore to break the naming conflict like class_ or def_.
  * `__var` rewrite the attribute name in order to avoid naming conflicts in subclasses; Like: `dir(t)` `['_ClassName__var'...]`
  * `__var__` reserved for special use in the language; Like; __init__ or __call__
  * `_` used as a name to indicate that a variable is temporary or insignificant; like `for _ in range(32)`

# Useful built-in functions
  * `dir()`

dbader.org
