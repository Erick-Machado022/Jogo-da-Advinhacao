import random
lista = ["mundo", "praia", "festa", "docei", "limao", "fruta", "manga", "fogao", "noite", "sonho", "campo", "grama", "vidro", "aluno", "tampa", "caixa", "livro", "chave", "tempo", "pedra", "cobra", "risco", "copos", "barca", "aneis"
]

palavra_aleatoria = random.choice(lista)
tentativas = 6
while tentativas > 0:
    print(f"Você tem {tentativas} tentativas")
    advinha = input('Tente advinhar a palavra que estou pensando: ').lower().strip()
    
    if len(advinha) != len(palavra_aleatoria):
        print(f'por favor digite uma palavra com {len(palavra_aleatoria)} letras')
        continue
    if advinha == palavra_aleatoria:
            print('Parabéns! Você acertou a palavra')
            break

