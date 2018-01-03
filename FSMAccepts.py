edges = {(1, 'a'): [2, 3],
         (2, 'a'): [2],
         (3, 'b'): [4, 3],
         (4, 'c'): [5]}

accepting = [2, 5]


def fsmaccepts(current, edges, accepting, visited):
    if current in accepting:
        return ""

    visited.append(current)

    for (state, char) in edges:
        if state == current:
            for next_state in edges[(state,char)]:
                if next_state not in visited:
                    accepted = fsmaccepts(next_state, edges, accepting, visited)
                    if accepted is None:
                        return char + accepted

    return None
