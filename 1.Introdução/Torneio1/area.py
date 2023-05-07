def area(pecas):
    pos = []
    i  = 0
    j = 0
    semreps = []
    for x,y,dir,dim in pecas:
        if dir == False:
            while i < dim:
                pos.append((x,y+i))
                i += 1
        elif dir == True:
            while i < dim:
                pos.append((x+i,y))
                i += 1
        i = 0
    for j in range(len(pos)):
        if pos[j] not in semreps:
            semreps.append(pos[j])
    return len(semreps)

def main():
    print("<h4>area</h4>")
    pecas = []
    print(area(pecas))
    
import unittest

class test(unittest.TestCase):

    def test0(self):
            pecas = [(0,0,True,3),(1,1,False,3)]
            self.assertEqual(area(pecas),6)

    def test1(self):
            pecas = [(0,1,True,3),(1,0,False,3)]
            self.assertEqual(area(pecas),5)
            
    def test2(self):
            pecas = [(0,0,True,3),(1,1,False,3),(0,1,True,3),(1,0,False,3)]
            self.assertEqual(area(pecas),8)
            
    def test3(self):
            pecas = [(0,0,True,3),(0,0,True,3)]
            self.assertEqual(area(pecas),3)
            
    

if __name__ == '__main__':
    main()
    #unittest.main()