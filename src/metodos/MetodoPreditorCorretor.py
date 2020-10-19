from MetodoRungeKutta import runge_kutta_quar_ord
import numpy as np

#Os Estados S1, S2 e S3 são encontrados por meio de Runge-Kutta de 4ª Ordem
def inic_pred_corr(edo, cond_inic, delta):
    S1 = runge_kutta_quar_ord(edo, cond_inic, delta)
    S2 = runge_kutta_quar_ord(edo, S1, delta)
    S3 = runge_kutta_quar_ord(edo, S2, delta)

    #Retorna uma array com os 4 ultimos edos calculados e o estado S3
    return np.array([edo(cond_inic), edo(S1), edo(S2), edo(S3)]), S3 

#Quando o metodo met_pred_corr() é chamado, a array deve ser atualizada para os 4 novos ultimos edos calculados
def at_F_array(edo, F_array, state):
    F_array_at = np.array([F_array[1], F_array[2], F_array[3], edo(state)])  

    return F_array_at


def met_pred_corr(edo, state, F_array, delta):
    
    #Calculo do valor estimado de Sbarra_i+1
    def fase_predicao(edo, state, F_array, delta):
        F_im3 = np.array(F_array[0])
        F_im2 = np.array(F_array[1])
        F_im1 = np.array(F_array[2])
        F_i = np.array(F_array[3])

        S_ip1 = np.array(state) + (delta/24) * (-9 * F_im3 + 37 * F_im2 \
            - 59 * F_im1 + 55 * F_i)

        return S_ip1

    F_im2 = np.array(F_array[1])
    F_im1 = np.array(F_array[2])
    F_i = np.array(F_array[3])

    #Valor estimado
    S_antigo = np.array(fase_predicao(edo, state, F_array, delta))

    #Valor atualizado
    S_novo = np.array(state) + (delta/24) * (F_im2 - 5 * F_im1 \
    + 19 * F_i + 9 * np.array(edo(S_antigo)))

    #Calculando Erro
    dif_S = abs((S_novo - S_antigo)/S_novo) 
    
    #Erro deve ser menor que 0.000001
    while dif_S.all() > 0.000001:      
        S_antigo = S_novo
        S_novo = np.array(state) + (delta/24) * (F_im2 - 5 * F_im1 \
            + 19 * F_i + 9 * np.array(edo(S_antigo)))

        dif_S = abs((S_novo - S_antigo)/S_novo)


    return S_novo
