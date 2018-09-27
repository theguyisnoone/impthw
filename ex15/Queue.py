from QueueNode import *

class Queue(object):
    def __init__(self):
        self.head=None
        self.tail=None

    def shift(self,obj):#stand the back of Queue
        """Shifts a new element onto the back of the queue."""
        if self.head:
            node=QueueNode(obj,None,self.tail)
            self.tail.next=node
            self.tail=node#!!!
        else:
            node=QueueNode(obj,None,None)
            self.head=node
            self.tail=node

    def unshift(self):#go out at the first positon
        if self.head:
            node=self.head  #要放在这里 不然if的代码块无法return
            if self.head==self.tail:    #just one element
                self.head=None
                self.tail=None
            else: #many
                
                self.head=node.next#head.next?
                self.head.prev=None
            return node.value
        else:
            return None


    def drop(self):
        """Take the tail item and forget about it."""
        if  self.head:
            if self.head==self.tail:#single element
                self.head=None
                self.tail=None
            else:
                self.tail=self.tail.prev
                self.tail.next=None

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.head !=None and self.head.value or  None
    def empty(self):
        """Indicates if the Queue is empty."""
        return self.head == None

    def count(self):
        """Counts the number of elements in the queue."""
        node=self.head
        count=0
        while node:#@!!!
            count +=1
            node=node.next
        return count


    def dump(self,mark="----"):
        """Debugging function that dumps the contents of the queue."""
        node=self.head
        print(mark,end="")
        while node:#!!!!!!@@@
            print(node,end="")
            node=node.next
        print()
