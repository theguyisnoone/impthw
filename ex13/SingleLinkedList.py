class SingleLinkedNode(object):
    def __init__(self,value,nxt):
        self.value=value
        self.next=nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


class SingleLinkedList(object):

    def __init__(self):
        self.begin=None#头结点
        self.end=None#尾节点



    def push(self, obj):
        """Appends a new value on the end of the list."""
        node=SingleLinkedNode(obj,None)
        if self.begin==None:
            self.begin=node
            self.end=self.begin#?
        else:
            self.end.next=node
            self.end=node#?
            assert self.begin !=self.end

        assert self.end.next ==None


        assert self.end.next == None


    def pop(self):
        """Removes the last item and returns it."""
        if self.end == None:
            return None
        elif self.end == self.begin:
            node = self.begin
            self.end = self.begin = None
            return node.value
        else:
            node = self.begin
            while node.next != self.end:
                node = node.next
            assert self.end != node
            self.end = node
            return node.next.value

    def shift(self, obj):
        """Another name for push."""

    def unshift(self):
        """Removes the first item and returns it."""

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""

    def first(self):
        """Returns a *reference* to the first item, does not remove."""

    def last(self):
        """Returns a reference to the last item, does not remove."""

    def count(self):
        """Counts the number of elements in the list."""
        node=self.begin
        count=0
        while node:
            count +=1
            node =node.next
        return count

    def get(self, index):
        """Get the value at index."""

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""



#push()
colors = SingleLinkedList()
colors.push("Pthalo Blue")

print(f'"begin:"{colors.begin}"end:"{colors.end}')
print(colors.end.next)
assert colors.count() == 1
print(colors.count())
colors.push("Ultramarine Blue")
print(f'"begin:"{colors.begin}"end:"{colors.end}')
assert colors.count() == 2
print(colors.count())
# colors.push("third")
# print(f'"begin:"{colors.begin}"end:"{colors.end}')


#pop()
colors.pop()
print(">>>pop1:")
print(f'"begin:"{colors.begin}"end:"{colors.end}')
colors.pop()
print(">>>pop2:")
print(f'"begin:"{colors.begin}"end:"{colors.end}')











colors=DoubleLinkedList()
#push()
colors.push("first")
print(f"'begin:'{colors.begin}'end:'{colors.end}")
colors.count()
colors.push("second")
print(f"'begin:'{colors.begin}'end:'{colors.end}")
colors.count()
colors.push("third")
print(f"'begin:'{colors.begin}'end:'{colors.end}")
colors.count()

#pop()
print('>>>first pop')
colors.pop()
print(f"'begin:'{colors.begin}'end:'{colors.end}")
print('>>>second pop')
colors.pop()
print(f"'begin:'{colors.begin}'end:'{colors.end}")
print('>>>third pop')
colors.pop()
print(f"'begin:'{colors.begin}'end:'{colors.end}")
