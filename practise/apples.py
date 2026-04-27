
a = str(input())
words = a.split()

result = {}




for word in words:
    if word in result:        # слово уже есть в словаре?
        result[word] += 1     # увеличь счётчик
    else:
        result[word] = 1
           # первый раз встретили — что ставим?

    
print(result)