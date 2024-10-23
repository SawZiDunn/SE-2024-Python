def find_route(start, routes):
    total_distance = 0.0
    route_list = []

    while start in routes.keys():
        total_distance += routes[start][1]
        route_list.append(start)
        start = routes[start][0]
    route_list.append(start)
    
    return (route_list, total_distance)

routes = {"i": ("j", 4.0), "a": ("b", 3.4), "j": ("k", 6.1), "c": ("d", 5.6), "b": ("c", 4.0)}
print(find_route("a", routes))
print(find_route("b", routes))