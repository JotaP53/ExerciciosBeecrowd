nome = str(input())
salario_fixo = float(input())
vendas_efetuadas = float(input())

comissao = vendas_efetuadas * 0.15

TOTAL = salario_fixo + comissao

print("TOTAL = R$ %.2f" % TOTAL)