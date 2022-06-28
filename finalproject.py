import pygame
from random import randint
pygame.init()
disw = 1200
dish = 720
screen= pygame.display.set_mode([disw,dish])
clock = pygame.time.Clock()
mouse_down = False
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
keep_true = True
key_down = False
playerx = disw/2
font = pygame.font.Font('freesansbold.ttf', 32)
boxes = []
coins = []
score = 0
dif = 3.0
class Faller:
    def __init__(self,color,speed,y):
        self.color = color
        self.speed = speed
        self.y = y
        fall = pygame.Rect((randint(0,disw - 50),self.y),(50,50))
        if len(boxes) < 1 + score:
            box = fall.copy()
            boxes.append(box)
        
class Coin:
    def __init__(self,color,speed,y):
        self.color = color
        self.speed = speed
        self.y = y
        coinR = pygame.Rect((randint(0,disw - 50),self.y),(50,50))
        if len(coins) < 3:
            coin = coinR.copy()
            coins.append(coin)
while keep_true:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_true = False
        if event.type == pygame.KEYDOWN:
            key_down = True
        if event.type == pygame.KEYUP:    
            key_down = False
    if key_down:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx -= 2.5
            if event.key == pygame.K_RIGHT:
                playerx += 2.5
        pygame.draw.rect(screen,red,playerRect) 
    ground = pygame.Rect(0,dish - 100,disw,100)
    screen.fill(blue)
    text = font.render('Score: ' + str(score * 100), True, green, blue)
    textRect = text.get_rect()
    screen.blit(text, textRect)
    pygame.draw.rect(screen,green,ground)
    playerRect = pygame.Rect(playerx, dish-150,50,50)
    pygame.draw.rect(screen,red,playerRect)
    for box in boxes:
      pygame.draw.rect(screen,red,box)
      if box.y < dish-150:
          box.y += dif
      else:
          boxes.remove(box)
      if pygame.Rect.colliderect(playerRect,box):
        print("                    You Lose!")
        print("                    Score = " + str(score * 100))
        f = open("scores.txt", "r")
        content = f.read()
        scores = content.splitlines()
        sco = []
        for scoo in scores:
            sc = scoo.split(': ')
            sco.append(sc)
        scor = {}
        for x in range(0,len(sco)):
            scor[sco[x][0]] = int(sco[x][1])
        sorted_tuples = sorted(scor.items(), key=lambda item: item[1])
        sorted_dict = {k: v for k, v in sorted_tuples}
        print(list(sorted_dict.items())[-1])
        print(list(sorted_dict.items())[-2])
        print(list(sorted_dict.items())[-3])
        keep_true = False
        break
    for coin in coins:
        pygame.draw.rect(screen,yellow,coin)
        if coin.y < dish-150:
            coin.y += dif
        else:
          coins.remove(coin)
        if pygame.Rect.colliderect(playerRect,coin):
            score += 1
            coins.remove(coin)
        
    f = Faller(red,5,0)
    c = Coin(yellow,5,0)
    dif = 3.0 + score / 10
    pygame.display.update()
    clock.tick(90)
name = input("Name:")
sw = name + ": " + str(score * 100)
with open('scores.txt', 'a') as file:
    file.write(sw)
pygame.quit()