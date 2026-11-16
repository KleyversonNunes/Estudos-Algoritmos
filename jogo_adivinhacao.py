import random as rd

def chutar(secret: int,value: int, attempt: int) -> tuple:
    """
    A presente função implenta um jogo de advinhação, onde um valor secreto entre 1 e 100 é sorteado aleatoriamente.
    Dessa forma, o jogado deve chutar valores dentro do intervalo de 1 a 100, usando a lógica da busca binária.
    """ 
    if value == secret:
        return (attempt,value)
    elif secret > value:
        print("Tente um valor maior")
    else:
        print("Tente um valor menor")

    value = int(input("Nova tentativa: "))
    return chutar(secret,value,attempt+1)

if __name__ == "__main__":
    value = int(input("Chute um valor entre 1 e 100: "))
    attempt, value = chutar(rd.randint(1,100),value,1)
    print(f"O valor {value} foi descoberto na tentativa {attempt}")