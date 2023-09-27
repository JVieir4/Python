'''

Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 

'''
def verifica(p,mapa,dic):
    w = len(mapa[0])
    l = len(mapa)
    xi, yi = p
    pontos = []
    cima = (xi,yi+1)
    baixo =(xi,yi-1)
    esq = (xi-1,yi)
    dir = (xi+1,yi)
    if yi < w-1 and mapa[xi][yi+1] == '.':
        pontos.append(cima)
        if cima not in dic:
            dic[cima] = set()
            verifica(cima,mapa,dic)
    if yi > 0 and mapa[xi][yi-1] == '.':
        pontos.append(baixo)
        if baixo not in dic:
            dic[baixo] = set()
            verifica(baixo,mapa,dic)
    if xi < l-1 and mapa[xi+1][yi] == '.':
        pontos.append(dir)
        if dir not in dic:
            dic[dir] = set()
            verifica(dir,mapa,dic)
    if xi > 0 and mapa[xi-1][yi] == '.':
        pontos.append((xi-1,yi))
        if esq not in dic:
            dic[esq] = set()
            verifica(esq,mapa,dic)
    for i in pontos:
        dic[p].add(i)
    
def area(p,mapa):
    dic = {}
    xi , yi  = p
    cont = 0
    if mapa[xi][yi] == '*':
        return cont
    cont += 1
    dic[p] = set()
    verifica(p,mapa,dic)
    print(dic)
    return len(dic)

def main():
    print("<h3>area</h3>")
    mapa = ["..*..",
            ".*.*.",
            "*....",
            ".*.*.",
            "..*.."]
    print("in:",(3,2))
    print('\n'.join(mapa))
    print("out:",area((3,2),mapa))

import unittest

class areaTest(unittest.TestCase):

    def test_area_1(self):
            mapa = ["..*..",
                    ".*.*.",
                    "*...*",
                    ".*.*.",
                    "..*.."]
            self.assertEqual(area((3,2),mapa),5)

    def test_area_2(self):
            mapa = ["..*..",
                    ".*.*.",
                    "*....",
                    ".*.*.",
                    "..*.."]
            self.assertEqual(area((3,2),mapa),12)
            
            
if __name__ == '__main__':
    main()
    unittest.main()