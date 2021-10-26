import syntax_parser as syn
import lexical_parser as lex


# tokenization
lex_parser = lex.LexicalParser('tests/test_01.cmm')
lex_parser.parse()
# build grammar
grammar = syn.Grammar()
grammar.construct(src='src/grammar.txt')
# build first
first_holder = syn.FirstHolder(grammar)
first_holder.construct()
first_holder.output(path='outputs/first.txt')
# build follow
follow_holder = syn.FollowHolder(grammar, first_holder, start_symbol='S')
follow_holder.construct()
follow_holder.output(path='outputs/follow.txt')
# build prediction table
pred_tab = syn.PredictionTable(grammar, first_holder, follow_holder)
pred_tab.construct()
pred_tab.output(path='outputs/prediction_table.csv')
# syntax parse
syn_parser = syn.SyntaxParser(prediction_table=pred_tab)
err, err_token, methods = syn_parser.parse(lex_parser.tokens, start_symbol='S')
if err:
    print(err_token, err_token.line_num)
syn_parser.print()
