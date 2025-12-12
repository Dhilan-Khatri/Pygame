import pygame 
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Color Changing Rectangle")

colors={
    "white":pygame.Color("white"),
    "red":pygame.Color("red"),
    "orange":pygame.Color("orange"),
    "yellow":pygame.Color("yellow"),
    "green":pygame.Color("green")
}
currentColor=colors["white"]
x,y=30,30
spritewidth, spriteheight=60,60
clock=pygame.time.Clock()

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        x-=3
    if pressed[pygame.K_RIGHT]:
        x+=3
    if pressed[pygame.K_UP]:
        y-=3
    if pressed[pygame.K_DOWN]:
        y+=3
    x=min(max(0,x), 500-spritewidth)
    y=min(max(0,y), 500-spriteheight)
    if x==0:
        currentColor=colors["red"]
    elif x==500-spritewidth:
        currentColor=colors["orange"]
    elif y==0:
        currentColor=colors["yellow"]
    elif y==500-spriteheight:
        currentColor=colors["green"]
    else:
        currentColor=colors["white"]
    screen.fill((100,100,100))

    pygame.draw.rect(screen, currentColor, pygame.Rect(x, y, spritewidth, spriteheight))
    pygame.display.flip()
    clock.tick(90)
pygame.quit()