from .src import *
import lexical_parser.automa as auto


def construct():

    dfa_num = nfa_num.convert2Dfa()
    dfa_num.minimize()

    dfa_letter = nfa_letter.convert2Dfa()
    dfa_letter.minimize()

    dfa_operator = nfa_operator.convert2Dfa()
    dfa_operator.minimize()

    dfa_string = nfa_string.convert2Dfa()
    dfa_string.minimize()

    dfa_char = nfa_char.convert2Dfa()
    dfa_char.minimize()

    return {
        auto.DfaType.NUMBER: dfa_num,
        auto.DfaType.PURE_LETTER: dfa_letter,
        auto.DfaType.OPERATOR: dfa_operator,
        auto.DfaType.STRING: dfa_string,
        auto.DfaType.CHAR: dfa_char
    }
