nickname = input("Digite o seu nickname: ")
xp = int(input("Digite o seu xp: "))

if xp <= 1000:
    print(f"O herói de nome {nickname} está no nível de Ferro")
elif 1001 <= xp <= 2000:
    print(f"O herói de nome {nickname} está no nível de Bronze")
elif 2001 <= xp <= 5000:
    print(f"O herói de nome {nickname} está no nível de Prata")
elif 5001 <= xp <= 6000:
    print(f"O herói de nome {nickname} está no nível de Ouro")
elif 6001 <= xp <= 7000:
    print(f"O herói de nome {nickname} está no nível de Platina")
elif 7001 <= xp <= 8000:
    print(f"O herói de nome {nickname} está no nível de Ascendente")
elif 8001 <= xp <= 10000:
    print(f"O herói de nome {nickname} está no nível de Imortal")
elif xp >= 10001:
    print(f"O herói de nome {nickname} está no nível de Radiante")
