#operador maior ou menor e igual ou maior e maior ou igual
#> operador maior
#< operador menor
#>= operador maior OU igual
#<= operador menor ou igual
#operadores sempre retornarao verdadeiro ou falso para a pergunta
print(10 > 10) #false, 10 nao e maior que 10
print(10 >= 10) # true, 10 e maior e igual a 10
print(1.1 > 10) # true, 1.1 e maior que 1

print(10 < 10) #false, 10 nao e maior que 10
print(10 <= 10) # true, 10 e menor e igual a 10
print(1.1 <= 10) # false, 1.1 nao e maior ou igual a 1

#operador de comparacao ==

#o operador == serve para comparacao do primeiro VALOR com o segundo 
#VALOR diferente do = que serve para atribuicao. 

#operador de difereça !=

#ele e utilizado para verificar se o primeiro valor e DIFERENTE
#do segundo valor, retornando sempre true ou false

print(10.0 == 10)                                    #true
print("nome@gmail.com == nome@cna.com")              #false
print(9.1 == 9)                                      #false

print(10.0 != 10)                                    #true
print("professor" != "professor")             #false
print(09.1 != 9)                                      #false


#estruturas condicionais 

#if que significa SE
#else que significa SE NAO
# else if que significa SE NAO SE

if  True:
    print("teste") #como retornou VERDADEIRO o bloco do codigo executa


if  False:
    pint("teste") # como retornou FALSO o bloco de codigo NAO executa


#exemplo 1


teste = True

if teste:
    print("É verdadeiro")

teste = False

if teste:
    print("É verdadeiro")



#EXEMPLO 2

teste = input("voce ja brincou com fogo?")  # input sempre retornar um string

if teste == "sim":
    print("entao ja se queimou:(")

else:
    print("entao nao brinque se nao vai se queimar.")

#exemplo 3  IF aninhado quando a primeira condicao do primeiro if
#precisa ser VERDADEIRO para que os demais IF dentro dele
#sejam executados. 

idade = 17
tem_documento = True
pagou_ingresso = True

if idade >= 18:
    print("é maior de idade.")

    if tem_documento:
        print("apresentou um documento")

        if pagou_ingresso:
            print("entrada permitida!")

print()            
print("exemplo if independentes")
print()

#if IDEPENDENTES, quando um IF não depende do outros ser verdadeiro
#para ser executado 


if idade >= 18:
    print("é maior de idade.")

if tem_documento:
        print("apresentou um documento")

if pagou_ingresso:
            print("entrada permitida!")


#estrutura de condicional ELIF

teste = input("voce ja brincou com fogo?")  # input sempre retornar um string

if teste == "sim":
    print("entao ja se queimou:(")

elif teste == "talves":
    print("entao nao brinque se nao vai se queimar.")

else:
    print("entao nao brinque se nao vai se queimar.")



    #operadores logicos nor"não", or "ou", and"E"

# not=not 
#  or = ||ou |
# and= && ou %

#operador not
estudante = True
print(not estudante)          		#Não é estudante? Não (False)
proplayer = True

print(not proplayer)         		 #Não é pro player? Não (False)
maior_de_idade = False

print(not maior_de_idade)     		#Não é maior de idade? Sim (True)
goku_venceria_madoka = False

print(not goku_venceria_madoka)  	#Goku não venceria a Madoka? Sim (True)

#OPERADOR OR
True or False		# -> True

True or True		# -> True

False or False		# -> False

10 >= 10 or 1 > 2	# -> True, a primeira condição é verdadeira

10 < 10 or 1 > 2	# -> False, ambas condições são falsas
# operador and 

True and False	# -> False

True and True		# -> True

False and False	# -> False

10 >= 10 and 1>2	# -> False, a segunda condição é falsa

10 < 11 and 1 < 2	# -> True, ambas condições são verdadeiras

# exemplo 4 - atividade pratica


coral = True

print("treinamento iniciado!")

resposta = input("a cobra registrada no sistema é uma coral verdadeira ? (s/n)")

if coral == True and resposta == "s" or resposta == "S" or resposta == "yes" or resposta == "sim":
     print("identificação correta!")

else:
     print("identificação incorreta")

coral = False

print("treinamento iniciado!")

resposta = input("a cobra registrada no sistema é uma coral verdadeira ? (s/n)")

if coral == False and resposta == "n" or resposta == "N" or resposta == "no" or resposta == "nao" or resposta == "não":
     print("identificação incorreta!")

else: 
     print("identificação correta")