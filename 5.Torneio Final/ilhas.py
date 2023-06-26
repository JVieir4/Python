'''
Neste problema pretende-se que implemente uma função que calcula quantas
ilhas existem num mapa.

O mapa é rectangular e definido por uma lista de strings de igual comprimento,
onde um caracter '#' marca uma quadrícula com terra e um ' ' uma quadrícula com 
mar. A função deve devolver o número de ilhas no mapa.
'''


def ilhas(mapa):
    if mapa=="":
        return 0
    
    ilhas = []
    
    for i in mapa:
        if (i[0]=='#' and i[1]==' '):
            ilhas.append(i[0])
        elif (i[-1]=='#' and i[-2]==' '):
            ilhas.append(i[-1])
        else:
            t=len(i)
            x=1
            while x<t:
                if (i[x-1]==' ' and i[x]=='#' and i[x+1]==' '):
                    ilhas.append(i[x])
                x+=1
    
    r = len(ilhas)
    
    return r+1

def main():
    print("<h3>ilhas</h3>")
    mapa = ["## ###",
            "## #  ",
            "#  #  ",
            "      ",
            "   ###"]
    print('\n'.join(mapa))
    print("out:",ilhas(mapa))
    
if __name__ == '__main__':
    main()

""" Testes
    # 1
    mapa = ["## ###",
            "## #  ",
            "#  #  ",
            "      ",
            "   ###"]
    > Resultado = 3

    # 2
    mapa = ["## ###",
            "####  ",
            "#  #  ",
            "###   ",
            "   ###"]
    > Resultado = 2
"""