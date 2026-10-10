# funcoes e parametros

def ola(): 
    print("olá")

ola()

def comprimentar(nome): 
    print("olá", nome)

comprimentar("Davi")


#return retorna o valor final do algoritimo que é a soma dos valores no parametro
#porém NÂO imprime por isso é necessario utilizar o print com a função como parametro para exibir o resultado
def somar_valores(valor1,valor2): 
    soma = valor1 + valor2

    return soma


print(somar_valores(10,20))

# apos o return a função se encerra ignorando qualquer codigo em baixo do return dentro da função
def subtrair_valores(valor1,valor2): 
    soma = valor1 - valor2

    print(soma)

    soma2 = valor1 + valor2
    print(soma2)

    return soma

    soma3 = valor1 + valor2

    print(soma3)

subtrair_valores(50,26)    
