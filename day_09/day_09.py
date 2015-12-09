import sys

def visit_connections(cur_node, trip_cost, best_total_cost):

    # we have visited every location
    if len(visited_locations) == num_locations:
        if trip_cost < best_total_cost:
            best_total_cost = trip_cost

    else:
        # don't revisit locations
        if cur_node not in visited_locations:

            # mark location as visited
            visited_locations.append(cur_node)

            for child_node, cost in locations_graph[cur_node]:
                best_total_cost = visit_connections(child_node, trip_cost + cost, best_total_cost)

            # mark location as unvisited (cleanup)
            visited_locations.remove(cur_node)

    return best_total_cost

if __name__ == "__main__":

    input_file = open(sys.argv[1])
    input_lines = input_file.readlines()

    locations_graph = {}
    visited_locations = []
    best_total_cost = 0

    for line in input_lines:

        # ignore whitespace and
        line = line.lstrip().rstrip()

        # split components
        line = line.replace(" to ", ",").replace(" = ", ",")
        source, target, cost = line.split(",")
        cost = int(cost)
        best_total_cost += cost # the initial best (worst) solution is to use every edge

        # add bidirectional connections to graph
        if source not in locations_graph.keys():
            locations_graph[source] = [[target, cost]]
        else:
            locations_graph[source].append([target, cost])

        if target not in locations_graph.keys():
            locations_graph[target] = [[source, cost]]
        else:
            locations_graph[target].append([source, cost])

    num_locations = len(locations_graph.keys())
    
    # we can start at any location
    for start_node in locations_graph.keys():
        best_solution_total_cost = visit_connections(start_node, 0, best_total_cost)
        if best_solution_total_cost < best_total_cost:
            best_total_cost = best_solution_total_cost

    # just a classic TSP problem, or rather, Travelling Present Giving Santa (TPGS)
    print(best_total_cost)
