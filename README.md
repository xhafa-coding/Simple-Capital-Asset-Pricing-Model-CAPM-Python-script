A simple Capital Asset Pricing Model (CAPM) created using Python.

The script makes use of the CAPM as given by:

Ri = Rf + (βi * (Rm – Rf))

The CAPM is used to give an insight into whether an invesment is worth the added risk compared to investing into a 
risk free security. Its heavily rooted in the Economic theory of 'Opportunity Cost', in which choosing one option 
means giving up another.

Beta is a measure of the volatility or systematic risk of a security compared to the entire market. Beta is used in
the CAPM model to describe the relationship between systematic risk and the expected return for assets. 

Beta = 1, denoted a price activity that is closely related with the market
Beta < 1, suggests a defensive security meaning it is less volatile than the market
Beta > 1, suggests an aggressive security meaning it is more volatile than the market. For example, a beta of 1.34 
suggests a security 34% more volatile than the market

Ra - The Expected Return of a Security
Rf - Risk free rate of return
Rm - Market return (In our case the S&P 500)
βi - Measure of systematic risk
(Rm - Rf) - Risk Premium/Incentive to invest

The dataset used and provided (stocks_dataset.csv) contains stock price data from 11/7/2013 to 8/7/2020. My attempt
uses Tesla stock (TSLA) compared to the S&P500
