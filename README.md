# _Práticando python - #100daysofcode_

## _Day 1_ - alguns exercicios com python para começar o chanllenge.

###### Data: 15/05/2022

---

---

#### _Exercicio 1_: Faça um programa que peça dois números e imprima o maior deles.

#### _Exercicio 2_: Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo.

#### _Exercicio 3_: Crie um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo # Inválido.

## _Day 2_ - estudando os principios básicos do python

###### Data: 16/05/2022

---

---

#### Como imprimir valores?

#### Operações Matemáticas

#### Comparadores

#### Strings

#### Variáveis e seu tipos

#### Interação com o usuário

#### Comando FORMAT

## _Day 3_ - condicionais IF, IF ELSE e ELIF

###### Data: 17/05/2022

---

---

#### Relembrando as condicionais

###### Comparadores

#### \* == : igual

#### \* != : diferente

#### \* > : maior que (>= maior ou igual)

#### \* < : menor que (<= menor ou igual)

#### \* in: texto dentro de outro texto

#### \* not: verifica o contrário da comparação

#### \* pass: para n fazer nada

#### Uso do IF e ELSE

#### Uso do IF e IF

#### Uso do ELIF

## _Day 4_ - STRINGS

###### Data: 20/05/2022

---

---

#### O QUE É UMA STRINGS PRO PYTHON?

#### É UMA LISTA DE CARACTERES QUE PODE SER QUALQUER COISA, UMA LETRA, UM ESPAÇO DE BARRA, UM @. O PRIMEIRO ITEM, O PRIMEIRO CARACTER É O INDICE 0.

##### nome = 'Rodrigo Cezar '

##### 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17

##### R o d r i g o C e z a r

##### print(nome[5])

###### resultado: g

###### print(nome[0])

##### resultudo: R

#### Quando os valores forem negativos, vai pegar o caracter de trás pra frente:

##### -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

##### R o d r i g o C e z a r

##### 0 1 2 3 4 5 6 7 8 9 10 11 12

###### print(nome[-1])

##### resultado: r

#### Para pegar um pedaço de texto usa-se o : ( texto[indice:]) --> indice : até o final da palavra ou ( texto[:indice]) --> do inicio da palavra : indice ou ( texto[indice:indice]) --> de um indice : até outro

#### print(nome[:3])

#### como resultado vai pegar todos os indices do 0 ao 2, preste atenção

#### resultado: Rod

#### perceba que ele não inclui o indice 3.

###### OPERAÇÕES COM STRINGS

#### str --> TRANFORMA NÚMERO EM STRING

#### in --> VERIFICA SE UM TEXTO ESTÁ CONTIDO DENTRO DO OUTRO

#### operator + --> CONCATENAR STRING

#### format e {} --> SUBSTITUIR VALORES

#### %s --> substituir textos

#### %d --> substituir números decimais

#### METODOS DE STRINGS

##### - capitalize() -> Coloca a 1ª letra Maiúscula

##### - casefold() -> Transforma todas as letras em minúsculas (existe lower() mas o casefold é melhor normalmente)

##### - count() -> Quantidade de vezes que um valor aparece na string

##### - endswith() -> Verifica se o texto termina com um valor específico e dá como resposta True ou False

##### - find() -> Procura um texto dentro de outro texto e dá como resposta a posição do texto encontrado

<p> Obs: lembrando como funciona a posição nas strings, então o @ está na posição 4

<p> l i r a @ g m a i l . c o m

<p> 0 1 2 3 4 5 6 7 8 9 10 11 12 13

##### - format() -> Formata uma string de acordo com os valores passados. Já usamos bastante ao longo do programa.

##### - isalnum() -> Verifica se um texto é todo feito com caracteres alfanuméricos (letras e números) -> letras com acento ou ç são considerados letras para essa função.

<p> Obs: se o texto fosse 'Jo~ao' ou então 'Joao#' o resultado seria False

##### - isalpha() -> Verifica se um texto é todo feito de letras.

<p> Obs: nesse caso se o texto fosse 'Joao123' o resultado seria False, porque 123 não são letras.

##### - isnumeric() -> Verifica se um texto é todo feito por números.

<p> Obs: existem os métodos isdigit() e isdecimal() que tem variações pontuais em caracteres especiais tipo textos com frações e potências, mas para 99% dos casos eles não vão ser necessários.

##### - replace() -> Substitui um texto por um outro texto em uma string.

<p> Obs: o replace precisa de 2 argumentos para funcionar. O 1º é o texto que você quer trocar. O 2º é o texto que você quer colocar no lugar daquele texto que você está tirando.

##### - split() -> Separa uma string de acordo com um delimitador em vários textos diferentes.

##### - splitlines() -> separa um texto em vários textos de acordo com os "enters" do texto

##### - startswith() -> Verifica se a string começa com determinado texto

##### - strip() -> Retira caracteres indesejados dos textos. Por padrão, retira espaços "extras" no início e no final

##### - title() -> Coloca a 1ª letra de cada palavra em maiúscula

##### - upper() -> Coloca o texto todo em letra maiúscula

<link> https://drive.google.com/file/d/1pMNXQUDCPA-yb0gKJjHeb_Kc03LRaT8a/view?usp=sharing <link>
