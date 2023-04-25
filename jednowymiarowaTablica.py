import numpy as np

A = np.arange(15)

for i in range(15):
    A[i] = i * 2 + 10

print(A)

A.resize(5, 3)

print(A, "\n",A.shape)

A += 3
print(A)

A *= 2
print(A)
'''
for i in range(5):
    for j in range(3):
        if A[i,j] % 6 == 2:
            A[i,j] = 0
'''
Div6 = A % 6 == 2
print(Div6)




