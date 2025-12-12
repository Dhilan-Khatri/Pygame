import pygame
import random
screenwidth,screenheight=500,400
movementspeed=5
fontsize=72

pygame.init()
backgroundimage=pygame.transform.scale(pygame.image.load("bg.jpg"),(screenwidth, screenheight))
font=pygame.font.SysFont("Times New Roman", fontsize)

sprite_Color_Change=pygame.USEREVENT+1
blue=pygame.Color("blue")
red=pygame.Color("red")
yellow=pygame.Color("yellow")
green=pygame.Color("green")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, xchange, ychange):
        old_x, old_y = self.rect.x, self.rect.y 
        self.rect.x = max(min(self.rect.x + xchange, screenwidth - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + ychange, screenheight - self.rect.height), 0)
        if (self.rect.x == 0 or 
            self.rect.x == screenwidth - self.rect.width or 
            self.rect.y == 0 or 
            self.rect.y == screenheight - self.rect.height):
            self.changeColor()

    def changeColor(self):
        self.image.fill(random.choice([red, blue, yellow, green]))


screen=pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Sprite Collison")

allSprites=pygame.sprite.Group()

sprite1=Sprite(pygame.Color("Black"), 20,30)
sprite1.rect.x,sprite1.rect.y=random.randint(0,screenwidth-sprite1.rect.width), random.randint(0,screenheight-sprite1.rect.height)
allSprites.add(sprite1)
sprite2=Sprite(pygame.Color("Red"), 20,30)
sprite2.rect.x,sprite2.rect.y=random.randint(0,screenwidth-sprite2.rect.width), random.randint(0,screenheight-sprite2.rect.height)
allSprites.add(sprite2)

running,won=True,False
clock=pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    if not won:
        keys=pygame.key.get_pressed()
        xchange=(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*movementspeed
        ychange=(keys[pygame.K_DOWN]-keys[pygame.K_UP])*movementspeed
        sprite1.move(xchange,ychange)
        if sprite1.rect.colliderect(sprite2.rect):
            allSprites.remove(sprite2)
            won=True
    screen.blit(backgroundimage,(0,0))
    allSprites.draw(screen)
    if won:
        wintext=font.render("You Win", True, pygame.Color("Black"))
        screen.blit(wintext,((screenwidth-wintext.get_width())//2,(screenheight-wintext.get_height())//2))
    pygame.display.flip()
    clock.tick(90)

pygame.quit()