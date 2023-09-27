
def horario(ucs,alunos):
    
    return [(10885,10),(20000,10),(3042,5)]

def main():
    print("<h4>horario</h4>")
    ucs = {"la2": ("quarta",16,2), "pi": ("terca",15,1), "cp": ("terca",14,2),"so": ("quinta",9,3)}
    alunos = {5000: {"la2","cp"}, 2000: {"la2","cp","pi"},3000: {"cp","poo"}, 1000: {"la2","cp","so"}}
    print(horario(ucs,alunos))

    
import unittest

class horarioTest(unittest.TestCase):

    def test_horario_1(self):
        ucs = {"la2": ("quarta",16,2), "pi": ("terca",15,1), "cp": ("terca",14,2),"so": ("quinta",9,3)}
        alunos = {5000: {"la2","cp"}, 2000: {"la2","cp","pi"},3000: {"cp","poo"}, 1000: {"la2","cp","so"}}
        self.assertEqual(horario(ucs,alunos),[(1000, 7), (5000, 4)])

    def test_horario_2(self):
        ucs = {"la2": ("quarta",16,2), "pi": ("terca",15,1)}
        alunos = {5000: {"la2","pi"}, 2000: {"pi","la2"}}
        self.assertEqual(horario(ucs,alunos),[(2000, 3), (5000, 3)])
            
            
if __name__ == '__main__':
    main()
    unittest.main()
