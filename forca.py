import random



def jogar():
    
    início()
    palavra_secreta=lista_de_palavras()
    letras_acertadas=lista_acertos(palavra_secreta)

    enforcou = False
    acertou = False
    erros=0

    while(1):
        chute=obter_chute()                
        if (chute in palavra_secreta):
            marca_acerto(chute, letras_acertadas, palavra_secreta)
        else:
            erros+=1
            desenha_forca(erros)
            
        acertou=("_") not in letras_acertadas
        enforcou=erros==7
                 
        if enforcou:
           mensagem_perdedor(letras_acertadas, palavra_secreta)
           break
        if acertou:
            mensagem_vencedor(letras_acertadas)
            break
        print(letras_acertadas)
        print("Jogando...")   
        
def início():
    print("*********************************")
    print("   Bem vindo ao jogo da Forca!   ")
    print("*********************************")
    
def lista_de_palavras(primeira_linha_valida=0, nome_arquivo="palavras.txt"):
    palavras=[]
    with open(nome_arquivo,"r") as arquivo:
        for linha in arquivo:
            linha=linha.strip()
            palavras.append(linha)
        
        índice=random.randrange(primeira_linha_valida,len(palavras))
        palavra_secreta = palavras[índice].upper()
        return palavra_secreta
    
def lista_acertos(palavra):
        return ["_" for letra in palavra]
    
def obter_chute():
    chute=input("tenta uma letra: ").strip().upper()
    return(chute)
    
def marca_acerto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
            index += 1

def mensagem_vencedor(letras_acertadas):
    print(letras_acertadas) 
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_perdedor(letras_acertadas, palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("você acertou as letras: {}".format(letras_acertadas))
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__== "__main__":
    jogar()