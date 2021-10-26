import syntax_parser.grammar as gmr
from .first import FirstHolder


def _list(lis: list):
    s = ''
    for i in lis:
        s += f'{i} '
    return s


class FollowHolder:

    def __init__(self, grammar: gmr.Grammar, first_holder: FirstHolder, start_symbol: str):
        self._grammar = grammar
        self._first_holder = first_holder
        self._start_symbol = start_symbol
        self._follow = {text: set() for text in grammar.whole}

    def get(self, text: str):
        return self._follow[text]

    def construct(self):
        for text in self._follow:
            self._follow[text] = self._calc(text)

    def _calc(self, text: str):
        # if it`s already calculated
        follow = self._follow[text]
        if len(follow):
            return follow
        # get related methods
        methods = self._grammar.get(text, text_on='right')
        follow = set()
        # if it`s the start symbol
        if text == self._start_symbol:
            follow.add(gmr.hashtag)
        # traverse all the related methods
        for method in methods:
            # get the index of text
            index = method.right.index(text)
            # if text is the last one
            if index == len(method.right) - 1:
                if method.left == text:
                    continue
                # get the follow of left side of the method
                follow_ = self._calc(method.left)
                self._follow[method.left] = follow_
                for f in follow_:
                    follow.add(f)
                continue
            # if text is not the last one
            # get the first of the list of symbols after text
            first_ = self._first_holder.get(text=method.right[index + 1:])
            includes_epsilon = False
            # update the follow
            for f in first_:
                if f == gmr.epsilon:
                    includes_epsilon = True
                    continue
                follow.add(f)
            # if first includes epsilon
            if includes_epsilon:
                follow_ = self._calc(method.left)
                self._follow[method.left] = follow_
                for f in follow_:
                    follow.add(f)
        return follow

    def output(self, path=None):
        if path is not None:
            with open(path, mode='w', encoding='utf-8') as file:
                file.write('{: ^20}{: ^20}'.format('symbol', 'follow'))
                file.write('\n')
                file.write('------------------------------------------------\n')
                for symbol in self._follow:
                    file.write('{: ^20}{: ^20}'.format(symbol, _list(self._follow[symbol])))
                    file.write('\n')
        else:
            for symbol in self._follow:
                print(f'{symbol}: {_list(self._follow[symbol])}')
