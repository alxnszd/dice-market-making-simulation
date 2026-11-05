# Dice Market-Making Simulation

## Overview

A Python-based market-making simulation exploring how bid-ask spread width affects trade frequency and profitability.

The simulation models a market maker quoting prices on a binary contract based on the outcome of rolling two fair six-sided dice.

The contract pays $1 if the dice sum to 7 and $0 otherwise.

The objective is to investigate the relationship between spread width, customer trade acceptance, and the market maker's simulated P&L.

## Mathematical Foundation

The probability of rolling a sum of 7 with two fair six-sided dice is:

P(Sum = 7) = 6/36 = 1/6

Therefore, the theoretical fair value of the contract is:

FV = $1 (1/6) + $0 (5/6) = $0.1667

The market maker sets bid and ask prices around fair value:

- Bid = Fair Value − Half Spread
- Ask = Fair Value + Half Spread

The spread width is varied from $0.01 to $0.10.

## Simulation Methodology

The simulation uses Python's `random` module to model customer behaviour and dice outcomes.

Each round follows this process:

1. A customer is assigned a randomly generated spread tolerance between $0.01 and $0.10.
2. If the quoted spread is within the customer's tolerance, a trade occurs.
3. The customer randomly decides whether to buy or sell the contract.
4. Two dice are rolled to determine the contract payout.
5. The market maker's cash balance is updated based on the trade and settlement.

Each executed contract is settled immediately.

A total of 10 million rounds are simulated for each spread width.

## Simulation Results

[Market Sim Records (1).xlsx](https://github.com/user-attachments/files/34440936/Market.Sim.Records.1.xlsx)


## Visualizations 
<img width="982" height="576" alt="image" src="https://github.com/user-attachments/assets/a695cf4c-48d4-4cf4-a885-48a91528abe5" />

<img width="981" height="582" alt="image" src="https://github.com/user-attachments/assets/fe167d57-61b6-47b3-bb97-8841b30a2e01" />


## Key Observations

- Wider spreads increase expected profit per executed trade because bid and ask prices move farther from fair value. Under the model's assumptions, expected profit per trade equals half the quoted spread.
- Increasing the spread reduces customer trade frequency, creating a trade-off between profit per trade and trading volume.
- Total P&L follows a nonlinear, inverted-U relationship with spread width because the increase in profit per trade must be weighed against the reduction in trade frequency.
- Spreads of $0.05 and $0.06 produce the same theoretical maximum expected P&L, despite having different trade frequencies.
- Simulated trade rates closely matched their theoretical expectations.
- The highest observed total P&L occurred at a spread width of $0.06. Small differences between observed and theoretical results are attributable to randomness.

## Limitations and Assumptions

This is an educational simulation, not a realistic market-making system.

The model assumes:

- Customer buy/sell decisions are equally likely.
- Customer trading decisions are independent of the dice outcome.
- There are no transaction fees.
- Contracts are settled immediately after each trade, so the market maker does not accumulate outstanding inventory or face inventory risk between rounds.
- The market maker knows the theoretical fair value.
- Customer spread tolerances are uniformly distributed between $0.01 and $0.10.

## Conclusion

The simulation illustrates the trade-off between spread width and trading frequency. Wider spreads generate greater expected profit per executed trade but reduce customer acceptance. Under the model's assumptions, spreads of $0.05 and $0.06 produce equal theoretical expected total P&L, despite having different trade frequencies.

## Technologies

- Python
- `random` module
- Google Sheets for recording and visualizing results

## Purpose

This project was built to explore probability, expected value, bid-ask spreads, randomized simulations, and the relationship between trade frequency and profitability.
