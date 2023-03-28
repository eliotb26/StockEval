# Stock Evaluator

Purpose to provide quick stock evaluation metrics for personal use. 


## Quandl 
`pip install nasdaq-data-link`
Documentation: https://demo.quandl.com/docs-and-help
Profile: https://data.nasdaq.com/account/profile

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