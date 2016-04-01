import colorama
init(autoreset=True)


from time import sleep
lines = [[] for i in range(9)]
lines2 = [[] for i in range(6)]
log = [' '*34,' '*34,' '*34,' '*34,' '*34,' '*34,' '*34,' '*34,' '*34]

def reset_printed_cards():
    global lines
    global lines2
    lines = [[] for i in range(9)]
    lines2 = [[] for i in range(6)]

def busted_screen(msg):
    if msg == 'busted':
        for x in range(15):
            print(Back.RED +   ' '*130)
        b = \
            "                                                                                  __    \n" \
            "                                         ,-----.                ,--.             |  |   \n" \
            "                                         |  |) /_ .-,,-, ,---. _|  |_ ,----.  ___|  |   \n" \
            "                                         |  .-.  \| || |(  .-'(_    _)   o__)/  /\  |   \n" \
            "                                         |  '--' /| || | .-' `) |  |  \  `--.\  \/  |   \n" \
            "                                         `------' `----'`----'  `--'   `----' `-----    \n" \
            "                                                                                           "
        print(Fore.RED + b, ' '*50)
        for x in range(15):
            print(Back.RED +   ' '*130)
    elif msg == 'dealing':
        b = \
            "                                                                                                  __            \n" \
            "                     ,----.               ,--.,--.                       ,-----.                 |  |           \n" \
            "                     |     \,----. ,--,--.|  |`--',-,----.  ,-----,     '  .--./,--,--.,--.--.___|  |,---.      \n" \
            "                     |  |) |   o__)  ,-. ||  |,--.|  ,-,  |'  (_)  |    |  |   ' ,-.  ||  .--/  /\  (  .-'      \n" \
            "                     |     /\  `--.  '-' ||  ||  ||  | |  |'.___,  |    '  '--'\ '-'  ||  |  \  \/ .-'  `)      \n" \
            "                     `----'  `----'`--`--'`--'`--'`--' '--',-,__|  |     `-----'`--`--'`--'   `----`----'       \n" \
            "                                                           \______/                                               "
        for x in range(15):
            print(Back.CYAN +   ' '*130)

        print(Fore.CYAN + b, ' '*50)
        for x in range(15):
            print(Back.CYAN +   ' '*130)
