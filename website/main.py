from browser import document, bind, html
# Note: If you could avoid unnecessary import, your script will save several seconds loading time
# For example, use `"message".title()` instead of `import string; string.capwords("message")`

#@bind("#say", "click")
#def echo(event):
#    message = document["message"].value
#    document["output"].text = message.title()

def create_cards(characters):
    for i, c in enumerate(characters):
        document["cards"].attach(html.DIV(c, id="char{}".format(i)))

create_cards("一知半解一心一意一丘之貉一目了然")

def mouseover(event):
    event.target.style.cursor = "pointer"

def dragstart(event):
    event.dataTransfer.setData("character", event.target.id)

for card in document.select("#cards div"):
    card.draggable = True
    card.bind("mouseover", mouseover)
    card.bind("dragstart", dragstart)

def dragover(event):
    event.dataTransfer.dropEffect = "move"
    event.preventDefault()

def drop(event):
    character = document[event.dataTransfer.getData("character")]
    if event.target.text == "——":
        event.target.text = character.text
    else:
        to_replace = event.target.text
        event.target.text = character.text
        character.text = to_replace
    event.preventDefault()

for cell in document.select("td"):
    cell.bind("dragover", dragover)
    cell.bind("drop", drop)