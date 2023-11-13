from functools import reduce

def test_list_equality():
    assert [1,2] == [1,2]

def test_set_equality():
    assert {1,2,1,1,2,2,2,1,1} == {1,2}

def test_set_comprehentions():
    assert {x ** 2 for x in {2,5,7}} == {4,25,49}

def test_list_comprehentions():
    assert [x ** 2 for x in [2,5,7]] == [4,25,49]

def test_list_comprehentions_condition():
    assert [x ** 2 for x in [2,5,7] if x % 2 == 1] == [25,49]

def test_anonymous_func():
    square = lambda p: p * p
    def square2(p):
        return p * p
    assert[square(x) for x in [2,5,7]] == [4,25,49]
    assert[square2(x) for x in [2,5,7]] == [4,25,49]

def test_map():
    square = lambda x: x**2
    assert list(map(square, [2,5,7])) == [4,25,49]

def test_reduce():
    add = lambda a, b: a + b
    assert reduce(add, [2,3,4]) == 9

# cell (column, row)

living_cells = {(1, 1), (1,2), (1,3)}

# def neighbors_of(cell):
#     r, c = cell
#     for row in [r - 1, r, r + 1]:
#         for column in [c - 1, c, c + 1]:
#             if (row, column) != (r, c):
#                 yield row, column

# def test_neighbors_of():
#     assert set(neighbors_of((2,2))) == {(1, 1), (2, 1), (1,2), (3, 2), (2, 3), (3, 1), (1, 3), (3, 3)}

def neighbors_of(cell):
    r, c = cell
    return { (row, column) for row in [r - 1, r, r + 1]
                for column in [c - 1, c, c + 1]
                    if (row, column) != (r, c)}

# Don't know if flatten works lol
def flatten(collections):
    return [collection for vs in collections 
        for collection in list]

def test_neighbors_of():
    assert neighbors_of((2,2)) == {(1, 1), (2, 1), (1,2), (3, 2), (2, 3), (3, 1), (1, 3), (3, 3)}

# itr = neighbors_of((2, 2))
#     while True:
#         try:
#             print(next(itr))
#         except StopIteration:
#             break
    
def next_generation_of(living_cells):
    # potentially living = living_cells + neighbors of living cells
    potential_cells = living_cells | flatten(map(neighbors_of, living_cells))
    return {cell for cell in potential_cells if will_live(cell, living_cells)}

def will_live(cell, living_cells):
    living_neighbors_count = count_living_neighbors(cell, living_cells)
    return cell in living_cells and living_neighbors_count == 2 or living_neighbors_count == 3

def count_living_neighbors(cell, living_cells):
    len([neighbor for neighbor in neighbors_of(cell) if neighbor in living_cells])


class BinarySearchTree:
    message = "hello"

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    pass

