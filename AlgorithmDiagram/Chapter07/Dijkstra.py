# 建立结点之间的关系
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {} #终点没有任何邻居

# 创建开销表
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 创建父节点表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 创建判断是否处理过结点的数组
processed = []

# 打印所有节点的开销
print(costs)

# 找到当前结点的所有邻居的最小权值节点
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: # 遍历所有的节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # 如果当前节点的开销更低且未处理过
            lowest_cost = cost # 就将其视为开销最低的节点
            lowest_cost_node = node
    return lowest_cost_node

def Dijkstra():
    node = find_lowest_cost_node(costs) # 在未处理的节点中找出开销最小的节点
    while node is not None: # 这个while循环在所有的节点都被处理过后结束
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys(): # 遍历当前节点的所有邻居
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost: # 如果经当前节点前往该邻居更近
                costs[n] = new_cost # 就更新该邻居的开销
                parents[n] = node # 同时将该邻居的父节点设置为当前节点
        processed.append(node) # 将当前结点标记为处理过
        node = find_lowest_cost_node(costs) # 找出接下来要处理的节点，并循环

# 迪杰斯特拉算法
Dijkstra()

# 打印所有节点的开销
print(costs)
