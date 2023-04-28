import random
import numpy as np
import pandas as pd

Tabelka = pd.DataFrame({'a': [4,2,6], 'b': [9,2,1], 'c': [6,4,5]})

print(Tabelka)

print(Tabelka._get_value(2, 'c'))
Tabelka.update()