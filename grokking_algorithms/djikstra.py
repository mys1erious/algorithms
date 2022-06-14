import json


def imitate_graph():
    graph = {
        'book': {'lp': 5, 'poster': 0},
        'lp': {'guitar': 15, 'drums': 20},
        'poster': {'guitar': 30, 'drums': 35},
        'guitar': {'piano': 20},
        'drums': {'piano': 10}
    }

    infinity = float('inf')
    costs = {
        'book': 0,
        'lp': 5,
        'poster': 0,
        'guitar': infinity,
        'drums': infinity,
        'piano': infinity
    }

    parents = {
        'book': None,
        'lp': 'book',
        'poster': 'book',
        'guitar': None,
        'drums': None,
        'piano': None
    }

    start = 'book'
    target = 'piano'

    return graph, costs, parents, start, target


def prettify_dict(dict):
    return json.dumps(dict, indent=4)


def get_cheapest_node(costs, processed):

    min_cost_node = None
    min_cost = float('inf')
    for node in costs:
        cost = costs[node]
        if node not in processed and cost < min_cost:
            min_cost = cost
            min_cost_node = node

    return min_cost_node


def djikstra(graph, costs, parents, target):
    processed = []

    cheapest_node = get_cheapest_node(costs, processed)
    while cheapest_node != target:
        children = graph[cheapest_node]
        for child in children:
            new_cost = costs[cheapest_node] + children[child]
            if new_cost < costs[child]:
                costs[child] = new_cost
                parents[child] = cheapest_node
        processed.append(cheapest_node)
        cheapest_node = get_cheapest_node(costs, processed)

    path = [target]
    cur_parent = parents[target]
    while cur_parent is not start:
        path.append(cur_parent)
        cur_parent = parents[path[-1]]
    path.append(start)

    return costs, path[::-1]


if __name__ == '__main__':
    graph, costs, parents, start, target = imitate_graph()
    print("Graph:", prettify_dict(graph))
    print("Costs:", prettify_dict(costs))
    print("Parents:", prettify_dict(parents))

    costs, path = djikstra(graph, costs, parents, target)

    print("Lowest costs:", prettify_dict(costs))
    print("Path:", path)
