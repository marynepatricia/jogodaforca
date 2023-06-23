PALAVRASECRETA = "PYTHON"
letra_acertada = ""
jogadas = 0 

import os

while True:
    tentativa = input("Digite uma letra para tentar advinhar a palavra: ").upper()
    jogadas += 1

    if len(tentativa) > 1:
        print("Você digitou mais de uma letra!")
        continue
    
    if tentativa in PALAVRASECRETA:
        letra_acertada += tentativa 
    
# Visualizar a palavra
    palavra_formada = ""
    for letra_secreta in PALAVRASECRETA:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    print(palavra_formada)

# Apresentação 
    if palavra_formada == PALAVRASECRETA:
        os.system('clear')
        print(f"Você acertou a palavra após {jogadas} jogadas")
        letra_acertada = ""
        jogadas = 0