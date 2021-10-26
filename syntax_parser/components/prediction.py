from .first import FirstHolder
from .follow import FollowHolder
import syntax_parser.grammar as gmr


class PredictionTable:

    def __init__(self, grammar: gmr.Grammar, first_holder: FirstHolder, follow_holder: FollowHolder):
        self._grammar = grammar
        self._fist_holder = first_holder
        self._follow_holder = follow_holder
        self._table = {
            non_terminal: {terminal: gmr.Method.empty_method() for terminal in gmr.terminals}
            for non_terminal in self._grammar.non_terminals
        }

    def _add(self, non_terminal: str, terminal: str, method: gmr.Method):
        self._table[non_terminal][terminal].left = method.left
        self._table[non_terminal][terminal].right = method.right
        self._table[non_terminal][terminal].empty = False

    def get(self, non_terminal: str, terminal=None):
        if terminal:
            return self._table[non_terminal][terminal]
        return self._table[non_terminal]

    def construct(self):
        # traverse all the methods
        for method in self._grammar.methods:
            # get first of right side of the method
            first = self._fist_holder.get(method.right)
            includes_epsilon = False
            # update the prediction table
            for f in first:
                if f == gmr.epsilon:
                    includes_epsilon = True
                    continue
                self._add(method.left, f, method)
            # if first includes epsilon
            if includes_epsilon:
                follow = self._follow_holder.get(method.left)
                for f in follow:
                    self._add(method.left, f, gmr.Method(left=method.left, right=[gmr.epsilon]))

    def output(self, path: str):

        import pandas as pd

        frame = pd.DataFrame(data=self._table)
        frame.to_csv(path)
