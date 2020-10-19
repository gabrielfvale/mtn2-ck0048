from PotenciaRegular import potencia_regular
import numpy as np

def matriz_inversa(A):
    if np.linalg.det(np.array(A)) == 0:
        return 'A matriz não é inversivel'
    return np.linalg.inv(A)
    
def potencia_inversa1(A, v0, error):
    A_inversa = matriz_inversa(A)
    (autovalor_dominante, autovetor_dominante) = potencia_regular(A_inversa, v0, error)
    autovalor = 1/autovalor_dominante
    autovetor = autovetor_dominante
    return (autovalor,autovetor)

def potencia_deslocamento(A, numero_proximo, v0, error):
    novo_A = A - numero_proximo * np.identity(len(A), dtype = int)
    (novo_autovalor, novo_autovetor) = potencia_inversa1(novo_A, v0, error)
    autovalor = novo_autovalor + numero_proximo
    autovetor = novo_autovetor
    return (autovalor, autovetor)


