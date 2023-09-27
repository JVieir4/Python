'''
O número de Erdos é uma homenagem ao matemático húngaro Paul Erdos,
que durante a sua vida escreveu cerca de 1500 artigos, grande parte deles em 
pareceria com outros autores. O número de Erdos de Paul Erdos é 0. 
Para qualquer outro autor, o seu número de Erdos é igual ao menor 
número de Erdos de todos os seus co-autores mais 1. Dado um dicionário que
associa artigos aos respectivos autores, implemente uma função que
calcula uma lista com os autores com número de Erdos menores que um determinado 
valor. A lista de resultado deve ser ordenada pelo número de Erdos, e, para
autores com o mesmo número, lexicograficamente.

'''
def build(artigos):
    adj = {}
    for autores in artigos.values():
        for autor in autores:
            for autor2 in autores:
                if autor != autor2:
                    if autor not in adj:
                        adj[autor] = set()
                    if autor2 not in adj:
                        adj[autor2] = set()
                    adj[autor].add(autor2)
                    adj[autor2].add(autor)
    return adj

def bfs(adj, o):
    vis = {}
    vis[o] = 0
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis[d] = vis[v]+1
                queue.append(d)
    print(vis)
    return vis

def erdos(artigos,n):
    adj = build(artigos)
    vis = bfs(adj,"Paul Erdos")
    final = [ k for k, v in sorted(vis.items(), key = lambda x: (x[1], x[0])) if v <= n ]          # k=key , v=value
    return final

def main():
    print("<h3>erdos</h3>")
    artigos = {"Adaptive register allocation with a linear number of registers": {"Carole Delporte-Gallet","Hugues Fauconnier","Eli Gafni","Leslie Lamport"},
               "Oblivious collaboration": {"Yehuda Afek","Yakov Babichenko","Uriel Feige","Eli Gafni","Nati Linial","Benny Sudakov"},
               "Optima of dual integer linear programs": {"Ron Aharoni","Paul Erdos","Nati Linial"}
              }
    print("in: 2")
    print('\n'.join(map(str,artigos.items())))
    print("out:",erdos(artigos,2))

import unittest

class erdosTest(unittest.TestCase):
    
    def test_erdos_1(self):
            artigos = {"Adaptive register allocation with a linear number of registers": {"Carole Delporte-Gallet","Hugues Fauconnier","Eli Gafni","Leslie Lamport"},
                       "Oblivious collaboration": {"Yehuda Afek","Yakov Babichenko","Uriel Feige","Eli Gafni","Nati Linial","Benny Sudakov"},
                       "Optima of dual integer linear programs": {"Ron Aharoni","Paul Erdos","Nati Linial"}
                      }
            self.assertEqual(erdos(artigos,2),['Paul Erdos', 'Nati Linial', 'Ron Aharoni', 'Benny Sudakov', 'Eli Gafni', 'Uriel Feige', 'Yakov Babichenko', 'Yehuda Afek'])

    def test_erdos_2(self):
            artigos = {"Specifying systems": {"Leslie Lamport"},
                       "Optima of dual integer linear programs": {"Ron Aharoni","Paul Erdos","Nati Linial"}
                      }
            self.assertEqual(erdos(artigos,1),['Paul Erdos', 'Nati Linial', 'Ron Aharoni'])
            
            
if __name__ == '__main__':
    main()
    #unittest.main()