# Métodos Numéricos II
# Gabriel Freire - 418788
# Pedro Ernesto - 418465

import PotenciaRegular as pr
import numpy as np

def matriz_inversa(A):
    if np.linalg.det(np.array(A)) == 0:
        return 'A matriz não é inversivel'
    return np.linalg.inv(A)

def decompLU(A):
    U = np.copy(A)
    n - np.shape(U)[0]
    L = np.eye(n)
    for c in np.arrange(n-1):
        for r in np.arrange(c+1, n):
            L[r, c] = U[r, c]/U[c, c]
            for k in np.arrange(j+1, n):
                U[r, k] = U[r, k] - L[r, c] * U[c, k]
            U[r, c] = 0
    return L, U

def potencia_inverso1(A, v0, error):
    L, U = decompLU(A)
    A_inversa = matriz_inversa(A)
    (autovalor_dominante, autovetor_dominante) = pr.potencia_regular(A_inversa, v0, error)
    autovalor = 1/autovalor_dominante
    autovetor = autovetor_dominante
    return (autovalor,autovetor)

def potencia_deslocamento(A, numero_proximo, v0, error):
    novo_A = A - numero_proximo * np.identity(len(A), dtype = int)
    (novo_autovalor, novo_autovetor) = potencia_inverso1(novo_A, v0, error)
    autovalor = novo_autovalor + numero_proximo
    autovetor = novo_autovetor
    return (autovalor, autovetor)

A1 = [[5,2,1],[2,3,1],[1,1,2]]
A2 = [[-14,1,-2],[1,-1,1],[-2,1,-11]]
A3 = [[40,8,4,2,1], [8,30,12,6,2], [4,12,20,1,2],[2,6,1,25,4], [1,2,2,4,5]]

print('----- Matriz A1 -----\n')
print(pr.potencia_regular(A1, [1,1,1], 0.00001))
print(potencia_inverso1(A1,[1,1,1],0.00001))
print(potencia_deslocamento(A1, 3, [1,1,1], 0.00001))

print('\n----- Matriz A2 -----\n')
print(pr.potencia_regular(A2, [1,1,1], 0.00001))
print(potencia_inverso1(A2,[1,1,1],0.00001))
print(potencia_deslocamento(A2, -10, [1,1,1], 0.00001))

print('\n----- Matriz A3 -----\n')
print(pr.potencia_regular(A3, [1,1,1,1,1], 0.00001))
print(potencia_inverso1(A3,[1,1,1,1,1],0.00001))
print(potencia_deslocamento(A3, 10, [1,1,1,1,1], 0.00001))
print(potencia_deslocamento(A3, 20, [1,1,1,1,1], 0.00001))
print(potencia_deslocamento(A3, 30, [1,1,1,1,1], 0.00001))

