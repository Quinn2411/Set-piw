import os
import pygame

pygame.init()

# setting up the window 
SCREEN_WIDTH = 880
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SET')
sourceFileDir = os.path.dirname(os.path.abspath(__file__))
iconPath = os.path.join(sourceFileDir, 'cards/greenovalshaded3.gif')
icon = pygame.image.load(iconPath) 
pygame.display.set_icon(icon)

# setting up the elements of the screen
font=pygame.font.Font(None,35)
titlefont=pygame.font.Font(None,150)
user_input=""
textbox=pygame.Rect(450,700,140,40)
textbox_colour=((0,0,0))

# card slots
from PlayingClasses import Table,cards,Deck
Mytable=Table()
Mydeck=Deck()

Table.newgame(Mytable,Mydeck)
kaart=Mytable._table[0]
print(type(kaart))
testkaart=cards("1","squiggle","filled","red")

class visualcards(pygame.sprite.Sprite):
    def __init__(self,cardindexontable,card):
        super().__init__()
        self.image=pygame.image.load('finalproject/cards/'+str(card._colour+card._symbol+card._shading+card._number)+'.gif').convert_alpha()
        if cardindexontable<7:
            yposition=275
            xposition=int(20+120*cardindexontable)
        if cardindexontable>=7:
            yposition=495
            xposition=int(140+120*(cardindexontable%7))
        self.rect=self.image.get_rect(center=(xposition,yposition))

def refreshVisualCards():
    for index in range(0,12):
        cards.add(visualcards(index + 1,Mytable._table[index]))
refreshVisualCards()

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
                if event.key==pygame.K_RETURN:
                    attempt=user_input
                    user_input=""
                    print(attempt)
                else:
                    user_input+=event.unicode

    # setting up the background
    gamemessage=''
    screen.fill((0, 150, 0))
    title_text=titlefont.render('SET', True,(255,255,255))
    screen.blit(title_text,(440-((title_text.get_width())/2),50))
    message_text=font.render(gamemessage, True,(255,255,255))

    # setting up the textbox with the text
    pygame.draw.rect(screen,textbox_colour,textbox,2,3)
    text_surface=font.render(user_input,True,(255,255,255))
    screen.blit(text_surface,(textbox.x+6,textbox.y+7))
    textbox.w=text_surface.get_width()+11
    textbox.x=450-(textbox.w/2)

    # showing the points of poth computer and player
    visualpointsplayer='2'
    visualpointscomputer='5'
    text_surface=font.render('Player: '+visualpointsplayer+' points',True,(255,255,255))
    screen.blit(text_surface,(670,700))
    text_surface=font.render('Computer: '+visualpointscomputer+' points',True,(255,255,255))
    screen.blit(text_surface,(20,700))

    cards.draw(screen)

    pygame.display.update()
