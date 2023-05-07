"""
A função distância pretende determinar a menor distância entre duas palavras, ou seja o 
número de passos (inserção, remoção ou substituição de letras) a aplicar para transformar uma
palavra noutra. Por exemplo, a distância entre as palavras invention e execution é 5,
e os passos são os seguintes:
0. -> invention <-
1.     nvention
2.     evention
3.     exention
4.     exection
5. -> execution <-
"""

#Isto é a função fibonacci com memoization

"""
def dist(a,b):
    return aux(a,len(a),b,len(b),{})

def aux(a,i,b,j,m):
    if (i,j) in m:
        return m[(i,j)]
    if i == 0:
        m[(i,j)] = j
    elif j == 0:
        m[(i,j)] = i
    elif a[i-1] == b[j-1]:
        m[(i,j)] = aux(a,i-1,b,j-1,m)
    else:
        m[(i,j)] = min(1+aux(a,i,b,j-1,m), 1+aux(a,i-1,b,j,m), 1+aux(a,i-1,b,j-1,m))
    return m[(i,j)]

"""

#Isto é afunção fibonacci com programação dinâmica

def dist(a,b):
    m = {}
    for j in range(len(b)+1):
        m[(0,j)] = j
    for i in range(len(a)+1):
        m[(i,0)] = i
    for j in range(1,len(b)+1):
        for i in range(1,len(a)+1):
            if a[i-1] == b[j-1]:
                m[(i,j)] = m[(i-1,j-1)]
            else:
                m[(i,j)] = min(1+m[(i,j-1)], 1+m[(i-1,j)], 1+m[(i-1,j-1)])
        for i in range(0,len(a)+1):
            del m[(i,j-1)]
    return m[(len(a),len(b))]

def main():
    print("<h3>distância</h3>")
    print("in: invention, execution")
    print("out:",dist("invention", "execution"))
    
if __name__ == '__main__':
    main()