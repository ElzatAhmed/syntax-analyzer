from .method import Method

epsilon = '$'
hashtag = '#'
terminals = [
    'while', 'for', 'continue', 'break', 'if', 'else', 'float', 'int', 'char', 'void', 'return',
    '+', '-', '*', '/', '%', '=', '>', '<', '==', '<=', '>=', '!=', '++', '--', '&&', '||', '!',
    '+=', '-=', '*=', '/=', '%=', '(', ')', '{', '}', ';', '[', ']', 'IDN', 'INT', 'FLOAT', 'STR',
    'CHAR', epsilon, ',', hashtag
]


class Grammar:
    """
    the grammar of the language
    """

    def __init__(self):
        self.methods = list()
        self.non_terminals = set()

    def _add(self, left: str, right: list):

        """
        add new word to the grammar
        :param left: the left side of the grammar
        :param right: the right side of the grammar
        :return:
        """

        method = Method(left, right)
        self.methods.append(method)
        self.non_terminals.add(left)

    def get(self, text: str, text_on='left'):

        """
        get the corresponding part of the word
        :param text_on:
        :param text: left side
        :return:
        """
        methods = []
        for method in self.methods:
            if text_on == 'left' and method.left == text:
                methods.append(method)
                continue
            if text_on == 'right' and text in method.right:
                methods.append(method)
                continue
        return methods

    def construct(self, src: str):

        """
        constructs the grammar
        :param src: given file path
        :return:
        """

        file = open(src, mode='r', encoding='utf-8')
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            left, right = line.split(sep='->', maxsplit=2)
            self._add(left=left.strip(), right=right.split())

    @property
    def whole(self):
        symbols = []
        for s in self.non_terminals:
            symbols.append(s)
        for s in terminals:
            symbols.append(s)
        return symbols
