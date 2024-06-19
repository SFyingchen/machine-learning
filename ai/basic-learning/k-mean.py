import re
import math
import random
import matplotlib.pyplot as plt
import networkx as nx

location_list_dict = """
{name:'兰州', geoCoord:[103.73, 36.03]},
{name:'嘉峪关', geoCoord:[98.17, 39.47]},
{name:'西宁', geoCoord:[101.74, 36.56]},
{name:'成都', geoCoord:[104.06, 30.67]},
{name:'石家庄', geoCoord:[114.48, 38.03]},
{name:'拉萨', geoCoord:[102.73, 25.04]},
{name:'贵阳', geoCoord:[106.71, 26.57]},
{name:'武汉', geoCoord:[114.31, 30.52]},
{name:'郑州', geoCoord:[113.65, 34.76]},
{name:'济南', geoCoord:[117, 36.65]},
{name:'南京', geoCoord:[118.78, 32.04]},
{name:'合肥', geoCoord:[117.27, 31.86]},
{name:'杭州', geoCoord:[120.19, 30.26]},
{name:'南昌', geoCoord:[115.89, 28.68]},
{name:'福州', geoCoord:[119.3, 26.08]},
{name:'广州', geoCoord:[113.23, 23.16]},
{name:'长沙', geoCoord:[113, 28.21]},
//{name:'海口', geoCoord:[110.35, 20.02]},
{name:'沈阳', geoCoord:[123.38, 41.8]},
{name:'长春', geoCoord:[125.35, 43.88]},
{name:'哈尔滨', geoCoord:[126.63, 45.75]},
{name:'太原', geoCoord:[112.53, 37.87]},
{name:'西安', geoCoord:[108.95, 34.27]},
//{name:'台湾', geoCoord:[121.30, 25.03]},
{name:'北京', geoCoord:[116.46, 39.92]},
{name:'上海', geoCoord:[121.48, 31.22]},
{name:'重庆', geoCoord:[106.54, 29.59]},
{name:'天津', geoCoord:[117.2, 39.13]},
{name:'呼和浩特', geoCoord:[111.65, 40.82]},
{name:'南宁', geoCoord:[108.33, 22.84]},
//{name:'西藏', geoCoord:[91.11, 29.97]},
{name:'银川', geoCoord:[106.27, 38.47]},
{name:'乌鲁木齐', geoCoord:[87.68, 43.77]},
{name:'香港', geoCoord:[114.17, 22.28]},
{name:'澳门', geoCoord:[113.54, 22.19]}
"""

# 将数据转换到下面的格式----使用正则表达式
pattern = re.compile(r"name:'(\w+)',\s+geoCoord:\[(\d+.\d+),\s(\d+.\d+)\]")

city_location = {}

for line in location_list_dict.split("\n"):
    info = pattern.findall(line)
    if not info: continue
    city, lat, long = info[0]
    city_location[city] = (float(lat), float(long))


# 这个函数用来计算地球上两个地点之间的距离
def geo_distance(origin, destination):
    """
    Calculate the Haversine distance.

    Parameters
    ----------
    origin : tuple of float
        (lat, long)
    destination : tuple of float
        (lat, long)

    Returns
    -------
    distance_in_km : float

    Examples
    --------
    >>> origin = (48.1372, 11.5756)  # Munich
    >>> destination = (52.5186, 13.4083)  # Berlin
    >>> round(distance(origin, destination), 1)
    504.2
    """
    lon1, lat1 = origin
    lon2, lat2 = destination
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d


# print(geo_distance(city_location["兰州"], city_location["北京"]))
#
# city_graph = nx.Graph()
# city_graph.add_nodes_from(list(city_location.keys()))
#
# nx.draw(city_graph, city_location, with_labels=True, node_size=30)


# plt.show()
#
# all_x = []
# all_y = []
# for _, location in city_location.items():
#     x, y = location
#     all_x.append(x)
#     all_y.append(y)
#
# k = 5


def get_center_by_random(all_x, all_y):
    x = random.uniform(min(all_x), max(all_x))
    y = random.uniform(min(all_y), max(all_y))
    return x, y


# print(center)

# 将所有点和随机点 进行归类
from collections import defaultdict
import numpy as np


# 开始更新中心点
def iteration_once(center, close_list, threshold=5):
    has_changed = False
    for c in close_list.keys():
        current_center = center[str(c)]
        neighbors_list = close_list[c]
        new_center = np.mean(neighbors_list, axis=0)
        print(geo_distance(current_center, new_center))
        if geo_distance(current_center, new_center) > threshold:
            center[str(c)] = new_center
            has_changed = True
        else:
            pass

    return center, has_changed


def K_mean(data_list, k, threshold=5):
    xs = data_list[:, 0]
    ys = data_list[:, 1]

    K = k
    # 随机获得中心点
    center = {"{}".format(str(i + 1)): get_center_by_random(xs, ys) for i in range(K)}

    changed = True
    while changed:
        close_list = defaultdict(list)

        for x, y, in zip(xs, ys):
            closePoint, distance = min([(i, geo_distance(center[i], (x, y))) for i in center], key=lambda t: t[1])
            close_list[closePoint].append([x, y])

        center, changed = iteration_once(center, close_list, threshold)
        print("iteration")

    return center


K_mean(np.array(list(city_location.values())), 5, threshold=5)
