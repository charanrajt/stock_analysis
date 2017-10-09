
This repository consists of python codes to generate few techincal and fundamental indicators of a stock lsted in US market.

This code geneartes few techincal and fundamental indicators of a stock lsted in US market. Techincal indicators are used according to  http://www.maheshkaushik.com/

##Requirements
Install the required packges using
pip install -r requirements.txt

#Usage 
python stock_summary.py

Enter the stock ticker, it will produce data.xlsx, an excel with

Ticker          : Ticker of the stock	
CMP	            : Current Market Price 
BP	            : Base price
                 Average  last three years closing price
                 buy near 1.2*base price in uptreand and sell near 
                 1.4 with stop loss of 1.1 * base price
                 For trading buy above 5% of base price in uptrend


CMP/BP	       : CMP/BP (look for the stocks near 1 to 1.2 ragnge)
52-High        : 52 wk high
52-Low	       : 52 wk low  
H/L	           : High to low ratio
               This is an indicator for the  voltality of the stock.
               Invest only when above ratio is less than 2  
H-away	       : How much % away from 52wk high
L-away         : How much % away from 52wk low
Div-Y	       : Dividebd yield, better to choose dividend giving stocks 
                in case holding for long-term, at least we will get some div 
P/E	           : Price to Earning ratio, aviod stocks with high PE (>20?)
P/B            : PB aviod stocks with high PB
PEG            : PEG ratio
PLP	           : Peter Lynch Fair Value=15*CMP/PE
PLP-away	   : How much % away from PLP
Gra_no         : Graham price= sqrt(22.5*CMP/PE*CMP/PB)
Gra_awy	       :  How much % away from Gra_no
TP             : Mahesh Kaushik Target price: (base_price+Sales+Book value)/3
TP_away	       :  How much % away from TP
Finviz_TP	   : Finviz Target price (avg of the NASDAQ analysit predictions)
Rec            : Finviz Reco 1-5(strong buy - strong sell)



## License
The MIT License
