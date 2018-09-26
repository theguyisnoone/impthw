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

    def get(self,index):
        """get the value at index"""
        node=self.begin
        i=0
        while node:
            if i==index:#找到了返回值
                return node.value
            else:#不然遍历
                i += 1
                node=node.next
        return None

    def shift(self,obj):
        """just another name for push"""
        self.push(obj)


    def unshift(self):
        """remove the first item(from begin) and returns it"""
        #if we have one  at begin
        if self.begin:
            #save the begin
            node=self.begin
            #if we have only None
            if self.begin ==self.end:
                #clear begin and end
                self.begin=None
                self.end=None
            #else  we have more
            else:
                #set begin to begin.next
                self.begin=node.next
                #set begin.prev to none
                self.begin.prev=None
            #return the value
            return node.value
        #else sekf.begin =None
            return  None


    def count(self):
         """Counts the number of elements in the list."""
         # do the slow count code from single linked lists
         node=self.begin
         count=0
         while node:
             count+=1
             node=node.next
         return count


    def _invariant(self):
        if self.begin == None:#链表头为空，尾巴也要空
            assert self.end==None ,"End set while begin is not."

        if self.begin:#如果链表不为空
            assert self.begin.prev ==None,"begin.prev not noen"#头没有前驱
            assert self.end.next ==None,"end.next not null"    #尾没有后继

    def detach_node(self,node):
        #if the node is at the end
        if self.end ==node:
            self.pop()
        #elif it's at the beginning
        elif self.begin == node:
            self.unshift()
        #else it's in the middle
        else:
            #skip over it
            #save node.prev,node.next
            prev=node.prev
            nxt=node.next
            #set prev.next to saved next
            prev.next=nxt
            #set next.prev to saved prev
            nxt.prev=prev

    def remove(self,obj):
        """Finds a matching item and removes it from the list."""
        #start at begin
        node=self.begin
        #keep the count as return value
        count=0
        #while we have a node
        while node:
            #if the node.value matches object
            if node.value == obj:
                self.detach_node(node)
                return count
            else:
                count+=1
                node=node.next
        #return -1  to indicate not there
        return -1

    def first(self):
        """return a reference to the first item doesn't remove"""
        return self.begin and self.begin.value or None

    def last(self):
        """return a reference to the first item doesn't remove"""
        return self.end and self.end.value or None

    def dump(self,mark="----"):
        #set node to begin
        node=self.begin
        print(mark)
        #while there's a node,print it out
        while node:
            print(node,end=" ")
            #next node
            node=node.next
        #print new line
        print()

#####test########

# colors=DoubleLinkedList()
# #push()
# colors.push("first")
# print(f"'begin:'{colors.begin}'end:'{colors.end}")
# print(colors.count())
# colors.push("second")
# print(f"'begin:'{colors.begin}'end:'{colors.end}")
# print(colors.count())
# colors.push("third")
# print(f"'begin:'{colors.begin}'end:'{colors.end}")
# print(colors.count())
#
# #pop()
# print('>>>first pop')
# colors.pop()
# print(f"'begin:'{colors.begin}'end:'{colors.end}")
# print('>>>second pop')
# colors.pop()
# print(f"'begin:'{colors.begin}'end:'{colors.end}")
# print('>>>third pop')
# colors.pop()
# print(f"'begin:'{colors.begin}'end:'{colors.end}")

#remove()
colors = DoubleLinkedList()
colors.push("Cobalt")
colors.push("Zinc White")
colors.push("Nickle Yellow")
colors.push("Perinone")
print(f"all:{colors.count()}")
print(f"first:{colors.first()}")#first()
print(f"last:{colors.last()}")#last()
print(colors.remove("Cobalt"))
print(f"now:{colors.count()}")
colors.dump("before perinone")
print(colors.remove("Perinone"))
colors.dump("after perinone")
print(f"now:{colors.count()}")
print(colors.remove("Nickle Yellow"))
