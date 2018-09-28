import sys
import ldd_core.grammar as grammar
import ldd_core.lexer as lexer
import ldd_core._parser as _parser
from ldd_core.exceptions import *

try:
  print(lexer.__doc__)
  lex = lexer.Lexer(grammar.token_exprs, grammar.sub_rules)
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