"""
Um vendedor ambulante tem que decidir que produtos levará na sua próxima viagem.
Infelizmente, tem um limite de peso que pode transportar e, tendo isso em atenção, 
tem que escolher a melhor combinação de produtos a transportar dentro desse limite 
que lhe permitirá ter a máxima receita.

Implemente uma função que, dado o limite de peso que o vendedor pode transportar, 
e uma lista de produtos entre os quais ele pode escolher (assuma que tem à sua 
disposição um stock ilimitado de cada produto), devolve o valor de receita máximo
que poderá obter se vender todos os produtos que escolher transportar, e a lista
de produtos que deverá levar para obter essa receita (incluindo repetições, 
caso se justifique), ordenada alfabeticamente.

Cada produto consiste num triplo com o nome, o valor, e o peso.

Caso haja 2 produtos com a mesma rentabilidade por peso deverá dar prioridade 
aos produtos que aparecem primeiro na lista de entrada.
"""


#######################################
#  Resolução 1 - 100%
#######################################

def vendedor(capacidade,produtos):
    d ={}
    d[0] = 0
    saco = {}
    for cap in range(1, capacidade+1):
        r = 0
        for p in produtos:
            if p[2] <= cap:
                a = p[1] + d[cap - p[2]]
                if a > r:
                    r = a
                    saco[cap] = p
        d[cap] = r
        
    valor = d[capacidade]
    lista = []
    
    while capacidade:
        if capacidade in saco:
            lista.append(saco[capacidade][0])
            capacidade -= saco[capacidade][2]
        else:
            break
    lista.sort()
    
    return (valor,lista)


#######################################
#  Resolução 2 - 100%
#######################################

def vendedor(capacidade,produtos):
    ht = {0:[]}
    mxs = {0:0}
    for c in range(1, capacidade+1):
        ht[c] = []
        mxs[c] = 0
        for n,v,p in produtos:
            if c-p>=0 and v+mxs[c-p] > mxs[c]:
                mxs[c] = v+mxs[c-p]
                ht[c] = ht[c-p].copy()
                ht[c].append(n)
    return (mxs[capacidade],sorted(ht[capacidade]))

def main():
    print("<h3>vendedor</h3>")
    produtos = [("biblia",20,2),("microondas",150,10),("televisao",200,15),("torradeira",40,3)]
    print("in:",14,produtos)
    print("out:",vendedor(14,produtos))
    
import unittest

class vendedorTest(unittest.TestCase):

    def test_vendedor_1(self):
            produtos = [("biblia",20,2),("microondas",150,10),("televisao",200,15),("torradeira",40,3)]
            self.assertEqual(vendedor(14,produtos),(190,["biblia","biblia","microondas"]))

    def test_vendedor_2(self):
            produtos = [("Verde",4,12),("Azul",2,2),("Cinzento",2,1),("Laranja",1,1),("Amarelo",10,4)]
            self.assertEqual(vendedor(15,produtos),(36,["Amarelo","Amarelo","Amarelo","Cinzento","Cinzento","Cinzento"]))
          
            
if __name__ == '__main__':
    main()
    #unittest.main()