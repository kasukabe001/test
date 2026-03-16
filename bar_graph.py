import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

st.set_page_config(
    page_title="Streamlit App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 日付範囲を生成
date_range = pd.date_range(start='2024-05-01', periods=15, freq='D')

# 売上見込と売上実績のデータをランダムに生成
sales_forecast = np.random.randint(100, 300, size=15)
sales_actual = np.random.randint(80, 250, size=15)

# データフレームを作成
data = pd.DataFrame({
    '日付': date_range,
    '売上見込': sales_forecast,
    '売上実績': sales_actual
})

# 日付列を文字列に変換
data['日付'] = data['日付'].dt.strftime('%Y-%m-%d')

# グラフ化するためにデータ型を更新
data_long = pd.melt(data, id_vars=['日付'], value_vars=['売上見込', '売上実績'])

# Altairチャートを作成
chart = alt.Chart(data_long).mark_bar(
    opacity=1
    ).encode(
    column=alt.Column('日付:O', spacing=5, header=alt.Header(labelOrient="bottom", title=None)),
    x=alt.X('variable', sort=['売上見込', '売上実績'], axis=None),
    y=alt.Y('value:Q', title=None),
    color=alt.Color('variable', title=None)
).configure_view().properties(width=60, height=400)

# Streamlitにチャートを表示
st.altair_chart(chart)

