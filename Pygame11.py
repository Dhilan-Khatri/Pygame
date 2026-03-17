import random
import pygame
import math
import array

screenWidth=800
screenHeight=500
playerStartX=370
playerStartY=380
enemyStartYMin=50
enemyStartYMax=150
enemySpeedX=4
enemySpeedY=40
bulletSpeed=10
collsionDistance = 27

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
screen=pygame.display.set_mode((screenWidth,screenHeight))
background=pygame.image.load("background.png")
pygame.display.set_caption("Space Invader")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

def make_sound(frequency, duration):
    sample_rate = 44100
    n_samples = int(sample_rate * duration)
    buf = array.array("h")

    for i in range(n_samples):
        t = i / sample_rate
        buf.append(int(32767 * math.sin(2 * math.pi * frequency * t)))

    return pygame.mixer.Sound(buffer=buf)

laserSound = make_sound(800, 0.1)       
explosionSound = make_sound(200, 0.2)   


playerImage=pygame.image.load("player.png")
playerX=playerStartX
playerY=playerStartY
playerXChange=0

enemyImage=[]
enemyX=[]
enemyY=[]
enemyXChange=[]
enemyYChange=[]
enemyNumber=7
for i in range(enemyNumber):
    enemyImage.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,screenWidth-64))
    enemyY.append(random.randint(enemyStartYMin,enemyStartYMax))
    enemyXChange.append(enemySpeedX)
    enemyYChange.append(enemySpeedY)

bulletImage=pygame.image.load("bullet.png")
bulletX=0
bulletY=playerStartY
bulletXChange=0
bulletYChange=bulletSpeed
bulletState="Ready"

scoreValue=0
font=pygame.font.Font("freesansbold.ttf", 32)
txtY=10
txtX=10
gameoveFont=pygame.font.Font("freesansbold.ttf", 64)

def showScore(x,y):
    score=font.render("score:"+str(scoreValue), True, pygame.Color("white"))
    screen.blit(score,(x,y))
def gameoverText():
    score=gameoveFont.render("Gameover", True, pygame.Color("white"))
    screen.blit (score, (200,250))
def player(x,y):
    screen.blit(playerImage,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImage[i], (x,y))
def fireBullet(x,y):
    global bulletState
    bulletState="Fire"
    screen.blit(bulletImage,(x+16,y+10))
def bulletColison(enemyX, enemyY, bulletX, bulletY):
    enemy_center_x = enemyX + 32
    enemy_center_y = enemyY + 32
    bullet_center_x = bulletX
    bullet_center_y = bulletY
    distance = math.sqrt(
        (enemy_center_x - bullet_center_x) ** 2 +
        (enemy_center_y - bullet_center_y) ** 2)
    return distance < collsionDistance


running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerXChange=-5
            if event.key==pygame.K_RIGHT:
                playerXChange=5
            if event.key == pygame.K_SPACE and bulletState == "Ready":
                bulletX = playerX
                fireBullet(bulletX, bulletY)
                laserSound.play()
        if event.type==pygame.KEYUP and event.key in[pygame.K_LEFT,pygame.K_RIGHT]:
            playerXChange=0
    playerX+=playerXChange
    playerX=max(0,min(playerX,screenWidth-64))
    for i in range(enemyNumber):
        if enemyY[i]>340:
            for j in range(enemyNumber):
                enemyY[j]=2000
            gameoverText()
            break
        enemyX[i]+=enemyXChange[i]
        if enemyX[i]<=0 or enemyX[i]>= screenWidth-64:
            enemyXChange[i]*=-1
            enemyY[i]+=enemyYChange[i]
        if bulletColison(enemyX[i], enemyY[i], bulletX + 16, bulletY + 10):
            bulletY = playerStartY
            bulletState = "Ready"
            scoreValue += 1
            enemyX[i] = random.randint(0, screenWidth - 64)
            enemyY[i] = random.randint(enemyStartYMin, enemyStartYMax)
            explosionSound.play()

        enemy(enemyX[i], enemyY[i], i)
    if bulletY<=0: 
        bulletY=playerStartY
        bulletState="Ready"
    elif bulletState=="Fire":
        fireBullet(bulletX, bulletY)
        bulletY-=bulletYChange
    player(playerX,playerY)
    showScore(txtX,txtY)
    pygame.display.update()