Array = []
def orden(l):
    final = []
    print(l)
    for i in range(len(l)):
        a = sorted(l[i])
        final.append(a)
    return final

num = int(input('Ingrese el numero de palabras: '))
for i in range(0, Num):
    Palabra = (input('Ingresa una palabra: '))
    Array.append(Palabra)  # adding the element
print("El resultado del ordenamiento es", orden(Array))