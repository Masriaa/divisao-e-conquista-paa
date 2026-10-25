"""
Algoritmo:

função multiplica(a, b)
Entrada: Inteiros positivos a e b
saída: O produto deles

se n = 1: retorna ab

w, x = [n/2] parte mais á esquerda e [n/2] parte mais à direita de a
y, z = [n/2] parte mais á esquerda e [n/2] parte mais à direita de b
P1 = multiplica(w, y) P2 = multiplica (x, z) P3 = multiplica (w+x, y+z) retorna P1*10^n + (P3-P1-P2)*10^10/2 + P2

"""

def mult(a, b):
  if a < 10 or b < 10:
    return a*b

  n = max(len(str(a)), len(str(b)))
  m = n//2

  w = a // 10**m
  x = a % 10**m
  y = b // 10**m
  z = b % 10**m

  p1 = mult(w, y)
  p2 = mult(x, z)
  p3 = mult(w+x, y+z)

  return p1*10**(2*m) + (p3-p1-p2)*10**m + p2

