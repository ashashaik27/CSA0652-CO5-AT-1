def is_subgraph(H, G):
    n = len(H)
    m = len(G)

    def backtrack(mapping, used):
        if len(mapping) == n:
            return True

        h_vertex = len(mapping)

        for g_vertex in range(m):
            if g_vertex not in used:

                valid = True

                for h_prev, g_prev in enumerate(mapping):
                    if H[h_vertex][h_prev] == 1 and G[g_vertex][g_prev] != 1:
                        valid = False
                        break

                if valid:
                    mapping.append(g_vertex)
                    used.add(g_vertex)

                    if backtrack(mapping, used):
                        return True

                    mapping.pop()
                    used.remove(g_vertex)

        return False

    return backtrack([], set())

G = [
    [0,1,1,0],
    [1,0,1,1],
    [1,1,0,1],
    [0,1,1,0]
]

H = [
    [0,1],
    [1,0]
]

print("Subgraph Exists:" if is_subgraph(H, G) else "Subgraph Does Not Exist")
