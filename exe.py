import lexical_parser as lex
import syntax_parser as syn
import sys


def tokens(path: str):
    lexical_parser = lex.LexicalParser(path)
    lexical_parser.parse()
    lexical_parser.print_tokens()


def token_list(path: str):
    lexical_parser = lex.LexicalParser(path)
    lexical_parser.parse()
    lexical_parser.print_token_list()


def first():
    grammar = syn.Grammar()
    grammar.construct(src='src/grammar.txt')
    first_holder = syn.FirstHolder(grammar)
    first_holder.construct()
    first_holder.output()


def follow():
    grammar = syn.Grammar()
    grammar.construct(src='src/grammar.txt')
    first_holder = syn.FirstHolder(grammar)
    first_holder.construct()
    follow_holder = syn.FollowHolder(grammar, first_holder, start_symbol='S')
    follow_holder.construct()
    follow_holder.output()


def table():
    grammar = syn.Grammar()
    grammar.construct(src='src/grammar.txt')
    first_holder = syn.FirstHolder(grammar)
    first_holder.construct()
    follow_holder = syn.FollowHolder(grammar, first_holder, start_symbol='S')
    follow_holder.construct()
    follow_holder.output()
    pred_table = syn.PredictionTable(grammar, first_holder, follow_holder)
    pred_table.construct()
    pred_table.output(path='outputs/prediction_table.csv')


def syntax_parse(path: str):
    lexical_parser = lex.LexicalParser(path)
    lexical_parser.parse()
    grammar = syn.Grammar()
    grammar.construct(src='src/grammar.txt')
    first_holder = syn.FirstHolder(grammar)
    first_holder.construct()
    follow_holder = syn.FollowHolder(grammar, first_holder, start_symbol='S')
    follow_holder.construct()
    pred_table = syn.PredictionTable(grammar, first_holder, follow_holder)
    pred_table.construct()
    syntax_parser = syn.SyntaxParser(pred_table)
    err, err_token, methods = syntax_parser.parse(lexical_parser.tokens, start_symbol='S')
    syntax_parser.print()
    if err:
        print('-------------------------error------------------------')
        print(f'error token {err_token} on line {err_token.line_num}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('missing argument!')
    else:
        if len(sys.argv) == 3 and sys.argv[1] == 'token':
            tokens(sys.argv[2])
        elif len(sys.argv) == 3 and sys.argv[1] == 'list':
            token_list(sys.argv[2])
        elif len(sys.argv) == 2 and sys.argv[1] == 'first':
            first()
        elif len(sys.argv) == 2 and sys.argv[1] == 'follow':
            follow()
        elif len(sys.argv) == 2 and sys.argv[1] == 'table':
            table()
        elif len(sys.argv) == 3 and sys.argv[1] == 'parse':
            syntax_parse(sys.argv[2])
        else:
            print('argument error!')
