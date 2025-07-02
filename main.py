import trimestres
import pedidos
import estadisticas

def main():
    anio, trimestre = trimestres.ingreso_trimestre()
    lista_pedidos = pedidos.ingresar_pedidos(anio, trimestre)
    estadisticas.mostrar_estadisticas(lista_pedidos)

main()
