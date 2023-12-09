import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# データの読み込み
df = pd.read_csv(r"C:\Users\junji\Desktop\大学院\thesis\HSS2023\scene_en\privateDB_en.csv", encoding='UTF-8')

# ネットワークごとに中心性を計算
for i in range(len(df)):  #len(df)
    # 各行ごとに無向グラフを作成
    G = nx.Graph()

    # ノードとエッジをグラフに追加する
    for j in range(6, len(df.columns) - 1, 2):  # 最後の製品IDと場所の列は無視
        location = df.iloc[i][j + 1]
        if pd.notnull(location):
            G.add_node(location)

    # エッジを追加する
    for j in range(6, len(df.columns) - 3, 2):  # 最後の2列（製品IDと場所）は無視
        location_1 = df.iloc[i][j + 1]
        location_2 = df.iloc[i][j + 3]
        if pd.notnull(location_1) and pd.notnull(location_2):
            G.add_edge(location_1, location_2)


# 次数中心性、近接中心性、媒介中心性を計算
    degree_centrality = nx.degree_centrality(G)
    closeness_centrality = nx.closeness_centrality(G)
    betweenness_centrality = nx.betweenness_centrality(G)
    pagerank_centrality = nx.pagerank(G)

    video_title = df.iloc[i]['title']

    print(f'動画タイトル: {video_title}')

    # 各工程の中心性を表示
    print("次数中心性:")
    for node, centrality in sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True):
        print(f'{node}: {centrality}')

    print("\n近接中心性:")
    for node, centrality in sorted(closeness_centrality.items(), key=lambda x: x[1], reverse=True):
        print(f'{node}: {centrality}')

    print("\n媒介中心性:")
    for node, centrality in sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True):
        print(f'{node}: {centrality}')

    print("\nPage Rank:")
    for node, centrality in sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True):
        print(f'{node}: {centrality}')

    print('\n')

# ネットワーク図の描画
    plt.figure()
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_size=8, node_size=1000, font_color='black', node_color='skyblue', font_weight='bold', arrowsize=10, font_family='Meiryo')
    #plt.title(f'動画タイトル: {df.iloc[i]["title"]}')
    plt.show()

# 最大値算出
"""
    max_degree = max(degree_centrality, key=degree_centrality.get)
    max_closeness = max(closeness_centrality, key=closeness_centrality.get)
    max_betweenness = max(betweenness_centrality, key=betweenness_centrality.get)

    video_title = df.iloc[i]['title']

    print(f'動画タイトル: {video_title}')
    print(f'次数中心性の最大値: {max_degree} - {degree_centrality[max_degree]}')
    print(f'近接中心性の最大値: {max_closeness} - {closeness_centrality[max_closeness]}')
    print(f'媒介中心性の最大値: {max_betweenness} - {betweenness_centrality[max_betweenness]}')
    print('\n')
"""


