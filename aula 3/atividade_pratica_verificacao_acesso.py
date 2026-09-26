email_salvo = "daviemailteste.com"
senha_salva = "davisenhateste"
email = input ("digite seu email")
senha = input ("digite sua senha")
if email_salvo == "daviemailteste.com" and senha_salva == "davisenhateste":
    print("login realizado com sucesso!")

elif email == email_salvo and senha != senha_salva:
    print("senha incorreta!")

elif email != email_salvo and senha == senha_salva:
    print("email incorreto")

else:
    print("email e senha incorretos!")