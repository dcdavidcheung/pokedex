"""
MIT License

Copyright (c) 2019 Claude SIMON (https://q37.info/s/rmnmqd49)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os, sys

os.chdir(os.path.dirname(os.path.realpath(__file__)))
sys.path.append("../atlastk")

import atlastk

from random import randint
from stats import get_pokedex

# DICTIONARY = [
#   "accommodate", "afterthought", "allegiance", "aloft", "ancestor", "anticipation", "antics",
#   "apparel", "ascend", "beckon", "brink", "catastrophe", "coax", "compassion", "complexion", "content",
#   "courteous", "cringe", "derelict", "dignity", "distaste", "dormant", "elaborate", "endure", "enforce",
#   "exertion", "expanse", "extraordinary", "foliage", "foremost", "frank", "function", "futile", "gaze",
#   "glimmer", "glimpse", "grimace", "headstrong", "hesitate", "hoist", "immense", "imperceptibly",
#   "indication", "inscription", "instinctive", "intent", "interior", "jar", "keepsake", "knack",
#   "literacy", "lurch", "makeshift", "malicious", "massive", "meager", "melancholy", "merge", "mingle",
#   "minuscule", "momentary", "nape", "nimble", "obstinate", "opt", "overwhelming", "pact", "pandemonium",
#   "persuade", "phenomenal", "ponder", "quantity", "quaver", "quench", "radiant", "ravine", "recipient",
#   "resentful", "satisfactory", "sensitive", "sentiment", "shudder", "sickly", "sleek", "solemn", "soothe",
#   "stagger", "stern", "tantalize", "temptation", "transform", "unscrupulous", "vain", "vengeance",
#   "violate", "vital", "vivid", "wistful", "yield", "zest"
# ]

# HANGED_MAN = "Head Body LeftArm RightArm LeftLeg RightLeg".split()


# class Core:
#   def reset(self):
#     self.errors = 0
#     self.correctGuesses = []
#     self.secretWord = ""

#   def __init__(self):
#     self.reset()


# def randword():
#   return DICTIONARY[randint(0, len(DICTIONARY)-1)]


# def showHanged(dom, errors):
#   if (errors):
#     dom.remove_class(HANGED_MAN[errors-1], "hidden")


# def showWord(dom, secretWord, correctGuesses):
#   output = ("_" * len(secretWord))
  
#   for i in range(len(secretWord)):
#     if secretWord[i] in correctGuesses:
#       output = output[:i] + secretWord[i] + output[i + 1:]

#   html = atlastk.createHTML()
#   html.put_tag_and_value("h1", output)
#   dom.inner("output", html)



# def reset(core,dom):
#   core.reset()
#   dom.inner("", open("Main.html").read())
#   core.secretWord = randword()
#   print(core.secretWord)
#   showWord(dom, core.secretWord, core.correctGuesses)



# def acConnect(core, dom):
#   reset(core,dom)


# def acSubmit(core, dom, id):
#   dom.add_class(id, "chosen")

#   guess = id.lower()

#   if guess in core.secretWord:
#     core.correctGuesses.append(guess)

#     correct = 0

#     for i in range(len(core.secretWord)):
#       if core.secretWord[i] in core.correctGuesses:
#         correct += 1

#     showWord(dom, core.secretWord, core.correctGuesses)

#     if correct == len(core.secretWord):
#       dom.alert("You've won! Congratulations!")
#       reset(core,dom)
#       return
#   else:
#     core.errors += 1
#     showHanged(dom, core.errors)

#   if core.errors >= len(HANGED_MAN):
#     dom.remove_class("Face", "hidden")
#     dom.alert("\nYou've run out of guesses. \nYou had " + str(core.errors) +
#           " errors and " + str(len(core.correctGuesses)) + " correct guesses. " +
#           "\n\nThe word was '" + core.secretWord + "'.")
#     reset(core, dom)


# def acRestart(core, dom):
#   if (core.secretWord != "" ):
#     dom.alert("You had " + str(core.errors) +
#         " errors and " + str(len(core.correctGuesses)) + " correct guesses. " +
#         "\nThe word was '" + core.secretWord + "'.")

#   reset(core, dom)

# callbacks = {
#   "": acConnect,
#   "Submit": acSubmit,
#   "Restart": acRestart
# }

# atlastk.launch(callbacks, Core, open("Head.html").read())

import atlastk

cwd = os.getcwd()
BODY = """
<fieldset style="background-color:#F5F5DC;">
  <span id="pokemon" style="width: 300px; height: 300px;"></span>
  <input id="Input" xdh:onevent="Enter" value=""/>
  <button xdh:onevent="Enter">Press to enter name</button>
  <hr/>
  <fieldset>
    <output id="Output">Type in pokemon name</output>
 </fieldset>
