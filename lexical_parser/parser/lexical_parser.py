import lexical_parser.tokenization as tok


class LexicalParser:

    def __init__(self, file_path: str):
        file = open(file_path, mode='r', encoding='utf-8')
        lines = file.readlines()
        self.code = []
        for line in lines:
            for c in line:
                self.code.append(c)
        self.tokenizer = tok.Tokenizer(tok.CodeIterator(self.code))
        self.tokens = []
        self.tags = []

    def parse(self):
        self.tokens = self.tokenizer.tokenize()

    def gen_tags(self):
        for token in self.tokens:
            if token.token_type == tok.TokenType.OP:
                self.tags.append('<OP, _>')
                continue
            if token.token_type == tok.TokenType.SE:
                self.tags.append(f'<SE, _>')
                continue
            if token.token_type == tok.TokenType.IDN:
                self.tags.append(f'<IDN, {token.value}>')
                continue
            if token.token_type == tok.TokenType.INT_LITERAL or \
                    token.token_type == tok.TokenType.FLOAT_LITERAL or \
                    token.token_type == tok.TokenType.CHAR_LITERAL or \
                    token.token_type == tok.TokenType.STR_LITERAL:
                self.tags.append(f'<CONST, {token.value}>')
                continue
            self.tags.append(f'<{token.token_type.name}, _>')

    def print_token_list(self):
        if len(self.tokens) == 0:
            print('[]')
            return
        if len(self.tokens) == 1:
            print(f'[{self.tokens[0].value}]')
            return
        print('[', end='')
        for i in range(len(self.tokens) - 1):
            print(f'{self.tokens[i].value}, ', end='')
        print(f'{self.tokens[len(self.tokens) - 1].value}]')

    def print_tokens(self):
        self.gen_tags()
        for i in range(len(self.tags)):
            print(f'{self.tokens[i].value}\t\t{self.tags[i]}')
