def DLS(graph,src, target, maxDepth):
    if src == target: return True
    if maxDepth <= 0: return False
    for i in graph[src]:
        if DLS(graph, i, target, maxDepth-1):
            return True
    return  False
def IDDFS(graph,src, target,maxDepth):
    for i in range(maxDepth):
        if DLS(graph,src,target,i):
            return True
    return False
graph = {
    'A': ['B','C'],
    'B': ['D','E','A'],
    'C': ['F','A'],
    'D': ['B'],
    'E': ['F','B'],
    'F': ['C']
}
print(IDDFS(graph, 'A','E',2))