import sys


def visit_connections(cur_node, trip_cost):

    global best_total_cost

    # we have visited every location
    if len(visited_locations) == num_locations:
        print(visited_locations, trip_cost)
        if trip_cost < best_total_cost:
            best_total_cost = trip_cost

    else:
        for child_node, edge_cost in locations_graph[cur_node]:

            # don't revisit locations
            if child_node not in visited_locations:

                # mark location as visited
                visited_locations.append(child_node)

                # propagate
                visit_connections(child_node, trip_cost + edge_cost)

                # mark location as unvisited (cleanup)
                visited_locations.remove(child_node)

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
        best_total_cost += cost  # the initial best (worst) solution is to use every edge

        # add bidirectional connections to graph
        if source not in locations_graph.keys():
            locations_graph[source] = [[target, cost]]
        else:
            locations_graph[source].append([target, cost])

        if target not in locations_graph.keys():
            locations_graph[target] = [[source, cost]]
        else:
            locations_graph[target].append([source, cost])

    num_locations = len(locations_graph)
    
    # we can start at any location
    for start_node in locations_graph.keys():
        visited_locations.append(start_node)
        visit_connections(start_node, 0)
        visited_locations.remove(start_node)

    # just a classic TSP problem, or rather, Travelling Present Giving Santa (TPGS)
    print(best_total_cost)
