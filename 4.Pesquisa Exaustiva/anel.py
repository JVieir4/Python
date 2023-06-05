'''
Um anel de tamanho n (um número par) consiste numa permutação do números de 1 
até n em que a soma de quaisquer dois números adjacentes é um número primo
(considera-se que o primeiro elemento da sequência é adjacente do último).
Implemente uma função que calcule um destes aneis de tamanho n.
'''


def isPrime(n):
    for i in range(2, int(n/2)):
        if n%i==0:
            return False
    return True

# testa se o candidato c está completo
def complete(p,c):
    return len(c) == p

# enumera as extensões válidas para o candidato parcial c
def extensions(p,c):
    l = list()
    if c == []:
        return range(1, p+1)
    for i in range(1, p+1):
        if i not in c and isPrime(i+c[-1]):
            if len(c) != p-1 or isPrime(i+c[0]):
                l.append(i)
    return l

# testa se um candidato c é uma solução válida para p
def valid(p,c):
    return True

# procurar solução para p com pesquisa exaustiva
def aux(p,c):
    if complete(p,c):
        return valid(p,c)
    for x in extensions(p,c):
        c.append(x)
        if aux(p,c):
            return True
        c.pop()
    return False

def anel(n):
    c = []
    if aux(n,c):
        return c
    
def main():
    print("<h3>anel</h3>")
    print("in:",4)
    print("out:",anel(4))

import unittest

class anelTest(unittest.TestCase):

    def test_anel_1(self):
            self.assertIn(anel(4),[[1,2,3,4],[1,4,3,2],[2,1,4,3],[2,3,4,1],[3,2,1,4],[3,4,1,2],[4,1,2,3],[4,3,2,1]])
            
    def test_anel_2(self):
            self.assertIn(anel(2),[[1,2],[2,1]])
          
            
if __name__ == '__main__':
    main()
    unittest.main()