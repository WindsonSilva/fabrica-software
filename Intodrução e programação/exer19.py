#verificando se é triângulo equilátero, isósceles ou escaleno
lad1 = float(input("Digite o primiro lado: "))
lad2 = float(input("Digite o segundo lado: "))
lad3 = float(input("Digite o terceiro lado: "))

if (lad1+lad2<lad3) or (lad1+lad3<lad2) or (lad2+lad3<lad1):
   print("Não é triângulo")
elif (lad1 == lad2) and (lad1 == lad3):
   print("Equilátero")
elif (lad1==lad2) or (lad1==lad3) or (lad2==lad3):
  print("Isósceles")
else:
  print("Escaleno")