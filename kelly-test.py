import random
import time

def gamble(chance, amount, multiplier):
    if random.random() < chance:
        return amount * multiplier
    return 0

def get_kelly_amount(chance, multiplier):
    if chance > (1/multiplier):
        return (chance*multiplier-1)/(multiplier-1)
    else:
        return 0

chance = 0.55
payout = 2
balance = 100
while True:
    print(balance)
    togamb = get_kelly_amount(chance, payout) * balance
    balance -= togamb
    print("Time to gamble", togamb, "dollars")
    result = gamble(chance, togamb, payout)
    balance += result
    if result != 0:
        print("yay I won", togamb, "dollars")
    else:
        print("rip i lost", togamb, "dollars")
    time.sleep(0.2)
