# Dashboard

Streamlit Cloud: <a href='https://bike-sharing.streamlit.app' target='_blank' title='Bike Sharing Dashboard | Streamlit'>Bike Sharing Dashboard</a>

## Description

Ini merupakan dasboard dari hasil belajar analisis EDA terhadap dataset <a href='https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ' target='_blank' title='Bike-sharing-dataset.zip'>Bike Sharing Dataset</a>. 

## Directory

- `/assets`: Berisi gambar aset
- `all_df.csv`: Dataset yang digunakan
- `README.md`: File informasi isi repo
- `Dashbard.py`: File utama untuk menjalankan dashboard
- `requirements.txt`: File untuk menuliskan library yang digunakan

## Installation

Ikuti langkah-langkah berikut:

1. Kloning repo
   ```bash
   git clone https://github.com/aNdr3W03/Bike-Sharing-Dashboard.git
   ```

2. Buat Python Virtual Environment
   ```bash
   virtualenv venv
   ```

2. Aktivasi Environtment
   ```bash
   venv\Scripts\activate
   ```

4. Instal semua library di "requirements.txt"
   ```bash
   pip install -r requirements.txt
   ```

5. Jalankan Streamlit Dashboard
   ```bash
   streamlit run Dashboard.py
   ```
