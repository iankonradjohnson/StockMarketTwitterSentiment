#!/usr/bin/env python # coding: utf-8 
# In[1]: 
# API Key: b6TQLG716rBiKFACGDMiBbWHO 
# API Secret Key: jzZqWLdVoRWiLRAmPjQOQqhMgTmUXvU34wOsYh5LIO05g275Tt 
# Bearer Token: AAAAAAAAAAAAAAAAAAAAALAtLQEAAAAAG%2BCbFgQRACOdtu2yDPmKw4YEdk0%3DsUY4lKocVflcCUnivhLQhtwdpE8bZ2YMwC4O2bmFIW55ZmWMJc # In[2]: 
# !pip install twint 
# !pip install nest_asyncio 
# In[4]: 
import twint 
from datetime import timedelta, date 
import nest_asyncio 
nest_asyncio.apply() 
# In[5]: 
def get_tweets_on_date(single_date, limit, csv_file): 
    c = twint.Config() 
    c.Hide_output = True
    c.Limit = limit 
    c.Search = "a" 
    day_before = single_date - timedelta(days=1) 
    day_after = single_date + timedelta(days=1) 
    c.Since = day_before.strftime("%Y-%m-%d") 
    c.Until = day_after.strftime("%Y-%m-%d") 
    c.Store_csv = True 
    c.Lang = 'en' 
    c.Custom_csv = ["id", "user_id", "username", "tweet"] 
    c.Output = (csv_file) 
    twint.run.Search(c) 
def daterange(start_date, end_date): 
    for n in range(int((end_date - start_date).days)): 
        yield start_date + timedelta(n) 
# In[ ]: 
def get_tweets_in_range(start_date, end_date, save_file, limit=50000):
    for single_date in daterange(start_date, end_date): 
        try:
            get_tweets_on_date(single_date, limit, save_file) # In[ ]: 
        except KeyboardInterrupt as ke:
            raise
        except Exception as e:
            print(e)
            continue