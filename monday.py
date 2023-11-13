from functools import reduce
def neighbors_of2(cell):
    r, c = cell
    for row in [r - 1, r, r + 1]:
        for column in [c - 1, c, c + 1]:
            if (row, column) != (r, c):
                yield row, column
def flatten(collections):
    return {value for collection in collections
                for value in collection}
def neighbors_of(cell):
    r, c = cell
    return {(row, column) for row in [r - 1, r, r + 1]
                for column in [c - 1, c, c + 1]
                    if (row, column) != (r, c)}
                
def count_living_neighbors(cell, living_cells):
    return len([neighbor for neighbor in neighbors_of(cell) if neighbor in living_cells])
def will_live(cell, living_cells):
    living_neighbor_count = count_living_neighbors(cell, living_cells)
    return cell in living_cells and living_neighbor_count == 2 or living_neighbor_count == 3
def next_generation_from(living_cells):
    potential_cells = living_cells | flatten(map(neighbors_of, living_cells))
    return {cell for cell in potential_cells if will_live(cell, living_cells)}
# itr = neighbors_of((2, 2))
# while True:
#     try:
#         print(next(itr))
#     except StopIteration:
#         break
def test_map():
    square = lambda x: x**2
    assert list(map(square, [2,3,5])) == [4,9,25]
def test_filter():
    is_even = lambda x: x % 2 == 0
    assert list(filter(is_even, [2,3,5,6])) == [2,6]
def test_reduce():
    add = lambda a, b: a + b
    assert reduce(add, [2,3,5]) == 10
def test_list_equality():
    assert [1,2] == [1,2]
def test_set_equality():
    assert {1,2,1,1,2} == {2,1}
def test_list_comprehensions():
    assert [x ** 2 for x in [2,5,7]] == [4, 25, 49]
def test_set_comprehensions():
    assert {x ** 2 for x in [2,5,7,2]} == {4,49,25}
def test_list_comprehensions_with_condition():
    assert [x ** 2 for x in [2,5,7] if x % 2 == 1] == [25, 49]
def test_anonymous_functions():
    square = lambda p: p * p
    def square2(p):
        return p * p
    
    assert [square(x) for x in [2,5,7]] == [4, 25, 49]
    assert [square2(x) for x in [2,5,7]] == [4, 25, 49]
def test_neighbors_of():
    assert neighbors_of((2, 2)) == {(1, 1), (2, 1), (3, 1), (1, 2), (1, 3), (3, 2), (2, 3), (3, 3)}
def test_next_generation_from():
    living_cells = { (1, 2), (2, 2), (3, 2) }
    assert set(next_generation_from(living_cells)) == {(2, 1), (2, 2), (2, 3)}
        


# class example in python
class BinarySearchTree:
    # note: this would is a static variable
    # message = "hello"
    # nested class
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right
    # constructor has a special name
    def __init__(self):
        # constructor populates the object with member variables
        self.root = None
    # methods all accept the object (self) expicitly
    def in_order_nodes_generator(self):
        def traverse(node):
            if node is not None:
                yield from traverse(node.left)
                yield node.value
                yield from traverse(node.right)
        return list(traverse(self.root))
    
    def get_length(self):
        return len(self.in_order_nodes_fast())
    
    def in_order_nodes_fast(self):
        values = []
        def traverse(node):
            if node is not None:
                traverse(node.left)
                values.append(node.value)
                traverse(node.right)
        traverse(self.root)
        return values
    
    def add(self, value):
        def after_adding(node, value):
            if node is None:
                return BinarySearchTree.Node(value)
            if value < node.value:
                node.left = after_adding(node.left, value)
            elif value > node.value:
                node.right = after_adding(node.right, value)
            return node
        self.root = after_adding(self.root, value)
        # returning self to allow chaining
        return self
    


from random import shuffle
def test_bst():
    b = BinarySearchTree()
    b.add(3).add(1).add(10)
    assert b.get_length() == 3
    assert b.in_order_nodes_fast() == [1, 3, 10]
    assert b.in_order_nodes_generator() == [1, 3, 10]

def test_bst_big():
    n = 50
    to_add = list(range(n))
    shuffle(to_add)
    b = BinarySearchTree()
    for v in to_add:
        b.add(v)
    assert b.in_order_nodes_fast() == sorted(to_add)

def time_comparison():
    from timeit import timeit
    n = 50
    to_add = list(range(n))
    shuffle(to_add)
    b = BinarySearchTree()
    for v in to_add:
        b.add(v)
    print(timeit(lambda: b.in_order_nodes_fast()))
    print(timeit(lambda: b.in_order_nodes_generator()))