#this function fills the lines list with the card graphics, changes size of cards depending on how many cards there are.
def create_card_to_print(suit, rank, dealer_first_card,number_of_cards):
    space = ' '
    if suit.suit == 'Clubs':
        suit = '♧'
    elif suit.suit == 'Diamonds':
        suit = '♢'
    elif suit.suit == 'Hearts':
        suit = '♡'
    elif suit.suit == 'Spades':
        suit = '♤'
    value = rank.value
    rank = rank.rank
    #If there are more than two cards, we use the lines2 list instead of lines1 and make smaller cards to print
    if number_of_cards > 2:
        if rank == '10':
            lines2[0].append('┌──────┐')
            lines2[1].append('│{}  {} │'.format(rank,suit))
            lines2[2].append('│      │')
            lines2[3].append('│      │')
            lines2[4].append('│ {}  {}│'.format(suit,rank))
            lines2[5].append('└──────┘')
        elif rank == 'A' and value == 11:
            lines2[0].append('┌──────┐')
            lines2[1].append('│ {}  {} │'.format(rank,suit))
            lines2[2].append('│      │')
            lines2[3].append('│      │')
            lines2[4].append('│  {}  │'.format(value))
            lines2[5].append('└──────┘')
        elif rank == 'A' and value == 1:
            lines2[0].append('┌──────┐')
            lines2[1].append('│ {}  {} │'.format(rank,suit))
            lines2[2].append('│      │')
            lines2[3].append('│      │')
            lines2[4].append('│  {}   │'.format(value))
            lines2[5].append('└──────┘')
        else:
            lines2[0].append('┌──────┐')
            lines2[1].append('│ {}  {} │'.format(rank,suit))
            lines2[2].append('│      │')
            lines2[3].append('│      │')
            lines2[4].append('│ {}  {} │'.format(suit,rank))
            lines2[5].append('└──────┘')

    if dealer_first_card:
        lines[0].append('┌─────────┐')
        lines[1].append('│▒▒▒▒▒▒▒▒▒│'.format(rank))
        lines[2].append('│▒▒▒▒▒▒▒▒▒│')
        lines[3].append('│▒▒▒▒▒▒▒▒▒│')
        lines[4].append('│▒▒▒▒▒▒▒▒▒│'.format(suit))
        lines[5].append('│▒▒▒▒▒▒▒▒▒│')
        lines[6].append('│▒▒▒▒▒▒▒▒▒│')
        lines[7].append('│▒▒▒▒▒▒▒▒▒│'.format(rank))
        lines[8].append('└─────────┘')

    else:
        if rank == '10':
            lines[0].append('┌─────────┐')
            lines[1].append('│{}       │'.format(rank))
            lines[2].append('│         │')
            lines[3].append('│         │')
            lines[4].append('│    {}    │'.format(suit))
            lines[5].append('│         │')
            lines[6].append('│         │')
            lines[7].append('│       {}│'.format(rank))
            lines[8].append('└─────────┘')


        elif rank == 'A' and value == 1:
            lines[0].append('┌─────────┐')
            lines[1].append('│{}{}       │'.format(rank, space))
            lines[2].append('│    {}    │'.format(value))
            lines[3].append('│         │')
            lines[4].append('│    {}    │'.format(suit))
            lines[5].append('│         │')
            lines[6].append('│    {}    │'.format(value))
            lines[7].append('│       {}{}│'.format(space, rank))
            lines[8].append('└─────────┘')

        elif rank == 'A' and value == 11:
            lines[0].append('┌─────────┐')
            lines[1].append('│{}{}       │'.format(rank, space))
            lines[2].append('│   {}    │'.format(value))
            lines[3].append('│         │')
            lines[4].append('│    {}    │'.format(suit))
            lines[5].append('│         │')
            lines[6].append('│    {}   │'.format(value))
            lines[7].append('│       {}{}│'.format(space, rank))
            lines[8].append('└─────────┘')
        else:
            lines[0].append('┌─────────┐')
            lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
            lines[2].append('│         │')
            lines[3].append('│         │')
            lines[4].append('│    {}    │'.format(suit))
            lines[5].append('│         │')
            lines[6].append('│         │')
            lines[7].append('│       {}{}│'.format(space, rank))
            lines[8].append('└─────────┘')


    return lines
#this updates the log area of the game board
def append_log(log_string):
    global log
    blank_space = False
    while True:
        if len(log_string) < 34:
            log_string += ' '
        else:
            break
    for x in range(len(log)):
        if log[x] == ' '*34:
            log[x] = log_string
            blank_space = True
            break
    if bool(blank_space) == False:
        l = log.pop(0)
        log.append(log_string)


