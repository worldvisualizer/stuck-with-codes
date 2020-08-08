"""
free thinking:

hashed: add, remove, contains O(1)
array implementation always takes O(n) for lookups
BST implementation: not really O(1), but O(lg n)

is map implementation the best? check if the hashed value 
is in the map, and add it if it doesn't.
"""

def hashit(number: int) -> str:
    return str(number)

class MyHashSet(object):
    def __init__(self):
        # lookup set initialization
        self.map = {}

    def add(self, number: int) -> bool:
        number = hashit(number)
        if not self.map.get(number, None):
            self.map[number] = 1
        return True

    def remove(self, number: int) -> bool:
        number = hashit(number)
        if self.map.get(number, None):
            del self.map[number]
        return True

    def contains(self, number: int) -> bool:
        number = hashit(number)
        return self.map.get(number, None) != None

    def __str__(self):
        return str(self.map.keys())

    def __repr__(self):
        return "MyHashSet()"

myset = MyHashSet()
myset.add(2)
print(myset)

myset.add(3)
myset.add(2)
print(myset)
