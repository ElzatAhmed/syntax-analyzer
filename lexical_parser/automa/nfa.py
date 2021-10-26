from .dfa import DFA
from .common import *


class NFA:

    def __init__(self, states: list, symbols: list,
                 initials: list, finales: list, trans_func: dict):

        """

        :param states:
        :param symbols:
        :param initials:
        :param finales:
        """

        self.states = states
        self.symbols = symbols
        if epsilon not in self.symbols:
            self.symbols.append(epsilon)
        self.initials = initials
        self.finales = finales
        self.trans_func = {state: {symbol: [] for symbol in self.symbols} for state in self.states}
        for state in trans_func:
            for symbol in trans_func[state]:
                self.trans_func[state][symbol] = trans_func[state][symbol]

    def convert2Dfa(self):

        """
        nfa determination
        :return:
        """

        q = queue.Queue(maxsize=-1)
        combined_states = list(list())
        state_alias = list()
        trans_dict = dict()
        state_count = 0
        for init in self.initials:
            epsilon_closure_ = epsilon_closure(self, [init])
            if contains_list(combined_states, epsilon_closure_):
                continue
            alias = f'S{state_count}'
            state_count += 1
            state_alias.append(alias)
            combined_states.append(epsilon_closure_)
            q.put(epsilon_closure_)
        while not q.empty():
            state = q.get()
            for symbol in self.symbols:
                if symbol == epsilon:
                    continue
                move_ = move(self, state, symbol)
                epsilon_closure_ = epsilon_closure(self, move_)
                if len(epsilon_closure_) == 0:
                    continue
                if not contains_list(combined_states, epsilon_closure_):
                    combined_states.append(epsilon_closure_)
                    q.put(epsilon_closure_)
                    alias = f'S{state_count}'
                    state_count += 1
                    state_alias.append(alias)
                else:
                    alias = find_match(combined_states, state_alias, epsilon_closure_)
                key_alias = find_match(combined_states, state_alias, state)
                if key_alias not in trans_dict:
                    trans_dict[key_alias] = {symbol: empty for symbol in self.symbols}
                trans_dict[key_alias][symbol] = alias
        initials = []
        finales = []
        for i in range(len(state_alias)):
            for init in self.initials:
                if init in combined_states[i]:
                    initials.append(state_alias[i])
                    continue
            for finale in self.finales:
                if finale in combined_states[i] and state_alias[i] not in finales:
                    finales.append(state_alias[i])
        return DFA(
            states=state_alias, symbols=self.symbols, initial=initials[0],
            finales=finales, trans_func=trans_dict
        )