def print_player_hand(number_of_cards,board_label,menu_selected,hand_score,current_turn):
    #changes the color of the menu item that is selected
    if menu_selected == 'bet':
        bet_color = Fore.RED + "(B)et "
        hit_color = Fore.CYAN + "(H)it "
        stay_color = Fore.CYAN + "(S)tand"
        ace_color = Fore.CYAN + "(A)ce "
    elif menu_selected == 'hit':
        bet_color = Fore.CYAN + "(B)et "
        hit_color = Fore.RED + "(H)it "
        stay_color = Fore.CYAN + "(S)tand"
        ace_color = Fore.CYAN + "(A)ce "
    elif menu_selected == 'stay':
        bet_color = Fore.CYAN + "(B)et "
        hit_color = Fore.CYAN + "(H)it "
        stay_color = Fore.RED + "(S)tand"
        ace_color = Fore.CYAN + "(A)ce "
    elif menu_selected == 'ace':
        bet_color = Fore.CYAN + "(B)et "
        hit_color = Fore.CYAN + "(H)it "
        stay_color = Fore.CYAN + "(S)tand"
        ace_color = Fore.RED + "(A)ce "
    else:
        bet_color = Fore.CYAN + "(B)et "
        hit_color = Fore.CYAN + "(H)it "
        stay_color = Fore.CYAN + "(S)tand"
        ace_color = Fore.CYAN + "(A)ce "
    if board_label == 'player':
        board_label = "PLAYER"
        #print all of the dealers/players cards
        #Need to change what the board looks like based on how many cards the player has in their hand
        #use lines2 list to print smaller cards
        if number_of_cards == 6:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)

            print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[0][0],Fore.CYAN  +lines2[0][1], Fore.CYAN + lines2[0][2],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*22,"{bet} ".format(bet=bet_color), Back.CYAN +   ' '*15,' ', Fore.CYAN  +lines2[1][0],Fore.CYAN  +lines2[1][1], Fore.CYAN + lines2[1][2],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*22,"{hit} ".format(hit=hit_color), Back.CYAN +   ' '*15,' ', Fore.CYAN  +lines2[2][0],Fore.CYAN  +lines2[2][1], Fore.CYAN + lines2[2][2],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*22,"{ace} ".format(ace=ace_color), Back.CYAN +   ' '*15,' ', Fore.CYAN  +lines2[3][0],Fore.CYAN  +lines2[3][1], Fore.CYAN + lines2[3][2],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*22,"{stay}".format(stay=stay_color), Back.CYAN +   ' '*15,' ', Fore.CYAN  +lines2[4][0],Fore.CYAN  +lines2[4][1], Fore.CYAN + lines2[4][2],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[5][0],Fore.CYAN  +lines2[5][1], Fore.CYAN + lines2[5][2],' ', Back.CYAN +   ' '*52)

            print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[0][3],Fore.CYAN  +lines2[0][4], Fore.CYAN + lines2[0][5],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[1][3],Fore.CYAN  +lines2[1][4], Fore.CYAN + lines2[1][5],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[2][3],Fore.CYAN  +lines2[2][4], Fore.CYAN + lines2[2][5],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[3][3],Fore.CYAN  +lines2[3][4], Fore.CYAN + lines2[3][5],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[4][3],Fore.CYAN  +lines2[4][4], Fore.CYAN + lines2[4][5],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[5][3],Fore.CYAN  +lines2[5][4], Fore.CYAN + lines2[5][5],' ', Back.CYAN +   ' '*52)

            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)


        elif number_of_cards == 5:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)

            print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[0][0],Fore.CYAN  +lines2[0][1], Fore.CYAN + lines2[0][2],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*22,"{bet} ".format(bet=bet_color), Back.CYAN +   ' '*15,' ', Fore.CYAN  +lines2[1][0],Fore.CYAN  +lines2[1][1], Fore.CYAN + lines2[1][2],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*22,"{hit} ".format(hit=hit_color), Back.CYAN +   ' '*15,' ', Fore.CYAN  +lines2[2][0],Fore.CYAN  +lines2[2][1], Fore.CYAN + lines2[2][2],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*22,"{ace} ".format(ace=ace_color), Back.CYAN +   ' '*15,' ', Fore.CYAN  +lines2[3][0],Fore.CYAN  +lines2[3][1], Fore.CYAN + lines2[3][2],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*22,"{stay}".format(stay=stay_color), Back.CYAN + ' '*15,' ', Fore.CYAN  +lines2[4][0], Fore.CYAN + lines2[4][1],Fore.CYAN + lines2[4][2],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[5][0],Fore.CYAN  +lines2[5][1], Fore.CYAN + lines2[5][2],' ', Back.CYAN +   ' '*52)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' '*5, Fore.CYAN  +lines2[x][3],'', Fore.CYAN + lines2[x][4],' '*5, Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)


        elif number_of_cards == 4:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)

            print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[0][0]," "*2, Fore.CYAN + lines2[0][1],' ', Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*22,"{bet} ".format(bet=bet_color), Back.CYAN +   ' '*18," ",Fore.CYAN  +lines2[1][0]," "*2,Fore.CYAN + lines2[1][1],' ',Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*22,"{hit} ".format(hit=hit_color), Back.CYAN +   ' '*18,' ',Fore.CYAN  +lines2[2][0]," "*2,Fore.CYAN + lines2[2][1],' ',Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*22,"{ace} ".format(ace=ace_color), Back.CYAN +   ' '*18,' ',Fore.CYAN  +lines2[3][0]," "*2,Fore.CYAN + lines2[3][1],' ',Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*22,"{stay}".format(stay=stay_color), Back.CYAN +   ' '*18,' ',Fore.CYAN  +lines2[4][0]," "*2,Fore.CYAN + lines2[4][1],' ',Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[5][0]," "*2, Fore.CYAN + lines2[5][1],' ', Back.CYAN +   ' '*55)


            print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[0][2], " "*2, Fore.CYAN + lines2[0][3],' ', Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[1][2], " "*2, Fore.CYAN + lines2[1][3],' ', Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[2][2], " "*2, Fore.CYAN + lines2[2][3],' ', Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[3][2], " "*2, Fore.CYAN + lines2[3][3],' ', Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[4][2], " "*2, Fore.CYAN + lines2[4][3],' ', Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[5][2], " "*2, Fore.CYAN + lines2[5][3],' ', Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)


        elif number_of_cards == 3:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)

            print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[0][0]," "*2, Fore.CYAN + lines2[0][1],' ', Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*22,"{bet} ".format(bet=bet_color), Back.CYAN +   ' '*18," ",Fore.CYAN  +lines2[1][0]," "*2,Fore.CYAN + lines2[1][1],' ',Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*22,"{hit} ".format(hit=hit_color), Back.CYAN +   ' '*18,' ',Fore.CYAN  +lines2[2][0]," "*2,Fore.CYAN + lines2[2][1],' ',Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*22,"{ace} ".format(ace=ace_color), Back.CYAN +   ' '*18,' ',Fore.CYAN  +lines2[3][0]," "*2,Fore.CYAN + lines2[3][1],' ',Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*22,"{stay}".format(stay=stay_color), Back.CYAN +   ' '*18,' ',Fore.CYAN  +lines2[4][0]," "*2,Fore.CYAN + lines2[4][1],' ',Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[5][0]," "*2, Fore.CYAN + lines2[5][1],' ', Back.CYAN +   ' '*55)

            print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[0][2], " "*2,' '*10, Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[1][2], " "*2,' '*10, Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[2][2], " "*2,' '*10, Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[3][2], " "*2,' '*10, Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[4][2], " "*2,' '*10, Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[5][2], " "*2,' '*10, Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)


        #If there are only two cards, print two big cards from lines1 list next to eachother
        elif number_of_cards == 2:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20, Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            print(Back.CYAN +   ' '*49,Fore.CYAN  +lines[0][0],Fore.CYAN + lines[0][1],Back.CYAN +   ' '*56)
            print(Back.CYAN +   ' '*22,"{bet} ".format(bet=bet_color), Back.CYAN +   ' '*18,Fore.CYAN  +lines[1][0],Fore.CYAN + lines[1][1],Back.CYAN +   ' '*56)
            print(Back.CYAN +   ' '*22,"{hit} ".format(hit=hit_color), Back.CYAN +   ' '*18,Fore.CYAN  +lines[2][0],Fore.CYAN + lines[2][1],Back.CYAN +   ' '*56)
            print(Back.CYAN +   ' '*22,"{ace} ".format(ace=ace_color), Back.CYAN +   ' '*18,Fore.CYAN  +lines[3][0],Fore.CYAN + lines[3][1],Back.CYAN +   ' '*56)
            print(Back.CYAN +   ' '*22,"{stay}".format(stay=stay_color), Back.CYAN +   ' '*18,Fore.CYAN  +lines[4][0],Fore.CYAN + lines[4][1],Back.CYAN +   ' '*56)
            print(Back.CYAN +   ' '*49,Fore.CYAN  +lines[5][0],Fore.CYAN + lines[5][1],Back.CYAN +   ' '*56)
            print(Back.CYAN +   ' '*49,Fore.CYAN  +lines[6][0],Fore.CYAN + lines[6][1],Back.CYAN +   ' '*56)
            print(Back.CYAN +   ' '*49,Fore.CYAN  +lines[7][0],Fore.CYAN + lines[7][1],Back.CYAN +   ' '*56)
            print(Back.CYAN +   ' '*49,Fore.CYAN  +lines[8][0],Fore.CYAN + lines[8][1],Back.CYAN +   ' '*56)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)


        elif number_of_cards == 1:
            for x in range(len(lines)):
                print(lines[x][0])
        else:

    else:
        board_label = "DEALER"
        if current_turn == 'player':
            hand_score = '??'
        if number_of_cards == 6:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label),Back.CYAN +   ' '*35,Fore.CYAN + "   LOG   ", Back.CYAN + " "*17)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)

            print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[0][0], Fore.RED + lines2[0][1], Fore.RED + lines2[0][2],' ' ,Back.CYAN +   ' '*12,'{}'.format(log[0]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[1][0], Fore.RED + lines2[1][1], Fore.RED + lines2[1][2],' ' ,Back.CYAN +   ' '*12,'{}'.format(log[1]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[2][0], Fore.RED + lines2[2][1], Fore.RED + lines2[2][2],' ' ,Back.CYAN +   ' '*12,'{}'.format(log[2]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[3][0], Fore.RED + lines2[3][1], Fore.RED + lines2[3][2],' ' ,Back.CYAN +   ' '*12,'{}'.format(log[3]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[4][0], Fore.RED + lines2[4][1], Fore.RED + lines2[4][2],' ' ,Back.CYAN +   ' '*12,'{}'.format(log[4]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[5][0], Fore.RED + lines2[5][1], Fore.RED + lines2[5][2],' ' ,Back.CYAN +   ' '*12,'{}'.format(log[5]),Back.CYAN +   ' '*4)


            print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[0][3], Fore.RED + lines2[0][4], Fore.RED + lines2[0][5],' ' ,Back.CYAN +   ' '*12,'{}'.format(log[6]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[1][3], Fore.RED + lines2[1][4], Fore.RED + lines2[1][5],' ' ,Back.CYAN +   ' '*12,'{}'.format(log[7]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[2][3], Fore.RED + lines2[2][4], Fore.RED + lines2[2][5],' ' ,Back.CYAN +   ' '*12,'{}'.format(log[8]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[3][3],Fore.RED  +lines2[3][4], Fore.RED + lines2[3][5],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[4][3],Fore.RED  +lines2[4][4], Fore.RED + lines2[4][5],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[5][3],Fore.RED  +lines2[5][4], Fore.RED + lines2[5][5],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)


        elif number_of_cards == 5:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label),Back.CYAN +   ' '*35,Fore.CYAN + "   LOG   ", Back.CYAN + " "*17)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)

            print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[0][0], Fore.RED + lines2[0][1], Fore.RED + lines2[0][2],' ' ,Back.CYAN +   ' '*12,'{}'.format(log[0]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[1][0], Fore.RED + lines2[1][1], Fore.RED + lines2[1][2],' ' ,Back.CYAN +   ' '*12,'{}'.format(log[1]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[2][0], Fore.RED + lines2[2][1], Fore.RED + lines2[2][2],' ' ,Back.CYAN +   ' '*12,'{}'.format(log[2]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[3][0], Fore.RED + lines2[3][1], Fore.RED + lines2[3][2],' ' ,Back.CYAN +   ' '*12,'{}'.format(log[3]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[4][0], Fore.RED + lines2[4][1], Fore.RED + lines2[4][2],' ' ,Back.CYAN +   ' '*12,'{}'.format(log[4]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[5][0], Fore.RED + lines2[5][1], Fore.RED + lines2[5][2],' ' ,Back.CYAN +   ' '*12,'{}'.format(log[5]),Back.CYAN +   ' '*4)

            print(Back.CYAN +   ' '*46,' '*5, Fore.RED  +lines2[0][3],'', Fore.RED + lines2[0][4],' '*5,Back.CYAN +   ' '*12,'{}'.format(log[6]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*46,' '*5, Fore.RED  +lines2[1][3],'', Fore.RED + lines2[1][4],' '*5,Back.CYAN +   ' '*12,'{}'.format(log[7]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*46,' '*5, Fore.RED  +lines2[2][3],'', Fore.RED + lines2[2][4],' '*5,Back.CYAN +   ' '*12,'{}'.format(log[8]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*46,' '*5, Fore.RED  +lines2[3][3],'', Fore.RED + lines2[3][4],' '*5,Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*46,' '*5, Fore.RED  +lines2[4][3],'', Fore.RED + lines2[4][4],' '*5,Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*46,' '*5, Fore.RED  +lines2[5][3],'', Fore.RED + lines2[5][4],' '*5,Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)

        elif number_of_cards == 4:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label),Back.CYAN +   ' '*35,Fore.CYAN + "   LOG   ", Back.CYAN + " "*17)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[0][0]," "*2, Fore.RED + lines2[0][1],' ', Back.CYAN +   ' '*16,'{}'.format(log[0]),Back.CYAN +   ' '*3)
            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[1][0]," "*2, Fore.RED + lines2[1][1],' ', Back.CYAN +   ' '*16,'{}'.format(log[1]),Back.CYAN +   ' '*3)
            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[2][0]," "*2, Fore.RED + lines2[2][1],' ', Back.CYAN +   ' '*16,'{}'.format(log[2]),Back.CYAN +   ' '*3)
            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[3][0]," "*2, Fore.RED + lines2[3][1],' ', Back.CYAN +   ' '*16,'{}'.format(log[3]),Back.CYAN +   ' '*3)
            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[4][0]," "*2, Fore.RED + lines2[4][1],' ', Back.CYAN +   ' '*16,'{}'.format(log[4]),Back.CYAN +   ' '*3)
            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[5][0]," "*2, Fore.RED + lines2[5][1],' ', Back.CYAN +   ' '*16,'{}'.format(log[5]),Back.CYAN +   ' '*3)

            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[0][2],' '*2, Fore.RED + lines2[0][3],' ',Back.CYAN +   ' '*16,'{}'.format(log[6]),Back.CYAN +   ' '*3)
            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[1][2],' '*2, Fore.RED + lines2[1][3],' ',Back.CYAN +   ' '*16,'{}'.format(log[7]),Back.CYAN +   ' '*3)
            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[2][2],' '*2, Fore.RED + lines2[2][3],' ',Back.CYAN +   ' '*16,'{}'.format(log[8]),Back.CYAN +   ' '*3)
            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[3][2],' '*2, Fore.RED + lines2[3][3],' ',Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[4][2],' '*2, Fore.RED + lines2[4][3],' ',Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[5][2],' '*2, Fore.RED + lines2[5][3],' ',Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)

        elif number_of_cards == 3:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label),Back.CYAN +   ' '*35,Fore.CYAN + "   LOG   ", Back.CYAN + " "*17)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)

            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[0][0]," "*2, Fore.RED + lines2[0][1],' ', Back.CYAN +   ' '*16,'{}'.format(log[0]),Back.CYAN +   ' '*3)
            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[1][0]," "*2, Fore.RED + lines2[1][1],' ', Back.CYAN +   ' '*16,'{}'.format(log[1]),Back.CYAN +   ' '*3)
            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[2][0]," "*2, Fore.RED + lines2[2][1],' ', Back.CYAN +   ' '*16,'{}'.format(log[2]),Back.CYAN +   ' '*3)
            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[3][0]," "*2, Fore.RED + lines2[3][1],' ', Back.CYAN +   ' '*16,'{}'.format(log[3]),Back.CYAN +   ' '*3)
            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[4][0]," "*2, Fore.RED + lines2[4][1],' ', Back.CYAN +   ' '*16,'{}'.format(log[4]),Back.CYAN +   ' '*3)
            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[5][0]," "*2, Fore.RED + lines2[5][1],' ', Back.CYAN +   ' '*16,'{}'.format(log[5]),Back.CYAN +   ' '*3)

            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[0][2], " "*2,' '*10, Back.CYAN +   ' '*16,'{}'.format(log[6]),Back.CYAN +   ' '*3)
            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[1][2], " "*2,' '*10, Back.CYAN +   ' '*16,'{}'.format(log[7]),Back.CYAN +   ' '*3)
            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[2][2], " "*2,' '*10, Back.CYAN +   ' '*16,'{}'.format(log[8]),Back.CYAN +   ' '*3)

            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[3][2], " "*2,' '*10, Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[4][2], " "*2,' '*10, Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[5][2], " "*2,' '*10, Back.CYAN +   ' '*55)

            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)

        #If there are only two cards, print two big cards from lines1 list next to eachother
        elif number_of_cards == 2:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label),Back.CYAN +   ' '*35,Fore.CYAN + "   LOG   ", Back.CYAN + " "*17)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)

            print(Back.CYAN +   ' '*49,Fore.RED +lines[0][0],Fore.RED + lines[0][1],Back.CYAN +   ' '*16,'{}'.format(log[0]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*49,Fore.RED +lines[1][0],Fore.RED + lines[1][1],Back.CYAN +   ' '*16,'{}'.format(log[1]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*49,Fore.RED +lines[2][0],Fore.RED + lines[2][1],Back.CYAN +   ' '*16,'{}'.format(log[2]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*49,Fore.RED +lines[3][0],Fore.RED + lines[3][1],Back.CYAN +   ' '*16,'{}'.format(log[3]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*49,Fore.RED +lines[4][0],Fore.RED + lines[4][1],Back.CYAN +   ' '*16,'{}'.format(log[4]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*49,Fore.RED +lines[5][0],Fore.RED + lines[5][1],Back.CYAN +   ' '*16,'{}'.format(log[5]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*49,Fore.RED +lines[6][0],Fore.RED + lines[6][1],Back.CYAN +   ' '*16,'{}'.format(log[6]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*49,Fore.RED +lines[7][0],Fore.RED + lines[7][1],Back.CYAN +   ' '*16,'{}'.format(log[7]),Back.CYAN +   ' '*4)
            print(Back.CYAN +   ' '*49,Fore.RED +lines[8][0],Fore.RED + lines[8][1],Back.CYAN +   ' '*16,'{}'.format(log[8]),Back.CYAN +   ' '*4)

            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)


        elif number_of_cards == 1:
            for x in range(len(lines)):
                print(lines[x][0])
        else:
            print("Can only print 1 - 5 cards in a hand. ")
#changes the color of the ace to show that it is selected, this happens the the ace select menu is selected
def change_ace_color(number_of_cards,current_turn,card_index_to_change,hand_score):
    if current_turn == 'player':
        board_label = "PLAYER"

    #Need to change what the board looks like based on how many cards the player has in their hand
    #use lines2 list to print smaller cards
    if number_of_cards == 6:
        if card_index_to_change == 5:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[x][0],Fore.CYAN  +lines2[x][1], Fore.CYAN + lines2[x][2],' ', Back.CYAN +   ' '*52)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[x][3],Fore.CYAN  +lines2[x][4], Fore.RED + lines2[x][5],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)


        elif card_index_to_change == 4:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[x][0],Fore.CYAN  +lines2[x][1], Fore.CYAN + lines2[x][2],' ', Back.CYAN +   ' '*52)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[x][3],Fore.RED  +lines2[x][4], Fore.CYAN + lines2[x][5],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)


        elif card_index_to_change == 3:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[x][0],Fore.CYAN  +lines2[x][1], Fore.CYAN + lines2[x][2],' ', Back.CYAN +   ' '*52)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[x][3],Fore.CYAN  +lines2[x][4], Fore.CYAN + lines2[x][5],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)



        elif card_index_to_change == 2:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[x][0],Fore.CYAN  +lines2[x][1], Fore.RED + lines2[x][2],' ', Back.CYAN +   ' '*52)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[x][3],Fore.CYAN  +lines2[x][4], Fore.CYAN + lines2[x][5],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)



        #If there are only two cards, print two big cards from lines1 list next to eachother
        elif card_index_to_change == 1:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[x][0],Fore.RED  +lines2[x][1], Fore.CYAN + lines2[x][2],' ', Back.CYAN +   ' '*52)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[x][3],Fore.CYAN  +lines2[x][4], Fore.CYAN + lines2[x][5],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)



        elif card_index_to_change == 0:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[x][0],Fore.CYAN  +lines2[x][1], Fore.CYAN + lines2[x][2],' ', Back.CYAN +   ' '*52)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[x][3],Fore.CYAN  +lines2[x][4], Fore.CYAN + lines2[x][5],' ', Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)


    elif number_of_cards == 5:
        if card_index_to_change == 4:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[x][0],Fore.CYAN  +lines2[x][1], Fore.CYAN + lines2[x][2],' ', Back.CYAN +   ' '*52)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' '*5, Fore.CYAN  +lines2[x][3],'', Fore.RED + lines2[x][4],' '*5, Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)


        elif card_index_to_change == 3:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[x][0],Fore.CYAN  +lines2[x][1], Fore.CYAN + lines2[x][2],' ', Back.CYAN +   ' '*52)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' '*5, Fore.RED  +lines2[x][3],'', Fore.CYAN + lines2[x][4],' '*5, Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)



        elif card_index_to_change == 2:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[x][0],Fore.CYAN  +lines2[x][1], Fore.RED + lines2[x][2],' ', Back.CYAN +   ' '*52)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' '*5, Fore.CYAN  +lines2[x][3],'', Fore.CYAN + lines2[x][4],' '*5, Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)



        #If there are only two cards, print two big cards from lines1 list next to eachother
        elif card_index_to_change == 1:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' ', Fore.CYAN  +lines2[x][0],Fore.RED  +lines2[x][1], Fore.CYAN + lines2[x][2],' ', Back.CYAN +   ' '*52)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' '*5, Fore.CYAN  +lines2[x][3],'', Fore.CYAN + lines2[x][4],' '*5, Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)



        elif card_index_to_change == 0:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' ', Fore.RED  +lines2[x][0],Fore.CYAN  +lines2[x][1], Fore.CYAN + lines2[x][2],' ', Back.CYAN +   ' '*52)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*46,' '*5, Fore.CYAN  +lines2[x][3],'', Fore.CYAN + lines2[x][4],' '*5, Back.CYAN +   ' '*52)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)


    elif number_of_cards == 4:
        if card_index_to_change == 3:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[x][0]," "*2, Fore.CYAN + lines2[x][1],' ', Back.CYAN +   ' '*55)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[x][2], " "*2, Fore.RED + lines2[x][3],' ', Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)


        elif card_index_to_change == 2:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[x][0]," "*2, Fore.CYAN + lines2[x][1],' ', Back.CYAN +   ' '*55)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[x][2], " "*2, Fore.CYAN + lines2[x][3],' ', Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)



        elif card_index_to_change == 1:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[x][0]," "*2, Fore.RED + lines2[x][1],' ', Back.CYAN +   ' '*55)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[x][2], " "*2, Fore.CYAN + lines2[x][3],' ', Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)



        #If there are only two cards, print two big cards from lines1 list next to eachother
        elif card_index_to_change == 0:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[x][0]," "*2, Fore.CYAN + lines2[x][1],' ', Back.CYAN +   ' '*55)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[x][2], " "*2, Fore.CYAN + lines2[x][3],' ', Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)



    elif number_of_cards == 3:
        if card_index_to_change == 2:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[x][0]," "*2, Fore.CYAN + lines2[x][1],' ', Back.CYAN +   ' '*55)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[x][2], " "*2,' '*10, Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)



        elif card_index_to_change == 1:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[x][0]," "*2, Fore.RED + lines2[x][1],' ', Back.CYAN +   ' '*55)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[x][2], " "*2,' '*10, Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)



        elif card_index_to_change == 0:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*49,' ', Fore.RED  +lines2[x][0]," "*2, Fore.CYAN + lines2[x][1],' ', Back.CYAN +   ' '*55)
            for x in range(len(lines2)):
                print(Back.CYAN +   ' '*49,' ', Fore.CYAN  +lines2[x][2], " "*2,' '*10, Back.CYAN +   ' '*55)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)


    elif number_of_cards == 2:
        if card_index_to_change == 1:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            for x in range(len(lines)):
                print(Back.CYAN +   ' '*49,Fore.CYAN  +lines[x][0],Fore.RED + lines[x][1],Back.CYAN +   ' '*56)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)


        elif card_index_to_change == 0:
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*20,Fore.CYAN + "CURRENT HAND",Back.CYAN +   ' '*21, Fore.CYAN + "  {LABEL}  ".format(LABEL=board_label), Back.CYAN + " "*63)
            print(Back.CYAN +   ' '*25,Fore.CYAN + "{score}".format(score=hand_score),Back.CYAN +   ' '*101)
            for x in range(len(lines)):
                print(Back.CYAN +   ' '*49,Fore.RED  +lines[x][0],Fore.CYAN + lines[x][1],Back.CYAN +   ' '*56)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)
            print(Back.CYAN +   ' '*130)

#easy way to print color text through colorama
def print_color(strings,color):
    string = "print(Fore.{COLOR}+ '{STRING}')".format(STRING=strings,COLOR=color)
    eval(string)
