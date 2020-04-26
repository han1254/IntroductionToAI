from pandas import DataFrame
#迭代加深搜索
_city_info = None
class Node:
   def __init__(self, state, parent, action, path_cost):
       self.state = state
       self.parent = parent
       self.action = action
       self.path_cost = path_cost

def main():
    global _city_info
    import_city_info()
    start_city = input("start_city:")
    end_city = input("end_city:")
    limit = int(input("limit:"))
    result = iterative_depending_search(start_city, end_city, limit)
    if result == "failure" or result == "cut_off":
        print("search failure")
    else:
        print("success")
        path = []
        while True:
            path.append(result.state)
            if result.path_cost is Node:
                break
            result = result.parent
        size = len(path)
        for i in range(size):
            if i < size - 1:
                print('%s -> '%path.pop(), end = '')
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


def depth_first_search(node, end_state, limit):
    global _city_info
    visited = []
    visited.append(node.state)
    #目标测试
    if node.state == end_state:
        print("find the goal!")
        return node
    elif limit == 0:
        print("this node is cutoff")
        return "cutoff"
    else:
        cutoff_occured = False
        for i in range(len(_city_info)):
            dest_city = ''
            if _city_info['city1'][i] == node.state:
                dest_city = _city_info['city2'][i]
            elif _city_info['city2'][i] == node.state:
                dest_city = _city_info['city1'][i]
            if dest_city == '':
                continue
            child = Node(dest_city, node, 'go', _city_info['path_cost'][i] + node.path_cost)
            if child.state in visited:
                print(child.state + "node has been visited")
                continue
            result = depth_first_search(child, end_state, limit - 1)
            if result == "cutoff":
                print('search failure, child state %s, parent state %s, limit cutoff!'%(child.state, child.parent.state))
                cutoff_occured = True
            elif result != 'failure':
                print('find goal!!!')
                return result
        if cutoff_occured:
            return "cut_off"
        else:
            return "failure"
def depth_limit_search(start_state, end_state, i):
    node = Node(start_state, None, None, 0)
    return depth_first_search(node, end_state, i)


def iterative_depending_search(start_state, end_state, limitation):
    for i in range(limitation):
        result = depth_limit_search(start_state,end_state, i)
        if result != "failure" and result != "cutoff":
            return result
    return "cutoff"

if __name__ == '__main__':
    main()