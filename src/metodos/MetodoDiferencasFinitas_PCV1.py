'''
Método das Diferenças Finitas aplicado a PVC-2
Gabriel Freire do Vale - 418788
Pedro Ernesto de Oliveira Primo - 418465
'''
import numpy as np

def PVC1(n: int) -> np.ndarray:
  delta_x = 1.0/n

  mask = { 'border': 1/(delta_x**2), 'center': -(2/(delta_x**2) + 1) }

  # Calculate coefficient matrix
  coeff_matrix = np.zeros((n-1, n-1))
  coeff_matrix = np.pad(coeff_matrix, 1)

  for i in range (1, n):
    coeff_matrix[i][i-1] = mask['border']
    coeff_matrix[i][i] = mask['center']
    coeff_matrix[i][i+1] = mask['border']

  # get values
  values = coeff_matrix[:, -1] * -1
  # unpad coefficients and values
  values = values[1:n]
  coeff_matrix = coeff_matrix[1:n, 1:n]
  # Calculate result
  inv_coeff_matrix = np.linalg.inv(coeff_matrix)
  result = np.dot(inv_coeff_matrix, values)
  return result

print(PVC1(4))
