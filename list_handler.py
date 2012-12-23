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
    self.file_handler   = open("/home/stuart/Dropbox/epistle/studo.txt", "a+")
    self.colour_counter = 0
    # Keep track of tags we've already coloured
    self.tag_colour_map = {}
    self.load_list()

  def load_list( self ):
    contents = self.file_handler.readlines()
    self.item_count    = 1

    for line in contents:
      item = Item( self.item_count, line )
      self.item_count += 1
      self.decide_tag_colours( item )
      self.items.append( item )

  def delete_item( self, item_id ):
    self.items.pop( item_id-1 )
    self.write_list()

  def write_list( self ):
    self.file_handler.close()
    self.file_handler   = open("/home/stuart/Dropbox/epistle/studo.txt", "w")
    for item in self.items:
      self.file_handler.write( item.text )

  def output( self, tag = None ):
    if tag and tag[0] != "#":
      tag = "#"+tag

    for item in self.items:
      if tag is None:
          print( item.render() )
      else:
        if tag in item.tags:
          print( item.render() )

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

  def add_item( self, item_text ):
    self.item_count += 1
    item = Item( self.item_count, item_text+"\n" )
    self.file_handler.write( item.text )
