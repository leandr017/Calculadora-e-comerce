print("CALCULADORA ECOMMERCE")
print("v1")
print("Calculos de basicos")

precio_venta= float(input("Precio de venta: "))
costo_producto = float(input("Costo por producto: "))
comision_producto = float(input("Comision por producto: "))
envio_producto = float(input("Envio por producto: "))
publicidad_total = float(input("Costo publicidad total: "))
cantidad_ventas = int(input("Cantidad de ventas: "))

if cantidad_ventas==0:
    print("La cantidad no puede ser 0")
elif cantidad_ventas<0:
    print("La cantidad no puede ser negativa")
else:
    publicidad_producto = publicidad_total / cantidad_ventas
    costo_total_producto = costo_producto * cantidad_ventas
    ingresos_totales = precio_venta * cantidad_ventas
    comision_total = comision_producto * cantidad_ventas
    envio_total = envio_producto * cantidad_ventas
    costo_total = costo_total_producto + comision_total + envio_total + publicidad_total
    ganancia_total= ingresos_totales - costo_total
    ganancia_producto = ganancia_total / cantidad_ventas
    margen = (ganancia_total)/ingresos_totales *100
    roas = ingresos_totales/publicidad_total
    ganancia_sin_publicidad = ganancia_total + publicidad_total
    porcentaje_sin_publicidad = ganancia_sin_publicidad / ingresos_totales
    breakeven = 1/porcentaje_sin_publicidad

    print("RESULTADOS")
    print(f"Ingresos totales:{ingresos_totales}")
    print(f"Costos Totales:{costo_total}")
    print(f"Comision Total:{comision_total}")
    print(f"Envio Total:{envio_total}")
    print(f"Costo de publicidad por producto:{publicidad_producto}")
    print(f"Ganancia total:{ganancia_total}")
    print(f"Ganancia por producto:{ganancia_producto}")
    print(f"Margen:{margen:.2f}%")
    print(f"Roas:{roas:.2f}")
    print(f"Roas Break-even:{breakeven}")






