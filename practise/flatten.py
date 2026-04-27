def flatten(lst):
    result = []

    for x in lst:
        if isinstance(x, list) == True:
            result.extend(flatten(x))
        else:
            result.append(x)
    return result

print(flatten([1, [2, 3], [4, [5, 6]], 7]))