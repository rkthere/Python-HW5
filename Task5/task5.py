# 5.Дан список чисел. Найдите все возрастающие последовательности. Порядок элементов менять нельзя.

X = [1, 5, 2, 3, 4, 6, 1, 7]

L = []
M = []
j = 1

while j < len(X):
  i = j
  N = X[:]
  while i < len(N)-1:
    if N[i] < N[i+1]:
      M.append(N[i])
      i += 1
    else:
      N.pop(i+1)

  j += 1
  if len(L) < len(M):
    L = M
  M = []

if X[-1] > L[-1]:
  L.append(X[-1])

if X[0] < L[0]:
  L.insert(0, X[0])

print(L)
