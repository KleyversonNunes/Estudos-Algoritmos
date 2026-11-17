from random import randint
from collections.abc import Sequence
from typing import Protocol, TypeVar

class Comparavel(Protocol):
    """Protocolo para tipos que suportam comparação de ordem."""
    def __lt__(self, outro: object, /) -> bool: ...
    def __eq__(self, outro: object, /) -> bool: ...

T = TypeVar("T", bound=Comparavel)

def binary_search(lista: Sequence[T], alvo: T) -> tuple[int, int]:
    '''
    Realiza uma busca binária em uma sequência ordenada.

    Pré-requesitos:
        A sequência deve estar ordenada em ordem crescente.
        Resultados em sequências não ordenadas são indefinidos.

    Args:
        lista: Sequência idexável ordenada de elementos comparáveis.
        alvo: Elemento a ser localizado na sequência.

    Returns:
        Uma tupla (indice,iteracoes), onde:
        - 'indice' é a posição do elemento encontrado (ou -1 se ausente).
        - 'iteracoes' é o total de comparações de ponto médio realizado.

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
        elif valor_meio < alvo:
            id_inicial = id_meio+1
        else:
            id_final = id_meio-1
    return -1, iteracoes

def executar_testes_casos_de_bordas() -> None:
    """
        Valida deterministicamente os casos de borda da implementação.
    """
    # 1. Lista vazia
    assert binary_search([],10) == (-1,0), "Falha em lista vazia"

    # 2. Lista unitária (presente e ausente)
    assert binary_search([42], 42) == (0, 1), "Falha em lista unitária (alvo presente)"
    assert binary_search([42], 77) == (-1, 1), "Falha em lista unitária (alvo ausente)"

    # 3. Elementos nas extremidades e no centro exato
    amostra = [10,20,30,40,50,60,70]
    assert binary_search(amostra, 40) == (3, 1), "Ponto médio inicial deve levar 1 iteração."
    assert binary_search(amostra, 10) == (0, 3), "Extremo esquerdo deve levar 3 iterações."
    assert binary_search(amostra, 70) == (6, 3), "Extremo direito deve levar 3 iterações."

    # 4. Invariante de complexdade máxima para N = 100 (máximo de 7 iterações)
    cem_elementos = list(range(1, 200, 2))
    indice, iteracoes = binary_search(cem_elementos,100) # Par ausente
    assert indice == -1 and iteracoes <= 7, "Excedeu o limite teórico de log2(100) + 1"

if __name__ == "__main__":
    executar_testes_casos_de_bordas()

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