
#Variável

nome = "Vitoria"
idade = 43
print(nome)
print(idade)

###

nome = input ("Digite o seu nome: ")

idade = int(input("Digite sua idade: "))

###

#Gravar informação em um arquivo de texto 
#CSV (Comma-Separated values)



  #Utilizando F strings

with open ("base_dados.csv", "a") as arquivo:
  arquivo.write (f"Seja bem vindo(a) {nome}.\n")