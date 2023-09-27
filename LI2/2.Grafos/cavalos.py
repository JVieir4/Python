'''

O objectivo deste problema é determinar quantos movimentos são necessários para 
movimentar um cavalo num tabuleiro de xadrez entre duas posições.
A função recebe dois pares de coordenadas, que identificam a origem e destino pretendido,
devendo devolver o número mínimo de saltos necessários para atingir o destino a partir da origem.
Assuma que o tabuleiro tem tamanho ilimitado.

'''
    
def saltos(o,d):
    jumps = 0
    pai = {}
    vis = {o}               # fila (neste caso uma lista) com os vértices a visitar a seguir
    queue = [o]             # i.e. vértices já descobertos mas ainda não visitados
    while queue:                    # enquanto existir algo na fila
        x,y = queue.pop(0)              # retira-se o elemento no topo da fila que será agora visitado - (x,y) porque tamos a trabalhar com coordenadas
        if (x,y) == d:                      # se o elemento agora visitado é o destino, então podemos parar a travessia
            break;
        for i in [-2,-1,1,2]:               # no xadrez, o cavalo move-se em L
            for j in [-2,-1,1,2]:
                if abs(i) != abs(j):            # como o movimento é em L, os valores i,j não podem ser iguais
                    if (x+i,y+j) not in vis:
                        vis.add((x+i,y+j))
                        pai[(x+i,y+j)] = (x,y)
                        queue.append((x+i,y+j))
    
    while d in pai:     # agora é só contar o nº de saltos até o destino
        d = pai[d]
        jumps += 1
    
    return jumps




def main():
    print("<h3>saltos</h3>")
    print("in: (0,0) (1,1)")
    print("out:",saltos((0,0),(1,1)))
    
import unittest

class saltosTest(unittest.TestCase):

    def test_saltos_1(self):
            self.assertEqual(saltos((0,0),(1,1)),2)
        
    def test_saltos_2(self):
            self.assertEqual(saltos((0,0),(7,7)),6)
            
            
if __name__ == '__main__':
    main()
    #unittest.main()