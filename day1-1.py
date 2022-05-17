# 1 Faça um programa que peça dois números e imprima o maior deles.
# 2 Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo.
# 3 Crie um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo # Inválido.

############## EXERCICIO 1 ##################################################
# 1 Faça um programa que peça dois números e imprima o maior deles.
print('Exercicio1')
numero1 = input('Digite um numero: ')
numero2 = input('Digite outro numero: ')

if numero1 > numero2:
    print("O {} é o maior número".format(numero1))
else:
    print("O {} é o maior número".format(numero1))

############## EXERCICIO 2 ##################################################
# 2 Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo.
print('Exercicio2')
valor = int(input("Digite um valor: "))

if valor >= 0:
    print("Esse valor é positivo")
else:
    print("Esse valor é negativo")

############## EXERCICIO 3 ##################################################
# 3 Crie um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, T - Transgênero, NOT - Prefiro não dizer.
print('Exercicio3')
sexo = input('Digite a primeira letra referente ao seu sexo: M, F, T ou NOT:  ')

if sexo == 'M' or sexo == 'm':
    print('Masculino')
elif sexo == 'F' or sexo == 'f':
    print('Feminino')
elif sexo == 'T' or sexo == 't':
    print('Transgênero')
elif sexo == 'NOT' or sexo == 'not':
    print('Prefiro não dizer')
else:
    print('Digite um das alternativas (F, M, T ou NOT')
