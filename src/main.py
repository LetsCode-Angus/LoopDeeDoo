import lexer
import _parser
import sys
import grammar
from exceptions import *

try:
  lex = lexer.Lexer(grammar.token_exprs)
  source = open(sys.argv[1], 'r').read()
  par = _parser.Parser(lex.tokenize(source))
  par.parse()
except UnbalancedQuotes as err:
  print("Unblanced quote error: " + err.message +" @ Position: " + str(err.position))
except UnknowTokenError as err:
  print("ERROR: " + err.message)