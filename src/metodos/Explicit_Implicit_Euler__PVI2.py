'''
Método de Euler Implícito e Euler Explícito aplicado a PVI-2
Gabriel Freire do Vale - 418788
Pedro Ernesto de Oliveira Primo - 418465
'''
import numpy as np
import pandas as pd

def euler_explicit(t0: float, v0: float, y0: float, k: float, m: float, delta_t: float, iterations: int, debug: bool = False):
  if debug:
    print('Using delta_t = ', delta_t)
  # return dict
  ret_dict = {'delta_t': delta_t}
  #define variables
  g = 10

  v1, y1 = 0, 0
  max_y, max_i = 0, 0
  max_t = -np.Infinity
  i = 0

  while i < iterations:
    v1 = v0 + delta_t * (-g -(k*v0/m))
    y1 = y0 + delta_t * v0

    v0, y0 = v1, y1

    if max_y < y1:
      max_y = y1
      max_t = t0 + i*delta_t + delta_t
      max_i = i + 1
    
    # Reached the ocean
    if y0 + delta_t*v0 < 0:
      if debug:
        print(f'Reached the ocean (iteration {i})')
        print('t =', t0 + i*delta_t + delta_t)
        print('v =', v1)
      ret_dict = {
        **ret_dict,
        'ocean_t': t0 + i*delta_t + delta_t,
        'ocean_v': v1
      }
      v1 = v0 + delta_t * (-g - (k*v0/m))
      y1 = y0 + delta_t * v0

      v0, y0 = v1, y1

      i = iterations

    i = i + 1
  if debug:
    print(f'Maximum height (iteration {max_i})')
    print('y =', max_y)
    print('t =', max_t)
    print('\n')

  return {**ret_dict, 'max_y': max_y, 'max_t': max_t, 'max_iteration': max_i}

def euler_implicit(t0: float, v0: float, y0: float, k: float, m: float, delta_t: float, iterations: int, debug: bool = False):
  if debug:
    print('Using delta_t = ', delta_t)
  # return dict
  ret_dict = {'delta_t': delta_t}

  #define variables
  g = 10
  v1, y1 = 0, 0
  max_y, max_i = 0, 0
  max_t = -np.Infinity
  i = 0

  while i < iterations:
    v1 = (m / (m + k*delta_t)) * (v0 - g*delta_t)
    y1 = y0 + (m*delta_t / (m + k*delta_t)) * (v0 - g*delta_t)

    v0, y0 = v1, y1

    if max_y < y1:
      max_y = y1
      max_t = t0 + i*delta_t + delta_t
      max_i = i + 1
    
    # Reached the ocean
    if y0 + delta_t*v0 < 0:
      if debug:
        print(f'Reached the ocean (iteration {i})')
        print('t =', t0 + i*delta_t + delta_t)
        print('v =', v1)
      ret_dict = {
        **ret_dict,
        'ocean_t': t0 + i*delta_t + delta_t,
        'ocean_v': v1
      }
      v1 = v0 + delta_t * (-g - (k*v0/m))
      y1 = y0 + delta_t * v0

      v0, y0 = v1, y1

      i = iterations

    i = i + 1
  if debug:
    print(f'Maximum height (iteration {max_i})')
    print('y =', max_y)
    print('t =', max_t)
    print('\n')

  return {**ret_dict, 'max_y': max_y, 'max_t': max_t, 'max_iteration': max_i}

'''
print('EXPLICIT EULER')
for delta in [0.1, 0.01, 0.001, 0.0001]:
  euler_explicit(t0=0, v0=5, y0=200, k=0.25, m=2, delta_t=delta, iterations=80000, debug = True);

print('IMPLICIT EULER')
for delta in [0.1, 0.01, 0.001, 0.0001]:
  euler_implicit(t0=0, v0=5, y0=200, k=0.25, m=2, delta_t=delta, iterations=80000, debug = True);
'''

# Create Dataframe for Explicit Euler, using delta 0.1 to 0.0001
explicit_df = pd.DataFrame([euler_explicit(t0=0, v0=5, y0=200, k=0.25, m=2, delta_t=delta, iterations=80000) for delta in [0.1, 0.01, 0.001, 0.0001]])

# Create Dataframe for Implicit Euler, using delta 0.1 to 0.0001
implicit_df = pd.DataFrame([euler_implicit(t0=0, v0=5, y0=200, k=0.25, m=2, delta_t=delta, iterations=80000) for delta in [0.1, 0.01, 0.001, 0.0001]])

print('Explicit Euler \n', explicit_df)
print('Implicit Euler \n', implicit_df)
