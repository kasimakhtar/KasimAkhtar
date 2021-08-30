## Python in financial market analysis


This is a python file to analyze data in the financial markets. It converts the data to a python dataframe using pandas, and then using talib, a technical calculation is applied to the data called the ADX. Then the data is scanned to find the number of rows where the ADX is greater than 25. And finally, this number (of rows) is gievn as a percentage of the total number of rows in the dataframe. Elsewhere, I created a bash script that can run this python file on a large number of datafiles at once.


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

The bulk of this code can be used on other technical market indicators as well, by just changing the ADX code to another calcultion. I found that the last line, where the result is shown as a percentage, is useful in comparing results of different sized dataframes. 
