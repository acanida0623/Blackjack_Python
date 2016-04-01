import getch #waits and gets an input key_down and saves it to variable, does not need to use enter
import graphics
import Deck
import time



class Game:
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.deck = Deck.Deck()
        self.current_turn = 'player'
        self.menu_selected = 'bet'
        self.ace_index_selected = ''
        self.winner = ''
    def input_keystroke(self):
        while True:
            key = getch.getch()

            if ord(key[0]) == 104: #h key reprints screen and passes 'hit' so that the (H)it menu item is selected
                self.menu_selected = 'hit'
                self.dealer.hand.show_cards(True,'dealer',self.menu_selected)
                graphics.reset_printed_cards()
                self.player.hand.show_cards(False,'player',self.menu_selected)
                graphics.reset_printed_cards()

            elif ord(key[0]) == 115: #s key for stay menu select
                self.menu_selected = 'stay'
                self.dealer.hand.show_cards(True,'dealer',self.menu_selected)
                graphics.reset_printed_cards()
                self.player.hand.show_cards(False,'player',self.menu_selected)
                graphics.reset_printed_cards()

            elif ord(key[0]) == 98: #b key for bet menu
                self.menu_selected = 'bet'
                self.dealer.hand.show_cards(True,'dealer',self.menu_selected)
                graphics.reset_printed_cards()
                self.player.hand.show_cards(False,'player',self.menu_selected)
                graphics.reset_printed_cards()

            elif ord(key[0]) == 97:#a key ace selecting menu, change values of aces
                self.menu_selected = 'ace'
                self.dealer.hand.show_cards(True,'dealer',self.menu_selected)
                graphics.reset_printed_cards()
                self.player.hand.show_cards(False,'player',self.menu_selected)
                graphics.reset_printed_cards()
            elif ord(key[0]) == 10:#enter
                if self.menu_selected == 'ace':
                    self.ace_selector_menu()

                elif self.menu_selected == 'hit':
                    self.hit_menu()

                elif self.menu_selected == 'stay':
                    check_certain = str(input("             Are you sure you want to stand? Make sure to set the value of any Ace's you have. [Y]/N ")).lower()
                    if check_certain == 'y' or check_certain == 'yes':
                        self.stand_menu()


    def play(self):

        #set the terminal size to 130x40 v
        print ("\x1b[8;35;130t")
        #Fill deck with cards and randomyl shuffle the order, argument = number of decks to create
        self.deck.create_deck(1)

        self.deck.shuffle_deck()

        self.dealer.hand.draw_from_deck(2)
        self.dealer.hand.get_value()

        #passing True here tells show_cards it is the dealer's first turn, hide the first card
        #passing the menu_selected property  turns the bet item in the menu to red to show its selected
        self.dealer.hand.show_cards(True,'dealer',self.menu_selected)
        #this line of code calls the reset function in my graphics module and
        #clears the lists used to hold the game board and cards that are printed in the terminal
        graphics.reset_printed_cards()
        self.player.hand.draw_from_deck(2)
        self.player.hand.get_value()
        #pass false if not dealer's first hand
        self.player.hand.show_cards(False,'player',self.menu_selected)
        graphics.reset_printed_cards()
        #Checks if Blackjack on first hand
        if self.dealer.hand.first_hand_check_21_() == True and self.player.hand.first_hand_check_21_() == True:
            self.dealer.hand.show_cards(False,'dealer',self.menu_selected)
            graphics.reset_printed_cards()
            self.player.hand.show_cards(False,'player',self.menu_selected)
            graphics.reset_printed_cards()
            graphics.print_color("                                      BOTH DEALER AND PLAYER DREW BLACKJACK(21) ON FIRST HAND. TIE GAME! ",'RED')
            time.sleep(2)
            graphics.append_log('TIE GAME, DEALER + PLAYER BLACKJACK')
            self.setup_new_hand()
        elif self.dealer.hand.first_hand_check_21_() == True and self.player.hand.first_hand_check_21_() == False:
            self.dealer.hand.show_cards(False,'dealer',self.menu_selected)
            graphics.reset_printed_cards()
            self.player.hand.show_cards(False,'player',self.menu_selected)
            graphics.reset_printed_cards()
            graphics.print_color("                                     DEALER DREW BLACKJACK(21) ON FIRST HAND. YOU LOSE! ",'RED')
            time.sleep(2)
            graphics.append_log('YOU LOSE, DEALER DREW BLACKJACK')
            self.setup_new_hand()
        elif self.player.hand.first_hand_check_21_() == True:
            self.dealer.hand.show_cards(False,'dealer',self.menu_selected)
            graphics.reset_printed_cards()
            self.player.hand.show_cards(False,'player',self.menu_selected)
            graphics.reset_printed_cards()
            graphics.print_color("                                   BLACKJACK! YOU DREW 21 ON THE FIRST HAND! YOU WIN!",'RED')
            time.sleep(2)
            graphics.append_log('YOU WIN! YOU DREW BLACKJACK' )
            self.setup_new_hand()
        #Cards are dealt, waits for user keyboard input by running input_keystroke
        self.input_keystroke()

    #Opens up menu that selects any aces you may have, you are able to change their values from 11 or 1
    def ace_selector_menu(self):
        #gets a list of indices of any ace cards in player's hand
        ace_list = self.player.hand.ace_finder()
        current_ace_array = 0
        #if list has an ace, we need to reprint the board and draw the correct card index in red to show the Ace is selected
        if bool(ace_list):
            self.ace_index_selected = ace_list[current_ace_array]
            while True:
                #reprint the dealers hand / top half of board
                self.dealer.hand.show_cards(True,'dealer',self.menu_selected)
                graphics.reset_printed_cards()
                #re print players cards
                for x in range(len(self.player.hand.cards)):
                    suit = self.player.hand.cards[x]
                    rank = self.player.hand.cards[x]
                    cards = (graphics.create_card_to_print(suit, rank, False,len(self.player.hand.cards)))

                graphics.change_ace_color(len(self.player.hand.cards),'player',self.ace_index_selected,self.player.hand.value)
                graphics.reset_printed_cards()
                graphics.print_color("                Use the > key to scroll through aces. Press Enter to change the value to 11 or 1. ",'RED')
                graphics.print_color("                                                      E(x)it to finish ",'RED')
                #wait for key input to select aces and change their values
                key = getch.getch()
                if ord(key[0]) == 46:# >
                    try:
                        current_ace_array += 1
                        self.ace_index_selected = ace_list[current_ace_array]
                    except IndexError:
                        current_ace_array = 0
                        self.ace_index_selected = ace_list[current_ace_array]
                if ord(key[0]) == 10: # enter
                    if self.player.hand.cards[self.ace_index_selected].value == 1:

                        self.player.hand.cards[self.ace_index_selected].value = 11
                        self.player.hand.get_value()
                        if self.player.hand.value > 21:
                            self.player.hand.cards[self.ace_index_selected].value = 1
                            self.player.hand.get_value()
                            graphics.print_color("                                           Not Possible. Changing that Ace would put your current hand over 21. ",'RED')
                            time.sleep(.3)
                    else:
                        self.player.hand.cards[self.ace_index_selected].value = 1
                        self.player.hand.get_value()
                if ord(key[0]) == 120: # x is to exit ave menu, reprint regular game board
                    self.player.hand.get_value()
                    self.menu_selected = 'bet'
                    self.dealer.hand.show_cards(True,'dealer',self.menu_selected)
                    graphics.reset_printed_cards()
                    self.player.hand.show_cards(False,'player',self.menu_selected)
                    graphics.reset_printed_cards()
                    break
        else:
            print("There are no Aces! ")
    def hit_menu(self):#draw new card from deck and place it in players hand. reprint cards
        print ("\x1b[8;38;130t")
        temp_score = 0
        self.player.hand.draw_from_deck(1)
        self.player.hand.get_value()
        self.dealer.hand.show_cards(True,'dealer',self.menu_selected)
        graphics.reset_printed_cards()
        self.player.hand.show_cards(False,'player',self.menu_selected)
        graphics.reset_printed_cards()
        #check for bust, temporarily make the aces to ones to see the minimum score possible
        for x in range(len(self.player.hand.cards)):
            if self.player.hand.cards[x].value == 11:
                temp_score += 1
            else:
                temp_score += self.player.hand.cards[x].value
        if temp_score > 21:
            time.sleep(1)
            graphics.busted_screen('busted')
            time.sleep(2)
            graphics.busted_screen('dealing')
            time.sleep(2)
            print ("\x1b[8;35;130t")
            graphics.append_log('YOU BUSTED. YOU LOSE.')
            self.setup_new_hand()

        while True: #if the new card drawn makes hand over 21, allow the player to change an ace value if possible- slows down the gameplay
            if self.player.hand.value > 21:
                graphics.print_color("                                   HAND CURRENTLY OVER 21, CHANGE ACE VALUES. {}".format(self.player.hand.value),'RED' )
                time.sleep(2)
                self.menu_selected = 'ace'

                self.ace_selector_menu()
            else:
                break
    def stand_menu(self):#stand and reprint all the cards passing False to show the dealer's first card
        self.current_turn = 'dealer'
        graphics.print_color("                                                   SHOWING DEALERS HAND",'RED')
        time.sleep(2)
        while True:
            self.dealer.hand.show_cards(False,'dealer',self.menu_selected)
            graphics.reset_printed_cards()
            self.player.hand.show_cards(False,'player',self.menu_selected)
            graphics.reset_printed_cards()
            time.sleep(2)
            temp_value = 0
            if self.dealer.hand.value > 21:#if the dealers hand is over 21, check if the dealer can change an ace to a 1 and do it
                for x in range(len(self.dealer.hand.cards)):
                    if self.dealer.hand.cards[x].value == 11:
                        self.dealer.hand.cards[x].value = 1
                        self.dealer.hand.get_value()
                        self.dealer.hand.show_cards(False,'dealer',self.menu_selected)
                        graphics.reset_printed_cards()
                        self.player.hand.show_cards(False,'player',self.menu_selected)
                        graphics.reset_printed_cards()
                        time.sleep(2)
                        if self.dealer.hand.value < 21: #if the dealers hand is less than 21, break the for loop and continue the lose/win messages or draw another card
                            break
                        else:#else continue until all the cards are checked for aces
                            continue
            if self.dealer.hand.value <= 21 and self.dealer.hand.value > self.player.hand.value:
                graphics.print_color("                                          DEALER WINS WITH A {}. YOUR SCORE WAS {}".format(self.dealer.hand.value,self.player.hand.value),'RED')
                time.sleep(2)
                graphics.append_log('DEALER WINS WITH {}. YOU HAD {}'.format(self.dealer.hand.value,self.player.hand.value))
                self.setup_new_hand()
                break
            elif self.dealer.hand.value < 17:
                graphics.append_log("DEALER HAS {SCORE}. DRAWING CARD.".format(SCORE=self.dealer.hand.value))
                graphics.print_color("                                          DEALER HAS {SCORE}. DEALER DRAWING ANOTHER CARD.".format(SCORE=self.dealer.hand.value),'RED' )
                time.sleep(2)
                self.dealer.hand.draw_from_deck(1)
                self.dealer.hand.get_value()

            elif self.dealer.hand.value > 21:
                graphics.print_color("                                              DEALER BUSTS WITH A {SCORE}. YOU WIN!".format(SCORE=self.dealer.hand.value),'RED')
                time.sleep(2)
                graphics.append_log('DEALER BUSTS {}. YOU WIN WITH {}'.format(self.dealer.hand.value,self.player.hand.value))
                self.setup_new_hand()
                break
            elif self.dealer.hand.value >= 17 and self.player.hand.value > self.dealer.hand.value:
                graphics.print_color("                                            DEALER HAS A {}! YOU WIN WITH A {}! ".format(self.dealer.hand.value,self.player.hand.value),'RED')
                graphics.append_log('YOU WIN WITH {}. DEALER HAD {}'.format(self.player.hand.value,self.dealer.hand.value))
                self.setup_new_hand()
                break
            elif self.dealer.hand.value == self.player.hand.value:
                graphics.print_color("                                              YOU AND THE DEALER TIED WITH A {SCORE}! ".format(SCORE=self.player.hand.value),'RED')
                graphics.append_log('TIE GAME! YOU AND DEALER HAD {}'.format(self.player.hand.value))
                self.setup_new_hand()
                break
    def setup_new_hand(self):
        self.current_turn = 'player'
        while True:
            del self.dealer.hand.cards[:]
            del self.player.hand.cards[:]
            self.menu_selected = 'bet'
            self.dealer.hand.draw_from_deck(2)
            self.dealer.hand.get_value()
            #passing True here tells show_cards it is the dealer's first turn, hide the first card
            #passing the menu_selected property  turns the bet item in the menu to red to show its selected
            self.dealer.hand.show_cards(True,'dealer',self.menu_selected)
            graphics.reset_printed_cards()
            self.player.hand.draw_from_deck(2)
            self.player.hand.get_value()
            #pass false if not dealer's first hand
            self.player.hand.show_cards(False,'player',self.menu_selected)
            graphics.reset_printed_cards()

            time.sleep(2)
            if self.dealer.hand.first_hand_check_21_() == True and self.player.hand.first_hand_check_21_() == True:
                graphics.print_color("                                           BOTH DEALER AND PLAYER DREW BLACKJACK(21) ON FIRST HAND. TIE GAME! ",'RED')
                time.sleep(2)
                graphics.append_log('TIE GAME! PLAYER AND DEALER DREW BLACKJACK')
                continue
            elif self.dealer.hand.first_hand_check_21_() == True and self.player.hand.first_hand_check_21_() == False:
                graphics.print_color("                                           DEALER DREW BLACKJACK(21) ON FIRST HAND. YOU LOSE! ",'RED')
                time.sleep(2)
                graphics.append_log('YOU LOSE! DEALER DREW BLACKJACK!')
                continue
            elif self.player.hand.first_hand_check_21_() == True:
                graphics.print_color("                                   BLACKJACK! YOU DREW 21 ON THE FIRST HAND! YOU WIN!",'RED')
                time.sleep(2)
                graphics.append_log('YOU WIN! YOU DREW A BLACKJACK!')
                continue
            else:
                break

