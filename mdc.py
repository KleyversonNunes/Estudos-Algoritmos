def euclides(a: int,b: int) -> int:
    """
    O propósito desta função é implementar o Algoritmos de Euclides, que tem como objetivo determinar o Máximo Divisor Comum (MDC) entre dois números inteiros.
    """
    if b == 0:
        return a
    return euclides(b,a%b)

def euclides_extendido(a: int,b: int) -> tuple:
    """
    Está é a versão estendida do Algoritmo de Euclides, que além do MDC também encontra o inversos modelares dos parâmetros A e B.
    """
    if b == 0:
        # (mdc, x, y)
        return (a,1,0)
    mdc,x_l,y_l = euclides_extendido(b,a%b)
    x = y_l
    y = x_l-y_l*(a//b)
    return (mdc,x,y)

if __name__ == "__main__":
    a,b = map(int,input("").split(" "))
    print("mdc =",euclides(a,b))
    mdc, x, y = euclides_extendido(a,b)
    print(f"{mdc} = ({x})*({a})+({y})*({b})")