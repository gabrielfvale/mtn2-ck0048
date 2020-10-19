'''
Método dos Elementos Finitos aplicado a PVC-1
Gabriel Freire do Vale - 418788
Pedro Ernesto de Oliveira Primo - 418465
'''
import numpy as np

def mef(n):
     Li = 1/n

     matriz_coef = np.zeros((n-1,n-1), dtype=float)
     
     vetor_direita = np.zeros(n-1)
     
     N_lin_in = -(1/2)
     N_lin_fin = 1/2

     k1 = [[(N_lin_in**2) * (2/Li) * 2, \
          (N_lin_in) * (2/Li) * (N_lin_fin) * 2], \
          [(N_lin_fin) * (2/Li) * (N_lin_in) * 2, \
          (N_lin_fin**2) * (2/Li) * 2]]
    
     k1 = np.matrix(k1)

     k2 = [[(Li/2) * (2/3), (Li/2) * (1/3)], \
          [(Li/2) * (1/3), (Li/2) * (2/3)]]
    
     k2 = np.matrix(k2)

     ki = k1 + k2

     vetor_direita[n-2] = -ki[0,1]

     matriz_coef[0][0] += ki[1,1]

     for i in range (0, n-2):
          matriz_coef[i][i] += ki[0, 0]
          matriz_coef[i][i+1] += ki[0, 1]
          matriz_coef[i+1][i] += ki[1, 0]
          matriz_coef[i+1][i+1] += ki[1, 1]

     matriz_coef[n-2][n-2] += ki[0,0]

     inversa = np.linalg.inv(matriz_coef)

     return np.dot(inversa, vetor_direita)
