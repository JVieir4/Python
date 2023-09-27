"""
Implemente uma função que dada uma palavra secreta e uma palavra tentativa
devolva uma lista com os caracteres da palavra tentativa que aparecem na
palavra secreta.
Mais concretamente, para cada caracter que apareça na palavra tentativa
deve também ser indicada a respectiva posição e um booleano que indica se
aparece na mesma posição na palavra secreta ou numa posição diferente.
"""

def wordle(secreta,tentativa):
    pos = []
    i = 0
    if len(tentativa) < len(secreta):
        for i in range(len(tentativa)):
            if tentativa[i] in secreta:
                if tentativa[i] == secreta[i]:
                    pos.append((tentativa[i],i,True))
                else:
                    pos.append((tentativa[i],i,False))
    else:
        for i in range(len(secreta)):
            if tentativa[i] in secreta:
                if tentativa[i] == secreta[i]:
                    pos.append((tentativa[i],i,True))
                else:
                    pos.append((tentativa[i],i,False))
    return pos

def main():
    print("<h4>wordle</h4>")
    print(wordle("programa","logica"))


import unittest

class test(unittest.TestCase):

    def test0(self):
            self.assertEqual(wordle("programa","logica"),[('o',1,False),('g',2,False),('a',5,True)])

    def test1(self):
            self.assertEqual(wordle("logica","programa"),[('o',2,False),('g',3,False),('a',5,True)])
    
    def test2(self):
            self.assertEqual(wordle("logica","logica"),[('l',0,True),('o',1,True),('g',2,True),('i',3,True),('c',4,True),('a',5,True)])
    
    def test3(self):
            self.assertEqual(wordle("aba","bba"),[('b',1,True),('a',2,True)])
    
if __name__ == '__main__':
    main()
    #unittest.main()
    