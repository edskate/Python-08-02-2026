nome = input("Digite seu nome: ").strip()
cidade = input("Digite sua cidade: ").strip()

if nome == "" or cidade == "":
    print("🏅 Por favor, preencha o nome e a cidade.")
else:
    print(f"Olá, {nome}!")
    print(f"Seja bem-vindo(a), visitante de {cidade}!")