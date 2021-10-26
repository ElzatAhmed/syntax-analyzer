import syntax_parser.grammar as gmr


def _list(lis: list):
    s = ''
    for i in lis:
        s += f'{i} '
    return s


class FirstHolder:

    def __init__(self, grammar: gmr.Grammar):
        self._grammar = grammar
        self._first = {text: set() for text in grammar.whole}

    def construct(self):
        for text in self._first:
            self._first[text] = self._calc(text)

    def get(self, text):
        if type(text) is str:
            return self._first[text]
        first = set()
        if type(text) is list or type(text) is set:
            includes_epsilon = False
            for symbol in text:
                first_ = self._first[symbol]
                includes_epsilon = False
                for f in first_:
                    if f == gmr.epsilon:
                        includes_epsilon = True
                        continue
                    first.add(f)
                if includes_epsilon:
                    continue
                break
            if includes_epsilon:
                first.add(gmr.epsilon)
            return first

    def _calc(self, text: str):
        # if it`s calculated already
        first = self._first[text]
        if len(first):
            return first
        # if it`s a terminal symbol
        if text in gmr.terminals:
            return {text}
        first = set()
        # get the methods that related with the text
        methods = self._grammar.get(text, text_on='left')
        # traverse the method
        for method in methods:
            includes_epsilon = False
            # traverse the symbol at the right side of the method
            for symbol in method.right:
                # if it`s epsilon
                if symbol == gmr.epsilon:
                    first.add(gmr.epsilon)
                    break
                # if it`s a terminal symbol
                if symbol in gmr.terminals:
                    first.add(symbol)
                    break
                # else
                # calculate the first of the symbol
                first_ = self._calc(symbol)
                self._first[symbol] = first_
                includes_epsilon = False
                # add all the first symbol to the first set
                for f in first_:
                    # if first symbols include epsilon continue the whole process
                    if f == gmr.epsilon:
                        includes_epsilon = True
                        continue
                    first.add(f)
                if includes_epsilon:
                    continue
                break
            if includes_epsilon:
                first.add(gmr.epsilon)
        return first

    def output(self, path=None):
        if path is not None:
            with open(path, mode='w', encoding='utf-8') as file:
                file.write('{: ^20}{: ^20}'.format('symbol', 'first'))
                file.write('\n')
                file.write('------------------------------------------------\n')
                for symbol in self._first:
                    file.write('{: ^20}{: ^20}'.format(symbol, _list(self._first[symbol])))
                    file.write('\n')
        else:
            for symbol in self._first:
                print(f'{symbol}: {_list(self._first[symbol])}')
