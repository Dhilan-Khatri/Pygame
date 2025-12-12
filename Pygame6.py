import pygame
import random
pygame.init()

sprite_Color_Change=pygame.USEREVENT+1
background_Color_Change=pygame.USEREVENT+2

blue=pygame.Color("blue")
red=pygame.Color("red")
yellow=pygame.Color("yellow")
green=pygame.Color("green")
orange=pygame.Color("orange")
purple=pygame.Color("purple")
pink=pygame.Color("pink")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image=pygame.Surface([width, height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]), random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundryhit=False
        if self.rect.left<=0 or self.rect.right>=500:
            self.velocity[0]=-self.velocity[0]
            boundryhit=True
        if self.rect.top<=0 or self.rect.bottom>=400:
            self.velocity[1]=-self.velocity[1]
            boundryhit=True
        if boundryhit:
            pygame.event.post(pygame.event.Event(sprite_Color_Change))
            pygame.event.post(pygame.event.Event(background_Color_Change))
    def changeColor(self):
        self.image.fill(random.choice([red,orange,yellow,green]))
def changeBackgroundColor():
    global bg_Color
    bg_Color=random.choice([blue,purple,pink])
    
all_Sprites_List=pygame.sprite.Group()
spirte1=Sprite(red, 20, 30)
spirte1.rect.x=random.randint(0,480)
spirte1.rect.y=random.randint(0,370)
all_Sprites_List.add(spirte1)
screen=pygame.display.set_mode((500,400))
pygame.display.set_caption("Colorful Bounce")
bg_Color=blue
screen.fill(bg_Color)
exit=True
clock=pygame.time.Clock()
while exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=False
        elif event.type==sprite_Color_Change:
            spirte1.changeColor()
        elif event.type==background_Color_Change:
            changeBackgroundColor()
    all_Sprites_List.update()
    screen.fill(bg_Color)
    all_Sprites_List.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()