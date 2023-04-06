import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# Define a function to simulate random walks
def RandomWalkSimulation(num_simulations, num_periods, start_price, volatility):
    # Calculate the daily change in price based on volatility
    daily_volatility = volatility / np.sqrt(num_periods)
    
    # Create an array of random returns for each simulation
    daily_returns = np.random.normal(0, daily_volatility, size=(num_simulations, num_periods))
    
    # Calculate the cumulative sum of returns for each simulation
    cumulative_returns = np.cumsum(daily_returns, axis=1)
    
    # Calculate the final price for each simulation
    final_price = start_price * np.exp(cumulative_returns)
    
    return final_price

# Get historical data for a stock using yfinance
ticker = "AAPL"
stock = yf.Ticker(ticker)
data = stock.history(period="15y")

# Set the starting price and volatility based on the stock's historical data
start_price = data["Close"].iloc[-1]
daily_returns = np.log(data["Close"] / data["Close"].shift(1)).dropna()
volatility = np.std(daily_returns)

# Set the number of simulations and periods to run
num_simulations = 1000
num_periods = 252*15  # Assuming 252 trading days in a year, for 15 years

# Simulate the stock's price for the next year using the RandomWalkSimulation function
simulated_prices = RandomWalkSimulation(num_simulations, num_periods, start_price, volatility)

# Calculate the VaR at a 95% confidence level
var = np.percentile(simulated_prices[-1, :], 5)

# Plot a histogram of the simulated prices
plt.hist(simulated_prices[-1, :], bins=50)
plt.axvline(x=var, color='r', linestyle='--', label='VaR at 95% Confidence Level')
plt.title("Monte Carlo Simulation of "+ ticker + " for the last 15 years")
plt.xlabel("Final Stock Price")
plt.ylabel("Frequency")
plt.legend()
plt.show()





