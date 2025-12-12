from pygame import *
init()
screen=display.set_mode((500,500))

display.set_caption("Adding Image & Background Image")
bg=transform.scale(image.load("images.png").convert(),(500,500))
ci=transform.scale(image.load("down.png").convert_alpha(),(200,200))
ci_rect=ci.get_rect(center=(250,220))
text=font.Font("Major_Mono_Display", 36).render("Hello Words", True, Color("white"))
text_rect=text.get_rect(center=(250,350))
clock=time.Clock()

running=True
while running:
    for e in event.get():
        if e.type==QUIT:
          running=False
    screen.blit(bg,(0,0))
    screen.blit(ci,ci_rect)
    screen.blit(text,text_rect)
    display.flip()
    clock.tick(30)
quit()