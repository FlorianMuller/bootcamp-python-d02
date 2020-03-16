
def ft_map(function_to_apply, *list_of_inputs):
    # return (function_to_apply(*args) for args in zip(*list_of_inputs))

    for args in zip(*list_of_inputs):
        yield function_to_apply(*args)


if __name__ == "__main__":
    lst1 = [1, 2, 3, 4]
    lst2 = [" is cool", " is bad", " is green"]

    res = map(lambda x, y: str(x) + y, lst1, lst2)
    print(next(res))
    print(list(res))

    res2 = ft_map(lambda x, y: str(x) + y, lst1, lst2)
    print(next(res2))
    print(list(res2))
