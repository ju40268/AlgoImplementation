# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @ param node, a undirected graph node
    # @ return a undirected graph node
    def cloneGraph(self, node):
        if node == None: return
        copy_node = UndirectedGraphNode(node.label)
        dic = {}
        dic[node] = copy_node
        queue = [node]
        
        while queue:
            current_vertex = queue.pop(0)
            for n in current_vertex.neighbors:
                if n in dic:
                    dic[current_vertex].neighbors.append(dic[n])
                else:
                    copy_node_local = UndirectedGraphNode(n.label)
                    dic[n] = copy_node_local
                    dic[current_vertex].neighbors.append(copy_node_local)
                    queue.append(n)
        return dic[node]