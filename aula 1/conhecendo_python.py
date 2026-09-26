valor = 10 #variavel inteira que guarda numeros inteiros

nome = "davi" #variavel do tipo string guarda palavras

idade_escrita = "quinze" #variavel do tipo string guarda palavras 



print(valor) # print imprimindo o conteudo da variavel"valor"
print(nome)# print imprimindo o conteudo da variavel"nome"
print(idade_escrita) #print imprimindo o conteudo da variavel"idade_escrita"

idade_escrita = 28 # variavel idade_escrita sendo alterada

print(idade_escrita)

nome = input("digite seu nome: ") # input serve para perguntar e recebar uma infromação do usuario

print("prazer", nome, "seja bem vindo") # virgula é utilizada para introduzir uma variavel no texto do print


numero1 = 10
numero2 = 15
numero3 = 0
numero4 = 0
resposta = 0

resposta2 = 0
numero1= input("digite um numero: ") # input recebe o texto do usuario do tipo string

numero2 = input("digite outro numero: ") # recebe um texto de numero inteiro

numero3 = input("digite um numero quebrado: ") # recebe um texto de numero quebrado separado por ponto

numero4 = input("digite outro numero quebrado: ")

resposta = int(numero1) + int(numero2) # para poder somar um valor numerico que foi recebido do input é preciso converter texto para o tipo do numero

resposta2 = float(numero3) + float(numero4) # convertendo para numero quebrado

print("resultado inteiro:",resposta)

print("resultado numero quebrado:",resposta2)

