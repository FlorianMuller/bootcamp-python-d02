from functools import reduce
import operator


def ft_reduce(function_to_apply, *list_of_inputs):
    if len(list_of_inputs) == 0:
        raise TypeError("ft_reduce expected at least 2 arguments, got 1")
    elif len(list_of_inputs) > 2:
        raise TypeError("ft_reduce expected at most 3 arguments, "
                        f"got {len(list_of_inputs) + 1}")

    lst = list(list_of_inputs[0])
    if len(list_of_inputs) == 2:
        lst.insert(0, list_of_inputs[1])

    if len(lst) == 0:
        raise TypeError("ft_reduce() of empty sequence with no initial value")

    while len(lst) > 1:
        lst.insert(0, function_to_apply(lst[0], lst[1]))
        del lst[1:3]

    return lst[0]


if __name__ == "__main__":
    lst = range(10)

    print(reduce(operator.add, lst))
    print(ft_reduce(operator.add, lst))

    print(reduce(operator.add, lst, 10))
    print(ft_reduce(operator.add, lst, 10))

    lst = ["je ", "suis ", "confiné", " ", "!"]
    print(reduce(operator.concat, lst))
    print(ft_reduce(operator.concat, lst))

    # Error

    # Too mnay arguments
    try:
        print(reduce(operator.concat, lst, 1, 2))
    except TypeError as e:
        print(e)
    try:
        print(ft_reduce(operator.concat, lst, 1, 2))
    except TypeError as e:
        print(e)

    # Not enough argument
    try:
        print(reduce(operator.concat))
    except TypeError as e:
        print(e)
    try:
        print(ft_reduce(operator.concat))
    except TypeError as e:
        print(e)

    # Empty list
    try:
        print(reduce(operator.concat, []))
    except TypeError as e:
        print(e)
    try:
        print(ft_reduce(operator.concat, []))
    except TypeError as e:
        print(e)

    # Empty list WITH init (No error)
    try:
        print(reduce(operator.concat, [], "toto"))
    except TypeError as e:
        print(e)
    try:
        print(ft_reduce(operator.concat, [], "toto"))
    except TypeError as e:
        print(e)
