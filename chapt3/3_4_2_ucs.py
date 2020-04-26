import pandas as pd
#uniform cost search
from pandas import DataFrame
_city_info = None

_frontier_priority = []

class Node:
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

def main():
    global _frontier_priority
    import_city_info()
    citys = []
    src_state = input('start_state:')
    des_state = input('des_state:')
    node = uniform_cost_search(src_state, des_state)
    if not node:
        print('find goal failed')
    else:
        while True:
            if node == None:
                break
            else:
                citys.append(node.state)
                node = node.parent
    size = len(citys)
    for i in range(size):
        if i < size - 1:
            print('%s->' % citys.pop(), end='')
        else:
            print(citys.pop())

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


def is_node_in_frontier(frontier, child):
    for x in frontier:
       if child.state == x.state:
           return True
    return False

def uniform_cost_search(src_state, des_state):
    global _city_info
    global _frontier_priority
    node = Node(src_state, None, None, 0)
    _frontier_priority_add(node)
    visited = []
    while True:
        if len(_frontier_priority) == 0:
            return False
        node = _frontier_priority.pop(0)
        if node.state == des_state:
            print('find goals!')
            return node
        visited.append(node)
        for i in range(len(_city_info)):
            des_city = ''
            if _city_info['city1'][i] == node.state:
                des_city = _city_info['city2'][i]
            elif _city_info['city2'][i] == node.state:
                des_city = _city_info['city1'][i]
            if des_city == '':
                continue
            child = Node(des_city, node, 'go', node.path_cost + _city_info['path_cost'][i])
            if child.state not in visited and not is_node_in_frontier(_frontier_priority, child):
                _frontier_priority_add(child)
            elif is_node_in_frontier(_frontier_priority, child):
                _frontier_priority_replace(child)

def _frontier_priority_add(node):
    global _frontier_priority
    size = len(_frontier_priority)
    for i in range(size):
        if node.path_cost < _frontier_priority[i].path_cost:
            _frontier_priority.insert(i, node)
            return
    _frontier_priority.append(node)

def _frontier_priority_replace(child):
    global _frontier_priority
    size = len(_frontier_priority)
    for i in range(size):
        if child.state == _frontier_priority[i].state and child.path_cost < _frontier_priority[i].path_cost:
            _frontier_priority[i] = child
            return
if __name__ == '__main__':
    main()


