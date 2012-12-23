# StuDo

Command line todo list with tag support (sorry about the name)


## Installation

Checkout/Download the repo whereever you wish.

Create a `.studo` file in your home directory and add the following

```bash
[studo]
save_file=PATH_TO_TEXT_FILE
```

PATH_TO_TEXT_FILE should be the full path to a text file anywhere on your
system.  I chose a DropBox folder.

## Usage

### Add Item

`python studo.py -a "#feature Add support for priorities"`

### List Items

`python studo.py`

Displays a numbered list of todo items

`python studo.py -t feature`

Displays only items with the tag 'feature'

### Delete Item

`python studo.py -d <ITEM_NUMBER>`
