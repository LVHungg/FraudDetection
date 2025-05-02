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

metric1, metric2, metric3 = st.columns([1, 1, 1])
metric1.metric(label="Total Transactions", value=df['Transaction_ID'].nunique())
metric2.metric(label="Total Fraud Transactions", value=df[df['Fraudulent'] == 1]['Transaction_ID'].nunique())
metric3.metric(label='Transaction Amount', value=f"{df['Transaction_Amount'].sum():,.2f}")
st.write("### Transaction Amount Distribution")

import plotly.graph_objects as go
import streamlit as st

# Tạo dữ liệu Sankey
sankey_data = df.groupby(['Transaction_Type', 'Device_Used', 'Payment_Method']).size().reset_index(name='Count')

# Mapping categorical values to numeric codes
transaction_types = sankey_data['Transaction_Type'].astype('category')
device_used = sankey_data['Device_Used'].astype('category')
payment_methods = sankey_data['Payment_Method'].astype('category')

transaction_type_codes = transaction_types.cat.codes
device_used_codes = device_used.cat.codes + transaction_types.cat.categories.size
payment_method_codes = payment_methods.cat.codes + transaction_types.cat.categories.size + device_used.cat.categories.size

# Combine source, target, value
source = transaction_type_codes.tolist() + device_used_codes.tolist()
target = device_used_codes.tolist() + payment_method_codes.tolist()
value = sankey_data['Count'].tolist() + sankey_data['Count'].tolist()

# Gộp tất cả nhãn lại
labels = list(transaction_types.cat.categories) + \
         list(device_used.cat.categories) + \
         list(payment_methods.cat.categories)

# Gán màu cho từng node
import random

def random_rgba(opacity=0.8):
    return f"rgba({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)},{opacity})"

# Tạo màu riêng cho từng node
node_colors = [random_rgba() for _ in range(len(labels))]

# Tạo màu link theo màu của node source
link_colors = [node_colors[src].replace("0.8", "0.4") for src in source]

# Vẽ biểu đồ Sankey
fig_optimized = go.Figure(data=[go.Sankey(
    valueformat=".0f",
    node=dict(
        pad=15,
        thickness=15,
        line=dict(color="black", width=0.5),
        label=labels,
        color=node_colors
    ),
    link=dict(
        source=source,
        target=target,
        value=value,
        color=link_colors
    )
)])

fig_optimized.update_layout(title_text="Transaction Flow Sankey Chart", font_size=10)
st.plotly_chart(fig_optimized, use_container_width=True)

# st.write("### Transaction Amount by Locatio

st.dataframe(df)