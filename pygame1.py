from pygame import *
init()

screen=display.set_mode((500,500))
running=False
while not running:
    for e in event.get():
        if e.type==QUIT:
            quit()
    display.flip()