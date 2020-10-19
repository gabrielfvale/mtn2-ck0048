import numpy as np
import pandas as pd
import MetodoPreditorCorretor as mpc

def pvi_2(state):
    return np.array([-10 -  (0.25/2) * state[0], state[0]])

dic = {'delta_t': [0.1, 0.01, 0.001, 0.0001] , 'y_max' : [], 't_max' : [] , \
    't_total' : [] , 'v_impacto' : []}

cond_inic = np.array([5,200])

for delta in dic['delta_t']:
    t = 3 * delta
    
    F_array, estado = mpc.inic_pred_corr(pvi_2, cond_inic, delta)
    
    #Tempo Total e Velocidade de Impacto
    while estado[1] >= 0: #O mar está na posição y(t) = 0
        t += delta
        estado = mpc.met_pred_corr(pvi_2, estado, F_array, delta)
        F_array = mpc.at_F_array(pvi_2, F_array, estado)


    dic['t_total'].append(t)
    dic['v_impacto'].append(estado[0])

    F_array, estado = mpc.inic_pred_corr(pvi_2, cond_inic, delta)
    t = 3 * delta

    #Altura Maxima e Tempo até Altura Maxima
    dif_altura = np.Infinity

    prox_estado = np.array([])

    while dif_altura >= 0: #A altura maxima ocorrerá quando a altura for menor que a anterior
        prox_estado = mpc.met_pred_corr(pvi_2, estado, F_array, delta)
        dif_altura = (prox_estado[1] - estado[1])
        estado = prox_estado
        F_array = mpc.at_F_array(pvi_2, F_array, estado)
        t += delta
    
    dic['t_max'].append(t)
    dic['y_max'].append(estado[1])

df = pd.DataFrame(dic).set_index('delta_t')
print(df)
