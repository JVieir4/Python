def cruzamentos(ruas):
    cruzamentos = {}
    for rua in ruas:
        if rua[0] not in cruzamentos.keys():
            cruzamentos[rua[0]] = 1
        else:
            cruzamentos[rua[0]] += 1
        if rua[-1] not in cruzamentos.keys():
            cruzamentos[rua[-1]] = 1
        elif rua[0] != rua[-1]:
            cruzamentos[rua[-1]] += 1
        
    res = list(cruzamentos.items())
    res.sort(key = lambda x: (x[1], x[0]) )
    return res


def main():
    print("<h3>cruzamentos</h3>")
    ruas = ["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]
    print("in:",ruas)
    print("out:",cruzamentos(ruas))

import unittest


class cruzamentosTest(unittest.TestCase):
    
    def test_cruzamentos_1(self):
            self.assertEqual(cruzamentos(["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]),[('t',1),('a',2),('e',2),('l',2),('r',2),('c',3),('o',3),('s',6)])

    def test_cruzamentos_2(self):
            self.assertEqual(cruzamentos(["ab","bc","bd","cd"]),[('a',1),('c',2),('d',2),('b',3)])
            
if __name__ == '__main__':
    main()
    unittest.main()
