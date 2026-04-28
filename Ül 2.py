import pygame
import sys

# Algseadistus
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ülesanne 2")

# Piltide lisamine
bg = pygame.image.load("bg_shop.jpg")
seller = pygame.image.load("seller.png")
chat = pygame.image.load("chat.png")

# Poemüüa suurus
seller = pygame.transform.scale(seller, (225, 300))

# Font ja teksti sätted
font = pygame.font.SysFont("comicsansms", 28)
text = font.render("Mariliis Metsjärv", True, (255, 255, 255))

# Jutumulli asukoht
chat_x, chat_y = 275, 30

# Mängutsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Taust
    screen.blit(bg, (0, 0))

    # Poemüüa
    screen.blit(seller, (150,150))

    # Jutumull
    screen.blit(chat, (chat_x, chat_y))

    # Teksti asukoht jutumullis
    text_rect = text.get_rect(center=(chat_x + chat.get_width() // 2,
                                      chat_y + chat.get_height() // 2.5))
    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()