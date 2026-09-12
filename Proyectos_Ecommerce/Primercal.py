print ("CALCULADORA PARA EMPRENDEDORES")
print ("Los calculos posibles son:")
print ("Conversión/TicketPromedio/MargenPorcentual/Cac/Ltv")
menu = input("Seleccione que desea calcular (C)/(T)/(M)/(Ca)/(L): ").lower()

if menu == "c":
    visitantes = int(input("Ingrese el numero de visitantes en el periodo que desea evaluar: "))
    ventas = int(input("Ingrese el numero de ventas en el mismo periodo: "))
    conversion = float((ventas/visitantes)*100)
    print ("Su valor de Conversión es:")
    print (conversion, "%")
elif menu == "t":
    facturacion = float(input("Ingrese la facturacion total en el periodo que desea evaluar: "))
    operaciones = int(input("Ingrese la cantidad de operaciones realizadas en dicho periodo: "))
    ticket = float(facturacion/operaciones)
    print ("Su ticket promedio es de: ")
    print (ticket)
elif menu == "m":
    ingresos = float(input("Ingrese el numero total de sus ingresos en el periodo que desea evaluar: "))
    costos = float(input("Ingrese los costos totales para toda la produccion en dicho periode de tiempo: "))
    beneficio = int((ingresos-costos)/ingresos*100)
    print ("Su porcentaje de margen es:",beneficio,"%")
elif menu == "ca":
    publicidad = float(input("Ingrese el costo total de publicidades y marketing: "))
    clientes = int(input("Ingrese el numero de clientes nuevos adquiridos por dichos medios: "))
    cac = int(publicidad/clientes)
    print ("Su CAC es de",cac,"$")
elif menu == "l":
    ticket = float(input("Ingrese su ticket promedio: "))
    frecuencia = int(input("Ingrese le frecuencia de compra del cliente: "))
    tiempo = int(input("Ingrese el tiempo util del cliente en meses: "))
    ltv = int(ticket*frecuencia*tiempo)
    print("El LTV del cliente es de:$",ltv)
else:
    print("Caracter invalido")













