def pedir_anio():
    anio = int(input("Ingrese el año del informe: "))
    while anio < 2024 or anio > 2027:
        print("El año debe ser entre 2024 y 2027")
        anio = int(input("Ingrese el año del informe: "))
    return anio

def pedir_trimestre():
    trimestre = int(input("Ingrese el numero del trimestre (1 a 4): "))
    while trimestre < 1 or trimestre > 4:
        print("El trimestre debe estar entre 1 y 4.")
        trimestre = int(input("Ingrese el numero del trimestre (1 a 4): "))
    return trimestre

def fecha_valida(dia, mes, anio):
    if mes < 1 or mes > 12:
        return False
    if dia < 1:
        return False
    if mes == 2:
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
            return dia <= 29
        else:
            return dia <= 28
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return dia <= 30
    else:
        return dia <= 31

def fecha_en_trimestre(mes, trimestre):
    if trimestre == 1 and (mes == 1 or mes == 2 or mes == 3):
        return True
    if trimestre == 2 and (mes == 4 or mes == 5 or mes == 6):
        return True
    if trimestre == 3 and (mes == 7 or mes == 8 or mes == 9):
        return True
    if trimestre == 4 and (mes == 10 or mes == 11 or mes == 12):
        return True
    return False

