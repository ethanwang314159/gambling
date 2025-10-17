import random
import time

UP = "\x1b[1A"

def gamble(chance, amount, multiplier):
    return amount * multiplier if random.random() < chance else 0

def pray_to_kelly(chance, multiplier):
    return (chance*multiplier-1)/(multiplier-1) if chance > 1/multiplier else 0

chance = 0.51
payout = 2
balance = 100
wins = 0
bets = 0
peak = balance
print("")
print(f"Playing simple gambling game starting on ${balance}, {chance} odds with a payout of {payout-1}x the bet amount.")
print("\n"*4)

while balance > 0:
    togamb = pray_to_kelly(chance, payout) * balance
    balance -= togamb
    result = gamble(chance, togamb, payout)
    balance += result
    bets += 1
    
    if result != 0:
        resultprint = f"OUTCOME OF LAST BET: + ${togamb:.2f}"
        wins += 1
    else:
        resultprint = f"OUTCOME OF LAST BET: - ${togamb:.2f}"
    if balance > peak:
        peak = balance
    peakprint = f"PEAK BALANCE: ${peak:.2f}"
    betsprint = "BETS: " + str(bets)
    winsprint = "WINS: " + str(wins)

    print(UP*6)
    print(f"Balance: ${balance:.2f}\n{resultprint}\n{peakprint}\n{betsprint}\n{winsprint}")
    
    #time.sleep(0.1)
