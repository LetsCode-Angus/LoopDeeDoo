RESERVED = 'RESERVED'
INT = 'INTEGER_LITERAL'
ID = 'IDENTIFIER'
STRING = 'STRING_LITERAL'
FLOAT = 'FLOAT_LITERAL'
TERMINATOR = 'TERMINATOR'
OPERATOR = 'OPERATOR'
SEPERATOR = 'SEPERATOR'

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

sub_rules = {
    'STRING' : [
          (r'\"', '\"'),
          (r'\\', '\\')
      ]
}