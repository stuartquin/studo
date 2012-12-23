import re

class Item:

  def __init__( self, item_text ):
    # mapping from tag to colour
    self.tag_colours = {}
    # Raw text content of an item
    self.text   = item_text
    self.pretty = item_text.strip("\n")
    self.parse_item_text()

  def parse_item_text( self ):
    """ Pull out stuff like tags """
    self.tags = re.findall( "(#[a-zA-Z0-9_-]+)", self.text )

  def set_tag_colour( self, tag, colour ):
    self.tag_colours[ tag ] = colour

  def colourify( self, tag, colour  ):
    self.pretty = re.sub( tag,
                          colour + tag + ConsoleColours.ENDC,
                          self.pretty )

class ConsoleColours:
  CYAN    = '\033[96m'
  PINK    = '\033[95m'
  BLUE    = '\033[94m'
  GREEN   = '\033[92m'
  YELLOW  = '\033[93m'
  RED     = '\033[91m'
  GREY    = '\033[90m'
  ENDC    = '\033[0m'

  @staticmethod
  def colourify( text, colour ):
    return colour + text + ConsoleColours.ENDC
