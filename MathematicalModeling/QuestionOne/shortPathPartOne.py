graph = {1: [2, 25],
         2: [1, 3],
         3: [2, 4, 25],
         4: [3, 5, 24, 25],
         5: [4, 6, 24],
         6: [5, 7, 23, 24],
         7: [6, 8, 22],
         8: [7, 9, 22],
         9: [8, 10, '15村庄', 16, 17, 21, 22],
         10: [9, 11, 13, '15村庄'],
         11: [10, '12矿山', 13],
         '12矿山': [11, 13, 14],
         13: [10, 11, '12矿山', 14, '15村庄'],
         14: ['12矿山', 13, '15村庄', 16],
         '15村庄': [9, 10, 13, 14, 16],
         16: [9, 14, '15村庄', 17, 18],
         17: [9, 16, 18, 21],
         18: [16, 17, 19, 20],
         19: [18, 20],
         20: [18, 19, 21],
         21: [9, 17, 20, 22, 23, '27终点'],
         22: [7, 8, 9, 21, 23],
         23: [6, 21, 22, 24, 26],
         24: [4, 5, 6, 23, 25, 26],
         25: [1, 3, 4, 24, 26],
         26: [23, 24, 25, '27终点'],
         '27终点': [21, 26]
         }


# 查找最短路径
def findShortestPath(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    shortestPath = []
    for node in graph[start]:
        if node not in path:
            newpath = findShortestPath(graph, node, end, path)
            if newpath:
                if not shortestPath or len(newpath) < len(shortestPath):
                    shortestPath = newpath
    return shortestPath


shortpath = findShortestPath(graph, 1, '27终点')
print('\n起点到终点最短路径：', shortpath)

shortpath1 = findShortestPath(graph, '15村庄', '27终点')
print('\n村庄到终点最短路径：', shortpath1)

shortpath2 = findShortestPath(graph, '12矿山', '27终点')
print('\n矿山到终点最短路径：', shortpath2)
shortpath3 = findShortestPath(graph, 1, '12矿山')
print('\n起点到矿山最短路径：', shortpath3)

shortpath4 = findShortestPath(graph, 1, '15村庄')
print('\n起点到村庄最短路径：', shortpath4)

shortpath5 = findShortestPath(graph, '12矿山', '15村庄')
print('\n村庄到矿山/矿山到村庄最短路径：', shortpath5)
