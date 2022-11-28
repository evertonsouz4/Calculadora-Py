# Calculadora básica #

print('CALCULADORA PYTHON\n')
print('Escolha uma das opções a baixo para calcular:\n')
print('1- Soma')
print('2- Subtração')
print('3- Multiplicação')
print('4- Divisão\n\n')

escolha = int(input('Digite uma das opções (1/2/3/4): '))

if escolha == 1:
    valor1 = int(input('\nDigite o primeiro número: '))
    valor2 = int(input('Digite o segundo número: '))
    soma = valor1 + valor2
    print(f'O resultado da soma é {soma}')