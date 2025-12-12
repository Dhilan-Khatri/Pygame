import pygame
import random
pygame.init()
sprite_Color_Change = pygame.USEREVENT + 1
background_Color_Change = pygame.USEREVENT + 2

blue = pygame.Color("blue")
red = pygame.Color("red")
yellow = pygame.Color("yellow")
green = pygame.Color("green")
orange = pygame.Color("orange")
purple = pygame.Color("purple")
pink = pygame.Color("pink")
white = pygame.Color("white")

colors = {
    "white": white,
    "red": red,
    "orange": orange,
    "yellow": yellow,
    "green": green
}

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-2, 2]), random.choice([-2, 2])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False

        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 500:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(sprite_Color_Change))
            pygame.event.post(pygame.event.Event(background_Color_Change))

    def changeColor(self):
        self.image.fill(random.choice([red, orange, yellow, green]))
def changeBackgroundColor():
    global bg_Color
    bg_Color = random.choice([blue, purple, pink])


all_Sprites = pygame.sprite.Group()
sprite1 = Sprite(red, 20, 30)
sprite1.rect.x = random.randint(0, 480)
sprite1.rect.y = random.randint(0, 480)
all_Sprites.add(sprite1)
x, y = 30, 30
sprite_width, sprite_height = 60, 60
currentColor = white

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("More Sprites")
bg_Color = blue
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == sprite_Color_Change:
            sprite1.changeColor()

        elif event.type == background_Color_Change:
            changeBackgroundColor()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        x -= 3
    if pressed[pygame.K_RIGHT]:
        x += 3
    if pressed[pygame.K_UP]:
        y -= 3
    if pressed[pygame.K_DOWN]:
        y += 3
    x = max(0, min(x, 500 - sprite_width))
    y = max(0, min(y, 500 - sprite_height))
    if x == 0:
        currentColor = colors["red"]
    elif x == 500 - sprite_width:
        currentColor = colors["orange"]
    elif y == 0:
        currentColor = colors["yellow"]
    elif y == 500 - sprite_height:
        currentColor = colors["green"]
    else:
        currentColor = colors["white"]
    all_Sprites.update()
    screen.fill(bg_Color)
    all_Sprites.draw(screen)
    pygame.draw.rect(screen, currentColor, pygame.Rect(x, y, sprite_width, sprite_height))

    pygame.display.flip()
    clock.tick(90)

pygame.quit()
