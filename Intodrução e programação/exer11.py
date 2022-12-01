nome = input("Digite seu nome:\n ")
idade = int(input("Digite sua idade:\n "))

if 0<= idade <=2:
    print("Bebe")
elif (idade >2) and (idade <=11):
    print("Criança")
elif (idade >11) and (idade <=21):
    print("Jovem")
elif (idade >21) and (idade <=64):
    print("Adulto")
elif (idade >64) and (idade <=100):
    print("Idoso")
else:
    print("Muito Velhinho")
