import numpy as np
class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0
    def __eq__(self, other):
        return self.position == other.position
    def search(maze, cost, start, end):
        start_node = Node(None, tuple(start))
        start_node.g = start_node.h=start_node.f = 0
        end_node = Node(None, tuple(end))
        end_node.g = end_node.h = end_node.f = 0

        yet_to_visit_list=[]
        yet_to_visit_list.append(start_node)

        outer_iterations = 0
        max_iterations = (len(maze)//2)**10
        move = [[-1,0],
                [0,-1],
                [1,0],
                [0,1]
                ]
        no_rows, no_columns = np.shape(maze)
        while len(yet_to_visit_list) > 0:
            outer_iterations += 1
            current_node = yet_to_visit_list[0]
            current_index = 0
            for index, item in enumerate(yet_to_visit_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index =index
            if outer_iterations > max_iterations:
                print("giving up on pathfinding too many iterations")
                return return_path(current_node,maze)
