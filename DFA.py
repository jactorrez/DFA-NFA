# Deterministic Finite State Machine simulator

edges = {(1, 'a'): 2,
         (2, 'a'): 2,
         (2, '1'): 3,
         (3, '1'): 3}

accepting = [3]

def dfasim(string, state, transitions, accepting):
    if string == "":
        return state in accepting
    else:
        next_char = string[0]
        if (state,next_char) in transitions:
            return dfasim(string[1:], transitions[(state,next_char)], transitions, accepting)
        else:
            return False
