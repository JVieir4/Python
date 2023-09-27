"""
Um fugitivo pretende atravessar um campo  no mínimo tempo possível (desde o 
canto superior esquerdo até ao canto inferior direito). Para tal só se poderá 
deslocar para a direita ou para baixo. No entanto, enquanto atravessa o campo 
pretende saquear ao máximo os bens deixados por fugitivos anteriores. Neste 
problema pretende-se que implemente uma função para determinar qual o máximo 
valor que o fugitivo consegue saquear enquanto atravessa o campo. 
A função recebe o mapa rectangular defindo com uma lista de strings. Nestas
strings o caracter '.' representa um espaço vazio, o caracter '#' representa 
um muro que não pode ser atravessado, e os digitos sinalizam posições onde há 
bens abandonados, sendo o valor dos mesmos igual ao digito.
Deverá devolver o valor máximo que o fugitivo consegue saquear enquanto 
atravessa o campo deslocando-se apenas para a direita e para baixo. Assuma que 
é sempre possível atravessar o campo dessa forma.
"""

def saque(mapa):
    c = len(mapa)
    l = len(mapa[0])
    meta = (c-1,l-1)
    
    dic = {}
    for i in range(c):
        for j in range(l):
            valor = 0
            if mapa[i][j] == '#':
                dic[(i,j)] = float("-inf")
            else:
                if mapa[i][j] != '.':
                    valor = int(mapa[i][j])
                
                if i>0 and j>0:
                    dic[(i,j)] = valor + max(dic[(i,j-1)],dic[(i-1,j)])
                elif i>0:
                    dic[(i,j)] = valor + dic[(i-1,j)]
                elif j>0:
                    dic[(i,j)] = valor + dic[(i,j-1)]
                
                else:
                    dic[(i,j)] = valor
    
    return dic[meta]

def main():
    print("<h3>saque</h3>")
    mapa = [".3......",
            "........",
            "...5#...",
            "...##...",
            ".....9..",
            "..2.....",
            "..2.....",
            "..2....."]
    print("in:")
    print('\n'.join(mapa))
    print("out:",saque(mapa))
    
import unittest

class saqueTest(unittest.TestCase):
    
    def test_saque_1(self):
            mapa = [".3......",
                    "........",
                    "...5#...",
                    "...##...",
                    ".....9..",
                    "..2.....",
                    "..2.....",
                    "..2....."]
            self.assertEqual(saque(mapa),12)
        
    def test_saque_2(self):
            mapa = ["11111",
                    "0###1",
                    "0###1",
                    "0###1",
                    "00001"]
            self.assertEqual(saque(mapa),9)
          
            
if __name__ == '__main__':
    main()
    #unittest.main()