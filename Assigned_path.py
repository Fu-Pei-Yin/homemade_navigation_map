class Assigned_Path:
    def __init__(self):
        self.pass_path=[]
        self.avoid_path=[]
    def choose_pass_path(self,graph,start_node,end_node):
        graph_node=list(graph.nodes.keys())
        while True:
            pass_choice=input("是否需要選擇必經路線(y/n):")
            if pass_choice!="y" and pass_choice!="n":
                print("輸入錯誤，請輸入y或n")
                continue
            elif pass_choice=="y":
                while True:
                    pass_spot=input("請輸入必經地點(輸入'-'結束輸入):")
                    if pass_spot=="-":
                        break
                    elif pass_spot not in graph_node:
                        print("該地點不存在，請重新輸入")
                    elif pass_spot==start_node:
                        print("必經地點不可為起點，請重新輸入")
                    elif pass_spot==end_node:
                        print("必經地點不可為終點，請重新輸入")
                    else:
                        self.pass_path.append(pass_spot)
            break
    def choose_avoid_path(self,graph,start_node,end_node):
        graph_node=list(graph.nodes.keys())
        while True:
            avoid_choice=input("是否需要選擇避開地點(y/n):")
            if avoid_choice!="y" and avoid_choice!="n": 
                print("輸入錯誤，請輸入y或n")
                continue
            elif avoid_choice=="y":
                while True:
                    avoid_spot=input("請輸入避開地點(輸入'-'結束輸入):")
                    if avoid_spot=="-":
                        break
                    elif avoid_spot not in graph_node:
                        print("該地點不存在，請重新輸入")
                    elif avoid_spot==start_node:
                        print("避開地點不可為起點，請重新輸入")
                    elif avoid_spot==end_node:
                        print("避開地點不可為終點，請重新輸入")
                    elif avoid_spot in self.pass_path:
                        print("避開地點不可同時為必經地點")
                    else:
                        self.avoid_path.append(avoid_spot)
            break