nome = input("Digite seu nome: ").strip().lower()

if nome == "edy":
    print("👉 Olá, Edy! O artista chegou! 🎤")
elif nome == "patrick":
    print("⛱ Olá, Patrick! Preparado para o ensaio? 🕺")
else:
    print(f"Olá, {nome.title()}! Seja bem-vindo(a)!")