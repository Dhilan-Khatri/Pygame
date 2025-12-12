import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My Game screen")

BG_COLOR = (255, 255, 255)
image = pygame.image.load("down.png")
image = pygame.transform.scale(image, (300, 300))
image_rect = image.get_rect(center=(320, 240))
font = pygame.font.Font(None, 40)
text = font.render("first game", True, (0, 0, 0)) 
text_rect = text.get_rect(center=(240, 610))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    screen.fill(BG_COLOR)
    screen.blit(image, image_rect)
    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()