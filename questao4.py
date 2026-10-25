"""
Algoritmo:

função buscaPico(A, inicio, fim)
entrada: Um vetor botônico A e os índices de início e fim
saída: O maior elemento do vetor A

se inicio = fim: retorna A[inicio]

meio = piso((inicio + fim) /2)

se A[meio] < A[meio+1]: retorna buscaPico(A, meio+1, fim)
se A[meio] > A[meio+1]: retorna buscaPico(A, inicio, meio)
"""

def buscaPico(A, inicio, fim):

  if inicio == fim:
    return A[inicio]

  meio = (inicio + fim) // 2

  if A[meio] < A[meio+1]:
    return buscaPico(A, meio+1, fim)
  if A[meio] > A[meio+1]:
    return buscaPico(A, inicio, meio)