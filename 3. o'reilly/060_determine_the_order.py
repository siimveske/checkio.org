'''
https://py.checkio.org/en/mission/determine-the-order/
'''
from collections import defaultdict


def checkio(data):
    graph = build_graph(data)
    solution = topological_order(graph)
    return solution


def build_graph(data):
    graph = {}
    for item in data:
        for i in range(len(item)):
            parent = item[i]
            if parent not in graph:
                graph[parent] = []
            for child in list(item[i + 1:]):
                if child not in graph[parent] and child != parent:
                    graph[parent].append(child)
    return graph


def topological_order(graph):
    num_parents = defaultdict(int)

    for node in graph:
        for child in graph[node]:
            num_parents[child] += 1

    solution = []
    ready = list(set(graph.keys()) - set(num_parents.keys()))

    while ready:
        ready.sort(reverse=True)
        current_item = ready.pop()
        solution.append(current_item)

        for child in graph[current_item]:
            num_parents[child] -= 1
            if num_parents[child] == 0:
                ready.append(child)

    return ''.join(solution)


if __name__ == "__main__":
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd"  # "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm"  # "Paste in"
    assert (checkio(["a", "b", "c"]) == "abc")  # "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs"  # "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg"  # "Concatenate and paste in"
    print("OK")
