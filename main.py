lista = [1,2,3,4,5,6,7,8,9]
x = '\033[0;34mX\033[m'
o = '\033[0;31mO\033[m'

pontosX = 0
pontosO = 0

#Mostra o jogo da velha (#);
def velha():
    return f'''
 {lista[0]} | {lista[1]} | {lista[2]} 
---+---+---
 {lista[3]} | {lista[4]} | {lista[5]}
---+---+---
 {lista[6]} | {lista[7]} | {lista[8]}

'''

def verifica(letra):
    letraN = letra[7]
    #Verifica se há ganhador;
    if (lista[0] == letra):
        if (lista[3] == letra and lista[6] == letra) or (lista[1] == letra and lista[2] == letra) or (lista[4] == letra and lista[8] == letra):
            if letraN == 'X':
                return f'\033[1;44mJogador {letraN} ganhou!\033[m'
            elif letraN == 'O':
                return f'\033[1;41mJogador {letraN} ganhou!\033[m'
    elif (lista[4] == letra):
        if (lista[1] == letra and lista[7] == letra) or (lista[3] == letra and lista[5] == letra) or (lista[2] == letra and lista[6] == letra):
            if letraN == 'X':
                return f'\033[1;44mJogador {letraN} ganhou!\033[m'
            elif letraN == 'O':
                return f'\033[1;41mJogador {letraN} ganhou!\033[m'
    elif (lista[8] == letra):
        if (lista[6] == letra and lista[7] == letra) or (lista[2] == letra and lista[5] == letra):
            if letraN == 'X':
                return f'\033[1;44mJogador {letraN} ganhou!\033[m'
            elif letraN == 'O':
                return f'\033[1;41mJogador {letraN} ganhou!\033[m'
    #Verifica se deu velha;
    count = 0
    for item in lista:
        if type(item) != int:
            count+=1
    if count == 9:
        return "\033[1;43mDeu velha!\033[m"
            
def pergunta(letra):
    while True:
        #Pergunta para o jogador a posição que ele deseja jogar:
        pergunta = input(f'Jogador {letra}, digite o número da posição que deseja substituir: ')
        try:
            pergunta = int(pergunta)
            
            if pergunta in lista:
                lista[pergunta-1] = letra
                break
            #Se o número não for de acordo com os disponíveis:
            else:
                print("\033[1;41mDIGITE UM VALOR VÁLIDO!\033[m")

        #Se não for um int:
        except ValueError:
            print("\033[1;41mDIGITE UM VALOR VÁLIDO!\033[m")

def jogo():
    while True:
        #Mostra o jogo da velha e pergunta para o jogador X:
        print(velha())
        pergunta(x)

        print('\n\n\n\n')

        #Verifica se o jogador X ganhou e mostra o jogo da velha:
        verifica(x)
        print(velha())
        if verifica(x) == '\033[1;44mJogador X ganhou!\033[m' or verifica(x) == "\033[1;43mDeu velha!\033[m":
            return verifica(x)

        #Pergunta para o jogador O:
        pergunta(o)
        print('\n\n\n\n')

        #Verifica se o jogador O ganhou:
        verifica(o)
        if verifica(o) == '\033[1;41mJogador O ganhou!\033[m' or verifica(o) == "\033[1;43mDeu velha!\033[m":
            print(velha())
            return verifica(o)

print(jogo())

if verifica(o) == '\033[1;41mJogador O ganhou!\033[m':
    pontosO+=1
elif verifica(x) == '\033[1;44mJogador X ganhou!\033[m':
    pontosX+=1

print(f'Pontos do jogador {o}: {pontosO}\nPontos do jogador {x}: {pontosX}')


while True:
    continuar = input(f'Jogar novamente? (y/n) ').lower()
    if continuar == 'y':
        lista = [1,2,3,4,5,6,7,8,9]
        print(jogo())
        if verifica(o) == '\033[1;41mJogador O ganhou!\033[m':
            pontosO+=1
        elif verifica(x) == '\033[1;44mJogador X ganhou!\033[m':
            pontosX+=1

        print(f'Pontos do jogador {o}: {pontosO}\nPontos do jogador {x}: {pontosX}')
    elif continuar == 'n':
        print('\033[1;42mOk, obrigado por jogar!\033[m')
        break
    else:
        print("\033[1;41mDIGITE 'Y' PARA SIM E 'N' PARA NÃO!\033[m")