class Player:
    def __init__(self, name):
        self.hand = Hand()
        self.name = name.lower()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
    def draw_from_deck(self, number_of_cards):
        for x in range(number_of_cards):
            self.cards.append(game1.deck.get_card())
    def show_cards(self,dealer_first_hand,board_label,menu_item_selected):
        #If the dealer_first_hand, print the dealer's two cards in the graphics module with one of the cards facedown
        if dealer_first_hand:
            suit = self.cards[0]
            rank = self.cards[0]
            #Passing True here tells function to hide dealer's first card
            cards = (graphics.create_card_to_print(suit, rank, True, len(self.cards)))
            #passing False again to show card
            suit = self.cards[1]
            rank = self.cards[1]
            cards = (graphics.create_card_to_print(suit, rank, False, len(self.cards)))

        #else go through each card in the hand
        else:
            for x in range(len(self.cards)):
                suit = self.cards[x]
                rank = self.cards[x]
                cards = (graphics.create_card_to_print(suit, rank, False,len(self.cards)))

        if board_label == 'dealer':
            graphics.print_player_hand(len(self.cards),'dealer',menu_item_selected,self.value,game1.current_turn)

        else:
            graphics.print_player_hand(len(self.cards),'player',menu_item_selected,self.value,game1.current_turn)
    #updates the hand value property by adding the value of the next card drawn
    def get_value(self):
        self.value = 0
        for x in range(len(self.cards)):
            self.value += self.cards[x].value

    def ace_finder(self):
        #Check if hand has Aces and save the card index in the list to change its color to red for selecting
        ace_indices_list = []
        for x in range(len(self.cards)):
            if self.cards[x].rank == 'A':
                #creates a list containing the index numbers of any ace cards in the hand
                ace_indices_list.append(self.cards.index(game1.player.hand.cards[x]))
        return(ace_indices_list)

    def first_hand_check_21_(self):
        ace_list = []

        #check if there are two aces in the hand(called at begginning)
        #If two aces: change one ace value to 1 and leave other at 11 else check if the hand is 21
        for x in range(len(self.cards)):
            if self.cards[x].rank == 'A':
                #creates a list containing the index numbers of any ace cards in the hand
                ace_list.append(1)
        if len(ace_list) > 1:
            self.cards[0].value = 1
            self.get_value()
            game1.dealer.hand.show_cards(True,'dealer',game1.menu_selected)
            graphics.reset_printed_cards()
            game1.player.hand.show_cards(False,'player',game1.menu_selected)
            graphics.reset_printed_cards()
            return False
        if self.value == 21:
            return True
        else:
            return False




game1 = Game(Player('Andrew'), Player('Dealer'))


game1.play()
