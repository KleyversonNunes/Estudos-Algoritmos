from random import randint
from copy import copy as cp

def binary_search(lista: list, alvo: int) -> tuple[int, int]:
    '''
        A seguinte função implementa uma versão simples da Busca Binária.
        O primeiro parâmetro é uma lista de 100 números aleatórios, entre 1 e 100 (com estes incluídos),
        o segundo parâmetro é valor buscado que também é um número aleátório entre 1 e 100 (com estes incluídos).
        Função retorna o id do valor quando este é encontrado, caso contrário retorna -1, além disso também é retornado
        o número de iterações do loop, que representa a quantidade de tentativas até encontrar o valor buscado ou não.
        A condição de parada do loop ocorre quando o a valor do id_inicial da lista atual for maior que o id_final, assim 
        indicando que o valor buscado não foi encontrado.

        Obs: Está primeira versão funciona apenas para uma lista de inteiros.
    '''
    id_inicial = 0
    id_final = len(lista)-1
    iteracoes = 0

    while id_inicial <= id_final:
        iteracoes+=1
        id_meio = id_inicial+(id_final-id_inicial)//2
        valor_meio = lista[id_meio]

        if valor_meio == alvo:
            return id_meio, iteracoes
        if valor_meio < alvo:
            id_inicial = id_meio+1
        else:
            id_final = id_meio-1
    return -1, iteracoes

if __name__ == "__main__":
    numeros = [ randint(1,500) for _ in range(20) ]
    numeros.sort()
    alvo = randint(1,500)
    print(numeros)
    #print(alvo)
    id_encontrado, iteracoes = binary_search(numeros,alvo)

    if id_encontrado == -1:
        print("Valor buscado não encontrado!")
    else:
        print(f"O valor {numeros[id_encontrado]} foi encontrado, na iteração nº {iteracoes}.")