def unique_elements(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result
print(unique_elements([3, 1, 2, 1, 3, 4]))