nome = ""

while nome == "":
    nome = input("Digite seu nome: ").strip()

    if nome == "":
        print("👉 O nome não pode ficar vazio. Tente novamente.")

print(f"Olá, {nome}! Seja muito bem-vindo(a)!")