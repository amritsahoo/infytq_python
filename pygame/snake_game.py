'''
Created on Jun 1, 2020

@author: amrit
'''
import pygame
import random
x=pygame.init()
#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,255,0)
#Creating game Window
screen_length=600
screen_width=400
gameWindow=pygame.display.set_mode((screen_length,screen_width))
pygame.display.set_caption("AMRIT'S Snake Game")
#Creating game Specific variable
exit_game=False
game_over=False
score=0
snake_x=45
snake_y=55
food_x=random.randint(2,screen_length-2)
food_y = random.randint(2,screen_width-2)
velocity_x=0
velocity_y=0
init_velocity=5
snake_size=10
fps=30
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,50)
snake_list=[]
snake_length=1
def text_score(text,colour,x,y):
    screen_text=font.render(text, True, colour)
    gameWindow.blit(screen_text,[x,y])
def plot_snake(gameWindow,colour,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, colour, [x,y, snake_size, snake_size])
#Creating game loop
while not exit_game:
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            exit_game=True
        if(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_RIGHT):
                velocity_x=init_velocity
                velocity_y=0
            if(event.key==pygame.K_LEFT):
                velocity_x=-init_velocity
                velocity_y=0
            if(event.key==pygame.K_UP):
                velocity_y=-init_velocity
                velocity_x=0
            if(event.key==pygame.K_DOWN):
                velocity_y=init_velocity
                velocity_x=0
    snake_x+=velocity_x
    snake_y+=velocity_y

    if(abs(snake_x-food_x)<6 and abs(snake_y - food_y)<6):
        score+=10
        food_x = random.randint(2, screen_length - 2)
        food_y = random.randint(2, screen_width - 2)
        snake_length+=5
    if(snake_x not in range(screen_length) or snake_y not in range(screen_width)):
        print("Game Over")
        print("Your Score is : ",score)
        exit_game=True
    head=[]
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)
    if(len(snake_list)>snake_length):
        del snake_list[0]
    gameWindow.fill(white)
    text_score("Score : "+str(score), green, 5, 5)
    pygame.draw.rect(gameWindow, red,[food_x,food_y,snake_size,snake_size])
    #pygame.draw.rect(gameWindow, black,[snake_x,snake_y,snake_size,snake_size])
    plot_snake(gameWindow,black,snake_list,snake_size)
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()