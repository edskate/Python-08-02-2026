nome = input("Digite seu nome: ")
idioma = input("Escolha português ou inglês: ").lower()

if idioma == "português" or idioma == "portugues":
    print(f"Olá, {nome}! Seja bem-vindo(a)!")
elif idioma == "inglês" or idioma == "ingles":
    print(f"Hello, {nome}! Welcome!")
else:
    print(f"Olá, {nome}! Idioma não encontrado.")