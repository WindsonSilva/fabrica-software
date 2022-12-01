primeiro = float(input("Digite o primeiro numero: "))
segundo = float(input("Digite o segundo numero: "))
terceiro = float(input("Digite o terceiro numero: "))
maior = primeiro
#achando maior numero
if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro
print("maior: ", maior)
#achando menor numero
menor = primeiro
if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro
print("menor: ", menor)
