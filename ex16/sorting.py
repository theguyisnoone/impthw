# from dllist import DoubleLinkedList
# from random import randint
#
#
#
#
# def  bubble_sort(numbers):
#     """Sorts a list of numbers using bubble_sort """
#     while True:
#         #start off asuming it's sorted
#         is_sorted=True
#         #comparing 2 at a time ,skipping around
#         node=numbers.begin.next#node is the second one in the list
#         #loop through comparing node to the end
#         while node:
#             #if the next is greater ,then we need to swap
#             node.prev.value,node.value=node.value,node.prev.value#change value
#             #oops,look like we have to scan again
#             is_sorted=False
#         #this is reset at the top but if we never swapped,it's sorted
#         if is_sorted:break
#
# #merge sort
# def count(node):#长度
#     count=0
#     while node:
#         count+=1
#         node=node.next
#     return count
#
# def merge_sort(numbers):
#     numbers.begin=merge_node(numbers.begin)
#
#     node=numbers.begin
#     while node.next:
#         node=node.next
#     numbers.end=node
#
# def merge_node(start):
#     if start.next==None:
#         return start
#
#     mid=count(start)//2
#     #scan to the middle
#     scanner=start
#     for i in range(0,mid-1):
#         scanner=scanner.next
#
#     #set mid node right after the scan point
#     mid_node=scanner.next
#     scanner.next=None#?
#     mid_node.prev=None#?
#
#     merged_left=merge_node(start)
#     merged_right=merge_node(mid_node)
#
#     return  merge(merge_left,merged_right)
#
# def merge(left,right):
#     """Peforms the merge of two lists """
#     result=None
#
#     if left==None: return right
#     if right==None: return left
#
#     if left.value>right.value:
#         result=right
#         result.next=merge(left,right.next)
#     else:
#         result=left
#         result.next=merge(left.next,right)
#
#     result.next.prev=result#??
#     return result
from dllist import DoubleLinkedList
from queue import Queue
from random import randint

def bubble_sort(numbers):
    """Sorts a list of numbers using bubble sort."""
    while True:
        # start off assuming it's sorted
        is_sorted = True
        # comparing 2 at a time, skipping ahead
        node = numbers.begin.next
        while node:
            # loop through comparing node to the next
            if node.prev.value > node.value:
                # if the next is greater, then we need to swap
                node.prev.value, node.value = node.value, node.prev.value
                # oops, looks like we have to scan again
                is_sorted = False
            node = node.next

        # this is reset at the top but if we never swapped then it's sorted
        if is_sorted: break


def count(node):
    count = 0

    while node:
        node = node.next
        count += 1

    return count


def merge_sort(numbers):
    numbers.begin = merge_node(numbers.begin)

    # horrible way to get the end
    node = numbers.begin
    while node.next:
        node = node.next
    numbers.end = node


def merge_node(start):
    """Sorts a list of numbers using merge sort."""
    if start.next == None:
        return start

    mid = count(start) // 2
    print(f">>>mid:{mid}")
    # scan to the middle
    scanner = start

    for i in range(0, mid-1):
        scanner = scanner.next

    # set mid node right after the scan point
    mid_node = scanner.next
    # break at the mid point
    scanner.next = None
    mid_node.prev = None

    merged_left = merge_node(start)
    merged_right = merge_node(mid_node)
    print(f"merged_left{merged_left},merged_right{merged_right}")
    return merge(merged_left, merged_right)



def merge(left, right):
    """Performs the merge of two lists."""
    result = None
    print(">>>",left,right)
    if left == None: return right
    if right == None: return left

    if left.value > right.value:
        result = right
        result.next = merge(left, right.next)
    else:
        result = left
        result.next = merge(left.next, right)

    result.next.prev = result
    print(f"result{result}")
    return result
