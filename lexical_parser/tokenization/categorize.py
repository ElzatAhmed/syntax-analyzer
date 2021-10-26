from .token import TokenType
from .consts import *
import lexical_parser.automa as auto
import lexical_parser.alphabet as alpha


def categorize(token, dfa_type: auto.DfaType):
    if dfa_type == auto.DfaType.LETTER or dfa_type == auto.DfaType.PURE_LETTER:
        if token.text in keywords:
            return _token_type_dict[token.text]
        return TokenType.IDN
    if dfa_type == auto.DfaType.OPERATOR:
        assert token.text in operators
        return _token_type_dict[token.text]
    if dfa_type == auto.DfaType.NUMBER:
        if alpha.DOT in token.text:
            return TokenType.FLOAT_LITERAL
        return TokenType.INT_LITERAL
    if dfa_type == auto.DfaType.STRING:
        return TokenType.STR_LITERAL
    if dfa_type == auto.DfaType.CHAR:
        return TokenType.CHAR_LITERAL


def value(token):
    if token.token_type == TokenType.INT_LITERAL:
        token.value = int(token.text)
        return
    if token.token_type == TokenType.FLOAT_LITERAL:
        token.value = float(token.text)
        return
    if token.token_type == TokenType.STR_LITERAL or \
            token.token_type == TokenType.CHAR_LITERAL:
        token.value = _get_text(token.text)
        return
    token.value = token.text


def _get_text(s: str):
    text = ''
    for i in range(len(s)):
        if i == 0:
            continue
        if i == len(s) - 1:
            break
        text += s[i]
    return text


_token_type_dict = {
    '+': TokenType.OP,
    '++': TokenType.OP,
    '+=': TokenType.OP,
    '-': TokenType.OP,
    '--': TokenType.OP,
    '-=': TokenType.OP,
    '*': TokenType.OP,
    '*=': TokenType.OP,
    '/': TokenType.OP,
    '//': TokenType.IGNORE,
    '/=': TokenType.OP,
    '%': TokenType.OP,
    '%=': TokenType.OP,
    '&': TokenType.OP,
    '&&': TokenType.OP,
    '&=': TokenType.OP,
    '|': TokenType.OP,
    '||': TokenType.OP,
    '|=': TokenType.OP,
    '!': TokenType.OP,
    '!=': TokenType.OP,
    '>': TokenType.OP,
    '>>': TokenType.OP,
    '>=': TokenType.OP,
    '<': TokenType.OP,
    '<<': TokenType.OP,
    '<=': TokenType.OP,
    '=': TokenType.OP,
    '==': TokenType.OP,
    'while': TokenType.WHILE,
    'for': TokenType.FOR,
    'continue': TokenType.CONTINUE,
    'break': TokenType.BREAK,
    'if': TokenType.IF,
    'else': TokenType.ELSE,
    'float': TokenType.FLOAT,
    'int': TokenType.INT,
    'char': TokenType.CHAR,
    'void': TokenType.VOID,
    'return': TokenType.RETURN,
    '(': TokenType.SE,
    ')': TokenType.SE,
    '{': TokenType.SE,
    '}': TokenType.SE,
    ';': TokenType.SE,
    ',': TokenType.SE,
    '[': TokenType.SE,
    ']': TokenType.SE
}
