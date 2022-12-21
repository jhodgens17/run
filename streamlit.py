#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import streamlit as st
df = pd.read_csv('activities.csv')
df2 = df[df['Activity ID'].isin([8266253440, 8270420755])]
df3 = df2[['Activity ID', 'Activity Date', 'Elapsed Time', 'Distance']]
st.write(df3)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




