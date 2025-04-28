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
# df = pd.read_csv('C:\\Users\\levan\\FraudDetection\\data\\Fraud Detection Dataset.csv')


# st.dataframe(df)