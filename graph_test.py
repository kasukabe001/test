import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# サンプルデータ生成
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
sales_data = pd.DataFrame({
    'date': dates,
    'sales': np.random.normal(100000, 20000, len(dates)).astype(int),
    'category': np.random.choice(['Electronics', 'Clothing', 'Books'], len(dates))
})

# 表データをアプリ上に表示
st.dataframe(sales_data)

# 月別集計
monthly_sales = sales_data.groupby(sales_data['date'].dt.to_period('M'))['sales'].sum().reset_index()
monthly_sales['date'] = monthly_sales['date'].dt.to_timestamp()

import streamlit as st

# これだけで折れ線グラフが完成

# H1見出し
st.markdown("# グラフアプリ")

st.line_chart(monthly_sales.set_index('date')['sales'])
# st.bar_chart(monthly_sales.set_index('date')['sales'])
# st.scatter_chart(monthly_sales.set_index('date')['sales'])
