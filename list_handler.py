# Read in a file, tag etc
from item import Item, ConsoleColours

class ListHandler:
  colours = [
    ConsoleColours.CYAN,
    ConsoleColours.PINK,
    ConsoleColours.BLUE,
    ConsoleColours.GREEN,
    ConsoleColours.YELLOW,
    ConsoleColours.RED,
    ConsoleColours.GREY,
    ConsoleColours.ENDC
  ]

  def __init__( self ):
    self.items   = []
    self.file_handler   = open("/home/stuart/Dropbox/epistle/studo.txt", "r+")
    self.colour_counter = 0
    # Keep track of tags we've already coloured
    self.tag_colour_map = {}
    self.load_list()

  def load_list( self ):
    contents = self.file_handler.readlines()

    for line in contents:
      item = Item( line )
      self.decide_tag_colours( item )
      self.items.append( item )

  def output( self ):
    for item in self.items:
      print( item.pretty )

  def decide_tag_colours(self,  item ):
    """ Takes an item, decide its tag colours and assign them """
    for tag in item.tags:
      # Add a new tag
      if tag not in self.tag_colour_map:
        # Looping index
        index = self.colour_counter % len( ListHandler.colours )
        self.tag_colour_map[tag] = ListHandler.colours[index]
        self.colour_counter += 1

      item.colourify( tag, self.tag_colour_map[tag] )

  def add_item( self, item ):
    self.file_handler.write( item.text+"\n" )
