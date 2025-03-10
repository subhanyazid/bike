"""
Nama: Ahmad Subhan Yazid
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datetime
plt.style.use("dark_background")

#dataset
dataset_df = pd.read_csv("all_data.csv")
dataset_df.sort_values(by="dteday", inplace=True)
dataset_df.reset_index(inplace=True)

#sidebar
dataset_df["dteday"] = pd.to_datetime(dataset_df["dteday"])
min_date = dataset_df["dteday"].min()
max_date = dataset_df["dteday"].max()


with st.sidebar:
    st.image('./assets/sepeda.jpg')
    mulai, selesai = st.date_input(
        label='Rentang Tanggal',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    
main_df = dataset_df[(dataset_df["dteday"] >= str(mulai)) & (dataset_df["dteday"] <= str(selesai))]

#fungsi
def penggunaan(df):
    penggunaan_df = df.resample(rule='M', on='dteday').agg({
        'cnt': 'sum'
    })
    penggunaan_df = penggunaan_df.reset_index() 
    return penggunaan_df

def casual(df):
    casual_df = df.resample(rule='M', on='dteday').agg({
        'casual': 'sum'
    })
    casual_df = casual_df.reset_index()
    return casual_df

def registered(df):
    registered_df = df.resample(rule='M', on='dteday').agg({
        'registered': 'sum'
    })
    registered_df = registered_df.reset_index()
    return registered_df

#eksekusi
penggunaan_df = penggunaan(main_df)
casual_df = casual(main_df)
registered_df = registered(main_df)

#plot
st.header('Dashboard untuk Dataset Bike-Sharing')
st.subheader('Penggunaan Harian')

#Penggunaan
total_penggunaan = penggunaan_df['cnt'].sum()
st.metric("Total Penggunaan", value=total_penggunaan)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    penggunaan_df["dteday"],
    penggunaan_df["cnt"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
 
st.pyplot(fig)

col1, col2 = st.columns(2)
#casual
with col1:
    total_casual = casual_df['casual'].sum()
    st.metric("Total Penggunaan", value=total_casual)

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        casual_df["dteday"],
        casual_df["casual"],
        marker='o', 
        linewidth=2,
        color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)

#registered
with col2:
    total_registered = registered_df['registered'].sum()
    st.metric("Total Penggunaan", value=total_registered)

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        registered_df["dteday"],
        registered_df["registered"],
        marker='o', 
        linewidth=2,
        color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)


year_now = datetime.date.today().year
nama = "Ahmad Subhan Yazid"
COPYRIGHT = 'Copyright © ' + str(year_now) + ' ' + nama
st.caption(COPYRIGHT)