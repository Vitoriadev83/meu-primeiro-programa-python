nome = input("digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if idade > 17:
  print("Você pode entrar na festa!")
else:
  print("Você não pode entrar na festa! ")

with open("condicional_dados.csv", "a", encoding = "utf-8") as arquivo:
  arquivo.write(f"Seja bem vindo(a) {nome}. \n")
  arquivo.write(f"Sua idade é {idade} anos. \n")

  #Acrescentar encoding= "utf-8" resolveu a questão dos acentos'    