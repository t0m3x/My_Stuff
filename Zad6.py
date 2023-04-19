def silnia(a):
    k = 1
    for i in range(a):
        k *= i + 1

    return k

def binom(n, k):
    return (silnia(n) / (silnia(n-k) * silnia(k)))

n = int(input("Podaj liczbe n: "))
k = int(input("Podaj liczbe k: "))

print("(",n, k,") =", binom(n,k))