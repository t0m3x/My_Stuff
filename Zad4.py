def ilpot(tab, n):
    a = 1

    for i in tab:
        a = a * (i ** n)

    return a

tab = []
a = 0

print("Podaj liczby lub wpisz 'stop' aby zamknąć listę")
n = ""

while n != "stop":
    n = input()
    if n.isdigit() == True:
        tab.append(int(n))
        a += 1
    else:
        if n != "stop":
            print("To nie jest liczba")

print(tab)
exp = int(input("Podaj potęge: "))

print("Iloczyn potęg ", tab, " = ", ilpot(tab, exp))