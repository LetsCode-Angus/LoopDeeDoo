import lexer
import _parser
import sys
import grammar
from exceptions import *

try:
  lex = lexer.Lexer(grammar.token_exprs)
  source = open(sys.argv[1], 'r').read()
  tokens = lex.tokenize(source)
  with open('tokens.txt', 'w') as file:
    for token in tokens:
      file.write(str(token) + '\n')
  par = _parser.Parser(tokens)
  par.parse()
except UnbalancedQuotes as err:
  print("Unblanced quote error: " + err.message +" @ Position: " + str(err.position))
except UnknowTokenError as err:
  print("ERROR: " + err.message)