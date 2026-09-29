all_route=[]
class Route:
    def __init__(self):
        self.route=[]
        self.distance=0
        self.time=0
        self.toll=0
def get_route(graph,all_output_route,vehicle_type):
    global all_route,sorted_routes
    sorted_routes=[]
    all_route=[]
    for route in all_output_route:
        path=Route()
        all_route.append(path)
        for node in route:
            path.route.append(node)
        for i in range(len(path.route)-1):
            start_node=path.route[i]
            end_node=path.route[i+1]
            edge=get_edge(graph,start_node,end_node)
            if edge:
                path.distance+=edge.route_length
                path.time+=edge.route_length*edge.rate/vehicle_type.speed
                if edge.start_node.tolltooth==True:
                    path.toll+=vehicle_type.toll
def get_edge(graph,start_node,end_node):
    for edge in graph.edges:
        if edge.start_node.name==start_node and edge.end_node.name==end_node:
            return edge
    return None
import heapq
def heap(all_route,type):
    if type=="distance":
        return heapq.nsmallest(len(all_route),all_route,key=lambda r:r.distance)
    elif type=="time":
        return heapq.nsmallest(len(all_route),all_route,key=lambda r:r.time)
    elif type=="toll":
        return heapq.nsmallest(len(all_route),all_route,key=lambda r:r.toll)
sorted_routes=[]
def route_min():
    global all_route,sorted_routes
    sorted_routes=[]
    all_route=heap(all_route,type="distance")
    all_route.reverse()
    for i in range(len(all_route)):
        path=all_route.pop()
        sorted_routes.append(path)
def route_max():
    global all_route,sorted_routes
    sorted_routes=[]
    all_route=heap(all_route,type="distance")
    for i in range(len(all_route)):
        path=all_route.pop()
        sorted_routes.append(path)
def time_min():
    global all_route,sorted_routes
    sorted_routes=[]
    all_route=heap(all_route,type="time")
    all_route.reverse()
    for i in range(len(all_route)):
        path=all_route.pop()
        sorted_routes.append(path)
def time_max():
    global all_route,sorted_routes
    sorted_routes=[]
    all_route=heap(all_route,type="time")
    for i in range(len(all_route)):
        path=all_route.pop()
        sorted_routes.append(path)
def toll_min():
    global all_route,sorted_routes
    sorted_routes=[]
    all_route=heap(all_route,type="toll")
    all_route.reverse()
    for i in range(len(all_route)):
        path=all_route.pop()
        sorted_routes.append(path)
def toll_max():
    global all_route,sorted_routes
    sorted_routes=[]
    all_route=heap(all_route,type="toll")
    for i in range(len(all_route)):
        path=all_route.pop()
        sorted_routes.append(path)
def avoid_tolltooth():
    global all_route,sorted_routes
    filtered_routes=[route for route in \
        all_route if route.toll==0]
    sorted_routes=heap(filtered_routes,type="distance")
    for i in range(len(sorted_routes)):
        path=sorted_routes.pop()
        sorted_routes.append(path)
def avoid_highway(graph):
    global all_route,sorted_routes
    filtered_routes=[]
    for route in all_route:
        edges=get_edges_for_route(graph,route.route)
        if not any(edge.route_type=="highway" for edge in edges):
            filtered_routes.append(route)
    sorted_routes=heap(filtered_routes,type="distance")
    for i in range(len(sorted_routes)):
        path=sorted_routes.pop()
        sorted_routes.append(path)
def avoid_congestion(graph):
    global all_route,sorted_routes
    filtered_routes=[]
    for route in all_route:
        edges=get_edges_for_route(graph,route.route)
        if not any(edge.rate<=0.4 for edge in edges):
            filtered_routes.append(route)
    sorted_routes=heap(filtered_routes,type="distance")
    for i in range(len(sorted_routes)):
        path=sorted_routes.pop()
        sorted_routes.append(path)
def get_edges_for_route(graph,route_nodes):
    edges=[]
    for i in range(len(route_nodes)-1):
        start_node=route_nodes[i]
        end_node=route_nodes[i + 1]
        edge=get_edge(graph,start_node,end_node)
        if edge:
            edges.append(edge)
    return edges
def get_sorted_routes():
    global sorted_routes
    return sorted_routes