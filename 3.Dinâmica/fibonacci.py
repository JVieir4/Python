"""
Esta função recebe um índice e tem o intuíto de devolver o número que se encontra
nessa posição na sequeência de Fibonacci. A sequência de Fibonacci é infinita e consiste na
soma dos dois elementos anteriores. Os primeiros elementos são os seguintes:
  1  1  2  3  5  8  13  21  34  55  89  144  233  377  610  987  1597  ...
( 0  1  2  3  4  5  6   7   8   9   10  11   12   13   14   15   16    ... )
"""

#Isto é a função fibonacci com memoization

""" 
def fib(n):
    return aux(n,{})

def aux(n,m):
    if n in m:
        return m[n]
    if n<2:
        m[n] = 1
    else:
        m[n] = aux(n-1,m)+aux(n-2,m)
    
    print(m)
    return m[n]
 """

#Isto é afunção fibonacci com programação dinâmica
 
def fib(n):
    m = {}
    m[0] = 1
    m[1] = 1
    for i in range(2,n+1):
        m[i] = m[i-1] + m[i-2]
     #  del m[i-2]        vai apagando os elementos não necessários do dicionario      
    print(m)
    return m[n]

# também é possível resolver sem dicionário, assim:
"""
def fib(n):
    a = 1
    b = 1
    for i in range(2,n+1):
        b, a = a + b, b
    return b
"""
def main():
    print("<h3>fibonacci</h3>")
    print("in:",5)
    print("out:",fib(5))
    
if __name__ == '__main__':
    main()