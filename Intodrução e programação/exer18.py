# calcular salario liquido
salario = float(input("Digite seu salário: R$"))

if (salario <= 900):
    salario = salario
    print("Salario Isento de descontos.")
elif (salario <=1500):
    print("Desconto do IR 5%:R$", salario*0.05, "\n","Desconto do INSS 10%: R$", salario*0.1, "\n" )
    print("Total de descontos:R$", (salario * 0.05) + (salario * 0.1))
    print("Salario Liquido será de:R$ ", salario-(salario * 0.05) - (salario * 0.1))
elif (salario <=2500):
    print("Desconto do IR 10%:R$", salario*0.1, "\n", "Desconto do INSS 10%: R$", salario*0.1, "\n")
    print("Total de descontos:R$", (salario * 0.1) + (salario * 0.1))
    print("Salario Liquido será de:R$ ", salario - (salario * 0.1) - (salario * 0.1))
else:
    print(f"Desconto do IR 20%:R$ ", salario*0.2, "\n", "Desconto do INSS 10%: R$", salario*0.1, "\n")
    print(f"Total de descontos:R$", (salario * 0.2) + (salario * 0.1))
    print("Salario Liquido será de:R$ ", salario - (salario * 0.2) - (salario * 0.1))