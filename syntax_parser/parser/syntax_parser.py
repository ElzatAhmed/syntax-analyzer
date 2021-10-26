import lexical_parser as lex
import syntax_parser.components as cpn
import syntax_parser.grammar as gmr
from .parse_table import ParseTable


class SyntaxParser:

    def __init__(self, prediction_table: cpn.PredictionTable):
        self._prediction_table = prediction_table
        self._parse_table = ParseTable()

    def parse(self, tokens: list, start_symbol: str):
        # the symbol stack
        stack = list()
        # push # in
        stack.append(gmr.hashtag)
        # push start symbol in
        stack.append(start_symbol)
        # input token stack
        # append a # token
        tokens.append(lex.Token(token_type=lex.TokenType.HASHTAG, text=gmr.hashtag))
        # used methods
        methods = []
        err = False
        err_token = None
        while True:
            # if input done break loop
            if len(tokens) == 0:
                break
            # pop from symbol stack
            stack_top = stack[-1]
            # pop from token stack
            token_top = tokens[0]
            # get token value
            token_value = token_top.get()
            # if current symbol equals to token value
            if stack_top == token_value:
                self._parse_table.add(stack, token_top, gmr.Method.empty_method())
                stack.pop(-1)
                tokens.pop(0)
                continue
            # if current symbol is epsilon
            if stack_top == gmr.epsilon:
                self._parse_table.add(stack, token_top, gmr.Method.empty_method())
                stack.pop(-1)
                continue
            # if current symbol is hashtag
            if stack_top == gmr.hashtag:
                stack_top = start_symbol
                stack.append(start_symbol)
            # if current symbol is a terminal
            if stack_top in gmr.terminals:
                err = True
                err_token = token_top
                break
            # get corresponding method
            method = self._prediction_table.get(stack_top, token_value)
            # method error
            if method.empty:
                err = True
                err_token = token_top
                break
            self._parse_table.add(stack, token_top, method)
            methods.append(method)
            # pop the stack
            stack.pop(-1)
            # push the right side of the method to the stack in reversed order
            for symbol in reversed(method.right):
                stack.append(symbol)
        return err, err_token, methods

    # def print(self):
    #     print("{: ^100}{: ^100}{: ^100}".format('stack', 'input', 'method'))
    #     for i in range(len(self._parse_table.tokens)):
    #         print("{: ^100}".format(str(self._parse_table.stacks[i])), end='')
    #         print("{: ^100}".format(str(self._parse_table.tokens[i])), end='')
    #         print("{: ^100}".format(str(self._parse_table.methods[i])))

    def print(self):
        for i in range(len(self._parse_table.tokens)):
            stack = self._parse_table.stacks[i]
            token = self._parse_table.tokens[i]
            method = self._parse_table.methods[i]
            print(f'({i}) ', end='')
            print(f'{stack[-1]}-{token}', end='')
            if method.empty:
                print('(跳过)', end='')
            print('          ', end='')
            for s in reversed(stack):
                print(s, end=' ')
            print('         ', end='')
            if not method.empty:
                print(method, end='\n')
            else:
                print()
