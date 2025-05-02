import streamlit as st 
import os
import pandas as pd

import plotly.express as px

icon_path = os.path.join("icons", "frauddetection.png")

st.set_page_config(
    page_title = 'Fraud Detection Monitoring',
    page_icon = 'frauddetection.png',
    # initial_sidebar_state="expanded",
    layout = 'wide',
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# ",
        'Get help': 'mailto:levanhung2611@gmail.com'
    }
)

st.header('Fraud Detection Monitoring')

# Lấy đường dẫn thư mục hiện tại của file Dashboard.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Di chuyển ra thư mục cha (ra khỏi /src) rồi vào thư mục data
data_path = os.path.join(BASE_DIR, '..', 'data', 'Fraud Detection Dataset.csv')

# Đảm bảo path đúng bằng cách chuẩn hóa lại
data_path = os.path.normpath(data_path)

# Đọc file
df = pd.read_csv(data_path)

st.dataframe(df)