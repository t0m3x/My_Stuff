def fib(a):
    k = 0
    n = 1
    m = 1
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        for i in range(a - 2):
            k = n + m
            m = n
            n = k
        return k

n = int(input("Podaj liczbę: "))
print(fib(n))