import lexical_parser.construction as ct
from .categorize import *
from .iterator import *
from .token import *


class Tokenizer:

    def __init__(self, iterator: CodeIterator):
        self.iterator = iterator
        self.dfa_dict = ct.construct()

    def tokenize(self):
        tokens = []
        ignore = False
        line_num = 1
        while self.iterator.has_next():
            cur = self.iterator.next()
            if cur == '\n':
                line_num += 1
                ignore = False
                continue
            if ignore:
                continue
            if cur in white_spaces:
                continue
            if cur in sequence_ends:
                token = Token(token_type=TokenType.SE, text=cur, line_num=line_num)
                value(token)
                tokens.append(token)
                continue
            dfa, dfa_type = self._get_dfa(cur)
            if dfa is None or dfa_type is None:
                print(f'illegal symbol {cur} on line {line_num}')
                return []
            token = self._run_dfa(dfa, dfa_type)
            token.line_num = line_num
            token_type, err, err_msg = Tokenizer._validate(token, dfa_type)
            if err:
                print(err_msg)
                return []
            token.token_type = token_type
            if token_type == TokenType.IGNORE:
                ignore = True
                continue
            value(token)
            tokens.append(token)
        return tokens

    def _get_dfa(self, cur: str):
        if cur not in alpha.WHOLE_ALPHABET:
            return None, None
        for dfa_type in self.dfa_dict:
            if cur in auto.dfa_type_dict[dfa_type]:
                return self.dfa_dict[dfa_type], dfa_type

    def _run_dfa(self, dfa: auto.DFA, dfa_type: auto.DfaType):
        cur_state = dfa.initial
        token = Token()
        self.iterator.backspace()
        cur = ''
        while self.iterator.has_next():
            nex = self.iterator.next()
            if dfa_type == auto.DfaType.STRING:
                if cur_state in dfa.finales:
                    next_state = None
                elif nex == '\"':
                    next_state = dfa.next_state(cur=cur_state, symbol=nex)
                else:
                    next_state = dfa.next_state(cur=cur_state, symbol=auto.anything)
            elif dfa_type == auto.DfaType.CHAR:
                if cur_state in dfa.finales:
                    next_state = None
                elif nex == '\'':
                    next_state = dfa.next_state(cur=cur_state, symbol=nex)
                else:
                    next_state = dfa.next_state(cur=cur_state, symbol=auto.anything)
            else:
                next_state = dfa.next_state(cur=cur_state, symbol=nex)
            if next_state is None:
                token.text = cur
                self.iterator.backspace()
                if cur_state not in dfa.finales:
                    token.illegal = True
                return token
            cur += nex
            cur_state = next_state
        token.text = cur
        if cur_state not in dfa.finales and cur_state != auto.empty:
            token.illegal = True
        return token

    @staticmethod
    def _validate(token, dfa_type):
        if token.illegal:
            return None, True, f'illegal token {token.text}'
        return categorize(token, dfa_type), False, ''
