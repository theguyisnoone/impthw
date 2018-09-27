class QueueNode(object):
    def __init__(self,value,nxt,prev):#get 4 arguments
        self.value=value
        self.next=nxt
        self.prev=prev

    def __repr__(self):
        pval=self.prev  and self.prev.value or None
        nval=self.next and self.next.value or None
        return f"{self.value}:nval={repr(nval)},pval={repr(pval)}"
