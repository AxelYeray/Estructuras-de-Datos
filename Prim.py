#Algoritmo de prim
def prim(w,n,s):
    v=[]
    while(len(v) != n):
        v.append(0)
    v[s] = 1
    E = []   
    suma = 0
    for i in range(0,n-1):
        minimo = 9
        agregar_vertice = 0
        e = []
        for j in range(0,n):
            if(v[j] == 1):
                for k in range(0,n):
                    if(v[k]==0 and w[j][k] < minimo):
                        agregar_vertice = k
                        e = [j,k]
                        minimo = w[j][k]
        suma += w[e[0]][e[1]]
        v[agregar_vertice] = 1
        E.append(e)
    return [E,suma]

n = 6
s = 0
w = [#1,2,3,4,5,6  #9 == No existe arista que conecta a esos vertices
     [9,3,1,2,9,9],#1
     [3,9,9,9,2,4],#2
     [1,9,9,5,2,9],#3
     [2,9,5,9,1,9],#4
     [9,2,2,1,9,2],#5
     [9,4,9,9,2,9],#6
    ]

print(prim(w,n,s))