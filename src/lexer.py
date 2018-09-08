# Inherits object for python 2.x compatability
class Lexer(object):
  """The primary tokenizer object"""

  def __init__(self, source):
    self.source = source

  def tokenize(self):
    """Converts source to token stream"""

    verbs = self.source.split()

    tokens = []
        
    # Implement lexer rules here
    # Need to research a good implementation
    
    return tokens