def fib(n):
    if n<=1:
        return 1
    return fib(n-1) + fib(n-2)

fib_dict = {
    0: 1,
    1: 1,
    2: 2,
    3: 3,
    4: 5,
    5: 8,
    25: 121393
}

for i in range(6):
    assert fib(i)==fib_dict[i]
