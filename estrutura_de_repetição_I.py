# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@MauriSudario'

def ex01()
    """Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja 
        inválido e continue pedindo até que o usuário informe um valor válido."""

nota=float(input("informe um numero de 0 a 10: "))
while (nota>10) or (nota<0):
    nota=float(input("informe um numero de 0 a 10: "))

def ex02()
    """Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual 
    ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""

print("Realize aqui seu cadastro:")
usuario=str(input("Digite seu usuário: "))
senha=str(input("Digite sua senha: "))
while usuario==senha:
	print("ERRO: O usuário não pode ser igual a senha, tente novamente")
	usuario=str(input("Digite seu usuário: "))
	senha=str(input("Digite sua senha: "))
else:
	print("Se cadastrado foi realizado com sucesso")

def ex03()
    """Faça um programa que leia e valide as seguintes informações:
       Nome: maior que 3 caracteres;
       Idade: entre 0 e 150;
       Salário: maior que zero;
       Sexo: 'f' ou 'm';
       Estado Civil: 's', 'c', 'v', 'd';"""

nome = str(input("informe seu nome: "))
while (len(nome) <= 3):
    nome = str(input("informe seu nome corretamente: "))

idade = int(input("informe sua idade: "))
while (idade > 150 or idade < 0):
    idade = int(input("informe sua idade corretamente: "))

salario = float(input("informe seu salário: "))
while (salario < 0):
    salario = float(input("informe seu salário corretamente: "))

sexo = str(input("informe a inicial do seu sexo (m ou f): "))
while sexo != "f" and sexo != "m":
    sexo = str(input("informe a inicial do seu sexo corretamente: "))

estado_civil = str(input("informe a inicial do seu estado civil (s, c, v ou d): "))
while (estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d"):
    estado_civil = str(input("informe a inicial do seu estado civil corrtamente: "))


def ex04()
    """Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de 
    crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
    Faça um programa que calcule e escreva o número de anos necessários para que a população do país A 
    ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento."""

população_A=80000
população_B=200000
ano=0
while população_A < população_B:
	população_A+=round((população_A*3.0)/100)
	população_B+=round((população_B*1.5)/100)
	ano=ano+1

print("Levará",ano,"anos para população da cidade A ser maior que a cidade B")
print("população_B: ",população_B,"habitantes")
print("população_A: ",população_A,"habitantes")

def ex05()
    """Copie o programa anterior e altere permitindo ao usuário informar as 
       populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação."""

população_A=float(input("Informe a população da cidade A: "))
população_B=float(input("Informe a população da cidade B: "))
ano=0
taxa_crescimento_A=float(input("Informe a taxa de crescimento da população da cidade A: "))
taxa_crescimento_B=float(input("Informe a taxa de crescimento da população da cidade B: "))
while população_A < população_B:
	população_A+=round((população_A*taxa_crescimento_A)/100)
	população_B+=round((população_B*taxa_crescimento_B)/100)
	ano=ano+1

print("Levará",ano,"anos para população da cidade A ser maior que a cidade B.")
print("população_B: ",população_B,"habitantes")
print("população_A: ", população_A,"habitantes")

def ex06()
    """Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro."""

for i in range(21):
    print(i)

def ex07()
        """Copie o programa anterior, modifique para que ele mostre os números um ao lado do outro."""

for i in range (21):
print(list(range(1,21)))

def ex08()
    """Faça um programa que leia 5 números e informe o maior número."""

lista = []
qtd = input('informe a quantidade de numeros: ')

for n in range(0,int(qtd)):
    lista.append(int(input('Digite um número: ')))

print ('Maior número da lista: ', max(lista))

def ex09()
    """Faça um programa que leia 5 números e informe a soma e a média dos números."""

num1=float(input("digite o 1º numero: "))
num2=float(input("digite o 2º numero: "))
num3=float(input("digite o 3º numero: "))
num4=float(input("digite o 4º numero: "))
num5=float(input("digite o 5º numero: "))
soma=num1+num2+num3+num4+num5
print("A soma dos números é: ",soma,)
print("A média dos números é: ",soma/5)

def ex10()
    """Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50."""

for i in range(1,51,2):
    print (i)

def ex11()
    """ Faça um programa que receba dois números inteiros e gere os números inteiros que estão 
    no intervalo compreendido por eles. """

num1=int(input("Digite um numero: "))
num2=int(input("Digite outro numero: "))
while num2<num1:
	num1=int(input("Digite um numero: "))
	num2=int(input("Digite outro numero: "))
else:
	for i in range(num1,num2,1):
		print(i)

def ex12()
    """ Copie e altere o programa anterior para mostrar no final a soma dos números."""


inicio = int(input("Digite um numero: "))
fim = int(input("Digite outro numero: "))
soma = 0
while (inicio < fim - 1):
    inicio = inicio + 1
    print(inicio)
    soma = inicio + soma

print("A soma dos intervalos é: ", soma)

def ex13()
    """ Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
     O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
