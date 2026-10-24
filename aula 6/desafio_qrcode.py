import qrcode

texto = "https://portal.ctrlplay.com.br/"

imagem = qrcode.make(texto)

imagem.save("ctrlplay.png")

import qrcode

texto = "https://github.com/?locale=pt-br"

imagem = qrcode.make(texto)

imagem.save("github.png")