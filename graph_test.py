import plotly.graph_objects as go

# 1. データの準備
x_data = ['January', 'February', 'March', 'April', 'May']
y_data = [10, 22, 15, 28, 20]

# 2. グラフ（棒グラフ）の作成
fig = go.Figure(data=[go.Bar(
    x=x_data,
    y=y_data,
    marker_color='indianred' # 棒の色をオシャレに
)])

# 3. レイアウトの設定（タイトルなど）
fig.update_layout(
    title='月別売上データ',
    xaxis_title='月',
    yaxis_title='売上（万円）',
    template='plotly_white' # 白背景の清潔感あるテーマ
)

# 4. HTMLファイルとして保存
# これをサーバーにアップロードすればWebで公開できます
# fig.write_html('my_graph.html')

# 5. 確認のために自動でブラウザを開く（任意）
fig.show()
