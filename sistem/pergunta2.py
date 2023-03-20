print ('-' *30)
print (' ' *3, 'Sequência de Fibonacci')
print ('-' *30)

fibonacci = [0, 1]

valor = int(input('Insira um número: '))  # Um input com números inteiros pois a Fibonacci não recebe números float


while valor > int(*fibonacci[-1:]):    # Estrutura de repetição While
    n1 = fibonacci[-2:][0]
    n2 = int(*fibonacci[-1:])

    fibonacci.append(n1 + n2)

    if valor in fibonacci:             # Um if para verificar se é verdadeiro o valor n Fibonacci
        print([n for n in fibonacci])
        print(f'O valor {valor} está dentro da Fibonacci')
        break    
    elif valor < int(*fibonacci[-1:]):    # Um elif para verificar se é falso o valor n Fibonacci
        print('O valor não pertence a Fibonacci')
        break

# Usei PY pois é minha segunda linguagem e nele da pra colocar inputs