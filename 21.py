nome = input("Digite seu nome: ")
quantidade = int(input("Quantas vezes deseja mostrar a mensagem? "))

for contador in range(quantidade):
    print(f"{contador + 1} - Bem-vindo(a), {nome}!")