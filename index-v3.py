nickname = input("Digite o seu nickname para começar a aventura do herói: ")

print(f"Olá, {nickname}! Seja bem-vindo") 

xp = int(input("Digite o seu xp para descobrir o seu nível de herói: "))

nivel = ""

if xp <= 1000:
  nivel = "Ferro"
elif 1001 <= xp <= 2000:
  nivel = "Bronze"
elif 2001 <= xp <= 5000:
  nivel = "Prata"
elif 5001 <= xp <= 6000:
  nivel = "Ouro"
elif 6001 <= xp <= 7000:
  nivel = "Platina"
elif 7001 <= xp <= 8000:
  nivel = "Ascendente"
elif 8001 <= xp <= 10000:
  nivel = "Imortal"
else: 
  nivel = "Radiante"

print(f"O seu nível de herói é: {nivel}")

if nivel == "Ferro" or nivel == "Bronze":
  print("Isso significa que você precisa fazer novas missões.")
elif nivel == "Prata":
  print("Isso significa que você está no caminho certo. Continue assim!")
elif nivel == "Ouro" or nivel == "Platina":
  print("Quase lá! Falta pouco para você ser Radiante")
elif nivel == "Ascendente" or nivel == "Imortal":
  print("Mandou bem! Você está brilhando!")
elif nivel == "Radiante":
  print("Uau! Você conseguiu! Chegou no último nível. Parabéns!")
