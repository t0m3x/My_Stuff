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


Div6 = A % 6 != 2
A *= Div6
print(A)

def change(A, x):
    Tab1 = A == 0
    print(Tab1)
    Tab2 = A != 0
    print(Tab2)
    return A * Tab2 + (Tab1 * x)


B = change(A, 8)
print(B)