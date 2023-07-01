def Fibonacci(n: int) ->int:
    if n in (1, 2):
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)


number = input()
number = int(number)
print(Fibonacci(number))
