from browser import document, bind, html
from random import shuffle
# Note: If you could avoid unnecessary import, your script will save several seconds loading time
# For example, use `"message".title()` instead of `import string; string.capwords("message")`

initial_cards = "一知半解一心一意一丘之貉一目了然"
initial_definitions = [
    "A little knowledge is a dangerous thing.",
    "John is a person who always works with undivided attention.",
    "These people are cut from the same cloth.",
    "His words just leapt to the eye.",
]
_characters_selector = "#table td.char"

def set_table(characters):
    for i, cell in enumerate(document.select(_characters_selector)):
        cell.text = characters[i]

set_table(initial_cards)

def write_definitions(definitions):
    for i, cell in enumerate(document.select("#table td.def")):
        cell.text = definitions[i]

write_definitions(initial_definitions)

def create_empty_cards(n):
    for i in range(n):
        document["cards"].attach(html.SPAN("", id="char{}".format(i), draggable=True))

create_empty_cards(16)

@bind("#start", "click")
def start(event):
    document["start"].text = "Restart"
    
    for cell in document.select(_characters_selector):
        if cell.id:
            cell.text = ""
    
    cards_list = list(initial_cards)
    shuffle(cards_list)
    for i, c in enumerate(cards_list):
        document["char" + str(i)].text = c

@bind("#check", "click")
def check(event):
    wrong_count = 0
    for i, cell in enumerate(document.select(_characters_selector)):
        if initial_cards[i] != cell.text:
            wrong_count = wrong_count + 1

    document["result"].text = (
        str(wrong_count) + " characters are in the wrong place."
        ) if wrong_count != 0 else "Correct!"


def mouseover(event):
    event.target.style.cursor = "pointer"

def dragstart(event):
    event.dataTransfer.setData("character", event.target.id)

for card in document.select("#cards span"):
    card.bind("mouseover", mouseover)
    card.bind("dragstart", dragstart)

def dragover(event):
    event.dataTransfer.dropEffect = "move"
    event.preventDefault()

def drop(event):
    character = document[event.dataTransfer.getData("character")]
    to_replace = event.target.text
    event.target.text = character.text
    character.text = to_replace
    event.preventDefault()

for cell in document.select(_characters_selector):
    cell.bind("dragover", dragover)
    cell.bind("drop", drop)