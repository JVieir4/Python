'''
Implemente uma função que calcula o perímetro externo de uma figura.
A figura está desenhada usando o símbolo '#' num mapa quadriculado 
onde cada quadrícula tem dimensão 1x1. Assuma que a figura nunca 
irá estar encostada às margens do mapa.

'''

def arredores(fig, x, y):
    soma = 0
    if fig[x-1][y] == "#":
        soma+= 1
    if fig[x+1][y] == "#":
        soma+= 1
    if fig[x][y-1] == "#":
        soma+= 1
    if fig[x][y+1] == "#":
        soma+= 1
    return soma


def perimetro(figura):
    length = len(figura[0])
    width = len(figura)
    per = 0
    for y in range(length):
        for x in range(width):
            if figura[x][y] == "#":
                per += 4
                per -= arredores(figura, x, y)
    return per

def main():
    print("<h3>perimetro</h3>")
    figura = [".......",
              "...#...",
              "..#.#..",
              ".#...#.",
              "..#.#..",
              "...#...",
              "......."]
    print("in:")
    print('\n'.join(figura))
    print("out:",perimetro(figura))

import unittest

class areaTest(unittest.TestCase):

    def test_1(self):
            figura = [".......",
                      "...#...",
                      "..###..",
                      ".#####.",
                      "..###..",
                      "...#...",
                      "......."]
            self.assertEqual(perimetro(figura),20)

    def test_2(self):
            figura = [".......",
                      "...#...",
                      "..#.#..",
                      ".#...#.",
                      "..#.#..",
                      "...#...",
                      "......."]
            self.assertEqual(perimetro(figura),20)
            
if __name__ == '__main__':
    main()
    #unittest.main()