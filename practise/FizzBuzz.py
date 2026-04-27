def fizzbuzz(n):
    result = []
    for a in range(1, n+1):
        if a % 5 == 0 and a % 3 == 0:
            result.append('FizzBuzz')

        elif a % 5 == 0:
            result.append('Buzz')
        elif a % 3 == 0:
            result.append('Fizz')
        else:
            result.append(a)
    
    return result

print(fizzbuzz(15))
