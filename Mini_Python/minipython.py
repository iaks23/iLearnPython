import pygame 
import random
import time

pygame.init()
window_x = 400
window_y = 400
game_screen = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Mini Python")

x, y = 200, 200
delta_x, delta_y = 10, 0

#initial cordinates of food.
food_x, food_y = random.randrange(0, window_y)//10*10, random.randrange(0, window_x)//10*10

body_list = [(x, y)]

clock = pygame.time.Clock()
game_over = False
font = pygame.font.SysFont("bahnschrift", 25)

def snake():
    global x, y, food_x, food_y, game_over, window_x, window_y
    x = (x + delta_x)%window_x
    y = (y + delta_y)%window_y
    
    
    if((x, y) in body_list):
        game_over = True
        return
    
    body_list.append((x,y))
    
    if(food_x == x and food_y == y):
        while((food_x, food_y) in body_list):
            food_x, food_y = random.randrange(0, window_y)//10*10, random.randrange(0,window_x)//10*10

    else:
        del body_list[0]
    #clear screen after every keyboard move
    game_screen.fill((255,174,185))
    score = font.render("Score: "+str(len(body_list)), True, (154,50,205))
    game_screen.blit(score, [0,0])
    pygame.draw.circle(game_screen, (220,20,60), (food_x, food_y), 5)
    for (i, j) in body_list:
        pygame.draw.rect(game_screen, (154,50,205), [i, j, 10, 10])
    pygame.display.update()

    
level = input("Choose your level: 1. Beginner 2. Intermediate 3. Advanced ")
if(level == '1'):
    speed = 10
elif(level == '2'):
    speed = 13
elif(level == '3'):
    speed = 18
else:
    speed = 10 #default speed
while True:
    if(game_over):
        font = pygame.font.SysFont("bahnschrift", 40)
        game_screen.fill((255,174,185))
        score = font.render("Score: "+str(len(body_list)), True, (0,0,0,0))
        game_screen.blit(score, [0,0])
        msg = font.render("GAME OVER :( !", True, (0,0,0,0))
        game_screen.blit(msg, [window_x//3, window_y//3])
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
        quit()
    events = pygame.event.get()
    for event in events:
        if(event.type == pygame.QUIT):
            pygame.quit()
            quit()
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):
                if(delta_x != 10):
                    delta_x = -10
                delta_y = 0
            elif(event.key == pygame.K_RIGHT):
                if(delta_x != -10):
                    delta_x = 10
                delta_y = 0
            elif(event.key == pygame.K_UP):
                if(delta_y != 10):
                    delta_y = -10
                delta_x = 0
            elif(event.key == pygame.K_DOWN):
                if(delta_y != -10):
                    delta_y = 10
                delta_x = 0
            else:
                continue
            snake() 
    if(not events):
        snake()
    clock.tick(speed) # difficulty rate is set here (10,15,20)