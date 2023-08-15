print("- - - Adivinhe o número - - -")
print("Regras:\n - O número sorteado está entre 0 a 100 e é um número par.\n - Você tem quatro chances e 200 de vida.\n - A cada erro você perderá o equivalente à diferença ao número sorteado.\n ")
print("\n")

import random
tent = 4
vida = 200

resto = 0
while resto == 0:
    n_sorteio = random.randrange(0, 100)
    resto = n_sorteio % 2

while tent > 0 and vida > 0:
    number = int(input("Digite o número: "))
    if number == n_sorteio:
        print("Parabéns! Você acertou o número!")
        break
    else:
        print("Você errou")
        tent = tent - 1
        prox_vida = n_sorteio - number
        vida = vida - abs(prox_vida)
        print(vida)
        continue

while tent == 0 or vida == 0:
    print("Suas chances ou vida acabaram, boa sorte na próxima vez!")
    break





