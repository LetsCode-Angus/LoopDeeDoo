
"""This is the grammar for LoopDeeDoo. This file defines the language tokens"""

# These are the token types.
# These are used by our parser to quickly make decisions
RESERVED = 'RESERVED'
INT = 'INTEGER_LITERAL'
ID = 'IDENTIFIER'
STRING = 'STRING_LITERAL'
FLOAT = 'FLOAT_LITERAL'
TERMINATOR = 'TERMINATOR'
OPERATOR = 'OPERATOR'
SEPERATOR = 'SEPERATOR'

# Token_exprs is a list of RegExs used to match token types
# Each one is a tuple in the form (RegEx, Type)
token_exprs = [
    (r'[ \n\t]+',               None),
    (r'\(:[^\n]*',              None), # Comment
    (r'\:=',                    RESERVED),
    (r',',                      SEPERATOR),
    (r'\.',                     SEPERATOR),
    (r'\(',                     RESERVED),
    (r'\)',                     RESERVED),
    (r';',                      TERMINATOR),
    (r'\+',                     OPERATOR),
    (r'-',                      RESERVED),
    (r'\*',                     RESERVED),
    (r'/',                      RESERVED),
    (r'<=',                     RESERVED),
    (r'<',                      RESERVED),
    (r'>=',                     RESERVED),
    (r'>',                      RESERVED),
    (r'=',                      RESERVED),
    (r'!=',                     RESERVED),
    (r'if',                     RESERVED),
    (r'END',                    RESERVED),
    (r'void',                   RESERVED),
    (r'loop dee doo',           ID),
    (r'[0-9]+f',                FLOAT),
    (r'[0-9]+\.[0-9]+(f|F)?',   FLOAT),
    (r'[0-9]+',                 INT),
    (r'[A-Za-z][A-Za-z0-9_]*',  ID),
    (r'"(.*?(?<!\\))"',         STRING),
]

# These rules are used by the lexer to perform special
# changes to the value of a token after creation.
# This is usefull if the value contains chars unecessary to the parser.
sub_rules = {
    'STRING_LITERAL' : [
          (r'\"', '\"'),
          (r'\\', '\\'),
    ],
    'FLOAT_LITERAL' : [
          (r'f' : ''),
    ]
}