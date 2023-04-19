class wielomiany:
    def __init__(self, wspolczynnik):           # Wielomiany są zapisywane kolejno stopniami od prawej do lewej
        self.wspolczynnik = wspolczynnik

        i = len(self.wspolczynnik) - 1          # Pozbywanie się zerowych wspolczynnikow o najwyższych potęgach
        while self.wspolczynnik[i] == 0:
            self.wspolczynnik.pop(i)
            i -= 1

    def __str__(self):
        stopien = len(self.wspolczynnik) - 1

        pelne_wyrazenie = ""                                                            # Zaczynamy od niczego, a nastepnie będziemy dodawać kolejne wyrażenia

        if stopien != 0:                                                                # Instrukcja warunkowa na wypadek wielomianu o zerowym stopniu
            pelne_wyrazenie += str(self.wspolczynnik[stopien]) + "x^" + str(stopien)    # Zaczynamy od najwyższego stopnia
            for i in range(stopien - 1, 0, -1):                                         # I lecimy loopem od 2-giego najwyższego do 2-giego najniższego
                if self.wspolczynnik[i] < 0:                                            # Instrukcja warunkowa aby nie otrzymać w pelne_wyrazenie "+-"
                    pelne_wyrazenie += str(self.wspolczynnik[i]) + "x^" + str(i)
                elif self.wspolczynnik[i] > 0:
                    pelne_wyrazenie += "+" + str(self.wspolczynnik[i]) + "x^" + str(i)
                                                                                        # Zerowe współczynniki są pomijane
            if self.wspolczynnik[0] < 0:                                                # I konczymy na stałej
                pelne_wyrazenie += str(self.wspolczynnik[0])
            elif self.wspolczynnik[0] > 0:
                pelne_wyrazenie += "+" + str(self.wspolczynnik[0])

        else:
            pelne_wyrazenie += str(self.wspolczynnik[0])                                # Przypadek dla stałej

        return f"{pelne_wyrazenie}"                                                     # Powinniśmy otrzymać wielomian w postaci ogólnej

    def degree(self):
        return len(self.wspolczynnik) - 1

    def plus(self, wspol, pot):
        stopien = len(self.wspolczynnik) - 1
        if pot < stopien:                               # Jeśli potęga dodawanego wyrażenia jest mniejsza od stopnia to po prostu dodajemy wspolczynnik do danego wyrazenia
            self.wspolczynnik[pot] += wspol
        else:                                           # W innymm przypadku musimy dodać dodatkowe zerowe wyrażenia
            for i in range(pot - stopien):
                self.wspolczynnik.append(0)
            self.wspolczynnik[pot] = wspol              # No i dodajemy współczynnik


Poly1 = wielomiany([3, 0, 6])   # Wielomiany są zapisywane kolejno stopniami od prawej do lewej, czyli w tym przypadku to 6x^2 + 3
Poly2 = wielomiany([5])

print(Poly1)
print(Poly1.degree())
Poly1.plus(-4, 7)
print(Poly1)
print(Poly1.degree())

print(Poly2)
