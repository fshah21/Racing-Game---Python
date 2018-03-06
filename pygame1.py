import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0 ,255,0)
car_width = 73
gameDisplay = pygame.display.set_mode((display_width , display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')

def things_dodged(count):
    font = pygame.font.SysFont(None , 25)
    text = font.render("Dodged: "+str(count) , True , black)
    gameDisplay.blit(text , (0,0))

def things(thingx , thingy , thingw , thingh , color):
    pygame.draw.rect(gameDisplay , color , [thingx , thingy , thingw , thingh])    

def car(x,y):
    gameDisplay.blit(carImg , (x,y))

def message_display(text):
    largeText = pygame.font.SysFont('comicsansms', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def text_objects(text , font):
    textSurface = font.render(text , True , black)
    return textSurface, textSurface.get_rect()


def crash():
    message_display('You Crashed')

def button(msg , x , y ,w, h ,i ,a, action = None ):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay , a , (x,y,w,h))
        if click[0] == 1 and action!= None:
            action()
    else:
        pygame.draw.rect(gameDisplay , i , (x,y,w,h))
        
    smallText = pygame.font.SysFont('comicsansms', 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ( (x+(w/2)) , (y + (h/2)))
    gameDisplay.blit(TextSurf,TextRect)

def quitgame():
    pygame.quit()
    quit()

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont('comicsansms', 115)
        TextSurf, TextRect = text_objects('A Bit Racey', largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        button('GO !' , 150 , 450 ,100, 50 ,green, bright_green,game_loop)
        button('QUIT !' , 550 , 450 ,100, 50 ,red, bright_red,quitgame )
        pygame.display.update()
        clock.tick(30)
    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    
    thing_startx1 = random.randrange(0 , display_width)
    
    thing_startx2 = random.randrange(0 , display_width)
    thing_starty1 = -600
    thing_starty2 = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    dodged = 0
    
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            

        x += x_change
        gameDisplay.fill(white)

       
        things(thing_startx1 , thing_starty1 , thing_width, thing_height , red)
        
       
        thing_starty1 += thing_speed
        
        things(thing_startx2 , thing_starty2 , thing_width, thing_height , black)
        
        thing_starty2 += thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty1 > display_height or thing_starty2 > display_height:
            thing_starty1 = 0 - thing_height
            thing_starty2 = 0 - thing_height
            thing_startx1 = random.randrange(0 , display_width)
            thing_startx2 = random.randrange(0 , display_width)
            while abs(thing_startx2 - thing_startx1) < car_width:
                thing_startx2 = random.randrange(0 , display_width)
            dodged += 1
            thing_speed += 1

        if y < thing_starty1 + thing_height or y < thing_starty2 + thing_height:
            if x > thing_startx1 and x < thing_startx1 + thing_width or x + car_width > thing_startx1 and x + car_width < thing_startx1 + thing_width:
                crash()
            if x > thing_startx2 and x < thing_startx2 + thing_width or x + car_width > thing_startx2 and x + car_width < thing_startx2 + thing_width:
                crash()
        
        pygame.display.update()
        clock.tick(60)
        
game_intro()
game_loop()
pygame.quit()
quit()
