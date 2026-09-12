print("CALCULADORA ECOMMERCE")
print("v1")
print("Calculos de basicos")

precioV = input("Precio de venta: ")
costoP = input("Costo por producto: ")
comisionP = input("Comision por producto: ")
envioP = input("Envio por producto: ")
publicidadT = input("Costo publicidad total: ")
cantV = input("Cantidad de ventas: ")

ingresosT = int(precioV * cantV)
costoP = int(costoP * cantV)
comisionT = int(comisionP * cantV)
envioT = int(envioP * cantV)
publicidadP = float(publicidadT / cantV)
gananciaT = int(ingresosT - costoT)
costoT = int(costoP - comisionP - envioP - publicidadP)
gananciaP = float(gananciaT / cantV)
margen = int((gananciaT - costoT)/gananciaT *100)
roas = float(ingresosT/publicidadT)




print("Ingresos totales:")











