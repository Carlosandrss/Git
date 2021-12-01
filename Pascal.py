array=[]
def maximo(array, P1, P2):
    Res = array[P1:P2]
    return max(Res)
Tam=int(input("Ingrese el tamaño: "))
for i in range(0, Tam):
    elemento = int(input("Ingrese los numeros del array: "))
    array.append(elemento)
validacion1= False
validacion2= False
def validacion(P1):
    entero = int(P1)
    return entero <= Tam
print('Ingrese la posicion A: ', end='')
while not validacion1:
    P1=int(input())
    validacion1=validacion(P1)
    if not validacion1:
        print("Por favor ingresar una posición menor o igual al tamaño del arreglo: ", end='')
print(f'La posicion {P1}. es valida  ')
def validacion(P2):
    entero = int(P2)
    return entero <= Tam
print('Ingrese la posicion B: ', end='')
while not validacion2:
    P2=int(input())
    validacion2=validacion(P2)
    if not validacion2:
        print("Por favor ingresar una posición menor o igual al tamaño del arreglo y mayor a la P1: ", end='')
print(f'La posicion {P2}. es valida  ')
print("El número máximo del arreglo es ", maximo(array,P1,P2))