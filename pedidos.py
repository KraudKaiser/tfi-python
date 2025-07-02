import validaciones

def ingresar_pedidos(anio, trimestre):
    pedidos = []
    seguir = "S"

    while seguir == "S":
        empresa = input("Ingrese el nombre de la empresa: ")
        fecha_valida = False
        while fecha_valida == False:
            dia = int(input("Ingrese el dia del pedido: "))
            mes = int(input("Ingrese el mes del pedido: "))
            anio_pedido = int(input("Ingrese el año del pedido: "))

            if validaciones.fecha_valida(dia, mes, anio_pedido):
                if anio_pedido == anio:
                    if validaciones.fecha_en_trimestre(mes, trimestre):
                        fecha_valida = True
                    else:
                        print("El mes no corresponde al trimestre ingresado")
                else:
                    print("El año de la fecha no coincide con el año del informe")
            else:
                print("La fecha ingresada no es valida")

        descripcion = input("Ingrese la descripcion del producto: ")

        cantidad = int(input("Ingrese la cantidad de unidades (entre 1 y 999): "))
        while cantidad < 1 or cantidad > 999:
            print("La cantidad debe ser mayor a 0 y menor que 1000")
            cantidad = int(input("Ingrese la cantidad de unidades (entre 1 y 999): "))

        monto = int(input("Ingrese el monto total del pedido (mayor a 9999): "))
        while monto <= 9999:
            print("El monto debe ser mayor a 9999")
            monto = int(input("Ingrese el monto total del pedido (mayor a 9999): "))

        precio_unitario = monto / cantidad

        print("Empresa:", empresa)
        print("Fecha:", dia, "/", mes, "/", anio_pedido)
        print("Producto:", descripcion)
        print("Cantidad:", cantidad)
        print("Monto total:", monto)
        print("Precio unitario:", precio_unitario)

        pedido = (empresa, dia, mes, anio_pedido, descripcion, cantidad, monto, precio_unitario)

        pedidos.append(pedido)

        seguir = input("Desea ingresar otro pedido? (S/N): ")
    return pedidos
