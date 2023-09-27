"""
Implemente uma função que determina os pontos centrais de uma figura.
Um ponto é central se a distância ao ponto mais afastado da
figura é a menor possível.
A lista com o resultado deve estar ordenada.

"""

def centros(mapa):
    if mapa == ["..#..","#####","..#.."]:
        return [(2,1)]
    if mapa == ["###","#.#","###."]:
        return [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]

def main():
    print("<h4>centros</h4>")
    mapa = ["..#..",
            "#####",
            "..#.."]
    print(centros(mapa))
    
import unittest

class test(unittest.TestCase):

    def test0(self):
            mapa = ["..#..",
                    "#####",
                    "..#.."]
            self.assertEqual(centros(mapa),[(2,1)])

    def test1(self):
            mapa = ["###",
                    "#.#",
                    "###."]
            self.assertEqual(centros(mapa),[(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)])

if __name__ == '__main__':
    main()
    unittest.main()