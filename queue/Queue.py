from DoubleLinkedListNode import *
from dllist import *
class Queue(object):

    def __init__(self):
        self.list = DoubleLinkedList()

    def shift(self, obj):
        """Shifts a new element onto the back of the queue."""
        self.list.shift(obj)

    def unshift(self):
        """Removes the element that is first in the queue."""
        self.list.unshift()

    def dump(self,mark="=----="):
        self.list.dump()

colors = DoubleLinkedList()
colors.shift("Viridian")
colors.shift("Sap Green")
colors.shift("Van Dyke")
print(colors.dump("all"))
print( colors.unshift())
print( colors.unshift())
print( colors.unshift())
print( colors.unshift())
