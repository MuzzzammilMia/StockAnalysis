#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


print('Pandas version:',pd.__version__)
print('Matplotlib version:',mpl.__version__)
print('Numpy version:',np.__version__)


# In[22]:


#Converting the csv file to the DataFrame.

CompanyCheck = pd.read_csv("ticker_list.csv")

#Formatting the Name column to be standardised.
CompanyCheck['Name'] = CompanyCheck['Name'].str.replace('.','')
CompanyCheck['Name'] = CompanyCheck['Name'].str.replace(' ','')
CompanyCheck['Name'] = CompanyCheck['Name'].str.lower()
CompanyCheck.head()


# In[23]:


#Formatting the Input to be the same as DataFrame name column.
ChosenCompany = input("Please enter a company name:") #CompanyName
ChosenCompany = ChosenCompany.lower()
ChosenCompany = ChosenCompany.replace('.','')
ChosenCompany = ChosenCompany.replace(' ','')

print(ChosenCompany)


# In[24]:


#filters for the company name, returns an arr with the corresponding ticker value.
TickValue = CompanyCheck[CompanyCheck['Name']==ChosenCompany]["Ticker"].values

print(TickValue)


# In[33]:


#Acceptable time params in order for the API to receive information
Intervals = ["1min","5min","15min","30min","45min","1h","2h","4h","1day","1week","1month"]
Time = input("Please enter a timeframe: ")
NumCalls = input("Please choose the number of calls:")


# In[37]:



#API 
td = TDClient(apikey="password") #Removed the API key
ts = td.time_series(symbol=TickValue[0],interval=time,outputsize=NumCalls, timezone="America/New_York",)

#Returning a dataFrame with the time series data
Stock1 = ts.as_pandas()


# In[35]:


# Plotting high/low values
plt.figure()
hl=Stock1.loc[:,"high":"low"]

hl.plot(linewidth=1)

#Formatting the graph
plt.xlabel('Time')
plt.grid(True)
plt.ylabel('Cost measured in dollars ($)')
plt.title('High/Low values : {}'.format(ChosenCompany))


# In[ ]:




