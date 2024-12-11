from auction_art import logo

print(logo)

all_data = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

repeat = True

while repeat:

    name = input("What is your name? ")
    price = int(input("What is your bid: $"))

    all_data[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower().strip()

    if should_continue == "no":
        repeat = False
        find_highest_bidder(all_data)
    elif should_continue == "yes":
        print("\n" * 100)

