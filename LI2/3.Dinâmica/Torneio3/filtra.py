'''
Implemente a seguinte função que dada uma lista de strings filtra as strings
que podem ser obtidas intercalando os caracteres das strings a e b também dadas
como parâmetro. Uma string palavra intercala as strings a e b sse apenas contem 
caracteres de a e b e todos os caracters de a e b aparecem pela mesma 
ordem em palavra. Sugere-se que comece pode definir recursivamente uma função 
auxiliar que testa se uma string palavra intercala as strings a e b, e que depois
optimize essa função com as técnicas de memoization e programação dinâmica.
'''

def filtra(strings, a, b):
    dic = {}
    res = []
    for palavra in strings:
        if aux(a, b, palavra, dic):
            res.append(palavra)
    return res

def aux(a, b, palavra, dic):
        if not a and not b and not palavra:
            return True
        if (a, b, palavra) in dic:
            return dic[(a, b, palavra)]
        if a and palavra.startswith(a[0]):
            if aux(a[1:], b, palavra[1:], dic):
                dic[(a, b, palavra)] = True
                return True
        if b and palavra.startswith(b[0]):
            if aux(a, b[1:], palavra[1:], dic):
                dic[(a, b, palavra)] = True
                return True
        dic[(a, b, palavra)] = False
        return False
    

def main():
    print("<h3>filtra</h3>")
    strings = ["ACDB","ABCD","ADCB"]
    print(filtra(strings,"AB","CD"))
    
import unittest

class filtraTest(unittest.TestCase):

    def test0(self):
            strings = ["ACDB","ABCD","ADCB"]
            self.assertEqual(filtra(strings,"AB","CD"), ["ACDB","ABCD"])

    def test1(self):
            strings = ["ACDABC","ABCACD","AACCBC","AABCDC"]
            self.assertEqual(filtra(strings,"ABC","ACD"), ["ACDABC","ABCACD","AABCDC"])


if __name__ == '__main__':
    main()
    unittest.main()