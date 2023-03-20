print ('-' *30)
print (' ' *3, 'Sequência de Fibonacci')
print ('-' *30)

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

valor = int(input('Insira um número: '))    # Um input com números inteiros pois a Fibonacci não recebe números float

for i, n in enumerate(fibonacci):        # Estrutura de repetição 
   print (' → {}'.format(n), end='')

   if valor == n:
      print(' O valor está dentro da Fibonacci')
      break
   elif n == fibonacci[-1:]:
      print('O valor não pertence a Fibonacci')
  
# Usei PY pois é minha segunda linguagem e nele da pra colocar inputs