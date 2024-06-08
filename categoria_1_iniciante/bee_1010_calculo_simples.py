cod1, quant1, valor_unit_1 = input().split()
cod2, quant2, valor_unit_2 = input().split()

VALOR_A_PAGAR = (int(quant1) * float(valor_unit_1)) + (int(quant2) * float(valor_unit_2))

print("VALOR A PAGAR: R$ %.2f" % VALOR_A_PAGAR)