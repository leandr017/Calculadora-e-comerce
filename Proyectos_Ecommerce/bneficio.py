print("##Calcular el beneficio de un producto")

costo = float(input ("Costo de producto: "))
comision = float(input("Comision de pagina: "))
publicidad = float(input("Costo de publicidad y marketing: "))
envio = float(input("Costo de envio: "))
venta = float(input("Precio de venta: "))

costos = int(costo + comision + publicidad + envio)
beneficio = int(venta - costos) 
margen = int((beneficio/venta)*100)
print(f"Beneficio del producto: {beneficio}")
print(f"Margen es de: {margen}%")



