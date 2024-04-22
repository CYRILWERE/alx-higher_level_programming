#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Use the values 0 for each missing integer
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Use only the first 2 integers
    result_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result_tuple

if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1,)))
    print(add_tuple(tuple_a, ()))

