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

# DICTIONARY
`mydict={1:2,2:4,3:6}`
```
for key, val in mydict.iteritems():
    print "the {} and {}".format(key, val)
```

# Generators
`yield`

  * returns only next item in list
  * saves memory; good for huge lists
