# STRINGS
email = 'rod2022@gmail.com'
nome = 'Rodrigo Cezar'


# Para descobrir o tamanho do texto
print(len(email))
print(len(nome))


# Para imprimir apenas o caracter de acordo com sua posição
print(nome[0])
print(nome[4])
print(nome[8])


# Para pegar caracteros da direita pra esquerda usa-se valores negativos
print(nome[-1])
print(nome[-4])

# Para pegar um pedaço de texto

print(email[:10])
print(email[10:])
print(email[4:10])

# Exercicio de Fixação: Completar os prints de forma correta
print(email)
print('Tamanho do email ' + str(len(email)) + ' caracteres')
print('Primeiro Caracter ' + email[0])
print('Ultimo caracter ' + email[-1])
print('Servidor do email ' + email[7:])

#### Operações em Strings #####

faturamento = 1000
custo = 500
lucro = faturamento - custo

# Uso do str() e do concatenar com +
# Só é possivel concatenar o mesmo tipo de valores srt + srt ou int + int
print('O faturamento da loja foi de: ' + str(faturamento))

# Uso do format
print('O faturamento foi de: {}'.format(faturamento))
# Caso repita de variaveis no print
print('O faturamento foi de: {0}, e o custo foi de: {1}. Lembrando que o faturamento foi de {0}'.format(
    faturamento, custo))

# Uso do %s (string) e %d (numero)
print('O faturamento foi de: %d. O custo foi de %d e o lucro foi de %d' %
      (faturamento, custo, lucro))

# Pra fazer se tem um texto dentro de outro (True or False)

print('@' in 'rod2022@gmail.com')
print('@' in 'rod2022gmail.com')


# Metodos de String na Documentação README.md (Consultar)
