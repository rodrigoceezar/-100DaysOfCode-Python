# ESTRUTURA IF
''' Estrutura IF e ELSE
if condição:
    o que fazer caso a condição seja verdadeira
else:
    o que fazer caso a condição seja falsa '''


# Lógica: Escreva	 um	 programa	 para	 ler	 o	 ano	 de	 nascimento	 de	 uma	 pessoa	 e	escrever	 uma	 mensagem	 que	 diga	 se	 ela	 poderá	 ou	 não	 votar	 este	 ano	(não	é	necessário	considerar	o	mês	em	que	ela	nasceu).
# Criando variáveis
print('******************código 1************************')
idade_min = 16
ano_nasc = int(input('Digite o ano que você nasceu: '))
ano_atual = int(input('Digite o ano atual:'))
idade = ano_atual - ano_nasc
# Condicional If Else
if idade >= idade_min:
    print('Você possui {} anos de idade, você poderá votar este ano!'.format(idade))
else:
    print('Você possui {} anos de idade, no entanto ainda não poderá votar este ano'.format(idade))
print('Fim do Código 1')


# Uma condição dentro de uma outra condição, ou seja, se uma condição for verdadeira e se a condição 2 for verdadeira também, executa a condição 1 e 2
print('****************código 2********************')
meta = 500
meta_funcionario = int(input('Digite quanto você vendeu este mês: '))
bonus = 0

if meta_funcionario >= meta:
    if meta_funcionario >= meta*2:
        bonus = 200
        print('Seu bonus foi de: {} reais'.format(bonus))
    else:
        bonus = 100
        print('Seu bonus foi de: {} reais'.format(bonus))
else:
    print('Você não atingiu a meta da empresa mas mês que vem vamo com tudo :)))')
print('Fim do Código 2')

# ESTRUTURA ELIF
''' Por exemplo:
    - if condição1:
- vai rodar se a condição1 for verdadeira
 <-- elif condição2:
   -vai rodar se a condição 1 for falsa e a condição2 for verdadeira
   -elif condição3:
   -vai rodar se a condição1 e a condição2 for falsa e a condição3 for verdadeira
   -else:
   -se nenhuma condição for verdadeira '''

# Exemplo:
print('****************código 3********************')

meta = 30000
vendas = int((input('Quantidade de Vendas do mês: ')))
if vendas < meta:
    print('A empresa não atingiu a meta de {} vendas, com {} dos produtos vendidos'.format(
        meta, vendas))
elif vendas == (meta*2):
    print('Parabêns, atingimos o dobro da meta com {} produtos '.format(vendas))
elif vendas >= (meta) and vendas < (meta*2):
    print('Parabêns, atingimos a meta com {} produtos vendidos'.format(vendas))
else:
    print('Parabêns, atingimos mais que o dobro {} produtos vendidos'.format(vendas))
