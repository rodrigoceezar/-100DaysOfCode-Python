# Introdução básica de python

# Como imprimir valores?
# print: serve para mostrar na tela algum valor
print('Hello, world')
print('Rodrigo')
print(22)
print(98.7)

# Operações Matemáticas
# Saber operacionalizar com python é essencial para qualquer código e pode ser feitos por:
print(3 + 4)  # soma
print(3 - 4)  # subtração
print(2*2)  # produto
print(3.1 * 4)  # produto com casa decimal
print(int(3.1 * 4))  # produto inteiro
print(6/3)  # divisão
print(7 % 3)  # resto da divisão

# Comparadores

# == : igual

# != : diferente

# > : maior que (>= maior ou igual)

# < : menor que (<= menor ou igual)

# in: texto dentro de outro texto

# not: verifica o contrário da comparação

# pass: para n fazer nada

# Strings
## String = Texto
print('Meu nome é rodrigo')
print('Meu nome é'+' rodrigo')  # Concatenação #
print('d' in 'rodrigo')  # d está contido no 'rodrigo'? true = sim false = não
print('Carlos' in 'Rodrigo tem 22 anos')
print(1 + 2)  # espaçamento (boas práticas)

# Variáveis e seu tipos
qtd_vendas = 1500  # qtd_vendas recebe 1500
nome = 'Vieira'
print(qtd_vendas)  # mostrar os valores de vendas
print(nome)
# Tipos de Variáveis
numero = 10  # int - inteiro
n_real = 10.4  # float - n com casa decimal
texto = 'Rodrigo'  # string - texto
boleano = True  # bool ou bolean --> True or False
print(type(numero))
print(type(n_real))
print(type(texto))
print(type(boleano))

# Misturando Variaveis (EXEMPLO)
faturamento = 1000
custo = 600
lucro = faturamento - custo
# concatenando string + int (variavel)
print('O faturamento foi: ' + str(faturamento))
print('O custo da loja foi: ' + str(custo) + ' reais')
print('Assim, o lucro da loja foi: ' + str(lucro) + ' reais')

# Interação com o usuário
# Quando se quer retirar uma informação do usuário usa-se 'Input': esse input fica gravado como uma variável
nome = input('Qual seu nome? \n')
sobrenome = input('E qual seu sobrenome? \n')


# Comando FORMAT
# ESSENCIAL
# Exemplo 1:
faturamento = 1000
custo = 600
lucro = faturamento - custo

print('O faturamento da loja foi {}'.format(faturamento))
print('O faturamento da loja foi {}. O custo da loja foi {}. E o lucro foi: {}'.format(
    faturamento, custo, lucro))

# Exemplo 2:

nome = 'Rodrigo'
idade = 23
peso = 75.9

print('Meu nome é {}, tenho {} anos de idade e peso {} kilos '.format(nome, idade, peso))
