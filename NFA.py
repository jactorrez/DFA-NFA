edges = {(1, 'a'): [2, 3],
         (2, 'a'): [2],
         (3, 'b'): [4, 3],
         (4, 'c'): [5]}

accepting = [2, 5]

def nfasim(string, current, edges, accepting):
    if string == ""
        return current in accepting

    next_char = string[0]
    check_state = (current, next_char)
    if check_state in edges:
        next_states = edges[check_state]
        for state in next_states:
            if nfasim(string[1:], state, edges, accepting):
                return True

    return False