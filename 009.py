nome = input("Digite seu nome: ")
periodo = input("Digite manhã, tarde ou noite: ").lower()

if periodo == "manhã":
    print(f"Bom dia, {nome}! Seja bem-vindo(a)!")
elif periodo == "tarde":
    print(f"Boa tarde, {nome}! Seja bem-vindo(a)!")
elif periodo == "noite":
    print(f"Boa noite, {nome}! Seja bem-vindo(a)!")
else:
    print(f"Olá, {nome}! Seja bem-vindo(a)!")