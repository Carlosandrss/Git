def escalones(num):
    if num <= 1:
        return num
    return escalones(num - 1) + escalones(num - 2)
def cuentamane(s):
    return escalones(s + 1)
Num = int(input('Ingrese numero de escalones:'))
print('cantidad de maneras para subir la escalera:')
print(cuentamane(num))