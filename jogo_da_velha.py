quadro = [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "]
    
def display():
    print("\n", "|".join(quadro[0:3]), "\n", "|".join(quadro[3:6]), "\n", "|".join(quadro[6:]), "\n")

def tratar_erros_de_jogadas(pos, quadro):
    if pos < 0 or pos > 9 or quadro[pos] in (" X ", " O "):
        print("Posição inválida")
        return False
    return True

def jog(caractere):
    #display()
    while True:
        display()
        pos = int(input("Escolha uma posição de 1 a 9: "))
        print("\n")
        if tratar_erros_de_jogadas(pos-1, quadro):
            quadro[pos-1] = caractere 
            break

def jogador1(caractere):
    jog(caractere)

def jogador2(caractere):
    jog(caractere)

def linhas():
    l1 = quadro[0] == quadro[1] and quadro[0] == quadro[2] and " - " != quadro[0]
    l2 = quadro[3] == quadro[4] and quadro[3] == quadro[5] and " - " != quadro[3]
    l3 = quadro[6] == quadro[7] and quadro[6] == quadro[8] and " - " != quadro[6]
    return (l1 or l2 or l3)

def colunas():
    c1 = quadro[0] == quadro[3] and quadro[0] == quadro[6] and " - " != quadro[0]
    c2 = quadro[1] == quadro[4] and quadro[1] == quadro[7] and " - " != quadro[1]
    c3 = quadro[2] == quadro[5] and quadro[2] == quadro[8] and " - " != quadro[2]
    return (c1 or c2 or c3)

def diagonais():
    d1 = quadro[0] == quadro[4] and quadro[0] == quadro[8] and " - " != quadro[0]
    d2 = quadro[2] == quadro[4] and quadro[2] == quadro[6] and " - " != quadro[2]
    return (d1 or d2)

def winner():
    return (diagonais() or linhas() or colunas())

def tema():
    print("1 - X ")
    print("2 - O ")
    op = input("Jogador 1 escolha o seu caractere: ")
    if op == "1":
        return " X ", " O "
    else:
        return " O ", " X " 

def jogo():
    escolhas = tema()
    jog1 = escolhas[0]
    jog2 = escolhas[1]
    n = 9
    while True:
        if n == 0:
            print("\nEMPATE\n")
            break
        jogador1(jog1)
        if winner():
            display()
            print("\n JOGADOR 1 VENCEU\n")
            break
        n -= 1
        if n == 0:
            print("\nEMPATE\n")
            break
        jogador2(jog2)
        if winner():
            display()
            print("\nJOGADOR 2 VENCEU\n")
            break
        n -= 2

jogo()
