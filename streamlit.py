#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import streamlit as st
df = pd.read_csv('activities.csv')
df2 = df[df['Activity ID'].isin([8266253440, 8270420755])]
df3 = df2[['Activity ID', 'Activity Date', 'Elapsed Time', 'Distance']]
df4 = df3.reset_index()
df4['date'] = pd.to_datetime(df4['Activity Date']).dt.date
df4['duration_minutes'] = df4['Elapsed Time']//60
df4['duration_seconds'] = df4['Elapsed Time'] - df4['duration_minutes']*60
df4['mileage']=df4['Distance']*0.621371
df5 = df4.drop(['index', 'Activity ID', 'Elapsed Time', 'Distance', 'Activity Date'], axis=1)
st.header('All run data:')
st.write(df5)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




