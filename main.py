import Map
def create_map():
    global graph
    graph=Map.Graph()
    graph.set_paraments()
    graph.select_tolltooth()
    graph.visualize("map")
def hasRoute(graph,node,end_node):
    def dfs(current):
        if current==end_node:
            return True
        for neighbor in graph.nodes[current].neighbor.keys():
            if neighbor not in visited:
                visited.append(neighbor)
                if dfs(neighbor):
                    return True
        return False
    global visited
    visited=[]
    visited.append(node)
    return dfs(node)
import Vehicle
import sys
existed=[]
def choose_vehicle():
    global graph,vehicle_type,existed
    print("1.機車\n2.汽車\n3.貨車\n4.緊急用車\n5.退出系統")
    while True:
        vehicle_type=Vehicle.Vehicle()
        try:
            option=int(input("請選擇車種:"))
            if option not in [1,2,3,4,5]:
                raise ValueError("選項須為1/2/3/4/5")
            if option==5:
                sys.exit("已退出系統")
            break
        except ValueError as e:
            print(f"輸入無效:{e},請重新輸入")
    if option==1:
        vehicle_type=Vehicle.Motor()
    elif option==2:
        vehicle_type=Vehicle.Car()
    elif option==3:
        vehicle_type=Vehicle.Truck()
    elif option==4:
        vehicle_type=Vehicle.Emergency()
    vehicle_type.set_vehicle_id(existed)
    while True:
        vehicle_type.set_start_node(graph)
        vehicle_type.set_end_node(graph)
        if hasRoute(graph,\
            vehicle_type.start_node,vehicle_type.end_node)==True:
            break
        else:
            print("無法到達該地點，請重新輸入起點與終點")
assigned_path=None
import Assigned_path
def choose_assigned_spot():
    global graph,vehicle_type,assigned_path
    graph_node=list(graph.nodes.keys())
    print("地圖中地點包含:")
    print(",".join(graph_node))
    assigned_path=Assigned_path.Assigned_Path()
    assigned_path.choose_pass_path(graph,\
        vehicle_type.start_node,vehicle_type.end_node)
    assigned_path.choose_avoid_path(graph,\
        vehicle_type.start_node,vehicle_type.end_node)
    str_pass_node=""
    for node in assigned_path.pass_path:
        if assigned_path.pass_path!=[]:
            str_pass_node=str_pass_node+node+" "
    if str_pass_node=="":
        str_pass_node="無"
    str_avoid_node=""
    for node in assigned_path.avoid_path:
        if assigned_path.avoid_path!=[]:
            str_avoid_node=str_avoid_node+node+" "
    if str_avoid_node=="":
        str_avoid_node="無"
    print(f"必經地點:{str_pass_node}")
    print(f"避開地點:{str_avoid_node}")
import Output_route
output_route=None
def output_routes():
    global graph,vehicle_type,assigned_path,output_route
    output_route=Output_route.Output_Route(graph,vehicle_type.start_node,\
        vehicle_type.end_node,assigned_path.pass_path,assigned_path.avoid_path)
    output_route.find_all_route()
    while output_route.all_output_route==[]:
        print("無法到達終點，請重新輸入指定路徑")
        choose_assigned_spot()
        output_route.find_all_route()
def choose_sequence_method():
    global option
    print("排序方式:")
    method=["路徑由近到遠","路徑由遠到近","時間由快到慢","時間由慢到快","收費由低到高",\
        "收費由高到低","避開收費站","避開高速公路","避開交通壅塞"]
    if isinstance(vehicle_type,Vehicle.Emergency):
        method=[m for m in method if m not in ["收費由低到高","收費由高到低","避開收費站"]]
    elif isinstance(vehicle_type,Vehicle.Motor):
        method=[m for m in method if m!="避開高速公路"]
    for i,m in enumerate(method):
        print(f"排序{i+1}.{m}")
    while True:
        try:
            option=int(input("請輸入排序方式:"))
            if option<1 or option>len(method):
                raise ValueError("請輸入正確選項")
            break
        except ValueError as e:
            print(f"輸入無效:{e},請重新輸入")
    run_method(option)
import Sequence
def run_method(option):
    global output_route,vehicle_type
    Sequence.get_route(graph,output_route.all_output_route,vehicle_type)
    if option==1:
        Sequence.route_min()
    elif option==2:
        Sequence.route_max()
    elif option==3:
        Sequence.time_min()
    elif option==4:
        Sequence.time_max()
    elif option==5 and isinstance(vehicle_type,Vehicle.Emergency):
        Sequence.avoid_highway(graph)
    elif option==5:
        Sequence.toll_min()
    elif option==6:
        Sequence.toll_max()
    elif option==7:
        Sequence.avoid_tolltooth()
    elif option==8 and isinstance(vehicle_type,Vehicle.Motor):
        Sequence.avoid_congestion(graph)
    elif option==8:
        Sequence.avoid_highway(graph)
    else:
        Sequence.avoid_congestion(graph)
def sorted_route(all_route,graph):
    sorted_routes=[]
    for route in all_route:
        valid=True
        for i in range(len(route.route)-1):
            edge=get_edge(graph,route.route[i],route.route[i+1])
            if edge:
                if vehicle_type.eligibility(edge.route_type)==False:
                    break
        if valid:
            sorted_routes.append(route)
    if not sorted_routes:
        print("你的車種無法通行，請重新輸入")
        existed.pop()
    return sorted_routes
def get_edge(graph,start_node,end_node):
    for edge in graph.edges:
        if edge.start_node.name==start_node and edge.end_node.name==end_node:
            return edge
    return None
import Update
def output_graph():
    all_route=Sequence.get_sorted_routes()
    sorted=sorted_route(all_route,graph)
    if not sorted: 
        return
    selected_path=Update.choose_route(sorted)
    graph.update_map(selected_path)
    graph.visualize("map")
def main():
    create_map()
    while True:
        choose_vehicle()
        choose_assigned_spot()
        output_routes()
        choose_sequence_method()
        output_graph()
main()