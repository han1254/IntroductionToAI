import pandas as pd
from pandas import Series, DataFrame

# 城市信息：city1 city2 path_cost
_city_info = None

# 按照路径消耗进行排序的FIFO,低路径消耗在前面
_frontier_priority = []


# 节点数据结构
class Node:
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost


def main():
    global _city_info
    import_city_info()

    while True:
        src_city = input('input src city\n')
        dst_city = input('input dst city\n')
        result = breadth_first_search(src_city, dst_city)
        if not result:
            print('from city: %s to city %s search failure' % (src_city, dst_city))
        else:
            print('from city: %s to city %s search success' % (src_city, dst_city))
            path = []
            while True:
                path.append(result.state)
                if result.parent is None:
                    break
                result = result.parent
            size = len(path)
            for i in range(size):
                if i < size - 1:
                    print('%s->' % path.pop(), end='')
                else:
                    print(path.pop())


def import_city_info():
    global _city_info
    data = [{'city1': 'Oradea', 'city2': 'Zerind', 'path_cost': 71},
            {'city1': 'Oradea', 'city2': 'Sibiu', 'path_cost': 151},
            {'city1': 'Zerind', 'city2': 'Arad', 'path_cost': 75},
            {'city1': 'Arad', 'city2': 'Sibiu', 'path_cost': 140},
            {'city1': 'Arad', 'city2': 'Timisoara', 'path_cost': 118},
            {'city1': 'Timisoara', 'city2': 'Lugoj', 'path_cost': 111},
            {'city1': 'Lugoj', 'city2': 'Mehadia', 'path_cost': 70},
            {'city1': 'Mehadia', 'city2': 'Drobeta', 'path_cost': 75},
            {'city1': 'Drobeta', 'city2': 'Craiova', 'path_cost': 120},
            {'city1': 'Sibiu', 'city2': 'Fagaras', 'path_cost': 99},
            {'city1': 'Sibiu', 'city2': 'Rimnicu Vilcea', 'path_cost': 80},
            {'city1': 'Rimnicu Vilcea', 'city2': 'Craiova', 'path_cost': 146},
            {'city1': 'Rimnicu Vilcea', 'city2': 'Pitesti', 'path_cost': 97},
            {'city1': 'Craiova', 'city2': 'Pitesti', 'path_cost': 138},
            {'city1': 'Fagaras', 'city2': 'Bucharest', 'path_cost': 211},
            {'city1': 'Pitesti', 'city2': 'Bucharest', 'path_cost': 101},
            {'city1': 'Bucharest', 'city2': 'Giurgiu', 'path_cost': 90},
            {'city1': 'Bucharest', 'city2': 'Urziceni', 'path_cost': 85},
            {'city1': 'Urziceni', 'city2': 'Vaslui', 'path_cost': 142},
            {'city1': 'Urziceni', 'city2': 'Hirsova', 'path_cost': 98},
            {'city1': 'Neamt', 'city2': 'Iasi', 'path_cost': 87},
            {'city1': 'Iasi', 'city2': 'Vaslui', 'path_cost': 92},
            {'city1': 'Hirsova', 'city2': 'Eforie', 'path_cost': 86}]

    _city_info = DataFrame(data, columns=['city1', 'city2', 'path_cost'])
    # print(_city_info)


def breadth_first_search(src_state, dst_state):
    global _city_info
    node = Node(src_state, None, None, 0)
    if node.state == dst_state:
        return node
    frontier = [node]
    visited = []
    while True:
        if len(frontier) == 0:
            return False
        node = frontier.pop(0)
        visited.append(node.state)
        for i in range(len(_city_info)):
            dst_city = ''
            if node.state == _city_info['city1'][i]:
                dst_city = _city_info['city2'][i]
            elif node.state == _city_info['city2'][i]:
                dst_city = _city_info['city1'][i]
            child = Node(dst_city, node, 'go', node.path_cost + _city_info['path_cost'][i])
            if child.state not in visited and not is_node_in_frontier(frontier, child):
                if child.state == dst_state:
                    print('\t\t find the goal!')
                    return child
                frontier.append(child)
                print('\t\t child be added to frontier')


def is_node_in_frontier(frontier, node):
    for x in frontier:
        if node.state == x.state:
            return True
    return False


if __name__ == '__main__':
    main()