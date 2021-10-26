import enum


class DfaType(enum.Enum):
    NUMBER = 0
    LETTER = 1
    OPERATOR = 2
    SEQUENCE_END = 3
    DOT = 4
    PURE_NUMBER = 5
    PURE_LETTER = 6
    STRING = 7
    CHAR = 8


dfa_type_dict = {
    DfaType.NUMBER: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'],
    DfaType.LETTER: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z', '_', 'A', 'B', 'C',
                     'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                     'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6',
                     '7', '8', '9'],
    DfaType.OPERATOR: ['+', '-', '*', '/', '%', '&', '|', '!', '=', '>', '<'],
    DfaType.STRING: ['\"'],
    DfaType.CHAR: ['\''],
    DfaType.SEQUENCE_END: ['(', ')', '{', '}', '[', ']', ';', ','],
    DfaType.DOT: ['.'],
    DfaType.PURE_NUMBER: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    DfaType.PURE_LETTER: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                          'u', 'v', 'w', 'x', 'y', 'z', '_', 'A', 'B', 'C',
                          'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                          'X', 'Y', 'Z'],
}
