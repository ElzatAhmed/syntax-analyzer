from lexical_parser import automa as fa, alphabet as alpha

nfa_num = fa.NFA(
    states=['S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7'],
    symbols=[n for n in fa.dfa_type_dict[fa.DfaType.NUMBER]],
    initials=['S0'],
    finales=['S7'],
    trans_func={
        'S0': {fa.epsilon: ['S1', 'S3']},
        'S1': {f'{i}': ['S2'] for i in range(0, 10)},
        'S2': {fa.epsilon: ['S3']},
        'S3': {fa.epsilon: ['S1'], '.': ['S4'], '0': ['S4'], '1': ['S4'], '2': ['S4'], '3': ['S4'],
               '4': ['S4'], '5': ['S4'], '6': ['S4'], '7': ['S4'], '8': ['S4'], '9': ['S4']},
        'S4': {fa.epsilon: ['S5', 'S7']},
        'S5': {f'{i}': ['S6'] for i in range(0, 10)},
        'S6': {fa.epsilon: ['S7']},
        'S7': {fa.epsilon: ['S5']}
    }
)

nfa_letter = fa.NFA(
    states=['S0', 'S1', 'S2', 'S3', 'S4'],
    symbols=[n for n in fa.dfa_type_dict[fa.DfaType.LETTER]],
    initials=['S0'],
    finales=['S4'],
    trans_func={
        'S0': {symbol: ['S1'] for symbol in alpha.LETTERS},
        'S1': {fa.epsilon: ['S2', 'S4']},
        'S2': {symbol: ['S1'] for symbol in fa.dfa_type_dict[fa.DfaType.LETTER]},
        'S3': {fa.epsilon: ['S4']},
        'S4': {fa.epsilon: ['S2']}
    }
)

nfa_string = fa.NFA(
    states=['S0', 'S1', 'S2', 'S3', 'S4', 'S5'],
    symbols=['\"', fa.anything],
    initials=['S0'],
    finales=['S5'],
    trans_func={
        'S0': {'\"': ['S1']},
        'S1': {fa.epsilon: ['S2', 'S4']},
        'S2': {fa.anything: ['S3']},
        'S3': {fa.epsilon: ['S4']},
        'S4': {fa.epsilon: ['S2'], '\"': ['S5']},
        'S5': {}
    }
)

nfa_char = fa.NFA(
    states=['S0', 'S1', 'S2', 'S3'],
    symbols=['\'', fa.anything],
    initials=['S0'],
    finales=['S3'],
    trans_func={
        'S0': {'\'': ['S1']},
        'S1': {fa.anything: ['S2'], fa.epsilon: ['S2']},
        'S2': {'\'': ['S3']},
        'S3': {}
    }
)

nfa_operator = fa.NFA(
    states=['S0', 'plu0', 'plu1', 'plu2', 'plu3', 'min0', 'min1', 'min2', 'min3',
            'mul0', 'mul1', 'mul2', 'div0', 'div1', 'div2', 'div3', 'mod0', 'mod1',
            'mod2', 'and0', 'and1', 'and2', 'and3', 'or0', 'or1', 'or2', 'or3', 'not0',
            'not1', 'not2', 'gre0', 'gre1', 'gre2', 'gre3', 'sma0', 'sma1', 'sma2', 'sma3',
            'equ0', 'equ1', 'equ2'],
    symbols=[n for n in fa.dfa_type_dict[fa.DfaType.OPERATOR]],
    initials=['S0'],
    finales=['plu0', 'min0', 'mul0', 'div0', 'mod0', 'and0', 'or0',
             'not0', 'gre0', 'sma0', 'equ0', 'plu2', 'plu3', 'min2',
             'min3', 'mul2', 'div2', 'div3', 'mod2', 'and2', 'and3',
             'or2', 'or3', 'not2', 'gre2', 'gre3', 'sma2', 'sma3', 'equ2'],
    trans_func={
        'S0': {
            '+': ['plu0', 'plu1'],
            '-': ['min0', 'min1'],
            '*': ['mul0', 'mul1'],
            '/': ['div0', 'div1'],
            '%': ['mod0', 'mod1'],
            '&': ['and0', 'and1'],
            '|': ['or0', 'or1'],
            '!': ['not0', 'not1'],
            '>': ['gre0', 'gre1'],
            '<': ['sma0', 'sma1'],
            '=': ['equ0', 'equ1']
        },
        'plu1': {
            '+': ['plu2'],
            '=': ['plu3']
        },
        'min1': {
            '-': ['min2'],
            '=': ['min3']
        },
        'mul1': {
            '=': ['mul2']
        },
        'div1': {
            '/': ['div2'],
            '=': ['div3']
        },
        'mod1': {
            '=': ['mod2']
        },
        'and1': {
            '&': ['and2'],
            '=': ['and3']
        },
        'or1': {
            '|': ['or2'],
            '=': ['or3']
        },
        'not1': {
            '=': ['not2']
        },
        'gre1': {
            '>': ['gre2'],
            '=': ['gre3']
        },
        'sma1': {
            '<': ['sma2'],
            '=': ['sma3']
        },
        'equ1': {
            '=': ['equ2']
        }
    }
)
