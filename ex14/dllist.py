class DoubleLinkedListNode(object):
    def __init__(self,value,nxt,prev):
        self.value=value
        self.next=nxt
        self.prev=prev

    def  __repr__(self):
        nval=self.next and self.next.value or None
        pval=self.prev  and self.prev.value or None
        return f"[{self.value},{repr(nval)},{repr(pval)}]"

class DoubleLinkedList(object):

    def __init__(self):
        self.begin=None
        self.end=None

    def push(self,obj):
        #if there are contents
        if self.end:
            node=DoubleLinkedListNode(obj,None,self.end)
            #node.next=new node
            self.end.next=node
            #new node  is end
            self.end=node
        #else begin  and end are new node with none
        else:
            #链表的begin&end都连接node（无需prev和next）
            self.begin=DoubleLinkedListNode(obj,None,None)
            self.end=self.begin

    def pop(self):
        """Removes the last item and returns it."""
        # if we have some
        if self.end:
            # get the end node
            node = self.end
            # if there is one
            if self.end == self.begin:
                self.end = None
                self.begin = None
            else:
                # detach end and reset it
                # end = end.prev
                self.end = node.prev
                # end.next = None
                self.end.next = None
                # if there's now one left, set begin to end
                if self.end == self.begin:
                    self.begin.next = None
            return node.value
        else:
            return None

    def count(self):
         """Counts the number of elements in the list."""
         # do the slow count code from single linked lists
         node=self.begin
         count=0
         while node:
             count+=1
             node=node.next
         return count


colors=DoubleLinkedList()
#push()
colors.push("first")
print(f"'begin:'{colors.begin}'end:'{colors.end}")
print(colors.count())
colors.push("second")
print(f"'begin:'{colors.begin}'end:'{colors.end}")
print(colors.count())
colors.push("third")
print(f"'begin:'{colors.begin}'end:'{colors.end}")
print(colors.count())

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
