import random
from art import logo

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Calculate the sum of the cards in a list and return the score calculated."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "It's a draw."
    elif c_score == 0:
        return "Opponent has a Blackjack. You lose."
    elif u_score == 0:
        return "You've got a Blackjack. You win!"
    elif u_score > 21:
        return "You went over. You lose."
    elif c_score > 21:
        return "Opponent went over. You win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose."

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_on = True

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while game_on:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_on = False
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower().strip()

            if should_continue == "y":
                user_cards.append(deal_card())
            else:
                game_on = False

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower().strip() == "y":
    print("\n" * 31)
    play_game()