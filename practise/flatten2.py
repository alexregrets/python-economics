def second_largest(lst):
    first = float('-inf')
    second = float('-inf')
    for x in lst:
        if x > first:
            second = first
            first = x
        elif x < first and x > second:
            second = x

    return first, second

print(second_largest([3, 1, 4, 1, 5, 9, 2, 6]))
