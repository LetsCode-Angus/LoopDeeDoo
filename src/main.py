import lexer

lex = lexer.Lexer("var Hello, World!")
print(lex.tokenize.__doc__)