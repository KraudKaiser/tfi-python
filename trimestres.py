import validaciones

def ingreso_trimestre():
    anio = validaciones.pedir_anio()
    trimestre = validaciones.pedir_trimestre()
    return anio, trimestre
