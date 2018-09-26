class QueueNode(object):
    def __init__(self,value,nxt,prev):#get 4 arguments
        self.value=value
        self.next=nxt
        self.prev=prev

    def __repr__(self):
        pval=self.prev  and self.prev.value or None
        nval=self.next and self.next.value or None
        return f"{self.value}:nval={repr(nval)}:pval={repr(pval)}"

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
            # node=self.head
            if self.head==self.tail:    #just one element
                self.head=None
                self.tail=None
            else: #many
                node=self.head
                self.head=node.next#head.next?
                self.head.prev=None
            return node.value
        else:
            return None


    def drop(self):
        pass

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



q1=Queue()
q1.shift("p1")
q1.shift("p2")
q1.shift("p3")
print(f"now:{q1.count()}people")
q1.dump("show:")
q1.unshift()
print(f"now:{q1.count()}people")
q1.dump("show:")
