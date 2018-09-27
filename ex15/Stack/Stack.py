class StackNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


class Stack(object):
    def __init__(self):
        self.top=None

    def push(self,obj):
        """push a new value to the top of the Stack """

        # if self.top !=None:
        #     node=StackNode(obj,self.top)
        #     self.top=node
        # else:
        #     node=StackNode(obj,None)
        #     self.top=node
        ##简便成
        self.top=StackNode(obj,self.top)


    def pop(self):
        """pops the value that is currently on the top of the stack """
        if self.top:
            node=self.top
            self.top=node.next
            return node.value
        else:
            return None

    # def top(self):#重名报错
    #     """returns a  reference to the first item,does not remove """
    #     return self.top!=None and self.top.value or None
    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.top != None and self.top.value or None

    def count(self):
        """count the numbers of elements in the stack """
        count=0
        node=self.top
        while node:
            count +=1
            node=node.next
        return count


    def dump(self,mark="------"):
        print(mark,end=" ")
        node=self.top
        while node:
            print(node,end=" ")
            node=node.next
        print()

colors = Stack()
colors.push("Cadmium Red Light")
print(colors.first())
colors.push("Hansa Yellow")
print(colors.dump("test"))
print(colors.first())
colors.push("Pthalo Green")
print(colors.first())
