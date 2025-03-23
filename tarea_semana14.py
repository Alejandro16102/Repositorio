# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Programa principal
# Primera llamada: solo se proporciona el monto total de la compra
monto_total_1 = 100.0
descuento_1 = calcular_descuento(monto_total_1)
monto_final_1 = monto_total_1 - descuento_1
print(f"Monto total: ${monto_total_1:.2f}")
print(f"Descuento (10% por defecto): ${descuento_1:.2f}")
print(f"Monto final a pagar: ${monto_final_1:.2f}\n")

# Segunda llamada: se proporcionan el monto total de la compra y el porcentaje de descuento
monto_total_2 = 200.0
porcentaje_descuento_2 = 20
descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
monto_final_2 = monto_total_2 - descuento_2
print(f"Monto total: ${monto_total_2:.2f}")
print(f"Descuento ({porcentaje_descuento_2}%): ${descuento_2:.2f}")
print(f"Monto final a pagar: ${monto_final_2:.2f}")
