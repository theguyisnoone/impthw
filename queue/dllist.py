from DoubleLinkedListNode import *

class DoubleLinkedList(object):

    def __init__(self):
        self.begin=None
        self.end=None

    def push(self, obj):
        if self.end:
            node = DoubleLinkedListNode(obj, None, self.end)
            self.end.next = node
            self.end = node
        else:
            self.begin = DoubleLinkedListNode(obj, None, None)
            self.end = self.begin

    # def pop(self):
    #     """Removes the last item and returns it."""
    #     # if we have some
    #     if self.end:
    #         # get the end node
    #         node = self.end
    #         # if there is one
    #         if self.end == self.begin:
    #             self.end = None
    #             self.begin = None
    #         else:
    #             # detach end and reset it
    #             # end = end.prev
    #             self.end = node.prev
    #             # end.next = None
    #             self.end.next = None
    #             # if there's now one left, set begin to end
    #
    #         return node.value
    #     else:
    #         return None

    # def get(self,index):
    #     """get the value at index"""
    #     node=self.begin
    #     i=0
    #     while node:
    #         if i==index:#找到了返回值
    #             return node.value
    #         else:#不然遍历
    #             i += 1
    #             node=node.next
    #     return None

    def shift(self,obj):
        """just another name for push"""
        self.push(obj)


    def unshift(self):
        if self.begin:
            node = self.begin

            if self.end == self.begin:
                self.end = None
                self.begin = None
            else:
                self.begin = node.next
                self.begin.prev = None

            return node.value
        else:
            return None




    #
    # def count(self):
    #      """Counts the number of elements in the list."""
    #      # do the slow count code from single linked lists
    #      node=self.begin
    #      count=0
    #      while node:
    #          count+=1
    #          node=node.next
    #      return count


    # def _invariant(self):
    #     if self.begin == None:#链表头为空，尾巴也要空
    #         assert self.end==None ,"End set while begin is not."
    #
    #     if self.begin:#如果链表不为空
    #         assert self.begin.prev ==None,"begin.prev not noen"#头没有前驱
    #         assert self.end.next ==None,"end.next not null"    #尾没有后继

    # def detach_node(self,node):
    #     #if the node is at the end
    #     if self.end ==node:
    #         self.pop()
    #     #elif it's at the beginning
    #     elif self.begin == node:
    #         self.unshift()
    #     #else it's in the middle
    #     else:
    #         #skip over it
    #         #save node.prev,node.next
    #         prev=node.prev
    #         nxt=node.next
    #         #set prev.next to saved next
    #         prev.next=nxt
    #         #set next.prev to saved prev
    #         nxt.prev=prev

    # def remove(self,obj):
    #     """Finds a matching item and removes it from the list."""
    #     #start at begin
    #     node=self.begin
    #     #keep the count as return value
    #     count=0
    #     #while we have a node
    #     while node:
    #         #if the node.value matches object
    #         if node.value == obj:
    #             self.detach_node(node)
    #             return count
    #         else:
    #             count+=1
    #             node=node.next
    #     #return -1  to indicate not there
    #     return -1

    # def first(self):
    #     """return a reference to the first item doesn't remove"""
    #     return self.begin and self.begin.value or None
    #
    # def last(self):
    #     """return a reference to the first item doesn't remove"""
    #     return self.end and self.end.value or None

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
