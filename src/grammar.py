RESERVED = 'RESERVED'
INT = 'INT'
ID = 'IDENTIFIER'
STRING = 'STRING'
TERMINATOR = 'TERMINATOR'

token_exprs = [
    (r'[ \n\t]+',               None),
    (r'\(:[^\n]*',              None), # Comment
    (r'\:=',                    RESERVED),
    (r'\(',                     RESERVED),
    (r'\)',                     RESERVED),
    (r';',                      TERMINATOR),
    (r'\+',                     RESERVED),
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