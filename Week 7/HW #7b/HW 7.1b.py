# This program simulates a simplified version of the game of Blackjack between two virtual players.
# The cards have the following values:
# - Numeric cards are assigned the value they have printed on them.
# - Jacks, queens, and kings are valued at 10.
# - Aces are valued at 1 or 11, depending on the player’s choice.

import random

suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

# initialize the deck
deck = []
for suit in suits:
    for rank in ranks:
        card_value = 11 if rank == 'ace' else 10 if rank in ['jack', 'queen', 'king'] else int(rank)
        deck.append((rank, suit, card_value))

# shuffle the deck
random.shuffle(deck)

def deal_cards(num_cards=1):
    return [deck.pop() for _ in range(num_cards)]

def calculate_hand(hand):
    total = sum(card[2] for card in hand)
    num_aces = sum(1 for card in hand if card[0] == 'ace')
    while total > 21 and num_aces > 0:
        total -= 10
        num_aces -= 1
    return total

def play_game():
    player1_hand = deal_cards(2)
    player2_hand = deal_cards(2)
    while deck:
        player1_total = calculate_hand(player1_hand)
        player2_total = calculate_hand(player2_hand)
        if player1_total > 21 and player2_total > 21:
            print("Both players have exceeded 21. It's a tie!")
            break
        elif player1_total > 21:
            print("Player 2 wins! Player 1 has exceeded 21.")
            break
        elif player2_total > 21:
            print("Player 1 wins! Player 2 has exceeded 21.")
            break
        elif len(deck) < 2:
            print("There are no more cards in the deck.")
            break
        else:
            player1_hand += deal_cards(1)
            player2_hand += deal_cards(1)
    print(f"Player 1's hand: {player1_hand}, total value: {calculate_hand(player1_hand)}")
    print(f"Player 2's hand: {player2_hand}, total value: {calculate_hand(player2_hand)}")

play_game()
