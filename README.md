# Stock Evaluator

Purpose to provide quick stock evaluation metrics for personal use. 


Reference github: https://github.com/kaushik316/Stocksheet
Reference quandl: https://docs.data.nasdaq.com/docs/python-time-series


## Quandl 
`pip install nasdaq-data-link`
Documentation: https://demo.quandl.com/docs-and-help
Profile: https://data.nasdaq.com/account/profile

Github Repo for nasdaqdatalink: https://github.com/Nasdaq/data-link-python/#local-api-key-environment-variable


### Local API Key File 
Consistently stored in `~/.nasdaq/data_link_apikey` the client will attempt to load this file if it exists. Note: if the file exists and empty, a ValueError will be thrown.


## Metrics
- DCF (Discounted Cash Flow)
        def dcf(growth_rate, WACC):
        cf_list = []
        for i in range(0, 4):
            cf = CF0 * (1.05 ** i)
            discounted = cf/(WACC ** i)
            cf_list.append(discounted)
    
        TCF = (cf_list[-1] * WACC^5)/ (WACC - growth rate)
        cf_list.append(TCF)
        PV = sum(cf_list)
        return PV
- Absolute Valuation
- P/E ratios
    - comaprisions between similar companies in the industry 
- Present Value 
    - PV = CF1 / (1+r)  +  CF2 / (1+r)^2  +  … [TCF / (r - g)] / (1+k)^n-1
    
    - CF (Cash flow growth)
    - r = Discount Rate
    - g = Growth Rate 
    - TCF = Terminal year cash flow (TCF = CFn / (r-g))
    - n = Number of periods in the valuation model


## Monte Carlo 
- Create simulations and test data from 2010-2020 and test vs real data from 2020-2022 and see how well they fit
    - or even from 2000-2010 and see how well that fits from 2010-2020

1. Price Simulation: Generate random price paths based on a stock's historical volatility to simulate potential future stock prices.

2. Return Simulation: Generate random return paths based on a stock's historical returns to simulate potential future returns.

3. Value at Risk (VaR) Simulation: Estimate the potential maximum loss in a portfolio using Monte Carlo simulation to model the distribution of possible returns.

4. Option Pricing Simulation: Simulate the price of an option using a random walk model and calculate its expected value.

5. Portfolio Optimization Simulation: Generate multiple portfolios with different combinations of assets and weights to identify the optimal portfolio based on expected returns and risk.

6. Scenario Analysis Simulation: Simulate various scenarios to understand how different economic, political, or market events could affect a portfolio.

7. Monte Carlo Sensitivity Analysis: Analyze how changes in key parameters such as volatility, interest rates, or inflation impact a portfolio's performance.

8. Volatility Smile Simulation: Simulate the implied volatility surface of a stock option and price the option based on the simulated implied volatility.

9. Monte Carlo Credit Risk Simulation: Simulate the potential losses on a credit portfolio due to default risk, based on the distribution of possible credit events.

10. Monte Carlo Retirement Planning Simulation: Simulate potential outcomes for retirement planning, based on a variety of factors such as investment returns, inflation, and spending habits.







## Bonds 
- Index Yield Curve


## Virtual Env

`cd project_folder`
`virtualenv venv`


choose python interpreter 
`virtualenv -p /usr/bin/python2.7 venv`

Activate virtual env 
`source venv/bin/activate`

Deactivate virtual env
`deactivate`

Delete virtual env
`rm -rf venv`

Notes: 
To keep requirements.txt up-to-date, store all pip imports into requirments.txt
`pip freeze > requirements.txt`

`pip install -r requirements.txt`



### Analysis on Stocks 


Fundamental analysis: This involves analyzing a company's financial statements, such as its revenue, earnings, debt, and cash flow. This can help you determine whether the company is profitable, how much debt it has, and whether it has a strong balance sheet.

Market analysis: This involves analyzing market trends, such as the overall direction of the stock market, the performance of the sector the company operates in, and the behavior of other market participants. This can help you understand whether the stock is overvalued or undervalued relative to the market.

Growth prospects: This involves analyzing a company's growth potential, such as its market share, product pipeline, and expansion plans. This can help you determine whether the company has the potential to grow its revenue and earnings in the future.

Competitive analysis: This involves analyzing a company's competitors, such as their market share, product offerings, and financial performance. This can help you understand whether the company is in a strong competitive position or not.

Management analysis: This involves analyzing the company's management team, such as their track record, experience, and leadership style. This can help you determine whether the company has a strong management team that can effectively execute its strategy.

Macroeconomic factors: This involves analyzing the broader economic environment, such as interest rates, inflation, and government policies. This can help you understand how the economy may impact the company's performance.

Technical analysis: This involves analyzing the stock's price and volume data, such as chart patterns, trading volume, and moving averages. This can help you identify trends and patterns in the stock's price behavior, which may provide insights into future price movements.