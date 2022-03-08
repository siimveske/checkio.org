from collections import defaultdict


class Friends:

    def __init__(self, connections):
        self.graph = defaultdict(set)
        for connection in connections:
            self.add(connection)

    def add(self, connection):
        a, b = connection
        if is_new := b not in self.graph[a]:
            self.graph[a].add(b)
            self.graph[b].add(a)
        return is_new

    def remove(self, connection):
        a, b = connection
        if connection_exists := a in self.graph and b in self.graph[a]:
            self.graph[a].remove(b)
            if not self.graph[a]:
                self.graph.pop(a)
            self.graph[b].remove(a)
            if not self.graph[b]:
                self.graph.pop(b)

        return connection_exists

    def names(self):
        return set(self.graph.keys())

    def connected(self, name):
        if name not in self.graph:
            return set()
        return self.graph[name]


if __name__ == '__main__':

    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])

    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"

    # 3. Remove/0
    f = Friends([{"1", "2"}, {"3", "1"}])
    assert f.remove({"2", "4"}) == False

    # 5. Connected/0
    f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))
    assert f.connected("nikola") == {"sophia"}

    print("OK")
