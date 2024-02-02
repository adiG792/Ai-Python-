# MiniMax Algorithm

from math import inf


def MaxV(state):
    v = -inf
    if Terminal(state):
        return Utility(state)
    
    for action in Actions(state):
        v = max(v, MinV(Result(state,action)))
    
    return v


def MinV(state):
    v = inf
    if Terminal(state):
        return Utility(state)
    
    for action in Actions(state):
        v = min(v, MaxV(Result(state,action)))

    return v