..
5 X 10 = 50  """

while 1==1:
    tabuada=int(input("Informe a taboada que voce deseja saber: "))
    numero=tabuada
    contador=0
    while (contador<=9):
        contador=contador+1
        print(numero,"*",contador,"=",tabuada)
        tabuada=tabuada+numero

def ex14()
    """ Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número 
    elevado ao segundo número. Não utilize a função de potência da linguagem. """

base = int(input('Informe a base: '))
expoente = int(input('Informe o expoente: '))
acumulador = 1
for c in range (0,expoente):
  acumulador = base*acumulador
print('resultado =',acumulador)

def ex15()
    """ Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números
        pares e a quantidade de números ímpares. """

print("Calcular a quantidade de numeros impares e pares.")
par=0
impar=0
for i in range(10):
    numero = int(input(" Degite um numero: "))
    if(numero%2==0):
         par=par+1
    else:
        impar=impar+1
print("Temos",par,"numeros pares.")
print("Temos",impar,"numeros impares.")

def ex16()
    """ A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
        Faça um programa capaz de gerar a série até o n−ésimo termo. """

Fibonacci=eval(input("Informe o tamanho da seqüência: "))
x, y = 1, 1
for c in range(Fibonacci):
    print (x)
    soma=x+y
    x,y=y,soma

def ex17()
    """ A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
    Faça um programa que gere a série até que o valor seja maior que 500. """

x, y = 1, 1
while (x<1000):
    print (x)
    soma=x+y
    x,y=y,soma

def ex18()
    """ Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
     Ex.: 5!=5.4.3.2.1=120 """

numero = int(input("Digite um número: "))
count1 = 0
count = 1
if count1 < numero:
    fatorial = numero * (numero - count)
    count = count - 1
    count1 = count + 1
    print("O fatorial ",numero, "é ", fatorial)

def ex19()
    """  Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e
          a soma dos valores.   """

lista = []
count = 0

quant = int(input("Digite a quantiade de número que deseja digitar: "))
while quant != count:
    numero = lista.append(float(input("Digite um número: ")))
    count += 1

print("Lista: ", lista, "\nMaior: ", max(lista), "\nMenor: ", min(lista))
print("Soma: ", max(lista) + min(lista))

def ex20()
    """  Copie e altere o programa anterior para que ele aceite apenas números entre 0 e 1000.   """


lista = []
count = 0

quant = int(input("Digite a quantiade de número que deseja digitar: "))
while quant != count:
    numero = float(input("Digite um número: "))

    while numero > 1000 or numero < 0:
        numero = float(input("Digite um número[erro]: "))

    lista.append(numero)
    count += 1

print("Lista: ", lista, "\nMaior: ", max(lista), "\nMenor: ", min(lista))
print("Soma: ", max(lista) + min(lista))

def ex21()
    """Copie e altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias 
       vezes e limitando o fatorial a números inteiros positivos e menores que 16.  """

import math
lista = []
count = 0

quant = int(input("Digite a quantiade de número que deseja digitar: "))
while quant != count:
    numero = float(input("Digite um número: "))
    while numero // 1 != numero or numero < 0 or 0 or numero < 16:
        numero = float(input("Digite um número[erro]: "))

    print("Fatorial do número digitado: ", math.factorial(numero))
    count += 1

def ex22()
    """Faça um programa que calcule e mostre a média aritmética de N notas. """


lista = []
count = 0
soma = 0
x = 0

quant = int(input("Digite a quantiade de número que deseja digitar: "))
while quant != count:
    numero = float(input("Digite um número: "))

while x < count:
    notas[x] = float(input("Nota %d:" % x))
    soma += notas[x]
    x += 1
x = 0
while x < count:
    print("Nota %d: %6.2f" % (x, notas[x]))
    x += 1
print("Média: %5.2f" % (soma / x))

def ex23()
    """Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
    Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120 """


import math
numero = int(input("\n Digite o numero que quer realizar a fatorial : "))
count = numero
fatorial = math.factorial(numero)

for i in range(numero - 1):
    print(count,, end=" * ")
    count -= 1
print("1 = ", fatorial)

def ex24()
    """O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia 
