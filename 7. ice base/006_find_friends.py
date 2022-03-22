'''https://py.checkio.org/en/mission/find-friends/'''

from collections import defaultdict


def build_graph(network: tuple[str]):
    graph = defaultdict(list)
    for connection in network:
        a, b = connection.split('-')
        graph[a].append(b)
        graph[b].append(a)
    return graph


def search(graph: dict[str, list], start: str, stop: str, visited: set) -> bool:
    if start == stop:
        return True

    visited.add(start)

    for node in graph[start]:
        if node in visited:
            continue
        if search(graph, node, stop, visited):
            return True

    return False


def check_connection(network: tuple[str], first: str, second: str):
    graph = build_graph(network)
    result = search(graph, first, second, set())
    return result


if __name__ == '__main__':
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."

    print("OK")
