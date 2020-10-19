import MetodoQR as mqr
import numpy as np
import MetodoHouseholder as mh

A = [[40,8,4,2,1], [8,30,12,6,2], [4,12,20,1,2], \
    [2,6,1,25,4], [1,2,2,4,5]]

met_qr = mqr.metodo_QR(A, 5, 0.000001)

print('Questão 1')

print('i)\n ------- Matriz Diagonal -------')
print(np.diag(met_qr[1]))


print('\nii)\n ------- Matriz Acumulada P -------')
print(np.matrix(met_qr[0]))

'''
print('\niii)\n ------- Matrizes de Cada Varredura -------')
for matriz in met_qr[2]:
    print(matriz, '\n')
'''

print('\niv)\n ------- Pares (Autovalor, Autovetor) de A -------')
for i in range (5):
    autovalor = met_qr[1][i]
    autovetor = np.transpose(met_qr[0])[i]
    print('({},{})'.format(autovalor, autovetor))


print('\nQuestão 2')
(matriz_tridiagonal, matriz_householder) = mh.metodo_de_householder(A)

#A matriz tridiagonal é passada no metodo de Jacobi
matriz_resultante = mqr.metodo_QR(matriz_tridiagonal, 5, 0.000001)[0]
array_autovalores = mqr.metodo_QR(matriz_tridiagonal, 5, 0.000001)[1]

#Para obter a matriz de autovetores correta, é preciso multiplicar a matriz de householder pela resultante do metodo de jacobi
matriz_autovetores = np.dot(matriz_householder, matriz_resultante)

print('\n ------- Pares (Autovalor, Autovetor) de A (Utilizando também método de Householder) -------')
for i in range (5):
    autovalor = array_autovalores[i]
    autovetor = np.transpose(matriz_autovetores)[i]
    print('({},{})'.format(autovalor, autovetor))

