print("CALCULADORA ECOMMERCE")
print("v1")
print("Calculos de basicos")

precioV = int(input("Precio de venta: "))
costoP = int(input("Costo por producto: "))
comisionP = int(input("Comision por producto: "))
envioP = int(input("Envio por producto: "))
publicidadT = int(input("Costo publicidad total: "))
cantV = int(input("Cantidad de ventas: "))

publicidadP = float(publicidadT / cantV)
costoTP = int(costoP * cantV)
ingresosT = int(precioV * cantV)
comisionT = int(comisionP * cantV)
envioT = int(envioP * cantV)
costoT = int(costoTP + comisionT + envioT + publicidadT)
gananciaT = int(ingresosT - costoT)
gananciaP = float(gananciaT / cantV)
margen = int((gananciaT)/ingresosT *100)
roas = float(ingresosT/publicidadT)
i = gananciaT + publicidadT
i = i / ingresosT
float(breakeven = 1/i)


print("RESULTADOS")
print(f"Ingresos totales:{ingresosT}")
print(f"Costos Totales:{costoT}")
print(f"Comision Total:{comisionT}")
print(f"Envio Total:{envioT}")
print(f"Costo de publicidad por producto:{publicidadP}")
print(f"Ganancia total:{gananciaT}")
print(f"Ganancia por producto:{gananciaP}")
print(f"Margen:{margen}%")
print(f"Roas:{roas}")
print(f"Roas Break-even:{breakeven}")






