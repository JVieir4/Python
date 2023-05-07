"""
Implemente uma função que dada uma sequência de inteiros, determinar o 
comprimento da maior sub-sequência (não necessariamente contígua) que se 
encontra ordenada de forma crescente.

Sugere-se que comece por implementar uma função auxiliar recursiva que determina 
o comprimento da maior sub-sequência crescente que inclui o primeiro elemento
da sequência, sendo o resultado pretendido o máximo obtido aplicando esta
função a todos os sufixos da sequência de entrada.

"""

def crescente(lista):
    return -1

def main():
    print("<h3>crescente</h3>")
    lista = [5,2,7,4,3,8]
    print("in:",lista)
    print("out:",crescente(lista))
    
import unittest

class crescenteTest(unittest.TestCase):
    
    def test_crescente_1(self):
            lista = [5,2,7,4,3,8]
            self.assertEqual(crescente(lista),3)

    def test_crescente_2(self):
            lista = [15,27,14,38,26,55,46,65,85]
            self.assertEqual(crescente(lista),6)
            
            
if __name__ == '__main__':
    main()
    #unittest.main()