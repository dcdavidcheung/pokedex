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

from random import randint
from stats import get_pokedex

import atlastk
import re

def convert_to_3_digit_string(number):
  number = int(number)
  if number < 100:
    if number < 10:
      return "00"+str(number)
    return "0"+str(number)
  return str(number)

def cap(s):
  return s[0].upper()+s[1:]

cwd = os.getcwd()

CURRENT = "bulbasaur"
SHINY = False

pokedex = get_pokedex()
pokedex.make_dict()

def acConnect(dom):
  dom.inner("", open( "Main.html").read() )
  pokemon = open("../bw_bulb.svg").read()

  dom.inner("pokemon", pokemon)
  dom.focus("Input")

def set_fields(dom, pokemon_entry):
  dom.inner("Name", f"<div>#{convert_to_3_digit_string(pokemon_entry.nat_dex_num)} {cap(pokemon_entry.name)} (The {pokemon_entry.title})</div>")
  dom.inner("Typing", f'<div>{pokemon_entry.type_1}<br>{pokemon_entry.type_2}</div>')
  dom.inner("Stats", f'''<div> HP : {int(pokemon_entry.HP )}<br>
                                ATK: {int(pokemon_entry.ATK)}<br>
                                DEF: {int(pokemon_entry.DEF)}<br>
                                SPA: {int(pokemon_entry.SPA)}<br>
                                SPD: {int(pokemon_entry.SPD)}<br>
                                SPE: {int(pokemon_entry.SPE)}</div>''')
  weakness_field = "<div>Weaknesses:<br>"
  for weakness in pokemon_entry.weaknesses:
    weakness_field += f'{cap(weakness)} '
  weakness_field += "</div>"
  dom.inner("Weaknesses", weakness_field)
  resistances_field = "<div>Resistances:<br>"
  for resistance in pokemon_entry.resistances:
    resistances_field += f'{cap(resistance)} '
  resistances_field += "</div>"
  dom.inner("Resistances", resistances_field)
  alt_field = "<div>Alternate Formes:<br>"
  if (pokemon_entry.alt_formes != None):
    for alt in pokemon_entry.alt_formes:
      alt_field += f'{alt}<br>'
  alt_field += "</div>"
  dom.inner("Alt_formes", alt_field)

# To display both the shiny forme and normal forme, just add the shiny form to
# the pokemon variable, will show up side by side
def goToMon(dom):
  global CURRENT
  global SHINY
  SHINY = False
  name = dom.get_value("Input")
  # Assuming user will spell name correctly right now, not much user sanitization
  dom.inner("", open( "Pokedex.html").read() )

  try:
    poke_name = "-".join(name.strip().lower().split(" ")) # Deal with name edge cases
    CURRENT = poke_name
    pokemon = open(f"../serebii_normal_svg/{CURRENT}.svg").read()
    dom.inner("pokemon", pokemon)
    capped = poke_name[0].upper()+poke_name[1:]
    pokemon_entry = pokedex.pokemon_dict[capped]
    set_fields(dom, pokemon_entry)
    
  except:
    pokemon = open(f"../serebii_normal_svg/eevee.svg").read()
    dom.inner("pokemon", pokemon)
    dom.begin("Name", f"<div>Sorry can't find what you're looking for</div>")
  
  dom.set_value("Input", "")
  dom.focus("Input")

def shiny(dom):
  # Assuming user will spell name correctly right now, not much user sanitization
  global SHINY
  if SHINY:
    SHINY = False
    dom.inner("", open( "Pokedex.html").read() )

    try:
      pokemon = open(f"../serebii_normal_svg/{CURRENT}.svg").read()
      dom.inner("pokemon", pokemon)
      capped = CURRENT[0].upper()+CURRENT[1:]
      pokemon_entry = pokedex.pokemon_dict[capped]
      set_fields(dom, pokemon_entry)
    except:
      pokemon = open(f"../serebii_normal_svg/eevee.svg").read()
      dom.inner("pokemon", pokemon)
    
    dom.set_value("Input", "")
    dom.focus("Input")
  else:
    SHINY = True
    dom.inner("", open( "Pokedex.html").read() )

    try:
      pokemon = open(f"../serebii_shiny_svg/{CURRENT}_s.svg").read()
      dom.inner("pokemon", pokemon)
      capped = CURRENT[0].upper()+CURRENT[1:]
      pokemon_entry = pokedex.pokemon_dict[capped]
      set_fields(dom, pokemon_entry)
    except:
      pokemon = open(f"../serebii_normal_svg/eevee.svg").read()
      dom.inner("pokemon", pokemon)
    
    dom.set_value("Input", "")
    dom.focus("Input")

def test(dom):
  print("Not needed right now")

def blackGuess(dom):
  dom.inner("", open( "Black.html").read() )

def shinyGuess(dom):
  dom.inner("", open( "Shiny.html").read() )

def comparePokemon(dom):
  dom.inner("", open( "Comparison.html").read() )

CALLBACKS = {
  "": acConnect,
  "Enter": goToMon,
  "Shiny": shiny,
  "BlackGuess": blackGuess,
  "ShinyGuess": shinyGuess,
  "Comparison": comparePokemon,
  "Home": acConnect,
}

atlastk.launch(CALLBACKS, None, open("Head.html").read())