class CodeIterator:

    """
    code text iterator
    """

    def __init__(self, text):
        self._index = -1
        self._len = len(text)
        self._list = [c for c in text]

    def has_next(self):

        """
        :return: true if there is a next character, false otherwise
        """

        return self._index + 1 < self._len

    def next(self):

        """
        :return: the next character if there is one, None otherwise
        """

        if not self.has_next():
            return None
        self._index += 1
        return self._list[self._index]

    def backspace(self):

        """
        :return: index goes back by one
        """

        self._index -= 1
