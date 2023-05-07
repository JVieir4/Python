"""

Implemente uma função que, dada uma frase cujos espaços foram retirados, 
tenta recuperar a dita frase. Para além da frase (sem espaços nem pontuação), 
a função recebe uma lista de palavras válidas a considerar na reconstrução 
da dita frase. Deverá devolver a maior frase que pode construir inserindo
espaços na string de entrada e usando apenas as palavras que foram indicadas 
como válidas. Por maior entende-se a que recupera o maior prefixo da string
de entrada. Só serão usados testes em que a maior frase é única.

"""

def espaca(frase,palavras):
    dic = {0:[]}
    mx = 0
    for i in range(1, len(frase)+1):
        print(i)
        for palavra in palavras:
            n = len(palavra)
            if i-n in dic and frase[i-n:].startswith(palavra):
                dic[i] = dic[i-n].copy()
                dic[i].append(palavra)
                print(dic[i])
                mx = i
    return ' '.join(dic[mx])

def main():
    print("<h3>espaca</h3>")
    palavras = ["e","o","so","maior","este","curso","urso","es","maio"]
    print("in:","estecursoeomaior",palavras)
    print("out:",espaca("estecursoeomaior",palavras))
    
import unittest

class espacaTest(unittest.TestCase):
    
    def test_espaca_1(self):
            palavras = ["e","o","so","maior","este","curso","urso","es","maio"]
            self.assertEqual(espaca("estecursoeomaior",palavras),"este curso e o maior")
        
    def test_espaca_2(self):
            palavras = ["o","oga","ga","gato","gatom","mia","eava","ava","e","a","va","vaca","mu","muge"]
            self.assertEqual(espaca("ogatomiaeavacamuge",palavras),"o gato mia e a vaca muge")
           
            
if __name__ == '__main__':
    main()
    #unittest.main()