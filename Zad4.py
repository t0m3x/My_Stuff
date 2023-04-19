def ilpot(*lic, n):
    a = 1
    for i in lic:
        a *= (i**n)

    return a

print(ilpot(4,5,2,3, n=2))