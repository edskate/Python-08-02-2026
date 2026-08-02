nome = input("Digite seu nome: ")
funcao = input("Digite sua função: artista, dançarino ou produtor: ").lower()

if funcao == "artista":
    print(f"Bem-vindo, artista {nome}! 🎤")
elif funcao == "dançarino":
    print(f"Bem-vindo, dançarino {nome}! 🕺")
elif funcao == "produtor":
    print(f"Bem-vindo, produtor {nome}! 🎬")
else:
    print(f"Olá, {nome}! Função não cadastrada.")