um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas,
 bem como a média das temperaturas. """

ntemps = int(input("Quantidade de temperaturas que irá digitar: "))
temps = []
ntemp = 1
for i in range(ntemps):
    print("Temperatura n° ", ntemp)
    temp = temps.append(float(input("Digite a temperatura: ")))
    ntemp += 1

print("Maior temperatura = ", max(temps))
print("Menor temperatura = ", min(temps))
print("Média = ", round(sum(temps) / len(temps), 2))

def ex25()
    """ Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do 
        aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo.
        Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.   """

numero_alunos = []
altura_alunos = []

for i in range(10):
    print("\nDigitação número ", i + 1," :")
    n_aluno = int(input("Digite o número do aluno: "))
    while n_aluno in numero_alunos:
        print("[Este número ja foi digitado]")
        n_aluno = int(input("Digite outro número: "))
    a_aluno = altura_alunos.append(float(input("Digite a altura do aluno: ")))
    numero_alunos.append(n_aluno)

indice_baixo = altura_alunos.index(min(altura_alunos))
indice_alto = altura_alunos.index(max(altura_alunos))

print("Aluno mais baixo \nNúmero: ", numero_alunos[indice_baixo], "\nAltura: ", min(altura_alunos))
print("Aluno mais alto \nNúmero: ", numero_alunos[indice_alto], "\nAltura: ", max(altura_alunos))

def ex26()
    """ Faça um programa que peça um número inteiro positivo e em seguida mostre este número invertido.
Exemplo:
  12376489  => 98467321 """

numero = input("Digite um número: ")
print("Número invertido: ", numero[:: -1])

def ex27()
    """ Faça um programa que mostre os n termos da Série a seguir:
 S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
 Imprima no final a soma da série."""

n1 = 1
n2 = 1
n1_lista = []
n2_lista = []
print("S = ", end = "")
while n1 <= 10 -1:
    print(n1, "/", n2, " + ", end="")
    n1_lista.append(n1)
    n2_lista.append(n2)
    n1 += 1
    n2 += 2

print(n1, "/", n2, " = ", sum(n1_lista), "/", sum(n2_lista))

def ex28()
    """ Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos."""

h = 1
n = 2
h_lista = []
n_lista = []
print("H = 1 +", end = "")
while n <= 10 -1:
    print(" ",h, "/", n, " + ", end="")
    h_lista.append(h)
    n_lista.append(n)
    n += 1

print(h, "/", n, " => ", sum(h_lista), "/", sum(n_lista), " => ", round(sum(h_lista) / sum(n_lista)), 2)

def ex29()
    """Faça um programa que mostre os n termos da Série a seguir:
 S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
 Imprima no final a soma da série. """

n1 = 1
n2 = 1
n1_lista = []
n2_lista = []
print("S = ", end = "")
while n1 <= 10 -1:
    print(n1, "/", n2, " + ", end="")
    n1_lista.append(n1)
    n2_lista.append(n2)
    n1 += 1
    n2 += 2

print(n1, "/", n2, " = ", sum(n1_lista), "/", sum(n2_lista))