"""
Implemente uma função que determina qual a probabilidade de um robot regressar 
ao ponto de partido num determinado número de passos. Sempre que o robot dá um 
passo tem uma determinada probabilidade de seguir para cima ('U'), baixo ('D'), 
esquerda ('L') ou direita ('R'). A função recebe o número de passos que o 
robot vai dar e um dicionário com probabilidades de se movimentar em cada uma
das direcções (as chaves são os caracteres indicados entre parêntesis).
O resultado deve ser devolvido com a precisao de 2 casas decimais.
"""
def aux(pa, pb, pos, dic):
    if pa == 0:
        return pos == (0,0)
    
    if (pa-1,(pos[0],pos[1]+1)) not in dic:
        dic[(pa-1,(pos[0],pos[1]+1))] = aux(pa-1, pb, (pos[0],pos[1]+1), dic)
    u = pb['U']*dic[(pa-1,(pos[0],pos[1]+1))]
    
    if (pa-1,(pos[0],pos[1]-1)) not in dic:
        dic[(pa-1,(pos[0],pos[1]-1))] = aux(pa-1, pb, (pos[0],pos[1]-1), dic)
    d = pb['D']*dic[(pa-1,(pos[0],pos[1]-1))]
    
    if (pa-1,(pos[0]+1,pos[1])) not in dic:
        dic[(pa-1,(pos[0]+1,pos[1]))] = aux(pa-1, pb, (pos[0]+1,pos[1]), dic)
    r = pb['R']*dic[(pa-1,(pos[0]+1,pos[1]))]
    
    if (pa-1,(pos[0]-1,pos[1])) not in dic:
        dic[(pa-1,(pos[0]-1,pos[1]))] = aux(pa-1, pb, (pos[0]-1,pos[1]), dic)
    l = pb['L']*dic[(pa-1,(pos[0]-1,pos[1]))]

    return u+d+r+l
    
    

def probabilidade(passos,probs):
    if passos %2 != 0:
        return 0.0
    
    return round(aux(passos, probs, (0,0), {}),2)

def main():
    print("<h3>probabilidade</h3>")
    probs = {'U':0.25,'D':0.25,'L':0.25,'R':0.25}
    print("in:",2,probs)
    print("out:",probabilidade(2,probs))
    
import unittest

class robotTest(unittest.TestCase):

    def test_probabilidade_1(self):
            probs = {'U':0.25,'D':0.25,'L':0.25,'R':0.25}
            self.assertEqual(probabilidade(2,probs),0.25)
        
    def test_probabilidade_2(self):
            probs = {'U':0.17,'D':0.33,'L':0.29,'R':0.21}
            self.assertEqual(probabilidade(6,probs),0.08)
          
            
if __name__ == '__main__':
    main()
    unittest.main()