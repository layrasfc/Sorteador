print("- - - ADIVINHE O NÚMERO - - -")
print("Regras:\n - O número sorteado está entre 0 a 100 e é um número par.\n - Você tem quatro chances e 200 de vida.\n - A cada erro você perderá o equivalente à diferença ao número sorteado.\n ")

import random
tent = 4
vida = 200
tentativas = 1
resto = 0
while resto == 0:
    n_sorteio = random.randrange(0, 100)
    resto = n_sorteio % 2

import time
tempo_comeco = time.time() #pega o tempo que começou
tempo_fim = 60 #fim é 60

while tent > 0 and vida > 0:
    print(tentativas, "º Tentativa")
    tentativas += 1
    number = int(input("Digite o número: "))
    tempo_agora = time.time()  # marca o tempo atual
    tempo_fim = tempo_agora - tempo_comeco #diferença do começo até o momento q digitou o chute
    print(f"Tempo: {tempo_fim:.02f}")
    if tempo_fim < 60:
        if number == n_sorteio:
            print("--- PARABÉNS! ---\nVocê acertou o número!")
            break
        elif vida < 0:
            vida = 0
            break
        else:
            tent = tent - 1
            vida = vida - abs(n_sorteio - number)
            print("Você errou! A sua vida agora é:", vida, "\n")
            continue
    else:
        print("Seu tempo acabou!")
    break


while tent == 0 or vida <= 0 or tempo_fim == 60:
    print("--- FIM DE JOGO ---\nSuas chances ou vida acabaram, boa sorte na próxima vez!")
    break

