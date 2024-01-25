import os
import pygame

pygame.init()

# setting up the window 
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SET')
sourceFileDir = os.path.dirname(os.path.abspath(__file__))
iconPath = os.path.join(sourceFileDir, 'greenovalshaded3.gif')
icon = pygame.image.load(iconPath) 
pygame.display.set_icon(icon)

# setting up the elements of the screen
font=pygame.font.Font(None,35)
user_input=""
textbox=pygame.Rect(450,700,140,40)
textbox_colour=((0,0,0))

# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
        # allowing the player to type in the screen
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_BACKSPACE:
                user_input=user_input[:-1]
            else:
                user_input+=event.unicode

    # setting up the background colour
    screen.fill((0, 150, 0))

    # setting up the textbox with the text
    pygame.draw.rect(screen,textbox_colour,textbox,2,3)
    text_surface=font.render(user_input,True,(255,255,255))
    screen.blit(text_surface,(textbox.x+6,textbox.y+7))
    textbox.w=text_surface.get_width()+11

    pygame.display.update()