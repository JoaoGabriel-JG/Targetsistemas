print ('-' *30)
print (' ' *3, 'Sequência de Fibonacci')
print ('-' *30)

valor = int(input('Insira um número: '))    # Um input com números inteiros pois a Fibonacci não recebe números float
inicio1 = 0
inicio2 = 1

print ('{} → {}'.format(inicio1, inicio2), end='')    # Formatação da saída
Contador = 3

while Contador <= valor:        # Estrutura de repetição While 
   valor1 = inicio1 + inicio2
   print (' → {}'.format(valor1), end='')
   inicio1 = inicio2
   inicio2 = valor1
   Contador += 1

print (' → FIM')    

# A sequencia em si já ira mostrar se o número pertence ou não
# Usei PY pois é minha segunda linguagem e nele da pra colocar inputs