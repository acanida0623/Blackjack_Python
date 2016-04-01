import random



class Deck:
    def __init__(self):
        self.cards = []


    def shuffle_deck(self):
        random.shuffle(self.cards)
        #self.put_deck()


    def get_card(self):#not in use
        #r = requests.get('https://glowing-heat-3466.firebaseio.com/deck.json')
        #d = eval(r.text)
        #self.cards[:] = []

        #print(len(d['cards']))

        #for x in range(len(d['cards'])):
            #newcard = Card(d['cards'][x][0],d['cards'][x][1],d['cards'][x][2],d['cards'][x][3])
            #self.cards.append(newcard)
        try:
            card = self.cards.pop(0)
            return card
        except IndexError:
            print("Not Enough Cards In Deck")
            exit()


    def create_deck(self,number_of_decks):
        suits = ['Clubs','Diamonds','Hearts','Spades']
        ranks = ['2','3','4','5','6','7','A','A','A','A','A','A','A']
        values = [2,3,4,5,6,7,11,11,11,11,11,11,11]
        cardnumber = 0
        for x in range(0,number_of_decks):
            for x in range(len(suits)):
                for y in range(len(ranks)):
                    newcard = Card(suits[x],ranks[y],values[y],cardnumber)
                    self.cards.append(newcard)
                    cardnumber += 1


    def print_cards(self):

        for x in range(len(self.cards)):
            print("{rank} of {suit} ".format(rank = self.cards[x].rank, suit = self.cards[x].suit))



    """def put_deck(self): #not in use
        cards_dict = {'cards':[]}

        for x in range(len(self.cards)):
            suit = self.cards[x].suit
            rank = self.cards[x].rank
            value = self.cards[x].value
            number = self.cards[x].inv_number
            list1 = (suit,rank,value,number)
            cards_dict['cards'].append(list1)

        #r = requests.put('https://glowing-heat-3466.firebaseio.com/deck.json', json = cards_dict)
"""

    def get_deck(self):
        pass


class Card:


    def __init__(self,suit,rank,value,inv_number):
        self.suit = suit
        self.value = value
        self.rank = rank
        self.inv_number = inv_number
