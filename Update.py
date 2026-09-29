def choose_route(all_routes):
    if not all_routes:
        print("沒有可供選擇的路徑")
        return None
    print("請選擇以下路徑進行地圖更新：")
    for num,route in enumerate(all_routes[:10],start=1):
        route_str=" -> ".join(route.route)
        print(f"{num}. 路徑: {route_str},距離: {route.distance} 公里,時間: {route.time:.2f} 小時,收費: {route.toll} 元")
    while True:
        try:
            if len(all_routes)==1:
                print("只有一條路徑，已自動選擇")
                return all_routes[0]
            else:
                choice=int(input(f"輸入選項編號(1-{min(len(all_routes),10)}): "))
                if 1<=choice<=min(len(all_routes),10):
                    return all_routes[choice-1]
                else:
                    print("輸入的編號無效，請重新輸入")
        except ValueError:
            print("請輸入有效的數字選項")

