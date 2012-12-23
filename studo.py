# simple command line app for creating and managing todos
# Saves to plain text files
import argparse
import os
import ConfigParser

from list_handler import ListHandler
from item import Item


class StuDo:

  def __init__( self ):
    self.app_description = """
        A simple command line utility for creating and managing plain text
        todo files"""
    self.read_config()
    # this is read from config
    self.list_handler = ListHandler( self.save_file )
    self.parse_args()

  def read_config( self, filename="~/.studo" ):
    config = ConfigParser.ConfigParser()
    config.read( os.path.expanduser( filename ) )
    self.save_file = config.get("studo", "save_file", None)

  def parse_args( self ):
    """ Parses command line args and calls appropriate function """
    parent_parser = argparse.ArgumentParser( description=self.app_description )

    parent_parser.add_argument( "-a", "--add",
                                type=str,
                                required=False)

    parent_parser.add_argument( "-d", "--delete",
                                type=int,
                                required=False)

    parent_parser.add_argument( "-t", "--tag",
                                type=str,
                                required=False)

    args = parent_parser.parse_args()

    # Either adding or listing
    if args.add:
      self.add_item( args.add )
      return

    if args.delete:
      self.delete_item( args.delete )

    self.list_items( args.tag )

  def add_item( self, item ):
    self.list_handler.add_item( unicode(item) )

  def delete_item( self, item_id ):
    self.list_handler.delete_item( item_id )

  def list_items( self, tag ):
    self.list_handler.output( tag )

if __name__ == "__main__":
  stu_do = StuDo()
