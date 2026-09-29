class Output_Route:
    def __init__(self,graph,start_node,end_node,pass_path,avoid_path):
        self.graph=graph
        self.start_node=start_node
        self.end_node=end_node
        self.pass_path=pass_path
        self.avoid_path=avoid_path
        self.all_output_route=[]
    def find_all_route(self):
        route=[self.start_node]
        self.dfs(self.start_node,route)
    def dfs(self,node,route):
        if node==self.end_node:
            if all(p_node in route for p_node in self.pass_path) \
                and all(a_node not in route for a_node in self.avoid_path):
                self.all_output_route.append(route[:])
            return
        for neighbor in self.graph.nodes[node].neighbor.keys():
            if neighbor not in route:
                route.append(neighbor)
                self.dfs(neighbor,route)
                route.pop()
    def get_edge(self,start_node,end_node):
        for edge in self.graph.edges:
            if edge.start_node.name==start_node and edge.end_node.name==end_node:
                return edge
        return None