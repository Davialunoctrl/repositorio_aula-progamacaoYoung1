#listas

alunos = ["pietro" , "paul" , "davi" , "professor matheus"]

print("Lista Original: ", alunos)

alunos.append("tiago") #adiciona um novo valor a variavel do tipo lista

print() #serve pra criar um espaço acima

print("Lista apos metodo append: ", alunos)

alunos.remove("professor matheus")

print("-"*200) #serve pra criar linhas pelo numero de vezes multiplicado

print("Lista apos metodo remove: ", alunos)

alunos.sort() # ordem crescente
print("Lista apos metodo sort", alunos)

print(len(alunos)) #funçao len funciona para ler a quantidade de dados dentro da lista ou outros metodos


contador = 0

while  contador < 3: #repete enquanto a condição for verdadeira exemplo o valor da variavel contador é menor que 3 se sim a repetiçao continuara até que o contador retorne nao(false)
    print(contador)
    contador = contador + 1


for alunos in ["pietro" , "paul" , "davi" , "professor matheus"]:

    print(alunos)


for contador in range(10):
    if contador == 3:
        print("O passo 3 será pulado :P")
        continue
    


    print("Degrau:", contador)
