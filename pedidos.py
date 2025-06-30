def crear_pedido():
    lista_pedidos = {}
    lista_pedidos["empresa"] = input(f"Porfavor, identifiqué la empresa a nombre del pedido: ")
    lista_pedidos["fecha_pedido"] = input(f"Ingresé la fecha del pedido. Solicitamos hacerla en el formado dia/mes/año: ")
    print(f"Ahora, empezara a ingresar uno a uno la cantidad de productos en el pedido")
    while True:
        descripcion_pedido, cant_unidades, precio_unitario = mini_pedido()
        if "productos" in lista_pedidos:
            lista_pedidos["productos"].append((descripcion_pedido, cant_unidades, precio_unitario))
        else:
            lista_pedidos["productos"] = []
            lista_pedidos["productos"].append((descripcion_pedido, cant_unidades, precio_unitario))
        pregunta = input("¿Quiere ingresar otro pedido? Si/No. (S/N)")
        if pregunta == "N" or pregunta == "n":
            break
        elif (pregunta != "N" or pregunta != "n") and (pregunta != "S" or pregunta != "s"):
            print("Porfavor, asegurese de seleccionar S para si, o N para no.")
    return lista_pedidos

    
def mini_pedido():
    descripcion_pedido = input(f"Ingresé la descripcion del producto: ")
    cant_unidades = int(input(f"Ingresé la cantidad de unidades del producto: "))
    monto_total = int(input(f"Ingresé el precio de venta de la unidad: "))
    precio_unitario = int(monto_total // cant_unidades)
    return descripcion_pedido,cant_unidades,precio_unitario

print(crear_pedido())