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

# Pertanyaan 2: Penggunaan berdasarkan hari
st.subheader("Distribusi Penggunaan Sepeda Berdasarkan Hari (Casual vs Registered)")

# Agregasi
by_day = main_df.groupby('weekday')[['casual', 'registered']].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
by_day.plot(x='weekday', kind='bar', stacked=True, ax=ax, color=["#FFB74D", "#4FC3F7"])

# Label dan judul
ax.set_title("Jumlah Pengguna Sepeda per Hari (0=Senin ... 6=Minggu)")
ax.set_xlabel("Hari")
ax.set_ylabel("Jumlah Pengguna")
ax.legend(["Casual", "Registered"])

st.pyplot(fig)

# Pertanyaan 3: Penggunaan berdasarkan jam
st.subheader("Distribusi Penggunaan Sepeda Berdasarkan Jam")

# Baca ulang data jam-jaman
hour_df = pd.read_csv("all_data.csv")  
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])
filtered_hour_df = hour_df[(hour_df["dteday"] >= str(mulai)) & (hour_df["dteday"] <= str(selesai))]

# Agregasi
by_hour = filtered_hour_df.groupby("hr")["cnt"].sum().reset_index()

fig, ax = plt.subplots(figsize=(10,6))
sns.lineplot(data=by_hour, x="hr", y="cnt", marker='o', ax=ax, color="#81C784")

ax.set_title("Jumlah Pengguna Sepeda per Jam")
ax.set_xlabel("Jam (0-23)")
ax.set_ylabel("Jumlah Pengguna")

st.pyplot(fig)


year_now = datetime.date.today().year
nama = "Ahmad Subhan Yazid"
COPYRIGHT = 'Copyright © ' + str(year_now) + ' ' + nama
st.caption(COPYRIGHT)