nome = input("Digite seu nome: ").strip()

if nome == "":
    print("⁉️ ⁉️ Erro: você precisa digitar um nome.")
elif len(nome) < 3:
    print("⁉️ ⁉️ Erro: o nome precisa ter pelo menos 3 letras.")
else:
    nome = nome.title()

    print("👉 ==============================")
    print(f"Olá, {nome}!")
    print("👉 Seu cadastro foi realizado.")
    print("👉 Seja muito bem-vindo(a)! ✅")
    print("👉 ==============================")