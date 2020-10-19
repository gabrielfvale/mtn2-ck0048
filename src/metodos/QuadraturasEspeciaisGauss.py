from math import sqrt, sin, pi


'''
Cálculo da Quadratura Especial de Gauss-Hermite

Parâmetros:
  function: função a ser utilizada no somatório
  n: grau do polinômio
  debug: condicional para printar o valor de r
'''
def gauss_hermite_quadrature(function, n = 2, debug = False) -> float:

  r = 0
  
  if n < 2 or n > 4:
    print("Por favor selecione n entre 2 e 4")
    return r;

  SQRT_PI = sqrt(pi)

  # valores de xk para k = 1..n
  values = [
    # n = 2
    [-1/sqrt(2), 1/sqrt(2)],
    # n = 3
    [-sqrt(3/2), 0, sqrt(3/2)],
    # n = 4
    [sqrt((3+sqrt(6))/2), sqrt((3-sqrt(6))/2), -sqrt((3-sqrt(6))/2), -sqrt((3+sqrt(6))/2)]
  ]

  # valores de wk para k = 1..n
  weights = [
    # n = 2
    [SQRT_PI/2, SQRT_PI/2],
    # n = 3
    [SQRT_PI/6, (2 * SQRT_PI)/3, SQRT_PI/6],
    # n = 4
    [(SQRT_PI * (3-sqrt(6)))/12, (SQRT_PI * (3+sqrt(6)))/12, (SQRT_PI * (3+sqrt(6)))/12, (SQRT_PI * (3-sqrt(6)))/12]
  ]

  for k in range(n):
    r = r + weights[n-2][k] * function(values[n-2][k])
    if debug:
      print('[Gauss-Hermite] valor de r quando k = %d' % k)
      print('  %f' % r)

  print('[Gauss-Hermite] valor de r = %f' % r)
  return r


'''
Cálculo da Quadratura Especial de Gauss-Laguerre

Parâmetros:
  function: função a ser utilizada no somatório
  n: grau do polinômio
  debug: condicional para printar o valor de r
'''
def gauss_laguerre_quadrature(function, n = 2, debug = False) -> float:

  r = 0
  
  if n < 2 or n > 4:
    print("Por favor selecione n entre 2 e 4")
    return r;

  SQRT_PI = sqrt(pi)

  # valores de xk para k = 1..n
  values = [
    # n = 2
    [2 - sqrt(2), 2 + sqrt(2)],
    # n = 3
    [0.41577, 2.29428, 6.28994],
    # n = 4
    [0.32254, 1.74576, 4.53662, 9.39507]
  ]
  # valores de wk para k = 1..n
  weights = [
    # n = 2
    [(2+sqrt(2))/4, (2-sqrt(2))/4],
    # n = 3
    [0.71109, 0.27851, 0.01038],
    # n = 4
    [0.60335, 0.35742, 0.03888, 0.00053]
  ]

  for k in range(n):
    r = r + weights[n-2][k] * function(values[n-2][k])
    if debug:
      print('[Gauss-Laguerre] valor de r quando k = %d' % k)
      print('  %f' % r)

  print('[Gauss-Laguerre] valor de r = %f' % r)
  return r


'''
Cálculo da Quadratura Especial de Gauss-Chebyshev

Parâmetros:
  function: função a ser utilizada no somatório
  n: grau do polinômio
  debug: condicional para printar o valor de r
'''
def gauss_chebyshev_quadrature(function, n = 2, debug = False) -> float:

  r = 0
  
  if n < 2 or n > 4:
    print("Por favor selecione n entre 2 e 4")
    return r;

  # guardando valores para evitar cálculos repetidos
  SQRT_PI = sqrt(pi)
  PI_OVER_N = pi/n

  # valores de xk para k = 1..n
  values = [
    # n = 2
    [-(1/sqrt(2)), 1/sqrt(2)],
    # n = 3
    [-(sqrt(3)/2), 0, sqrt(3)/2],
    # n = 4
    [sqrt(2+sqrt(2))/2, sqrt(2-sqrt(2))/2, -sqrt(2+sqrt(2))/2, -sqrt(2-sqrt(2))/2]
  ]

  for k in range(n):
    r = r + PI_OVER_N * function(values[n-2][k])
    if debug:
      print('[Gauss-Chebyshev] valor de r quando k = %d' % k)
      print('  %f' % r)

  print('[Gauss-Chebyshev] valor de r = %f' % r)
  return r


def function_1(x):
  # (sen(2x) + 4x² + 3x)²
  return (sin(2 * x) + 4 * (x ** 2) + 3 * x) ** 2


gauss_hermite_quadrature(function_1, 4)
gauss_laguerre_quadrature(function_1, 4)
gauss_chebyshev_quadrature(function_1, 4)
