from .common import empty, sub, identical, partition


class DFA:

    def __init__(self, states: list, symbols: list,
                 initial: str, finales: list, trans_func: dict):
        self.states = states
        self.symbols = symbols
        self.initial = initial
        self.finales = finales
        self.trans_func = {s: {symbol: empty for symbol in self.symbols} for s in self.states}
        for state in trans_func:
            for symbol in trans_func[state]:
                self.trans_func[state][symbol] = trans_func[state][symbol]

    def minimize(self):

        """
        the minimization method of dfa
        :return:
        """

        finales, not_finales = self._partition()
        p = [not_finales, finales]
        while True:
            sub_ = sub(self, p)
            if identical(l1=sub_, l2=p):
                break
            p = partition(sub_, p)
        self._reconstruct(p)

    def _partition(self):

        """

        :return:
        """

        finales = self.finales
        not_finales = []
        for state in self.states:
            if state in finales:
                continue
            not_finales.append(state)
        return finales, not_finales

    def next_state(self, cur, symbol):
        if cur not in self.trans_func:
            return None
        if symbol not in self.symbols:
            return None
        nex = self.trans_func[cur][symbol]
        if nex == empty:
            return None
        return nex

    def _reconstruct(self, states: list):
        new_states = [f'S{i}' for i in range(len(states))]
        new_trans = {state: {symbol: empty for symbol in self.symbols} for state in new_states}
        for i in range(len(states)):
            for j in range(len(states[i])):
                for symbol in self.symbols:
                    to = self.trans_func[states[i][j]][symbol]
                    if to == '':
                        continue
                    if to in states[i]:
                        new_trans[new_states[i]][symbol] = new_states[i]
                        continue
                    for k in range(len(states)):
                        if to in states[k]:
                            new_trans[new_states[i]][symbol] = new_states[k]
        self.states = new_states
        self.trans_func = new_trans
        for i in range(len(states)):
            if self.initial in states[i]:
                self.initial = new_states[i]
                break
        new_finales = []
        for i in range(len(states)):
            for state in states[i]:
                if state in self.finales and new_states[i] not in new_finales:
                    new_finales.append(new_states[i])
        self.finales = new_finales
