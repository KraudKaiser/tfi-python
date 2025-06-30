def ingreso_trimestre():

    while True:
        año = int(input(f"Ingrese el año del trimestre a chequear: "))
        if año < 2023 or año > 2027:
            print(f"Porfavor, seleccioné una fecha valida desde 2023 hasta 2027")
            
        else:
            break
    while True:    
        trimestre = int(input(f"Ingrese el numero de Trimestre en el que se encuentra: "))
        if trimestre < 1 or trimestre > 4:
            print(f"Porfavor, seleccioné un trimestre valido entre 1 y 4.")
            trimestre = int(input(f"Ingrese el numero de Trimestre en el que se encuentra: "))
        else:
            break

    return año, trimestre
    
ingreso_trimestre()