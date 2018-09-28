import re
import sys
from ldd_core.exceptions import *

# Inherits object for python 2.x compatability
class Lexer(object):
  """The primary tokenizer object"""

  def __init__(self, token_exprs):
    self.token_exprs = token_exprs

  def tokenize(self, source):
    """Converts source to token stream"""

    exprs = self.token_exprs
    pos = 0
    tokens = []

    while pos < len(source):
      match = None
      for expression in exprs:
        pattern, tag = expression
        regex = re.compile(pattern)

        # Tests for regex match at pos, if found continues to match characters until
        # no further matches are found. If there is no match, match returns 'None'
        match = regex.match(source, pos)
        if match:
          text = match.group(0)
          if tag:
            token = (tag, text)
            # ! HACK: Handles string escaping
            # TODO: Implement proper sub rules here
            if tag == 'STRING':
              token = (tag, text[1:-1].replace('\\"', '\"'))
            
            tokens.append(token)
          break

      if not match:
        if source[pos] == '"': raise UnbalancedQuotes(pos, "Quotes were unbalanced")
        else: raise UnknowTokenError(pos, source[pos])
      else:
        pos = match.end(0)
        
    return tokens