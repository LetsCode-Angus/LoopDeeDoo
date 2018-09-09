class UnknowTokenError(Exception):

  def __init__(self, position, char):
    self.message = "An uknown fatal error has occured at position: " + str(position) + f'[{char}]'

class UnbalancedQuotes(Exception):
  """There are unbalnced quotes in source file"""

  def __init__(self, position, message):
    self.position = position
    self.message = message