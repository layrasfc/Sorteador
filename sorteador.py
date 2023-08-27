# R E G R A S D O J O G O
print("- - - ADIVINHE O NÚMERO - - -")
print("\nRegras:\n - O número sorteado está entre 0 a 100 e é um número par.\n - Você tem 60 segundos de jogo, quatro chances e 200 de vida.\n - A cada erro você perderá o equivalente à diferença ao número sorteado.\n ")

# I M P O R T & V A R I A V E I S
import random
tent = 4
vida = 200
tentativas = 1
resto = 0 # Define um valor ao resto!

import time
tempo_comeco = time.time() # Começa a conta o tempo aqui!
tempo_fim = 60 # Define que irá até 60!


# S O R T E I O
# Sorteia o número até que o resto seja diferente de 0 (impar):
while resto == 0:
    n_sorteio = random.randrange(0, 100)
    resto = n_sorteio % 2
    # print(n_sorteio, resto)


# O J O G O C O M E Ç A
while tent > 0 and vida > 0:
    #Solicita input
    print(tentativas,"º Tentativa")
    tentativas += 1
    number = int(input("• Digite o número: "))
    if number > 100 or number < 0: # Não aceitar chute acima de 100 nem menores que 0
        print("\nNúmero inválido, tente outro chute.\n")
        continue


    # M a r c a r  t e m p o
    tempo_agora = time.time()  # Marca hora que o usuário escreve cada chute
    tempo_fim = tempo_agora - tempo_comeco
        # Diferença do começo até o momento que o usuário digitou o chute
    print(f"• Tempo: {tempo_fim:.02f}\n")

    if tempo_fim < 60: # Se a diferença for menor que 60...
        if number == n_sorteio: # Chute igual ao número sorteado
            print("--- PARABÉNS! ---\nVocê acertou o número!")
            break
        else: # Perde uma tent e perde vida
            tent = tent - 1
            vida = vida - abs(n_sorteio - number)

            if vida <= 0: # Evitar que printe vida negativa
                vida = 0

            print("Você errou! A sua vida agora é:", vida, "\n")
            continue
    else: # Se a diferença for maior que 60...
        print("Seu tempo acabou!")
    break

# F I M D E J O G O
while tent == 0 or vida <= 0 or tempo_fim == 60:
    print("--- FIM DE JOGO ---\nBoa sorte na próxima vez!")
    break
