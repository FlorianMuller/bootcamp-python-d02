
def ft_filter(function_to_apply, list_of_inputs):
    for elem in list_of_inputs:
        if function_to_apply is None:
            if elem:
                yield elem
        else:
            if function_to_apply(elem):
                yield elem


if __name__ == "__main__":
    lst = range(20)

    res = filter(lambda x: x > 10, lst)
    print(list(res))

    res = ft_filter(lambda x: x > 10, lst)
    print(list(res))
