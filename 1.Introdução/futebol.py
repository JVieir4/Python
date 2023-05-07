
def tabela(jogos):
    tabpontos = {}
    tabgolos = {}
    lista = []
    lista2 = []
    for e1,g1,e2,g2 in jogos:
        if e1 not in tabpontos and e1 not in tabgolos:
            tabpontos[e1] = 0
            tabgolos[e1] = 0
        if e2 not in tabpontos and e2 not in tabgolos:
            tabpontos[e2] = 0
            tabgolos[e2] = 0
        if g1 > g2:
            tabpontos[e1] += 3
        if g2 > g1:
            tabpontos[e2] += 3
        elif g2 == g1:
            tabpontos[e1] += 1
            tabpontos[e2] += 1
        tabgolos[e1] += g1-g2
        tabgolos[e2] += g2-g1
    for i in tabpontos:
        for j in tabgolos:
            if i == j:
              lista2.append((j,tabpontos[i], tabgolos[j]))
    
    lista2.sort(key = lambda p: (p[1], p[2]), reverse = True)

        
    for i in lista2:
        lista.append((i[0],i[1]))
        
    return lista

def main():
    print("<h3>tabela</h3>")
    jogos = [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",4,"Benfica",1),("Sporting",2,"Porto",2)]
    print("in:",jogos)
    print("out:",tabela(jogos))

import unittest

class tabelaTest(unittest.TestCase):

    def test_tabela_1(self):
        jogos = [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",4,"Benfica",1),("Sporting",2,"Porto",2)]
        self.assertEqual(tabela(jogos),[('Porto', 4), ('Benfica', 4), ('Sporting', 2)])

    def test_tabela_2(self):
        jogos = [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",2,"Benfica",1),("Sporting",2,"Porto",2)]
        self.assertEqual(tabela(jogos),[('Benfica', 4), ('Porto', 4), ('Sporting', 2)])
            
if __name__ == '__main__':
    main()
    unittest.main()