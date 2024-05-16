import pygame
import random

# Define algumas constantes
LARGURA, ALTURA = 800, 600
TAMANHO_BLOCO = 30

# Define as formas dos blocos
FORMAS = [
    # A forma T
    [
        [1, 1, 1],
        [0, 1, 0]
    ],
    # A forma I
    [
        [1, 1, 1, 1]
    ],
    # A forma O
    [
        [1, 1],
        [1, 1]
    ],
    # A forma L
    [
        [1, 1, 1],
        [1, 0, 0]
    ],
    # A forma J
    [
        [1, 1, 1],
        [0, 0, 1]
    ],
    # A forma S
    [
        [0, 1, 1],
        [1, 1, 0]
    ],
    # A forma Z
    [
        [1, 1, 0],
        [0, 1, 1]
    ]
]

# Define as cores
CORES = [
    (255, 0, 0),    # Vermelho
    (0, 255, 0),    # Verde
    (0, 0, 255),    # Azul
    (255, 255, 0),  # Amarelo
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Ciano
    (128, 128, 128) # Cinza
]

class Bloco:
    def __init__(self, forma, x, y):
        self.forma = forma
        self.x = x
        self.y = y

    def desenhar(self, tela):
        for i, linha in enumerate(self.forma):
            for j, celula in enumerate(linha):
                if celula:
                    pygame.draw.rect(tela, CORES[self.forma.index(linha)], pygame.Rect(self.x + j * TAMANHO_BLOCO, self.y + i * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO))

def verificar_colisao(bloco, matriz):
    for i, linha in enumerate(bloco.forma):
        for j, celula in enumerate(linha):
            if celula and matriz[bloco.y // TAMANHO_BLOCO + 1][bloco.x // TAMANHO_BLOCO + j]:
                return True
    return False

def main():
    pygame.init()

    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Tetris")

    relogio = pygame.time.Clock()

    bloco = Bloco(random.choice(FORMAS), LARGURA // 2, 0)

    matriz = [[0 for _ in range(LARGURA // TAMANHO_BLOCO)] for _ in range(ALTURA // TAMANHO_BLOCO)]

    jogo_acabou = False

    while not jogo_acabou:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    bloco.x -= TAMANHO_BLOCO
                    if bloco.x < 0:
                        bloco.x = 0
                if evento.key == pygame.K_RIGHT:
                    bloco.x += TAMANHO_BLOCO
                    if bloco.x + len(bloco.forma[0]) * TAMANHO_BLOCO > LARGURA:
                        bloco.x -= TAMANHO_BLOCO
                if evento.key == pygame.K_DOWN:
                    bloco.y += TAMANHO_BLOCO
                    if bloco.y + len(bloco.forma) * TAMANHO_BLOCO > ALTURA:
                        bloco.y -= TAMANHO_BLOCO
                if evento.key == pygame.K_UP:
                    bloco.forma = [list(linha[::-1]) for linha in bloco.forma]

        if bloco.y + len(bloco.forma) * TAMANHO_BLOCO > ALTURA:
            bloco.y -= 1

        tela.fill((0, 0, 0))
        bloco.desenhar(tela)
        pygame.display.flip()
        relogio.tick(60)

        if bloco.y + len(bloco.forma) * TAMANHO_BLOCO == ALTURA:
            bloco = Bloco(random.choice(FORMAS), LARGURA // 2, 0)
            bloco.y -= 1

        for i, linha in enumerate(bloco.forma):
            for j, celula in enumerate(linha):
                if celula and bloco.y + i * TAMANHO_BLOCO + TAMANHO_BLOCO >= ALTURA:
                    bloco.forma[i][j] = 0

        if verificar_colisao(bloco, matriz):
            jogo_acabou = True

        for y, linha in enumerate(matriz):
            if 0 not in linha:
                matriz = [linha[:i] + [0] + linha[i + 1:] for i, celula in enumerate(linha) if celula == 0]

    pygame.quit()

if __name__ == "__main__":
    main()
