a = str(input())


def is_palindrom(a):

    b = a[::-1]
    if a == b:

        return 'true'
    else:
        return 'false'
    
    
print(is_palindrom(a))