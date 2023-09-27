'''
Implemente a uma função que dada uma palavra s só com minúsculas 
descubra a menor palavra com os mesmos caracteres que esteja à distância k
de s. A distância entre duas palavras com o mesmo tamanho é o número de
caracteres diferentes na mesma posição.
'''

def segredo(s,k):
    return "estaquase"

def main():
    print("<h3>segredo</h3>")
    pal = "abc"
    print("in:",pal)
    print("out:",segredo(pal,4))
    
import unittest

class segredoTest(unittest.TestCase):

    def test_0(self):
            pal = "abc"
            self.assertEqual(segredo(pal,4),"bca")

    def test_1(self):
            pal = "batata"
            self.assertEqual(segredo(pal,36),"tabata")
            

if __name__ == '__main__':
    main()
    #unittest.main()