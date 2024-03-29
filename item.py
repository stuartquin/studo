import re

class Item:

  def __init__( self, id, item_text ):
    # mapping from tag to colour
    self.id          = id
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
  def get_numbered( self ):
    return unicode(self.id) + ". " + self.text

  def render( self ):
    return self.pretty

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
