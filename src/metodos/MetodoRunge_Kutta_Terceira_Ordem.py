import MetodoRungeKutta as rk
import pandas as pd
import numpy as np


def sol_exata(g, m, k, t, v0, y0):
    v_t = -g * (m/k) + (v0 + g * (m/k)) * (np.e)**(-(k/m) * t)
    y_t = y0 - g * (m/k) * t - (v0 + g * (m/k)) * (m/k) * ((np.e) ** (-(k/m) * t) - 1)
    return (v_t, y_t)

def pvi_2(state):
    return np.array([-10 -  (0.25/2) * state[0], state[0]])


dic = {'delta_t': [0.1, 0.01, 0.001, 0.0001] , 'y_max' : [], 't_max' : [] , 't_total' : [] , 'v_impacto' : []}

#Fazendo para cada valor de delta
for delta in dic['delta_t']:
    t = 0
    estado = np.array([5,200])

    #Tempo Total e Velocidade de Impacto
    while estado[1] >= 0: #O mar está na posição y(t) = 0
        t += delta
        estado = rk.runge_kutta_terc_ord(pvi_2, estado, delta)
        
    dic['t_total'].append(t)
    dic['v_impacto'].append(estado[0])


    estado = np.array([5,200])
    t = 0

    #Altura Maxima e Tempo até Altura Maxima
    dif_altura = np.Infinity

    prox_estado = np.array([])

    while dif_altura >= 0: #A altura maxima ocorrerá quando a altura for menor que a anterior
        prox_estado = rk.runge_kutta_terc_ord(pvi_2, estado, delta)
        dif_altura = (prox_estado[1] - estado[1])
        estado = prox_estado
        t += delta
    
    dic['t_max'].append(t)
    dic['y_max'].append(estado[1])
                
df = pd.DataFrame(dic).set_index('delta_t')
print(df)


'''
#Para y(5)
dic_2 = {'delta_t': [0.1, 0.01, 0.001, 0.0001] , 'y_approx' : [] , 'erro_rel_y' : [], 'v_approx' : [], 'erro_rel_v' : []}
(v_exato, y_exato) = sol_exata(10, 2, 0.25, 5, 5, 200)
print(v_exato, y_exato)

for delta in dic_2['delta_t']:
    t = 0
    estado = np.array([5,200])

    while round(t,4) != 5: 
        t += delta
        estado = rk.runge_kutta_terc_ord(pvi_2, estado, delta)
    
    dic_2['y_approx'].append(round(estado[1],8))
    dic_2['v_approx'].append(estado[0])

    erro_rel_v = 100 * ((v_exato - estado[0])/v_exato)
    erro_rel_y = 100 * ((y_exato - estado[1])/y_exato)

    dic_2['erro_rel_y'].append(erro_rel_y)
    dic_2['erro_rel_v'].append(erro_rel_v)

df_2 = pd.DataFrame(dic_2).set_index('delta_t')
print(df_2)
'''
