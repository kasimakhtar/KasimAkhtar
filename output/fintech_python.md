## Python in financial market analysis


This is a python file to analyze data in the financial markets. It converts the raw data to a python dataframe using pandas. Then, using talib, a technical calculation is applied to the data, in this case, the ADX calculation. An ADX greater than 25 is considered a useful indicator of a trend in the data. The number of rows where the ADX is greater than 25 is returned as a percentage of the total number of rows in the dataframe. This percentage can then be used to assess the usefulness of the technical indicator in the question (in this case, the ADX). In another post, I show a bash script that can run this python file on a large number of datafiles at once.


~~~

import pandas as pd
import talib

mydata = pd.read_table(r'/path/to/data/ZW_continuous_adjusted_1hour_sample.txt')
mydata = pd.DataFrame(mydata.DateTime.str.split(',').tolist(), columns = ['DateTime','Open','High','Low','Close','Volume'])



# CALCULATING ADX

def adx(high,low,close,period=14):
  return talib.ADX(high, low, close, period)
ADX = adx(mydata['High'],mydata['Low'],mydata['Close'])

criteria = ADX.where(ADX > 25).dropna()
nomRows = criteria.shape[0]
print(round((nomRows/len(mydata))*100))

~~~

The bulk of this code can be used on other technical market indicators as well, by just changing the ADX code to another calculation instead. I found that the last line, where the result is shown as a percentage, is useful in comparing results of different dataframes, as it reduces the size of the dataframe as a varying factor.
