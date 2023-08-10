import random
tent = 4
vida = 200

resto = 0
while resto == 0:
    n_sorteio = random.randrange(0, 100)
    resto = n_sorteio % 2
    print(n_sorteio, resto)

while tent > 0 and vida > 0:
    number = int(input("Digite o número: "))
    if number == n_sorteio:
        print("Você acertou!")
        break
    else:
        print("Você errou")
        tent = tent - 1
        prox_vida = n_sorteio - number
        vida = vida - abs(prox_vida)
        print(vida)
        continue


