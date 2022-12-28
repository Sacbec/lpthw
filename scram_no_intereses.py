meses = 12
precio_original = 109990
pago_inicial = 32217.45
seguro = 7126.01
seguro_vida = 900
comision_apertura = 3093.44
enganche = 21998
monto_financiar = 88892
cuota_mensual = 7407.66

print("El pago inicial se compone de: ", seguro + comision_apertura + enganche )
print("En total estaria pagando: ", pago_inicial + monto_financiar)
print("Diferencia entre el pago de contado con el bono y el pago a meses: ", 
round(pago_inicial + monto_financiar - precio_original - seguro - seguro_vida, 2))
# tambien esta bien esta opcion, porque lo que eleva el precio es la comision por apertura, 
# el seguro de vida y el seguro de la moto en $1000, pero con la ventaja de hacer pagos mensuales. 
# y bueno la comision por apertura yo creo que la van a cobrar a fuerza. 
