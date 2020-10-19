import numpy as np
import math

#Mascara para arredondamento
def mascara(vetor, casas_decimais):

    if len(vetor.shape) == 1:
        matriz_com_mascara = [round(item, casas_decimais) for item in vetor]

    else:        
        matriz_com_mascara = [[0] * len(vetor) for i in range (len(vetor))]
    
        for i in range(len(vetor)):
            for j in range(len(vetor)):
                matriz_com_mascara[i][j] = round(vetor[i][j], casas_decimais)
        
    return matriz_com_mascara

#Função que retorna a matriz de Jacobi
def matriz_jacobi_por_elemento_ij (matrix, i, j, n):
    error = 0.000001
    theta = 0.0

    matrix = np.matrix(matrix)
    J = np.identity(n)

    if abs(matrix[i,j]) <= error:
        return J

    if abs(matrix[i,i] - matrix[j,j]) <= error:
        theta = (math.pi)/4
    
    else:
        theta = 0.5 * math.atan((-2 * matrix[i,j]) / (matrix[i,i] - matrix[j,j]))
    
    J[i,i], J[j,j], J[i,j], J[j,i] = math.cos(theta), math.cos(theta), math.sin(theta), - math.sin(theta)

    return J

#Função usada para tentar retornar uma matriz próxima de uma matriz diagonal
def varredura_de_jacobi(matriz, n):
    J = np.identity(n)
    matriz_velha = matriz

    for i in range (0, n-1):
        for j in range (i + 1, n):
            J_ij = matriz_jacobi_por_elemento_ij(matriz_velha, i, j, n)

            #Transformação de Similaridade
            matriz_nova = np.dot(np.transpose(J_ij), np.dot(matriz_velha, J_ij))
            
            #Salvar matriz nova
            matriz_velha = matriz_nova

            #Matriz de acúmulo
            J = np.dot(J, J_ij)

    return (matriz_nova, J)

#Função para checar se os termos fora da diagonal principal são zero ou muito proximos a zero
def soma_dos_quadrados_termos_abaixo_diagonal(matriz, n):
    soma = 0
    for i in range (n-1):
        for j in range(i + 1, n):
            soma += math.pow(matriz[i][j], 2)
    return soma 

def metodo_de_jacobi(matriz, n, error):
    lamb = np.zeros(n)
    vetor_acumulo_jacobi = []
    P = np.identity(n)
    matriz_velha = matriz
    val = 100

    while val > error:
        (matriz_nova, J) = varredura_de_jacobi(matriz_velha, n)
        vetor_acumulo_jacobi.append(J)
        matriz_velha = matriz_nova
        P = np.dot(P, J)
        val = soma_dos_quadrados_termos_abaixo_diagonal(matriz_nova, n)

    #Copiando termos da matriz diagonal para o vetor de autovalores
    for i in range (n):
        lamb[i] = matriz_nova[i,i]
    
    #Retorna a matriz P usada para achar os autovetores da matriz original e o vetor de autovalores
    return (mascara(P,6), mascara(lamb,6), vetor_acumulo_jacobi)





    