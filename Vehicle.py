class Vehicle:
    def __init__(self):
        self.vehicle_id=""
        self.start_node=""
        self.end_node=""
        self.speed=0
        self.toll=0
    def set_vehicle_id(self,existed):
        while True:
            vehicle_id=input("請輸入車牌(ex:ABC-1234):")
            if len(vehicle_id)!=8:
                print("車牌格式錯誤，請重新輸入")
            elif "-" not in vehicle_id:
                print("車牌格式錯誤，須包含-，請重新輸入")
            elif not vehicle_id[:3].isupper():
                print("車牌格式錯誤，前三碼為大寫英文，請重新輸入")
            elif not vehicle_id[4:].isdigit():
                print("車牌格式錯誤，末四碼為數字，請重新輸入")
            elif vehicle_id in existed:
                print("此車牌已存在，請重新輸入")
            else:
                self.vehicle_id=vehicle_id
                existed.append(vehicle_id)
                break
    def set_start_node(self,graph):
        while True:
            graph_node=list(graph.nodes.keys())
            start_node=input("請輸入起點:")
            if start_node not in graph_node:
                print("查無該地點，請重新輸入")
            else:
                self.start_node=start_node
                break
    def set_end_node(self,graph):
        while True:
            graph_node=list(graph.nodes.keys())
            end_node=input("請輸入終點:")
            if end_node not in graph_node:
                print("查無該地點，請重新輸入")
            elif self.start_node==end_node:
                print("起點與終點不可相同，請重新輸入")
            else:
                self.end_node=end_node
                break
    def eligibility(self,route_type):
        raise NotImplementedError("請在子類別複寫該方法")
class Motor(Vehicle):
    def __init__(self):
        super().__init__()
        self.speed=60
        self.toll=10
    def eligibility(self, route_type):
        if route_type=="highway":
            return False
        else:
            return True
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.speed=80
        self.toll=30
    def eligibility(self, route_type):
        return True
class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.speed=70
        self.toll=50
    def eligibility(self, route_type):
        if route_type=="residential":
            return False
        else:
            return True
class Emergency(Vehicle):
    def __init__(self):
        super().__init__()
        self.speed=100
        self.toll=0
    def eligibility(self, route_type):
        return True