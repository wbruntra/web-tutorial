def prefix_routes(routes,prefix):
    result = []
    for route in routes:
        result.append((prefix+route[0],route[1]))
    return result
