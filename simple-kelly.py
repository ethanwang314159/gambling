import random
import time

UP = "\x1b[1A"
CHANCE = 0.51
PAYOUT = 2
START_BALANCE = 1

def gamble(chance, amount, multiplier):
    return amount * multiplier if random.random() < chance else 0

def pray_to_kelly(chance, multiplier):
    return (chance*multiplier-1)/(multiplier-1) if chance > 1/multiplier else 0

balance = START_BALANCE
peak = START_BALANCE
wins = 0
bets = 0

print("")
print(f"Playing binary return gambling game starting on ${balance}, {CHANCE} odds with a payout of {PAYOUT}x the bet amount.")
print("\n"*4)

running = True
reason = "bad"
while balance > 0 and running:
    togamb = pray_to_kelly(CHANCE, PAYOUT) * balance
    if togamb < 0.01:
        running = False
        reason = "Gambler's ruin"
        print(UP*6)
        continue
    balance -= togamb
    result = gamble(CHANCE, togamb, PAYOUT)
    balance += result
    bets += 1
    peak = max(peak, balance)
    wins += 1 if result > 0 else 0

    resultprint = f"OUTCOME OF LAST BET: {'+' if result > 0 else '-'} ${togamb:.2f}"
    peakprint = f"PEAK BALANCE: ${peak:.2f}"
    betsprint = f"BETS: {bets}"
    winsprint = f"WINS: {wins}"

    print(UP*6)
    print(f"Balance: ${balance:.2f}\n{resultprint}\n{peakprint}\n{betsprint}\n{winsprint}")
    
    #time.sleep(0.1)

match reason:
    case "bad":
        print("ok you're so bad you literally broke the system like you should not be able to see this at all like ever")
    case "Gambler's ruin":
        print("it's not worth it")
    case _:
        print("how did you get here")