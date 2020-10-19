# Métodos Numéricos II
# Gabriel Freire - 418788
# Pedro Ernesto - 418465

import numpy as np
from functools import reduce

def normalizar(vetor):
    comprimento = np.sqrt(reduce(lambda acumulador, coordenada: acumulador + coordenada**2, vetor, 0))
    return list(map(lambda coordenada : coordenada/comprimento, vetor))

def produto_matriz_vetor(matriz, vetor):
    produto = []

    for i in range(0, len(matriz)):
        soma_por_linha = 0
        for j in range (0, len(matriz[i])):
            soma_por_linha += matriz[i][j] * vetor[j]
        produto.append(soma_por_linha)

    return produto 

def produto_escalar(vetor1, vetor2):
    prod_esc = 0

    if len(vetor1) == len(vetor2):
        for i in range(len(vetor1)):
            prod_esc += vetor1[i] * vetor2[i]
    
    return prod_esc

def potencia_regular(A, v, error):
    autovalor_novo = 0
    v_k_novo = v
    erro = np.Infinity

    while (erro > error):
        autovalor_velho = autovalor_novo
        v_k_velho = v_k_novo
        autovetor_velho = normalizar(v_k_velho)
        v_k_novo = produto_matriz_vetor(A, autovetor_velho)
        autovalor_novo = produto_escalar(autovetor_velho, v_k_novo)
        erro = abs((autovalor_novo - autovalor_velho)/autovalor_novo)
    
    return (autovalor_novo, autovetor_velho)
