import random


print(
    """
*********************************
Bem vindo ao jogo de adivinhação!
*********************************
"""
)

secret_number = random.randint(1, 100)
total_tentativas = 0
rodada = 1
pontos = 1000

print("""
*** Escolha o level ***
[1] Fácil
[2] Médio
[3] Difícil
""")

level = int(input("Escolha o level: "))

if level == 1:
    total_tentativas = 20
elif level == 2:
    total_tentativas = 10
else:
    total_tentativas = 5

for rodada in range(1, total_tentativas + 1):
    print(f"\nTentativas {rodada} de {total_tentativas}")
    guesses = int(input("Qual é o seu palpite? Escolha um numero de 1 a 100: "))
    print(f"Você digitou o numero: {guesses}\n")

    if guesses < 1 or guesses > 100:
        print("Por favor! Digite um numero entre 1 e 100: ")
        continue

    if guesses == secret_number:
        print(
            f"""
        Vc acertou!
        Seu palpite: {guesses} | Número sorteado: {secret_number}
        Seus pontos: {pontos}
        """
        )
        break
    else:
        if guesses > secret_number:
            print("Você Errou! Seu palpite foi maior que o numero secreto!")
        elif guesses < secret_number:
            print("Você Errou! Seu palpite foi menor que o numero secreto!")
        pontos_perdidos = abs(secret_number - guesses)
        pontos = pontos - pontos_perdidos

print("Game over!")
