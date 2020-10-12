
#
#  item2.c
#  Item 2 do Exercício Proposto: Paradigmas Linguagens de Programação
#
#  Created by Vinicius Giacomini on 10/11/2020.
#  Copyright © 2020 Vinicius Giacomini. All rights reserved.
#


# Criação da classe dos atletas arremessadores de peso
class Atleta_Arremesso:

    def __init__(self, nome_atletaP):
        self.nome_atletaP = nome_atletaP
        self.arremessos = []

        #inicializando o vetor de arremessos com zero
        for i in range(0, 3):
            self.arremessos.append(0)
#########

# Criação da classe de atletas de ginástica
class Atleta_Ginastica:

    def __init__(self, nome_atletaG):
        self.nome_atletaG = nome_atletaG
        self.notas = []

        #iniciando o vetor de notas com zero
        for i in range(0, 5):
            self.notas.append(0)
#########

# Função de ordenação de vetores através do método Bubble Sort
def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


## Arremesso de Peso
def arremesso_peso():

# Associação das classes
    atleta1 = Atleta_Arremesso("na")
    atleta2 = Atleta_Arremesso("na")

    print("Digite o nome do(a) primeiro(a) atleta: ")
    atleta1.nome_atletaP = raw_input()

    print("Digite os 3 arremessos do(a) atleta "+atleta1.nome_atletaP)
    for i in range(0, 3):
        atleta1.arremessos[i] = input()

    print("Digite o nome do(a) segundo(a) atleta: ")
    atleta2.nome_atletaP = raw_input()

    print("Digite os 3 arremessos do(a) atleta "+atleta2.nome_atletaP)
    for i in range(0, 3):
        atleta2.arremessos[i] = input()


# Ordena os vetores de arremesso
    bubbleSort(atleta1.arremessos)
    bubbleSort(atleta2.arremessos)

    print("Arremessos do(a) "+atleta1.nome_atletaP+str(atleta1.arremessos))
    print("Arremessos do(a) "+atleta2.nome_atletaP+str(atleta2.arremessos))


# Parte onde é feita a comparação para determinar o campeão
    if atleta1.arremessos[2] > atleta2.arremessos[2]:
        print("O "+atleta1.nome_atletaP+" ganhou")
    elif atleta1.arremessos[2] < atleta2.arremessos[2]:
        print("O "+atleta2.nome_atletaP+" ganhou")
    elif atleta1.arremessos[2] == atleta2.arremessos[2]:
        if atleta1.arremessos[1] > atleta2.arremessos[1]:
            print("O "+atleta1.nome_atletaP+" ganhou")
        elif atleta1.arremessos[1] < atleta2.arremessos[1]:
            print("O "+atleta2.nome_atletaP+" ganhou")
        else:
            print("Empate!")


## Ginastica Artistica
def ginastica_artistica():

# Associação das classes
    atleta3 = Atleta_Ginastica("na")
    atleta4 = Atleta_Ginastica("na")

    print("Digite o nome do(a) primeiro(a) atleta: ")
    atleta3.nome_atletaG = raw_input()

    print("Digite as 5 notas do(a) atleta "+atleta3.nome_atletaG)
    for i in range(0, 5):
        atleta3.notas[i] = input()

    print("Digite o nome do(a) segundo(a) atleta: ")
    atleta4.nome_atletaG = raw_input()

    print("Digite as 5 notas do(a) atleta "+atleta4.nome_atletaG)
    for i in range(0, 5):
        atleta4.notas[i] = input()


# Ordena os vetores de arremesso
    bubbleSort(atleta3.notas)
    bubbleSort(atleta4.notas)

    print("Arremessos do(a) "+atleta3.nome_atletaG+str(atleta3.notas))
    print("Arremessos do(a) "+atleta4.nome_atletaG+str(atleta4.notas))


# Parte onde é feita a comparação para determinar o campeão
    soma1 = 0
    for i in range(1, 5):
        soma1 = soma1 + atleta3.notas[i]
    print("Soma 1: "+str(soma1))

    soma2 = 0
    for i in range(1, 5):
        soma2 = soma2 + atleta4.notas[i]
    print("Soma 2: "+str(soma2))

    if soma1 > soma2:
        print("O(A) "+atleta3.nome_atletaG+" ganhou")
    elif soma2 > soma1:
        print("O(A) "+atleta4.nome_atletaG+" ganhou")
    else:
        print("Empate!")



# Corpo do programa, a variavel "pick" é para selecao de modalidade

pick = input("Bem vindo! Digite 1 para calcular a classificacao de Arremesso de Peso ou 2 para a Gisnastica Artistica: ")

if pick == 1:
    arremesso_peso()
elif pick == 2:
    ginastica_artistica()
else:
    # Caso o usuário digite um código de modalidade fora do estabelecido
    print("Modalidade nao exite!!!")

##fim
