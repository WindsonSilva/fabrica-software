nome = input("Digite seu nome:\n")
dic = input("Digite o nome da disciplica:\n")
nota1 = float(input("Digite o valor da 1º prova:\n"))
nota2 = float(input("Digite o valor da 2° prova:\n"))
nota3 = float(input("Digite o valot da 3º prova:\n"))
soma = nota1+nota2+nota3
med = (nota1+nota2+nota3)/3
print("Nome:\n", nome)
print("Disciplina:\n", dic)
print("Soma total das 3 provas foi de:\n", soma)
print(f"Média do aluno {nome} foi {med:.2f} ")
if (med >=6):
    print(f"O Aluno {nome} esta APROVADO")
else:
    print(f"O Aluno {nome} esta REPROVADO")
