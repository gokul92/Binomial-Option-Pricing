# Binomial-Option-Pricing
Binomial Lattice method used to obtain the arbitrage free price of options based on the Black-Scholes equation.

Given the following parameters :

1. Volatility  - voltly
2. Duration of time period - T
3. Number of time periods - n
4. Initial Price of the underlying - S0
5. Strike Price - strike
6. Risk free rate - r

The python code calculates the risk neutral probabilities, builds the stock-lattice and based on the strike price,
calculates the payoff from the option. Then it calculates the arbitrage free option price backwards by discounting 
the option price at every time instant.


