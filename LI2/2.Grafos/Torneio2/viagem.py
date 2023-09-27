'''
Alguém pretende realizar uma viagem com início num determinado
aeroporto, e visitando em cada momento o aeroporto mais distante que
ainda não visitou. Implemente uma função que calcule o itinerário
que deve ser seguido. Para além do aeroporto de partida, irá receber uma 
lista com a descrição dos ligações existentes entre aeroportos, 
sendo que cada ligação consiste numa string com os dois códigos dos 
aeroportos, intercalados pela distância entre os mesmos. Se num determinado
ponto da viagem existirem dois aeroportos não visitados à mesma distância 
máxima deve ser visitado primeiro o que tiver o código mais pequeno 
em ordem lexicográfica.
'''
def build(voos):
    adj = {}
    for voo in voos:
        ori = voo[0:3]
        des = voo[6:9]
        tam = voo[3:6]
        if ori not in adj:
            adj[ori] = {}
        if des not in adj:
            adj[des] = {}
        adj[ori][des] = int(tam)
        adj[des][ori] = int(tam)
    return adj

def fw(adj):
    dist = {}
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")    
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d]
    return dist

def viagem(inicio,voos):
    adj = build(voos)
    dist = fw(adj)
    print(adj)
    print(dist)
    itin = [inicio]
      
    return itin



def main():
    print("<h3>viagem</h3>")
    voos = ["OPO300LIS","LIS150FAO","OPO500MAD","MAD500LIS"]
    print("in:",voos)
    print("out:",viagem("OPO",voos))

import unittest

class distanciaTest(unittest.TestCase):

    def test0(self):
            voos = ["OPO300LIS","LIS150FAO","OPO500MAD","MAD500LIS"]
            self.assertEqual(viagem("OPO",voos), ["OPO","MAD","FAO","LIS"])

    def test1(self):
            voos = ["OPO300LIS","LIS200FAO","OPO500MAD","MAD500LIS"]
            self.assertEqual(viagem("LIS",voos), ["LIS","MAD","FAO","OPO"])

if __name__ == '__main__':
    main()
    #unittest.main()