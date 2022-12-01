nome = input("Digite o nome de um aluno:\n")
materia = input("Digite o nome da materia:\n")
nota1 = float(input("Nota da 1º prova:\n"))
nota2 = float(input("Nota da 2º prova:\n"))
nota3 = float(input("Nota da 3º prova:\n"))

media = (nota1+nota2+nota3)/3
soma = (nota1+nota2+nota3)
print("Nome do Aluno:\n", nome)
print("Nome da materia:\n", materia)
print("Soma total das 3 provas:\n", soma)
print("Média do aluno foi de: ", media)