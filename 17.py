nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

if nome.lower() == "edy" and senha == "2034":
    print(f"Bem-vindo, {nome}! Acesso autorizado. ✅")
else:
    print("👉 Nome ou senha incorretos. ❌")