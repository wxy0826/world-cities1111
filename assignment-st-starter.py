# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# show the title
st.title("Titanic App by Xiaoyue Wu")

# read csv and show the dataframe
df = pd.read_csv('train.csv') 
st.subheader('Dataframe Preview')
st.write(df) 

# create a figure with three subplots, size should be (15, 5)
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
# show the box plot for ticket price with different classes
sns.boxplot(x='class', y='ticket_price', data=df, ax=axes[0])
axes[0].set_xlabel('Class')
axes[0].set_ylabel('Ticket Price')
axes[0].set_title('Ticket Price Distribution by Class')
# you need to set the x labels and y labels
sns.boxplot(x='another_category', y='another_value', data=df, ax=axes[1])
axes[1].set_xlabel('Another Category')  
axes[1].set_ylabel('Another Value')  
axes[1].set_title('Another Visualization Title')  
# a sample diagram is shown below


