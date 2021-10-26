from enum import Enum


class TokenType(Enum):
    """
    types of different tokens of the original language
    """

    WHITE_SPACE = 0
    WHILE = 1
    FOR = 2
    CONTINUE = 3
    BREAK = 4
    IF = 5
    ELSE = 6
    FLOAT = 7
    INT = 8
    CHAR = 9
    VOID = 10
    RETURN = 11
    OP = 12
    SE = 13
    IDN = 14
    INT_LITERAL = 15
    FLOAT_LITERAL = 16
    CHAR_LITERAL = 17
    STR_LITERAL = 18
    IGNORE = 19
    HASHTAG = 20


class Token:

    def __init__(self, token_type=TokenType.WHITE_SPACE, text=' ', line_num=0, illegal=False):
        self.token_type = token_type
        self.text = text
        self.line_num = line_num
        self.illegal = illegal
        self.value = '#'

    def __str__(self):
        return self.text

    def get(self):
        if self.token_type == TokenType.IDN:
            return self.token_type.name
        if self.token_type == TokenType.HASHTAG:
            return self.text
        if self.token_type == TokenType.INT_LITERAL:
            return 'INT'
        if self.token_type == TokenType.FLOAT_LITERAL:
            return 'FLOAT'
        if self.token_type == TokenType.STR_LITERAL:
            return 'STR'
        if self.token_type == TokenType.CHAR_LITERAL:
            return 'CHAR'
        return self.value
