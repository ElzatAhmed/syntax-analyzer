import queue

epsilon = '$'
empty = '@'
anything = '#'


def _closure(nfa, state: str, symbol: str):
    """
    closure function of state on symbol
    :param nfa
    :param state:
    :param symbol:
    :return:
    """

    closure = set()
    q = queue.Queue(maxsize=-1)
    q.put(state)
    while not q.empty():
        front = q.get()
        for s in nfa.states:
            if s == front:
                continue
            if s in closure:
                continue
            if s in nfa.trans_func[front][symbol]:
                closure.add(s)
                q.put(s)
    return closure


def epsilon_closure(nfa, states: list):
    """

    :param nfa:
    :param states:
    :return:
    """

    closure = set()
    for state in states:
        ep_closure = _closure(nfa, state, epsilon)
        for c in ep_closure:
            closure.add(c)
        closure.add(state)
    return list(closure)


def move(nfa, states: list, symbol: str):
    """

    :param nfa:
    :param states:
    :param symbol:
    :return:
    """

    closure = set()
    for state in states:
        mov = _closure(nfa, state, symbol)
        for c in mov:
            closure.add(c)
    return list(closure)


def contains_list(contain: list, contained: list):
    for elem in contain:
        if equals(elem, contained):
            return True
    return False


def contains_elements(contain: list, contained: list):
    for elem in contain:
        contains = True
        for e in contained:
            if e not in elem:
                contains = False
                break
        if contains:
            return True
    return False


def equals(l1: list, l2: list):
    if len(l1) != len(l2):
        return False
    eq = True
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            eq = False
            break
    return eq


def find_match(states: list, alias: list, state):
    assert len(states) == len(alias)
    for i in range(len(states)):
        if equals(states[i], state):
            return alias[i]
    return None


def identical(l1: list, l2: list):
    if len(l1) != len(l2):
        return False
    for i in range(len(l1)):
        if len(l1[i]) != len(l2[i]):
            return False
        for j in range(len(l1[i])):
            if l1[i][j] != l2[i][j]:
                return False
    return True


def partition(subset: list, p: list):
    new = []
    for states in p:
        appended = False
        for s in subset:
            if s not in states:
                new.append(states)
                appended = True
                break
        if not appended:
            new.append(subset)
            left = list()
            for state in states:
                if state not in subset:
                    left.append(state)
            new.append(left)
    return new


def sub(dfa, p: list):
    for states in p:
        sub_states = []
        next_states = []
        if len(states) <= 1:
            continue
        for symbol in dfa.symbols:
            sub_states.clear()
            next_states.clear()
            for state in states:
                nex = dfa.trans_func[state][symbol]
                next_states.append(nex)
                if contains_elements(contain=p, contained=next_states):
                    sub_states.append(state)
                    continue
                elif nex == '@':
                    if len(sub_states) == 0:
                        sub_states.append(state)
                        continue
                    elif nex == dfa.trans_func[sub_states[0]][symbol]:
                        sub_states.append(state)
                        continue
                    else:
                        return sub_states
                return sub_states
    return p
