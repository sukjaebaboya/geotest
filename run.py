import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point, Polygon

# 가상 예산 데이터 생성
data = {
    'Project': ['Project A', 'Project B', 'Project C', 'Project D', 'Project E'],
    'Initial Budget': [500000, 750000, 300000, 450000, 600000],
    'Final Budget': [520000, 760000, 310000, 470000, 620000],
    'Spent': [480000, 720000, 290000, 430000, 580000],
    'Latitude': [37.5665, 35.1796, 37.4563, 35.9078, 37.5407],
    'Longitude': [126.9780, 129.0756, 126.7052, 127.7669, 126.9780]
}

df = pd.DataFrame(data)

# 예산 초과 여부 계산
df['Over Budget'] = df['Final Budget'] - df['Initial Budget']
df['Under Budget'] = df['Initial Budget'] - df['Spent']

# 데이터 출력
print(df)

# 지리 데이터프레임 생성
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))

# 세계 지도 불러오기
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# 지도에 프로젝트 위치 시각화
ax = world.plot(figsize=(10, 6))
gdf.plot(ax=ax, color='red', markersize=50)
plt.title('Project Locations')
plt.show()
