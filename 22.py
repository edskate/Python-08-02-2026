nome = input("Digite seu nome: ")

print("👉 \nEscolha uma mensagem:")
print("👉 1 - Boas-vindas")
print("💣 2 - Bom dia")
print("🎓 3 - Boa tarde")
print("🎓 4 - Boa noite")

opcao = input("Digite uma opção: ")

if opcao == "1":
    print(f"Seja bem-vindo(a), {nome}!")
elif opcao == "2":
    print(f"Bom dia, {nome}!")
elif opcao == "3":
    print(f"Boa tarde, {nome}!")
elif opcao == "4":
    print(f"Boa noite, {nome}!")
else:
    print("👾 Opção inválida.")