salario = float(input("Digite o salário atual: R$"))

if (salario <= 280):
    percentual = 20
elif (salario <=700):
    percentual = 15
elif (salario <= 1500):
    percentual = 10
else:
    percentual = 5
percentual = percentual/100.0

print("Salario Original: R$", salario)
print("Percentual: ",percentual*100, "%")
nsalario = percentual*salario

print("Valor do aumento em reais: ", nsalario )
print("Novo salario será de: ", nsalario+salario)