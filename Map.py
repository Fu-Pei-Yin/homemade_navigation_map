from graphviz import Digraph
class Node:
    def __init__(self,name):
        self.name=name
        self.neighbor={}
        self.tolltooth=False
    def set_neighbor(self,neighbor_name,route_weight,route_length,route_type,traffic_flow,rate):
        self.neighbor[neighbor_name]=[route_weight,route_length,route_type,traffic_flow,rate]
    def set_tolltooth(self):
        self.tolltooth=True
    def set_traffic_flow(self,neighbor):
        self.neighbor[neighbor][3]+=1
import random
class Edge:
    def __init__(self,start_node,end_node):
        self.start_node=start_node
        self.end_node=end_node
        self.route_weight=0
        self.route_length=0
        self.route_type=""
        self.traffic_flow=0
        self.rate=0
    def set_route_weight(self):
        self.route_weight=random.randint(1,5)
    def set_route_length(self):
        self.route_length=random.randint(1,20)
    def set_route_type(self):
        self.route_type=random.choice(["normal","highway","residential"])
    def set_traffic_flow(self):
        self.traffic_flow=random.randint(1,self.route_weight*40)
    def set_rate(self):
        if self.traffic_flow<self.route_weight*10:
            self.rate=1
        elif self.route_weight*10<self.traffic_flow<self.route_weight*20:
            self.rate=0.8
        elif self.route_weight*20<self.traffic_flow<self.route_weight*30:
            self.rate=0.6
        else:
            self.rate=0.4
    def set_paraments(self):
        self.set_route_weight()
        self.set_route_length()
        self.set_route_type()
        self.set_traffic_flow()
        self.set_rate()
class Graph:
    def __init__(self):
        self.nodes={}
        self.edges=[]
    def add_node(self,name):
        if name not in self.nodes:
            self.nodes[name]=Node(name)
    def add_edge(self,start_node,end_node):
        if start_node in self.nodes and end_node in self.nodes:
            start=self.nodes[start_node]
            end=self.nodes[end_node]
            edge=Edge(start,end)
            edge.set_paraments()
            start.set_neighbor(end.name,edge.route_weight,\
                edge.route_length,edge.route_type,\
                edge.traffic_flow,edge.rate)
            self.edges.append(edge)
    def select_tolltooth(self):
        num=random.randint(1,len(self.nodes))
        for n in range(num):
            choice=random.choice(list(self.nodes.values()))
            choice.set_tolltooth()
    def set_paraments(self):
        node_num=random.randint(3,7)
        edge_num=random.randint(1,node_num)
        nodes=[chr(65+i) for i in range(node_num)]
        for name in nodes:
            self.add_node(name)
        exist=[]
        for n in range(node_num):
            start=chr(65+n)
            root_num=0
            while root_num!=edge_num:
                end=random.choice(nodes)
                if start!=end and (start,end) not in exist:
                    exist.append((start,end))
                    self.add_edge(start,end)
                    root_num+=1
    def visualize(self,output_file,view=True):
        graph=Digraph(comment="Graph",format="png")
        for node in self.nodes.values():
            if node.tolltooth==True:
                graph.node(node.name,style="filled",fillcolor="lightblue")
            else:
                graph.node(node.name)
        for edge in self.edges:
            graph.edge(edge.start_node.name,edge.end_node.name,\
                label=str(f"weight:{edge.route_weight}\nlength:{edge.route_length}\
                \ncategory:{edge.route_type}\ntraffic:{edge.traffic_flow}\
                \nrate:{edge.rate}"),len=str(edge.route_length))
        graph.render(output_file,view=view)
    def update_map(self,route):
        for edge in self.edges:
            for i in range(len(route.route)-1):
                if edge.start_node.name==route.route[i] and edge.end_node.name==route.route[i+1]:
                    edge.traffic_flow+=1
                    edge.set_rate()
                    edge.start_node.neighbor[edge.end_node.name][3]=edge.traffic_flow
                    edge.start_node.neighbor[edge.end_node.name][4]=edge.rate