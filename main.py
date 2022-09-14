# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def hipoteca(total, tipo, años):
    total = total
    tipo = tipo
    interes_mensual = (tipo / 12) / 100
    años = años
    cuotas = 25 * 12
    cuota_mensual = total * (
                (((1 + interes_mensual) ** cuotas) * interes_mensual) / (((1 + interes_mensual) ** cuotas) - 1))

    return round(cuota_mensual)



