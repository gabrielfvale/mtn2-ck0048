import numpy as np

def runge_kutta_seg_ord(edo, cond_inic, delta):
    S_barra = np.array(cond_inic) + delta * np.array(edo(cond_inic))
    S = np.array(cond_inic) + (delta/2) * (np.array(edo(cond_inic)) + edo(S_barra))

    return S

def runge_kutta_terc_ord(edo, cond_inic, delta):

    #Calculando estimativas dos estados Sbarra_{i+1/2} e Sbarra_{i+1}
    F_1 = np.array(edo(cond_inic))
    Sb_ip12 = np.array(cond_inic) + (delta/2) * F_1

    F_2 = np.array(edo(Sb_ip12))
    Sb_ip1 = np.array(cond_inic) + (delta) * (- F_1 + 2 * F_2)

    F_3 = np.array(edo(Sb_ip1))

    #Atualização melhorada do estado S_{i+1}
    S_ip1 = np.array(cond_inic) + delta * ((1/6) * F_1 + (4/6) * F_2 + (1/6) * F_3)

    return S_ip1

def runge_kutta_quar_ord(edo, cond_inic, delta):

    F_1 = np.array(edo(cond_inic))
    S_2 = np.array(cond_inic) + (delta/2) * F_1

    F_2 = np.array(edo(S_2))
    S_3 = np.array(cond_inic) + (delta/2) * F_2

    F_3 = np.array(edo(S_3))
    S_4 = np.array(cond_inic) + delta * F_3

    F_4 = np.array(edo(S_4))

    S = np.array(cond_inic) + (delta/6) * (F_1 + 2 * F_2 + 2 * F_3 + F_4)

    return S


