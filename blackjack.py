import random
import time

#creates a list with the txt of all the cards
with open("deck.txt","r") as f:
    deck = f.readlines()

#list of the values equivalent to all cards
values = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

#lists of cards that were already dealt, their value, how many rounds have been played and the player's money
dealer_first_card = []
dealer_cards = [0]
player_cards = [0]
rounds = [0]
roundsum = sum(rounds)
money = [1000]

#dealer's action at the start of the round
def dealer_start():
    c = random.randrange(1,52)
    card = deck.pop(c)
    value = values.pop(c)
    print("")
    print("DEALER: ")
    print(card)
    dealer_cards.append(value)
    dealer_first_card.append(card)
    print("The dealer's score so far:  ", sum(dealer_cards))
    print("")

#player's action at the start of the round
def player_start():
    a = random.randrange(1,51)
    card_a = deck.pop(a)
    value_a = values.pop(a)
    b = random.randrange(1,50)
    card_b = deck.pop(b)
    value_b = values.pop(b)
    print(card_a)
    print(card_b)
    player_cards.append(value_a)
    player_cards.append(value_b)
    print("Your score so far:  ", sum(player_cards))
    print("")

#player draws one more card
def player_turn():
    c = random.randrange(len(deck))
    card = deck.pop(c)
    value = values.pop(c)
    print("")
    print(card)
    player_cards.append(value)

#dealer draws one more card
def dealer_turn():
    c = random.randrange(len(deck))
    card = deck.pop(c)
    value = values.pop(c)
    print("")
    print(card)
    dealer_cards.append(value)
    print("The dealer's score so far:  ", sum(dealer_cards))
    print("")

#actions of each round
def new_round():
    dealer_start()
    print("Your money:  ", sum(money))
    bet = float(input("Type how much you wanna bet:  "))
    if int(bet) <= sum(money):
        withdraw = -float(bet)
        deposit = float(bet)
        money.append(withdraw)

        player_start()

        while True:
            player_choice = input("Type Y for another card or N to stop:  ")
            player_choice_lower = player_choice.lower()
            if player_choice_lower == "y":
                player_turn()
                print("Your current score: ", sum(player_cards))
            if player_choice_lower == "n":
                print("Your current score: ", sum(player_cards))
                break
            if sum(player_cards) > 21:
                print("You bust !")
                break
            else:
                print("  ")

        print("")
        print("DEALER")
        print("")
        print(dealer_first_card[0])

        dealer_turn()
        time.sleep(2)

        while sum(dealer_cards) < 17:
            dealer_turn()
            time.sleep(2)

        if sum(player_cards) > sum(dealer_cards) and sum(player_cards) < 22:
            print("You win !")
            money.append(deposit)
            money.append(deposit)
            print("Your money:  ",sum(money))
        if sum(player_cards) < sum(dealer_cards) and sum(dealer_cards) < 22:
            print("The House wins !")
            print("Your money:  ", sum(money))
        if sum(player_cards) is sum(dealer_cards) or sum(player_cards) > 21 and sum(dealer_cards) > 21:
            print("It's a tie.")
            money.append(deposit)
            print("Your money:  ", sum(money))
        if sum(player_cards) < 22 and sum(dealer_cards) > 21:
            print("You win !")
            money.append(deposit)
            money.append(deposit)
            print("Your money:  ", sum(money))
        if sum(player_cards) > 21 and sum(dealer_cards) < 22:
            print("The House wins !")
            print("Your money:  ", sum(money))

        print("Your money:  ", sum(money))
        dealer_first_card.clear()
        dealer_cards.clear()
        dealer_cards.append(0)
        player_cards.clear()
        player_cards.append(0)
        rounds.append(1)
    else:
        print("Type a valid amount:  ")
        return

#repeats the round, shuffles the deck every 2 rounds, restarts the game if the player runs out of money
for x in range(99999999999):
    new_round()
    for roundsum in range(2):
        with open("deck.txt", "r") as f:
            deck = f.readlines()

        values = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9,
                  9,
                  9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

        if sum(money) < 1 :
            print("You ran out of money. Restarting the game...")
            with open("deck.txt", "r") as f:
                deck = f.readlines()

            values = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9,
                      9,
                      9,
                      9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

            money = [0]
            money.append(1000)