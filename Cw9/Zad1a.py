import numpy as np
import pandas as pd
import random

tab1 = []
for i in range(20):
    tab1.append(random.randint(0,999))
liczby = pd.Series(tab1)

print(liczby)

tab2 = ["Costam", "Zapelniacz", "Placeholder", "LoremIpsum", "BottomText"]
stringi = pd.Series(tab2)

print("\n", stringi)

tab3 = pd.Series.tolist(stringi)

print("\n", tab3)

tab4 = np.arange(30)
for i in range(30):
    tab4[i] = random.randint(0,100)

nowaseria = pd.Series(tab4)

print("\n", nowaseria)

nowatablica = np.asarray(tab1)

print("\n", nowatablica)

tab5 = []
for i in range(20):
    tab5.append(random.randint(0,999))
liczby2 = pd.Series(tab5)

tab6 = liczby + liczby2

print("\n",tab6)

tab7 = []
for i in range(10):
    tab7.append(random.randint(-10,10))
losowe = pd.Series(tab7)

losoweujemne = pd.Series([])

for i in losowe:
    if i < 0:
        losoweujemne.Series.append(i)

print(losoweujemne)
