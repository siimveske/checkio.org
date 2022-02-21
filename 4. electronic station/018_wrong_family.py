def is_family(tree: list[list[str]]) -> bool:
    graph, all_parents, all_children = parse_tree(tree)

    root = all_parents - all_children
    if len(root) != 1:
        return False

    visited = set()
    stack = [root.pop()]
    while stack:
        parent = stack.pop()
        if parent in visited:
            return False
        visited.add(parent)
        for children in graph.get(parent, []):
            stack.append(children)

    people = all_parents.union(all_children)
    return visited == people


def parse_tree(tree):
    graph = {}
    all_children = set()
    all_parents = set()

    for node in tree:
        parent, child = node
        all_parents.add(parent)
        all_children.add(child)

        if parent in graph:
            graph[parent].append(child)
        else:
            graph[parent] = [child]

    return (graph, all_parents, all_children)


if __name__ == "__main__":
    assert is_family([
        ['Logan', 'Mike']
    ]) == True  # 'One father, one son'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack']
    ]) == True  # 'Two sons'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == True  # 'Grandfather'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Logan']
    ]) == False  # 'Can you be a father to your father?'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Jack']
    ]) == False  # 'Can you be a father to your brother?'
    assert is_family([
        ['Logan', 'William'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == False  # 'Looks like Mike is stranger in Logan\'s family'
    assert is_family([
        ['Jack', 'Mike'],
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
    ]) == False  # 'Two fathers'

    assert is_family([["Logan", "Mike"], ["Alexander", "Jack"], ["Jack", "Logan"]]) == True

    print("Looks like you know everything. It is time for 'Check'!")
