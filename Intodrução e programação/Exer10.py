num1 = float(input("Digite um numero: "))
print("Numero:", num1)
if(num1 == 10):
  print(f"O numero {num1: .1f} é igual a 10")
elif (num1 < 10):
  print(f"O numero {num1: .1f} é menor que numero 10")
else:
  print(f"O numero {num1} é maior a 10")