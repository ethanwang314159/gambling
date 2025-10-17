import random
import time
import re


UP = "\x1b[1A"

try:
    CHANCE = float(re.sub(r'[^0-9.]', '', input("Enter a probability between 0 and 1 for winning(DONT JUST PUT 1 OR 0 DUDE PUT LIKE 0.55): ")))
    if CHANCE >= 1.0 or CHANCE <= 0.0:
        print("bruh i said not to im just making it 51%")
        CHANCE = 0.51
except:
    print("ok you did something bad im just making the chance 53%")
    CHANCE = 0.53
try:
    PAYOUT = float(re.sub(r'[^0-9.]', '', input("Enter a payout for winning(2 means you win your bet, if you bet $5 and win you earnt $5): ")))
except:
    print("you naughty person follow instructions will you anyways payout is 2")
    PAYOUT = 2
try:
    START_BALANCE = float(re.sub(r'[^0-9.]', '', input("enter a start balance dont be ridiculous: ")))
    if START_BALANCE < 0.5:
        print("dude thats ridiculous invest more than 50 cents will you thats it im taking $10 from you")
        START_BALANCE = 10
except:
    print('ok bad person please follow instructions im just making the start balance $100')
    START_BALANCE = 100
try:
    euh = input("do you want to wait (Y|N) defaults to wait btw so like if you want to wait and sit there bored you can").strip().upper()
    if euh == "N":
        NOWAIT = True
    else:
        NOWAIT = False
        WAIT = int(input("how long do you want to wait per bet? enter in milliseconds and no decimal points or i will crash out"))/1000
except:
    print("you did something wrong there.")
    print("now you're gonna have to wait 1 second per bet.")
    NOWAIT = False
    WAIT = 1
        

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
reason = "idk"
while balance > 0 and running and balance < 2147483647:
    togamb = pray_to_kelly(CHANCE, PAYOUT) * balance
    if togamb < 0.01:
        running = False
        reason = "Gambler's ruin" if bets < 20 else "damn"
        if bets == 0: print(UP*6)
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
    
    if not NOWAIT:

        time.sleep(WAIT)
print("ENDINGGGGGGGGGGGGGGGGGGGG")
if reason == "idk":
    if balance > 4294967295:
        reason = "hacker"
    elif balance > 2147483647:
        reason = "hacker" if bets == 0 else "rich"
    else:
        reason = "bad"

match reason:
    case "damn":
        print("(4) wow you really just did that. like you really just put a really small amount of money just to see the bot run out of money. wow. i know what you are. \nyou also probably did something like put the odds of winning small. ok bro. not funny.")
    case "bad":
        print("(5) ok you're so bad you literally broke the system like you should not be able to see this at all like ever \nno seriously why are you here.")
    case "Gambler's ruin":
        print("(3) it's not worth it, see https://en.wikipedia.org/wiki/Gambler's_ruin")
    case "hacker":
        print("(2) you hacker you set your balance above the limit")
    case "rich":
        print("(1) you're just rich")
    case _:
        print("(6) how did you get here bro (secret ending you're not meant to see)")