Nome = input("Digite seu nome: ")
Notas1 = int(input("Digite sua nota do primeiro bimestre: "))
Notas2 = int(input("Digite sua nota do segundo bimestre: "))
Notas3 = int(input("Digite sua nota do terceiro bimestre: "))
Notas4 = int(input("Digite sua nota do quarto bimestre: "))

print("Nome: \n", Nome)
print("Sua nota do 1º Bimestre foi:\n", Notas1)
print("Sua nota do 2º Bimestre foi:\n", Notas2)
print("Sua nota do 3º Bimestre foi:\n", Notas3)
print("Sua nota do 4º Bimestre foi:\n", Notas4)
soma = Notas1+Notas2+Notas3+Notas4
media = (Notas1+Notas2+Notas3+Notas4)/4
print("Soma de todos dos bimestre: ", soma)
print("Média Final dos Bimestre: ", media)
