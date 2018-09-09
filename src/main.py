import lexer
import _parser
import sys
import grammar

lex = lexer.Lexer(grammar.token_exprs)
source = open(sys.argv[1], 'r').read()
par = _parser.Parser(lex.tokenize(source))
par.parse()