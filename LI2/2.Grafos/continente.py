'''
O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.

'''
def build(vizinhos):
    adj = {}
    for fronteira in vizinhos:
        for pais in fronteira:
            if pais not in adj:
                adj[pais] = set()
            for pais2 in fronteira:
                if pais != pais2:
                    if pais2 not in adj:
                        adj[pais2] = set()
                    adj[pais].add(pais2)
    return adj

def bfs(adj,o):
    vis = {o}				# "queue" - fila (neste caso uma lista) com os vértices a visitar a seguir 
    queue = [o]				 # i.e. vértices já descobertos mas ainda não visitados
    while queue:			  # enquanto existir algo na fila
        v = queue.pop(0)	   # retira-se o elemento no topo da fila que será agora visitado
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                queue.append(d)
    print(vis)
    return vis

def maior(vizinhos):
    adj = build(vizinhos)
    vis = []
    tamanho = 0
    for fronteira in vizinhos:
        for pais in fronteira:
            if pais not in vis:
                continente = bfs(adj,pais)
                vis.append(list(continente))
                tamanho = max(tamanho, len(continente))
    return tamanho

def main():
    print("<h3>maior</h3>")
    vizinhos = [["Portugal","Espanha"],["Espanha","Franca"],["Franca","Belgica","Alemanha","Luxemburgo"],["Canada","Estados Unidos"]]
    print("in:", vizinhos)
    print("out:", maior(vizinhos))
    
import unittest

class maiorTest(unittest.TestCase):

    def test_maior_1(self):
            vizinhos = [["Portugal","Espanha"],["Espanha","França"],["França","Bélgica","Alemanha","Luxemburgo"],["Canada","Estados Unidos"]]
            self.assertEqual(maior(vizinhos), 6)

    def test_maior_2(self):
            vizinhos = [["Portugal","Espanha"],["Espanha","França"]]
            self.assertEqual(maior(vizinhos), 3)
            
            
if __name__ == '__main__':
    main()
    #unittest.main()