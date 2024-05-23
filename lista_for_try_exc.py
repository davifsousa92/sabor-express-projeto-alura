#listas_numero_nomes_ano

print('\nLista numeros\n')

lista_numeros = ['1','2','3','4','5','6','7','8','9','10']

for numero in lista_numeros:
    print(numero)

print('\nLista nomes\n')

lista_nomes = ['Davi','Matheus','Ana','Claúdia']

for nome in lista_nomes:
    print(nome)

print('\nLista anos\n')

lista_ano_nascimento = ['1992']
lista_ano_atual = ['2024']

for ano_nascimento in lista_ano_nascimento:
    print(ano_nascimento)

for ano_atual in lista_ano_atual:
    print(ano_atual)

#soma_numeros_impares

print('\nLista soma números impares\n')

soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)

#ordem_decrescente_numeros

print('\nLista ordem descrescente\n')

for i in range(10, 0, -1):
    print(i)

#tabuada

numero_tabuada = int(input('\nDigite um número para a tabuada: '))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f'{numero_tabuada} x {i} = {resultado}')

#soma_elementos

print('\nLista soma elementos\n')

lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f'Soma dos elementos: {soma}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')

#media_valores

print('\nLista valores em média\n')

lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f'Média dos valores: {media}\n')
except ZeroDivisionError:
    print('A lista está vazia, não é possível calcular a média.')
except Exception as e:
    print(f'Ocorreu um erro: {e}')
