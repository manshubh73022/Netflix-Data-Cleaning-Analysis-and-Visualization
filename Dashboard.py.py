#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("netflix1.csv")

st.title("Netflix Data: Cleaning, Analysis and Visualization")

# Top states
data = df.groupby('country')['rating'].sum().sort_values(ascending=False)

# Bar Chart
st.subheader("Top rating countries with most content on netflix")
st.bar_chart(data)

# Show Data
if st.checkbox("Show Raw Data"):
    st.write(df)


# In[ ]:




