import os
import pygame
# card slots
from PlayingClasses import Table,cards,Deck
from Check_Set import check_set,checkelement
from FINDONESET import findoneset
pygame.init()
attempt=None

# setting up the window
screeninfo = pygame.display.Info()
# screen width and height to use instead of our original width and height, in case the game doesn't fit on your screen:
# SCREEN_WIDTH = screeninfo.current_w
# SCREEN_HEIGHT = screeninfo.current_h
SCREEN_WIDTH = 880
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SET')
pygame.display.set_icon(pygame.image.load('FINALPROJECT/Cards/greenovalfilled3.gif'))

# setting up the elements of the screen
font=pygame.font.Font(None,35)
titlefont=pygame.font.Font(None,150)
user_input=""
textbox=pygame.Rect(450,700,140,40)
textbox_colour=((0,0,0))

displayed_message = ""
isMessageDisplayed = False
DISPLAY_MESSAGE_EVENT = pygame.USEREVENT + 1
REMOVE_MESSAGE_EVENT = pygame.USEREVENT + 2

Mytable=Table()

Mydeck=Deck()
Mydeck.shuffle()
Table.newgame(Mytable,Mydeck)

# card visualisation
class visualcards(pygame.sprite.Sprite):
    def __init__(self,cardindexontable,card):
        super().__init__()
        self.image=pygame.image.load('FINALPROJECT/Cards/'+str(card._colour+card._symbol+card._shading+card._number)+'.gif').convert_alpha()
        if cardindexontable<7:
            yposition=275
            xposition=int(20+120*cardindexontable)
        if cardindexontable>=7:
            yposition=495
            xposition=int(140+120*(cardindexontable%7))
        self.rect=self.image.get_rect(center=(xposition,yposition))
cards=pygame.sprite.Group()
def refreshVisualCards():
    for index in range(0,12):
        cards.add(visualcards(index + 1,Mytable._table[index]))
refreshVisualCards()
def main(deck, table,index1,index2,index3):
        def inputforcards(tableyourusing):
            card1 = tableyourusing._table[int(index1)-1]
            card2=tableyourusing._table[int(index2)-1]
            card3=tableyourusing._table[int(index3)-1]
            return card1,card2,card3
        cardv1,cardv2,cardv3=inputforcards(Mytable)
        def whogetsapoint(deck, table, card1, card2, card3):
            if check_set(cardv1,cardv2,cardv3)==True:
                messageforplayer="Congrats, that's a set! You got a point:"
                k=[index1,index2,index3]
                setthattheplayerfound=" ".join(str(e)for e in k)
                Mytable.setisfound(Mydeck,k[0],k[1],k[2])
                return True,messageforplayer,setthattheplayerfound
            else:
                if findoneset(Mytable) != None:
                    messageforplayer='The computer found a set, so the computer got a point:'
                    k=findoneset(Mytable)
                    Mytable.setisfound(Mydeck,k[0],k[1],k[2])
                    setthatthecomputerfound=" ".join(str(e)for e in k)
                    return False,messageforplayer,setthatthecomputerfound
                else: 
                    messageforplayer="There was no set, we are going to get new cards on the table"
                    Mytable.setisnotfound(Mydeck)   
                    return Mytable,messageforplayer,"Three new cards"
        updatedtable = [whogetsapoint(Mydeck, Mytable, cardv1, cardv2, cardv3)[1],whogetsapoint(Mydeck, Mytable, cardv1, cardv2, cardv3)[2]]
        hetverhaal=" ".join(str(e)for e in updatedtable)
        return hetverhaal
def setisnotfound(self,other):
      for i in range(0,3):
       cards.remove(visualcards( 1,Mytable._table[0]))
       Mytable._table.pop(0)
      for i in range(0,3):
        Table.fill(self,other)
        cards.add(visualcards(i+1),Mytable._table(i))
def setisfound(self,other,other1,other2,other3):
      cards.remove(other1,Mytable._table[other1-1])
      cards.remove(other2,Mytable._table[other2-1])
      cards.remove(other3,Mytable._table[other3-1])

      self._table.pop(int(other1)-1)
      self._table.pop(int(other2)-2)
      self._table.pop(int(other3)-3)
      for i in range(0,3):
         Table.fill(self,other)
      return self._table

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
                    attempt=user_input.split(",")
                    user_input=""
                    print()
                    displayed_message = main(Mydeck, Mytable, attempt[0], attempt[1], attempt[2])
                    refreshVisualCards()
                    pygame.event.post(pygame.event.Event(DISPLAY_MESSAGE_EVENT))
                    refreshVisualCards()
                else:
                    user_input+=event.unicode
        if event.type == DISPLAY_MESSAGE_EVENT:
            isMessageDisplayed = True
            pygame.time.set_timer(pygame.event.Event(REMOVE_MESSAGE_EVENT), 3000)
        if event.type == REMOVE_MESSAGE_EVENT:
            isMessageDisplayed = False

    # setting up the background
    screen.fill((0, 150, 0))
    title_text=titlefont.render('SET', True,(255,255,255))
    screen.blit(title_text,(440-((title_text.get_width())/2),35))
    if (isMessageDisplayed):
        message_text=font.render(displayed_message, True,(255,255,255))
        screen.blit(message_text, (SCREEN_WIDTH / 2 - message_text.get_width()/2, SCREEN_HEIGHT/5*4.3))

    # setting up the textbox with the text
    pygame.draw.rect(screen,textbox_colour,textbox,2,3)
    text_surface=font.render(user_input,True,(255,255,255))
    screen.blit(text_surface,(textbox.x+6,textbox.y+7))
    textbox.w=text_surface.get_width()+11
    textbox.x=450-(textbox.w/2)

    # card numbering
    cardnumber1=font.render('1', True, (255,255,255))
    screen.blit(cardnumber1,(135,150))
    cardnumber2=font.render('2', True, (255,255,255))
    screen.blit(cardnumber2,(255,150))
    cardnumber3=font.render('3', True, (255,255,255))
    screen.blit(cardnumber3,(375,150))
    cardnumber4=font.render('4', True, (255,255,255))
    screen.blit(cardnumber4,(495,150))
    cardnumber5=font.render('5', True, (255,255,255))
    screen.blit(cardnumber5,(615,150))
    cardnumber6=font.render('6', True, (255,255,255))
    screen.blit(cardnumber6,(735,150))
    cardnumber7=font.render('7', True,(255,255,255))
    screen.blit(cardnumber7,(135,600))
    cardnumber8=font.render('8', True, (255,255,255))
    screen.blit(cardnumber8,(255,600))
    cardnumber9=font.render('9', True, (255,255,255))
    screen.blit(cardnumber9,(375,600))
    cardnumber10=font.render('10', True, (255,255,255))
    screen.blit(cardnumber10,(485,600))
    cardnumber11=font.render('11', True, (255,255,255))
    screen.blit(cardnumber11,(605,600))
    cardnumber12=font.render('12', True, (255,255,255))
    screen.blit(cardnumber12,(725,600))

    # showing the points of poth computer and player
    visualpointsplayer='0'
    visualpointscomputer='0'
    text_surface=font.render('Player: '+visualpointsplayer+' points',True,(255,255,255))
    screen.blit(text_surface,(670,700))
    text_surface=font.render('Computer: '+visualpointscomputer+' points',True,(255,255,255))
    screen.blit(text_surface,(20,700))
    cards.draw(screen)

    pygame.display.update()