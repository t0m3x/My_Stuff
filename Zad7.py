class wielomian:
    def __init__(self, wspolczynniki):
        self.wspolczynniki = wspolczynniki

    def __str__(self):
        n = "" + str(self.wspolczynniki[0])
        for i in range (len(self.wspolczynniki) - 1):
            if i >= 0:
                n = n + "+" + str(self.wspolczynniki[i + 1]) + "x^" + str(i + 1)
            else:
                n = n + str(self.wsoplczynniki[i + 1]) + "x^" + str(i + 1)

        return f"{n}"

    def degree(self):
        return len(self.wspolczynniki) - 1




mian1 = wielomian([3,6,4])
mian2 = wielomian([5,5,-3, -20])
print(mian1)
print(mian1.degree())

print(mian2)
print(mian2.degree())