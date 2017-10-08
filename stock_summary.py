import time
import urllib2
from bs4 import BeautifulSoup
from yahoo_finance import Share
import string
from yahoo_historical import Fetcher

data = Fetcher("AAPL", [2007,1,1], [2017,1,1])

def func_finviz_reader(symbol):    
  
    url = r'http://finviz.com/quote.ashx?t={}'\
    				.format(symbol.lower())
    #SITE = "http://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(url, headers=hdr)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page,'lxml')
    
    Rec=  soup.find(text = r'Recom')
    Rec_ = Rec.find_next(class_='snapshot-td2').text
    
    TP=  soup.find(text = r'Target Price')
    TP_ =TP.find_next(class_='snapshot-td2').text
    
    if TP_=='-':
        TP_=0;
    if Rec_=='-':
        Rec_=1000;    
    
    return Rec_, TP_, 


def get_historical_data(name, date1,date2):
    d1=[int(date1[0:4]),int(date1[5:7]),int(date1[8:10])]
    d2=[int(date2[0:4]),int(date2[5:7]),int(date2[8:10])]
    temp=Fetcher(name,d1,d2).getHistorical()
    return temp['Adj Close']

import datetime
#import pandas as pd
import xlsxwriter
#import matplotlib.pyplot as plt

import numpy as np
today= datetime.datetime.now()
date2= str(today.date())
date1= str(today.replace(2014).date())

workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()
t1=time.time()
row = 0
col = 0

worksheet.write(row, col,'Ticker')
worksheet.write(row, col + 1, 'CMP')
worksheet.write(row, col + 2, 'BP')
worksheet.write(row, col + 3, 'CMP/BP')
worksheet.write(row, col + 4, '52-High')
worksheet.write(row, col + 5, '52-Low')
worksheet.write(row, col + 6, 'H/L')
worksheet.write(row, col + 7, 'H-away')
worksheet.write(row, col + 8, 'L-away')
worksheet.write(row, col + 9, 'Div-Y')
worksheet.write(row, col + 10, 'P/E')
worksheet.write(row, col + 11, 'P/B')
worksheet.write(row, col +12, 'PEG')
worksheet.write(row, col +13, 'PLP')
worksheet.write(row, col +14, 'PLP-away')
worksheet.write(row, col +15, 'Gra_no')
worksheet.write(row, col +16, 'Gra_awy')
worksheet.write(row, col +17, 'TP')
worksheet.write(row, col +18, 'TP_away')
worksheet.write(row, col + 19, 'Finviz_TP')
worksheet.write(row, col + 20, 'Rec')  
ticker=raw_input('Enter stock ticker\n')

row=row+1;
for jj in range(1) :   
    
    stock=Share(ticker)
    data1= get_historical_data(ticker, date1,date2)
#    h_l_ratio=float(stock.get_year_high())/float(stock.get_year_low())
    if np.shape(data1)[0]!=0:
        data=np.array(data1);
        CMP=data[-1]   
        
        if stock.get_year_high():
            high=float(stock.get_year_high());
        else :
            high=1.0;         
        if stock.get_year_low():
            low=float(stock.get_year_low());
        else :
            low=1.0;  
            
        if stock.get_dividend_yield():
            div=float(stock.get_dividend_yield());
        else :
            div=0.0;         
        if stock.get_price_earnings_ratio():
            PE=float(stock.get_price_earnings_ratio());
        else :
            PE=1000.0;     
            
        if stock.get_price_book():
            PB=float(stock.get_price_book());
        else :
            PB=1000.0;         
        if stock.get_price_earnings_growth_ratio():
            PEG=float(stock.get_price_earnings_growth_ratio());
        else :
            PEG=1000.0;
        if stock.get_price_sales():
            PSR=float(stock.get_price_sales());
        else :
            PSR=1000.0;   
            
        if PB==0.0:
           PB=1000.0; 
        if PSR==0.0:
           PSR=1000.0;  
        tik=string.replace(ticker,".","-")
        Rec_, Finviz_TP_=func_finviz_reader(tik)
        
        if Rec_:
            Rec=float(Rec_);
        else :
            Rec=1000.0; 
            
        if Finviz_TP_:
            Finviz_TP=float(Finviz_TP_);
        else :
            Finviz_TP=0.0;    
           
           
        Sales=CMP/PSR;    
        H_away=np.round((high-CMP)/CMP*100,2)
        L_away=np.round((low-CMP)/CMP*100,2)
        H_L=np.round(high/low,2)
        pl_price=15*CMP/PE;
        gh_no=np.sqrt(22.5*CMP/PE*CMP/PB)
        pl_away=(pl_price-CMP)/CMP*100;
        gh_away=(gh_no-CMP)/CMP*100;        
        base_price=np.mean(data) #Avg of last three years data
        target_price=(base_price+Sales+CMP/PB)/3
        tp_away=(target_price-CMP)/CMP*100;
        
        
        worksheet.write(row, col,ticker)
        worksheet.write(row, col + 1, CMP)
        worksheet.write(row, col + 2,  base_price)
        worksheet.write(row, col + 3,  np.round(CMP/base_price,2))
        worksheet.write(row, col + 4, high)
        worksheet.write(row, col + 5, low)
        worksheet.write(row, col + 6, H_L)
        worksheet.write(row, col + 7, H_away)
        worksheet.write(row, col + 8, L_away)
        worksheet.write(row, col + 9, div)
        worksheet.write(row, col + 10, PE)
        worksheet.write(row, col + 11, PB)
        worksheet.write(row, col + 12, PEG)
        worksheet.write(row, col + 13, pl_price) 
        worksheet.write(row, col + 14, pl_away)   
        worksheet.write(row, col +15, gh_no)
        worksheet.write(row, col +16, gh_away)
        worksheet.write(row, col +17, target_price)
        worksheet.write(row, col +18, tp_away)
        worksheet.write(row, col + 19, Finviz_TP)
        worksheet.write(row, col + 20, Rec)     

    
        row=row+1;
        print jj
    
    
#    worksheet.write(row, col,     tickers[jj])
#    worksheet.write(row, col + 1, cost)
#    



workbook.close()   
print "Running time is: ", time.time()-t1, 'sec'  
 
