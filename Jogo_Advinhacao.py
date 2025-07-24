import random, time
lista = [
    "limão", "carro", "roupa", "canal", "mudar", "nuvem", "pazez", "jogar",
    "neves", "livro", "folha", "sorte", "andar", "fruta", "cinto", "pular",
    "velho", "banco", "janes", "rádio", "festa", "matar", "troca", "vazio",
    "corpo", "nadar", "risco", "perda", "sinal", "campo", "linha", "trigo",
    "cofre", "casar", "chuva", "vinho", "pedra", "verde", "morro", "norte",
    "sulco", "dente", "vapor", "fraco", "ruído", "feira", "magia", "verão",
    "coisa", "tempo"
]

print("Bem-vindo ao jogo de adivinhação de palavras!")
time.sleep(1.5)
print("Tente descobrir a palavra secreta de 5 letras.")
time.sleep(1.5)
print("Você terá 6 tentativas.")
time.sleep(1.5)
print("As letras aparecerão coloridas para te ajudar:")
time.sleep(1.5)
print("\033[32mVerde\033[m: letra correta no lugar certo")
time.sleep(1.5)
print("\033[33mAmarelo\033[m: letra correta no lugar errado")
time.sleep(1.5)
print("\033[31mVermelho\033[m: letra que não existe na palavra")
time.sleep(1.5)
print("-="*20)


while True:   
    palavra_aleatoria = random.choice(lista)  
    tentativas = 6
    while tentativas > 0:
        if tentativas > 1:
            print(f"Você tem {tentativas} tentativas")
        else:
            print(f"Você tem {tentativas} tentativa")
        advinha = input('Tente advinhar a palavra que estou pensando: ').lower().strip()
        
        if len(advinha) != len(palavra_aleatoria):
            print(f'por favor digite uma palavra com {len(palavra_aleatoria)} letras')
            continue
        if advinha == palavra_aleatoria:
                print(f'\033[32m{palavra_aleatoria}\033[m')
                print('\033[32mParabéns\033[m! Você acertou a palavra')
                break
        for indice, letra in enumerate(advinha):
            
            if letra == palavra_aleatoria[indice]:
                print(f'\033[32m{letra}\033[m', end=' ') #Se a letra estiver certa aparece verde
                time.sleep(.2)
            elif letra in palavra_aleatoria:
                print(f'\033[33m{letra}\033[m', end=' ') # Se tiver a letra mas no lugar errado aparece amarelo
                time.sleep(.2)
            else:
                print(f'\33[31m{letra}\033[m', end=' ') # Se não t iver a letra aparece vermelho
                time.sleep(.2)
        print()
        print('-='*10)
        tentativas -= 1
    if tentativas == 0:
        print(f'\n\033[31mVocê perdeu!\033[m A palavra era: {palavra_aleatoria}')
    resp = input('Deseja continuar?  [S/N]').lower()[0]
    if resp == 'n':
        break
print('Obrigado por jogar!')
