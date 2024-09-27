# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# show the title
st.title('Titanic App by Xiaoyue Wu')

# read csv and show the dataframe
df = pd.read_csv('train.csv')
st.write(df)

# create a figure with three subplots, size should be (15, 5)
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# show the box plot for ticket price with different classes
first_class = df[df.Pclass==1].Fare
second_class = df[df.Pclass==2].Fare
third_class = df[df.Pclass==3].Fare

first_class.plot.box(ax=ax[0])
ax[0].set_xlabel('PClass = 1')
ax[0].set_ylabel('Fare')

second_class.plot.box(ax=ax[1])
ax[1].set_xlabel('PClass = 2')
ax[1].set_ylabel('Fare')

third_class.plot.box(ax=ax[2])
ax[2].set_xlabel('PClass = 3')
ax[2].set_ylabel('Fare')


# you need to set the x labels and y labels


# a sample diagram is shown below
st.pyplot(fig)

