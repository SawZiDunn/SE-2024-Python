def find_route(start, routes):
    if start not in routes:
        return 0.0
    else:
        new_start = routes[start][0]
        return routes[start][1] + find_route(new_start, routes)

routes = {"i": ("j", 4.0), "a": ("b", 3.4), "j": ("k", 6.1), "c": ("d", 5.6), "b": ("c", 4.0)}
print(find_route("a", routes))
print(find_route("b", routes))