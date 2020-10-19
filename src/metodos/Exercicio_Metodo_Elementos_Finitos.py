'''
Método dos Elementos Finitos aplicado a PVC-1
Gabriel Freire do Vale - 418788
Pedro Ernesto de Oliveira Primo - 418465
'''
from MetodoElementosFinitos import mef
import numpy as np
import pandas as pd
from math import exp

def sol_exata(x):
    return round((exp(-x) - exp(x))/(exp(-1) - exp(1)),8)

solucao_exata = np.array([sol_exata((i+1) * 0.125) for i in range (7)])
solucao_mef = np.array(mef(8))

dic = {'Solucao Exata' : solucao_exata, 'Elementos Finitos' : solucao_mef, 'Erro Relativo' : abs(solucao_exata - solucao_mef)/solucao_exata}
df = pd.DataFrame(dic)

print(df)

