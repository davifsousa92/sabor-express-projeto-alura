#par ou ímpar

numero_escolhido = int(input('Digite um número: \n'))

if numero_escolhido %2 == 0:
    print(f'O número digitado {numero_escolhido} é par')
else:
    print(f'O número digitado {numero_escolhido} é impar')

#idade 

idade_digitada = int(input('Digite a idade: \n'))

if 0 <= idade_digitada <= 12:
    print('Essa pessoa é uma criança')
elif 12 < idade_digitada < 18:
    print('Essa pessoa é uma adolescente')
else:
    print('Essa pessoa é um adulto')

#senha e usuário alura

usuario_correto = "alura"
senha_correta = "alura123"

usuario = input("Digite o nome de usuário: \n")
senha = input("Digite a senha: \n")

if usuario == usuario_correto and senha == senha_correta:
    print("Login bem sucedido!")
else:
    print("Credenciais inválidas. Tente novamente.")

#plano cartesiano

x = float(input("Digite a coordenada x: \n"))
y = float(input("Digite a coordenada y: \n"))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")





