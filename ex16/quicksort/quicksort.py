from dllist import DoubleLinkedList
from queue import Queue
from random import randint

def node_at(numbers, i):
    count = 0
    node = numbers.begin
    while count < i:
        count += 1
        node = node.next
        assert node, f"Attempted to get node past end {i}"
    return node


def quick_sort(numbers, lo, hi):
    """Sorts a list of numbers using quick sort.
    You must implement this one based on the p-code
    at https://en.wikipedia.org/wiki/Quicksort or
    any other reference.
    """
    if lo < hi:
        p = quick_sort_partition(numbers, lo, hi)
        quick_sort(numbers, lo, p - 1)
        quick_sort(numbers, p + 1, hi)

def quick_sort_partition(numbers, lo, hi):
    print(f">>lo{lo},hi{hi}")
    pivot = node_at(numbers, hi)
    i = lo - 1

    for j in range(lo, hi):
        node_j = node_at(numbers, j)
        if node_j.value < pivot.value:
            i += 1
            if i != j:
                node_i = node_at(numbers, i)
                print(f">>>less before swap node_i,node_i{node_i},node_j{node_j}")
                node_i.value, node_j.value = node_j.value, node_i.value
                print(f">>>less after swap node_i,node_i{node_i},node_j{node_j}")
    node_hi = node_at(numbers, hi)
    node_i = node_at(numbers, i + 1)

    if node_hi.value < node_i.value:
        print(f">>>final less swap node_i,node_i{node_i},node_j{node_j}")
        node_hi.value, node_i.value = node_i.value, node_hi.value
        print(f">>>final after swap node_i,node_i{node_i},node_j{node_j}")
        print("整的一行排好了",numbers.dump())
    return i + 1



def random_list(count):
    numbers = DoubleLinkedList()
    for i in range(count, 0, -1):
        numbers.shift(randint(0, 10))

    return numbers

max_numbers=5

numbers = random_list(max_numbers)
print(">>before")
print(numbers.dump())
quick_sort(numbers, 0, numbers.count() - 1)#lo=0 high=4
print(">>after")
print(numbers.dump())
