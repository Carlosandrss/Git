def pascal(fi,co):
    fi = fi-1
    co = co-1
    row = [1]
    for i in range(fi):
        row = [ l + r for l, r in zip(row + [0], [0] + row)]
    return row[co]
k = int(input('Digite el nivel: '))
valido1= False
def validar(l):
    entero = int(l)
    return entero <= k

print('Digite la posicion: ', end='')
while not valido1:
    l=int(input())
    valido1=validar(l)
    if not valido1:
        print("¡ por favor ingresar una posición menor o igual al nivel: ", end='')

print(f'La posicion {l}. es valida  ')
print("El número en esa ubicación es: ",pascal(k,l))