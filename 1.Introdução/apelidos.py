##Esta resolução só dá 80% correto
def apelidos(nomes):
    d = {}
    for p in nomes:
        n = -1
        for i in p.split():
            n +=1
        d[p] = n
    
    abcsort =(list(d.keys()))
    abcsort.sort()
    ans = (sorted(abcsort, key = lambda p:d[p]))
    return ans

##Esta, do mário, dá 100%
def apelidoss(nomes):
    nomes.sort(key = lambda x: (len(x.split())-1,x))
    return nomes


def main():
    print("<h3>apelidos</h3>")
    nomes = ["Jose Carlos Bacelar Almeida",
             "Maria Joao Frade",
             "Jose Bernardo Barros",
             "Jorge Manuel Matos Sousa Pinto",
             "Manuel Alcino Pereira Cunha",
             "Xico Esperto"]
    print("in:",nomes)
    print("out:",apelidoss(nomes))
    
import unittest


class apelidosTest(unittest.TestCase):
    
    def test_apelidos_1(self):
        self.assertEqual(apelidos(['Jose Carlos Bacelar Almeida', 'Maria Joao Frade', 'Jose Bernardo Barros', 'Jorge Manuel Matos Sousa Pinto', 'Manuel Alcino Pereira Cunha', 'Xico Esperto']),['Xico Esperto', 'Jose Bernardo Barros', 'Maria Joao Frade', 'Jose Carlos Bacelar Almeida', 'Manuel Alcino Pereira Cunha', 'Jorge Manuel Matos Sousa Pinto'])

    def test_apelidos_2(self):
        self.assertEqual(apelidos(['Pedro Silva','Pedro Pereira']),['Pedro Pereira','Pedro Silva'])

            
if __name__ == '__main__':
    main()
    unittest.main()
