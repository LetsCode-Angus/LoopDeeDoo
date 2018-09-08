# Inherits object for python 2.x compatability
class Parser(object):
  """Genrates abstract syntax tree from tokens"""

  def __init__(self, tokens):
    self.tokens = tokens

  def parse(self):
    """Converts token stream to AST"""

    tokens = self.tokens