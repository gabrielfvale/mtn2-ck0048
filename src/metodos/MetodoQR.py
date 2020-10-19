from MetodoJacobi import soma_dos_quadrados_termos_abaixo_diagonal, mascara
import math
import numpy as np

def matriz_jacobi_por_elemento_ij (matrix, i, j, n):
    error = 0.000001
    theta = 0.0

    matrix = np.matrix(matrix)
    J = np.identity(n)

    if abs(matrix[i,j]) <= error:
        return J

    if abs(matrix[j,j]) <= error:
        if matrix[i,j] < 0:
            theta = (math.pi)/2
        else:
            theta = - (math.pi)/2
    
    else:
        theta = math.atan( -(matrix[i,j]) / matrix[j,j])
    
    J[i,i], J[j,j], J[i,j], J[j,i] = math.cos(theta), math.cos(theta), math.sin(theta), - math.sin(theta)

    return J

def decomposicao_QR(matrix, n):
    QT = np.identity(n)
    R_velha = np.matrix(matrix)

    for j in range (n - 1):
        for i in range (j+1, n):
            J_ij = matriz_jacobi_por_elemento_ij(R_velha, i, j, n)
            R_nova = np.dot(J_ij, R_velha)
            R_velha = R_nova
            QT = np.dot(J_ij, QT)

    Q = np.transpose(QT)
    R = R_nova

    return(Q,R)

def metodo_QR(matrix, n, error):
    lamb = np.zeros(n)
    vetor_acumulo_qr = []
    erro_atual = 100

    P = np.identity(n)
    matriz_velha = matrix

    while (erro_atual > error):
        (Q, R) = decomposicao_QR(matriz_velha, n)
        matriz_nova = np.dot(R,Q)
        matriz_velha = matriz_nova
        vetor_acumulo_qr.append(matriz_nova)

        P = np.dot(P, Q)
        erro_atual = soma_dos_quadrados_termos_abaixo_diagonal(matriz_nova, n)

    for i in range (n):
        lamb[i] = matriz_nova[i,i]
    
    return (mascara(P,6), mascara(lamb,6), vetor_acumulo_qr)


