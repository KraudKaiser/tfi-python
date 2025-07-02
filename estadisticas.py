def mostrar_estadisticas(pedidos):
    total_pedidos = 0
    total_unidades = 0
    total_monto = 0
    mayor_precio_unitario = 0
    
    for pedido in pedidos:
        total_pedidos = total_pedidos + 1
        total_unidades = total_unidades + pedido[5]
        total_monto = total_monto + pedido[6]
        if pedido[7] > mayor_precio_unitario:
            mayor_precio_unitario = pedido[7]
            
    print("La cantidad total de pedidos:", total_pedidos)
    print("El total de unidades vendidas:", total_unidades)
    print("El monto total de ventas:", total_monto)
    print("El precio unitario más alto:", mayor_precio_unitario)
