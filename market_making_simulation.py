import random

spread_width = 0.05
half_spread = spread_width/2
# Simulate rolling two six-sided dice
def twodice():

    
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
#creating the condition for fulfilling the contract    
    if (dice1 + dice2) == 7:

        return "pay"
    else:
        return "no pay"

#Fair value of the contract
def fairV():
    theovalue = 1/6
    return theovalue
#Bid is the price at which you buy, ask is the price at which you sell
bid = fairV()-half_spread
ask = fairV()+half_spread

#creating customer bot that randomly decided to buy, sell or not trade depending on the spread width
def customer():
    randspread = random.randint(1,10)
    spreadtolerance = randspread/100

    if spread_width <= spreadtolerance:
        tradeno = random.randint(0,1)

        if tradeno == 1:
            return "buy"
        else:
            return "sell"
    return "no trade"
#setting variables for number of trades and PnL
cash = 0
trade = 0
#probability of trade rate
theoretical_trade_rate = (11 - (spread_width*100))*10
# Simulate 10 million customer interactions while tracking trades and P&L
for i in range (10000000):

    decision = customer()
    outcome = twodice()
    if decision == "buy":
        cash+=ask
        trade += 1
        if outcome == "pay":
            cash -= 1

    elif decision == "sell":
        cash -= bid
        trade += 1

        if outcome == "pay":
            cash += 1

print("Total P&L:", round(cash, 3))
print("Total trades:", trade)
print("Theoretical Trade rate: ", theoretical_trade_rate, "%")
print("Actual Trade rate:", round((trade / 10000000) * 100, 2), "%")
if trade > 0:
    print("Average P&L per trade:", round(cash / trade, 5))
