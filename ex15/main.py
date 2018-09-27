#like main test  not automatic test
#just wanna see the result in the console
from QueueNode import  *
from Queue import *
q1=Queue()
q1.shift("p1")
q1.shift("p2")
q1.shift("p3")
print(f"now:{q1.count()}people")
q1.dump("show:")
q1.unshift()
print(f"now:{q1.count()}people")
q1.dump("show:")