</fieldset>
</body>
"""

POKEDEX_ENTRY = """
<output id="Name"></output>
<fieldset>
  <span id="pokemon" style="width: 300px; height: 300px;"></span>
</fieldset>
<fieldset>
  <input id="Input" xdh:onevent="Enter" value=""/>
  <button xdh:onevent="Enter">Press to enter name</button>
  <button xdh:onevent="Shiny">Press for Shiny</button>
</fieldset>
"""
# global CURRENT
CURRENT = "bulbasaur"

pokedex = get_pokedex()
pokedex.make_dict()
print(pokedex.pokemon_dict['Eevee'].nat_dex_num)
print(pokedex.pokemon_dict['Wooloo'].nat_dex_num)
def acConnect(dom):
  dom.inner("", BODY)
  # pokemon = open("../svg_sprites/bulbasaur.svg").read()
  # pokemon = open("../test_vtracer/bulbasaur_custom_own_build.svg").read()
  # dom.inner("pokemon", pokemon)
  # pokemon = open("../svg_sprites/bulbasaur.svg").read()
  # dom.inner("pokemon1", pokemon)
  pokemon = open("../test_vtracer/bulbasaur_own_build.svg").read()
  dom.inner("pokemon", pokemon)
  dom.focus("Input")

def goToMon(dom):
  global CURRENT
  name = dom.get_value("Input")
  # Assuming user will spell name correctly right now, not much user sanitization
  # poke_name = name.lower()
  # poke_name = "-".join(name.strip().lower().split(" ")) # Deal with name edge cases
  # CURRENT = poke_name
  dom.inner("", POKEDEX_ENTRY)

  try:
    poke_name = "-".join(name.strip().lower().split(" ")) # Deal with name edge cases
    CURRENT = poke_name
    # pokemon = open(f"../svg_sprites/{poke_name}.svg").read()
    pokemon = open(f"../own_converted/{poke_name}.svg").read()
    dom.inner("pokemon", pokemon)
    capped = poke_name[0].upper()+poke_name[1:]
    dom.begin("Name", f"<div>{capped} (The {pokedex.pokemon_dict[capped].title})</div>")
  except:
    # pokemon = open(f"../svg_sprites/eevee.svg").read()
    pokemon = open(f"../own_converted/eevee.svg").read()
    dom.inner("pokemon", pokemon)
    dom.begin("Name", f"<div>Sorry can't find what you're looking for</div>")
  
  dom.set_value("Input", "")
  dom.focus("Input")

def shiny(dom):
  # name = dom.get_value("Input")
  # Assuming user will spell name correctly right now, not much user sanitization
  # poke_name = name.lower()
  # poke_name = "-".join(name.strip().lower().split(" ")) # Deal with name edge cases
  dom.inner("", POKEDEX_ENTRY)

  try:
    pokemon = open(f"../serebii_shiny_svg/{CURRENT}_s.svg").read()
    dom.inner("pokemon", pokemon)
  except:
    pokemon = open(f"../svg_sprites/eevee.svg").read()
    dom.inner("pokemon", pokemon)
  capped = CURRENT[0].upper()+CURRENT[1:]
  dom.begin("Name", f"<div>{capped} (The {pokedex.pokemon_dict[capped].title})</div>")
  
  dom.set_value("Input", "")
  dom.focus("Input")

def test(dom):
  name = dom.get_value("Input")
  # Assuming user will spell name correctly right now, not much user sanitization
  # poke_name = name.lower()
  poke_name = "-".join(name.strip().split(" ")) # Deal with name edge cases
  try:
    pokemon = open(f"../svg_sprites/{poke_name}.svg").read()
    dom.inner("pokemon", pokemon)
    dom.begin("Output", f"<div>Hi bubby, here is {name}!</div>")
  except:
    pokemon = open(f"../svg_sprites/eevee.svg").read()
    dom.inner("pokemon", pokemon)
    dom.begin("Output", f"<div>Sorry bubby, don't have picture for {name}:(</div>")
  dom.set_value("Input", "")
  dom.focus("Input")

CALLBACKS = {
  "": acConnect,
  "Enter": goToMon,
  "Shiny": shiny,
}

atlastk.launch(CALLBACKS)