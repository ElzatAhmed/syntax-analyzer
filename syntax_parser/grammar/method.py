class Method:

    def __init__(self, left: str, right: list, empty=False):
        self.left = left
        self.right = right
        self.empty = empty

    def __str__(self):
        if self.empty:
            return '###'
        s = f'{self.left} ->'
        for symbol in self.right:
            s += f' {symbol}'
        return s

    @staticmethod
    def empty_method():
        return Method(left='', right=[], empty=True)
