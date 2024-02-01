import string
import pygame
# card slots
from models import Table, Card, Deck
from set_logic import check_set, find_one_set

pygame.init()
attempt = None

# setting up the window
screeninfo = pygame.display.Info()
# screen width and height to use instead of our original width and height, in case the game doesn't fit on your screen:
# SCREEN_WIDTH = screeninfo.current_w
# SCREEN_HEIGHT = screeninfo.current_h
SCREEN_WIDTH = 880
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SET')
pygame.display.set_icon(pygame.image.load('Eindproject Wiskunde/Cards/greenovalfilled3.gif'))


# setting up the elements of the screen
font = pygame.font.Font(None, 35)
titlefont = pygame.font.Font(None, 150)
user_input = ""
textbox = pygame.Rect(450, 700, 140, 40)
textbox_colour = ((0, 0, 0))

displayed_message = ""
isMessageDisplayed = False
DISPLAY_MESSAGE_EVENT = pygame.USEREVENT + 1
REMOVE_MESSAGE_EVENT = pygame.USEREVENT + 2

my_deck = Deck()
my_deck.shuffle()

my_table = Table()
Table.new_game(my_table, my_deck)


# card visualisation
class visualcards(pygame.sprite.Sprite):
    def __init__(self, cardindexontable, card):
        super().__init__()
        self.image = pygame.image.load('Eindproject Wiskunde/Cards/' + str(
            card._colour + card._symbol + card._shading + card._number) + '.gif').convert_alpha()
        if cardindexontable < 7:
            yposition = 275
            xposition = int(20 + 120 * cardindexontable)
        if cardindexontable >= 7:
            yposition = 495
            xposition = int(140 + 120 * (cardindexontable % 7))
        self.rect = self.image.get_rect(center=(xposition, yposition))


cards = pygame.sprite.Group()


def refreshVisualCards():
    for index in range(0, 12):
        cards.add(visualcards(index + 1, my_table._table[index]))


refreshVisualCards()


# putting the input in an index to make the code runs smoother and is more userfriendly, and using try to handle incorrect inputs
def get_input_cards(table):
    try:
        index1, index2, index3 = actual_user_input.split(",")
    except KeyboardInterrupt:
        exit()
    except:
        print("invalid input, try again in the form a,b,c")
        return None, None, None

    try:
        card1 = table[int(index1) - 1]
        card2 = table[int(index2) - 1]
        card3 = table[int(index3) - 1]
        return card1, card2, card3
    except:
        print("invalid input, try again in the form a,b,c")
        return None, None, None


player_points = 0
computer_points = 0


def main(deck, table, card1, card2, card3):
    # failsafe in case of incorrect input
    card1, card2, card3 = get_input_cards(my_table)
    player_points = 0
    computer_points = 0
    if card1 == None:
        return my_table

        # checking if the given cards form a set
    if check_set(card1, card2, card3):
        player_points += 1
        print(f"congrats you got a point\n the score is now: computer: {computer_points}, player: {player_points}")
        my_table.remove_set(my_deck, card1, card2, card3)
        return "congrats you found a set and got a point, make another attempt"
    else:
        if find_one_set(my_table) != None:
            computer_points += 1
            print(
                f"the computer found a set, so the computer got a point\n the score is now: computer: {computer_points}, player: {player_points}")
            card1, card2, card3 = find_one_set(my_table)
            print(f"{card1}, {card2}, {card3}")

            my_table.remove_set(my_deck, card1, card2, card3)
            return "Your attempt was not a set so the computer found one"
        # failsafe incase of CAP_Set on table
        else:
            print("there is no set")
            my_table.refresh(my_deck)
            return "There is no set so we reset the deck"
    return my_table


# game loop
run = True
actual_user_input = ""
player_points = 0
computer_points = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # allowing the player to type in the screen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                if event.key == pygame.K_RETURN:
                    actual_user_input = user_input
                    attempt = actual_user_input.split(",")
                    # user_input = ""
                    print(actual_user_input)
                    displayed_message = main(my_deck, my_table, attempt[0], attempt[1], attempt[2])
                    if displayed_message == "congrats you found a set and got a point, make another attempt":
                        player_points += 1
                    if displayed_message == "Your attempt was not a set so the computer found one":
                        computer_points += 1
                    if len(my_deck) == 0:
                        run = False;
                    refreshVisualCards()
                    pygame.event.post(pygame.event.Event(DISPLAY_MESSAGE_EVENT))
                    refreshVisualCards()
                else:
                    user_input += event.unicode
        if event.type == DISPLAY_MESSAGE_EVENT:
            isMessageDisplayed = True
            pygame.time.set_timer(pygame.event.Event(REMOVE_MESSAGE_EVENT), 3000)
        if event.type == REMOVE_MESSAGE_EVENT:
            isMessageDisplayed = False

    # setting up the background
    screen.fill((0, 150, 0))
    title_text = titlefont.render('SET', True, (255, 255, 255))
    screen.blit(title_text, (440 - ((title_text.get_width()) / 2), 35))
    if (isMessageDisplayed):
        message_text = font.render(displayed_message.__repr__(), True, (255, 255, 255))
        screen.blit(message_text, (SCREEN_WIDTH / 2 - message_text.get_width() / 2, SCREEN_HEIGHT / 5 * 4.3))

    # setting up the textbox with the text
    pygame.draw.rect(screen, textbox_colour, textbox, 2, 3)
    text_surface = font.render(user_input, True, (255, 255, 255))
    screen.blit(text_surface, (textbox.x + 6, textbox.y + 7))
    textbox.w = text_surface.get_width() + 11
    textbox.x = 450 - (textbox.w / 2)

    # card numbering
    cardnumber1 = font.render('1', True, (255, 255, 255))
    screen.blit(cardnumber1, (135, 150))
    cardnumber2 = font.render('2', True, (255, 255, 255))
    screen.blit(cardnumber2, (255, 150))
    cardnumber3 = font.render('3', True, (255, 255, 255))
    screen.blit(cardnumber3, (375, 150))
    cardnumber4 = font.render('4', True, (255, 255, 255))
    screen.blit(cardnumber4, (495, 150))
    cardnumber5 = font.render('5', True, (255, 255, 255))
    screen.blit(cardnumber5, (615, 150))
    cardnumber6 = font.render('6', True, (255, 255, 255))
    screen.blit(cardnumber6, (735, 150))
    cardnumber7 = font.render('7', True, (255, 255, 255))
    screen.blit(cardnumber7, (135, 600))
    cardnumber8 = font.render('8', True, (255, 255, 255))
    screen.blit(cardnumber8, (255, 600))
    cardnumber9 = font.render('9', True, (255, 255, 255))
    screen.blit(cardnumber9, (375, 600))
    cardnumber10 = font.render('10', True, (255, 255, 255))
    screen.blit(cardnumber10, (485, 600))
    cardnumber11 = font.render('11', True, (255, 255, 255))
    screen.blit(cardnumber11, (605, 600))
    cardnumber12 = font.render('12', True, (255, 255, 255))
    screen.blit(cardnumber12, (725, 600))

    # showing the points of poth computer and player
    visualpointsplayer = '0'
    visualpointscomputer = '0'
    text_surface = font.render('Player: ' + str(player_points) + ' points', True, (255, 255, 255))
    screen.blit(text_surface, (670, 700))
    text_surface = font.render('Computer: ' + str(computer_points) + ' points', True, (255, 255, 255))
    screen.blit(text_surface, (20, 700))
    cards.draw(screen)

    pygame.display.update()