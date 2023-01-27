import csv
import copy

# Types also represented as indicies
types = {
    'normal': 0,
    'fire': 1,
    'water': 2,
    'electric': 3,
    'grass': 4,
    'ice': 5, 
    'fighting': 6,
    'poison': 7,
    'ground': 8,
    'flying': 9,
    'psychic': 10,
    'bug': 11,
    'rock': 12,
    'ghost': 13,
    'dragon': 14,
    'dark': 15,
    'steel':16,
    'fairy': 17,
    '': None
}

#   Entry (x, y) = z means that x is z times effective on y
#     e.g (1, 0) = 0.5 means that fire is 0.5 times effective on fire
type_matchups = [
    [  1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 0.5,   0,   1,   1, 0.5,   1], # Normal
    [  1, 0.5, 0.5,   1,   2,   2,   1,   1,   1,   1,   1,   2, 0.5,   1, 0.5,   1,   2,   1], # Fire
    [  1,   2, 0.5,   1, 0.5,   1,   1,   1,   2,   1,   1,   1,   2,   1, 0.5,   1,   1,   1], # Water
    [  1,   1,   2, 0.5, 0.5,   1,   1,   1,   0,   2,   1,   1,   1,   1, 0.5,   1,   1,   1], # Electric
    [  1, 0.5,   2,   1, 0.5,   1,   1, 0.5,   2, 0.5,   1, 0.5,   2,   1, 0.5,   1, 0.5,   1], # Grass
    [  1, 0.5, 0.5,   1,   2, 0.5,   1,   1,   2,   2,   1,   1,   1,   1,   2,   1, 0.5,   1], # Ice
    [  2,   1,   1,   1,   1,   2,   1,   1,   1, 0.5, 0.5, 0.5,   2,   0,   1,   2,   2, 0.5], # Fighting
    [  1,   1,   1,   1,   2,   1,   1, 0.5, 0.5,   1,   1,   1, 0.5, 0.5,   1,   1,   0,   2], # Poison
    [  1,   2,   1,   2, 0.5,   1,   1,   2,   1,   0,   1, 0.5,   2,   1,   1,   1,   2,   1], # Ground
    [  1,   1,   1, 0.5,   2,   1,   2,   1,   1,   1,   1,   2, 0.5,   1,   1,   1, 0.5,   1], # Flying
    [  1,   1,   1,   1,   1,   1,   2,   2,   1,   1, 0.5,   1,   1,   1,   1,   0, 0.5,   1], # Psychic
    [  1, 0.5,   1,   1,   2,   1, 0.5, 0.5,   1, 0.5,   2,   1,   1, 0.5,   1,   2, 0.5, 0.5], # Bug
    [  1,   2,   1,   1,   1,   2, 0.5,   1, 0.5,   2,   1,   2,   1,   1,   1,   1, 0.5,   1], # Rock
    [  0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   1,   1,   2,   1, 0.5,   1,   1], # Ghost
    [  1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   1, 0.5,   0], # Dragon
    [  1,   1,   1,   1,   1,   1, 0.5,   1,   1,   1,   2,   1,   1,   2,   1, 0.5,   1, 0.5], # Dark
    [  1, 0.5, 0.5, 0.5,   1,   2,   1,   1,   1,   1,   1,   1,   2,   1,   1,   1, 0.5,   2], # Steel
    [  1, 0.5,   1,   1,   1,   1,   2, 0.5,   1,   1,   1,   1,   1,   1,   2,   2, 0.5,   1]  # Fairy
]
num_types = len(type_matchups[0])

def transpose(L):
    ret = copy.deepcopy(L)
    for i in range(len(L)):
        for j in range(len(L[0])):
            ret[i][j] = L[j][i]
    return ret

# resistance_matchups = transpose(type_matchups)

# Return list documenting weaknesses
# Input: Indicies of types (type2 optional, but type1 can only be None if specified)
# Output: List of weaknesses
def get_weakness(type1, type2=None):
    base = [1] * num_types

    # Typeless have no weaknesses
    if type1 == None:
        return base
    
    # Dual-type
    if not type2 == None:
        for i in range(num_types):
            base[i] = base[i] * type_matchups[type2][i]
    
    # Mono-type & Dual-type
    for i in range(num_types):
            base[i] = base[i] * type_matchups[type1][i]

    ret_list = copy.deepcopy(base)
    return ret_list

# Deal with typeless later
def get_matchups(type1, type2):
    base = [1] * num_types

    t1 = types[type1.lower()]
    t2 = types[type2.lower()]
    if not t2 == None:
        for i in range(num_types):
            base[i] = base[i] * type_matchups[i][t2]
    # Mono-type & Dual-type
    for i in range(num_types):
            base[i] = base[i] * type_matchups[i][t1]
    ret_list = copy.deepcopy(base)
    return ret_list

# Database for each pokemon object
class Pkmn_Data(object):
    def __init__(self):
        self.pokemon_list = []
        self.pokemon_dict = {}
        self.type_matchups = copy.deepcopy(type_matchups)

    def add_init_info(self):
        self = self

    def add_pkmn(self, newpkmn):
        self.pokemon_list.append(newpkmn)

    def add_alt_forme(self, prior_num, alt_formes_list):
        # Pokemon in list will be offset by 1, prior_num in pokdex_number is 1 more
        if (prior_num != 0 and alt_formes_list != []):
            self.pokemon_list[-1].add_alt_forme(alt_formes_list)

    def make_dict(self):
        for pokemon in self.pokemon_list:
            self.pokemon_dict[pokemon.name] = pokemon

    # TODO: Add modifiers to allow this to seperate by {Normal, Sub Legendary, Mythical, Legendary} and {1, 2, 3, 4, 5, 6 ,7, 8} for generation
    def get_avg_stat(self, stat='total'):
        ret = 0
        for pokemon in self.pokemon_list:
            match stat:
                case 'hp':
                    ret += pokemon.HP
                case 'attack':
                    ret += pokemon.ATK
                case 'defense':
                    ret += pokemon.DEF
                case 'sp_attack':
                    ret += pokemon.SPA
                case 'sp_defense':
                    ret += pokemon.SPD
                case 'speed':
                    ret += pokemon.SPE
                case 'total':
                    ret += pokemon.HP + pokemon.ATK + pokemon.DEF + pokemon.SPA + pokemon.SPD + pokemon.SPE
                case 'height_m':
                    ret += pokemon.height
                case 'weight_kg':
                    ret += pokemon.weight
                case default:
                    print('Unexpected, change to error interrupt later')
        return ret / len(self.pokemon_list)


# Pokemon object containing data for each pokemon
class Pkmn(object):

    def __init__(self, info_vector):
        self.init_info   = info_vector
        self.nat_dex_num = None
        self.type_1      = None
        self.type_2      = None
        self.name        = None
        self.title       = None
        self.ability_1   = None
        self.ability_2   = None
        self.ability_h   = None
        self.HP          = None
        self.ATK         = None
        self.DEF         = None
        self.SPA         = None
        self.SPD         = None
        self.SPE         = None
        self.height      = None
        self.weight      = None
        self.weaknesses  = None
        self.resistances = None
        self.alt_formes  = None

        self.use_init_info()

    def use_init_info(self):
        # Initialize each part, trap errors later
        self.nat_dex_num    =              self.init_info['pokedex_number']
        self.type_1         =              self.init_info['type_1']
        self.type_2         =              self.init_info['type_2']
        self.name           =              self.init_info['name']
        self.gen            =              self.init_info['generation']
        self.status         =              self.init_info['status']
        self.title          =              self.init_info['species']
        self.ability_1      =              self.init_info['ability_1']
        self.ability_2      =              self.init_info['ability_2']
        self.ability_h      =              self.init_info['ability_hidden']
        self.HP             =        float(self.init_info['hp'])
        self.ATK            =        float(self.init_info['attack'])
        self.DEF            =        float(self.init_info['defense'])
        self.SPA            =        float(self.init_info['sp_attack'])
        self.SPD            =        float(self.init_info['sp_defense'])
        self.SPE            =        float(self.init_info['speed'])
        self.height         =        float(self.init_info['height_m'])
        try:self.weight     =        float(self.init_info['weight_kg'])
        except:self.weight  =              None
        self.type_matchups  = get_matchups(self.type_1, self.type_2)
        self.weaknesses     =  get_weaknesses(self.type_matchups)
        self.resistances    = get_resistances(self.type_matchups)

    def add_alt_forme(self, alt_formes_list):
        self.alt_formes = alt_formes_list

# Get average of a list (Float)
def listavg(L):
    sum = 0
    count = len(L) # Can count up as well, but O(n) is the same
    for i in L:
        if i >= count:
            exit("Why")
        if not isinstance(L[i], (int, float)):
            exit("Why")
        sum += L[i]
    return sum / count

# Return list of pokemon each accounted for once
# Sort out edge cases
def get_PokedexList(L):
    retlist = []
    for ent in L:
        if " " in ent:
            if ent in ["Mr. Mime", "Mime Jr.", "Type: Null", "Mr. Rime", "Deoxys Normal Forme", "Wormadam Plant Cloak", "Giratina Altered Forme", "Shaymin Land Forme", "Basculin Red-Striped Form", "Darmanitan Standard Mode", "Tornadus Incarnate Forme", "Thundurus Incarnate Forme", "Landorus Incarnate Forme", "Keldeo Ordinary Forme", "Meloetta Aria Forme", "Meowstic Female", "Aegislash Blade Forme", "Pumpkaboo Average Size", "Gourgeist Average Size", "Zygarde 50% Forme", "Hoopa Hoopa Confined", "Oricorio Baile Style", "Lycanroc Midday Form", "Wishiwashi School Form", "Minior Meteor Form", "Tapu Koko", "Tapu Lele", "Tapu Bulu", "Tapu Fini", "Toxtricity Amped Form", "Eiscue Ice Face", "Indeedee Male", "Morpeko Full Belly Mode", "Zacian Hero of Many Battles", "Zamazenta Hero of Many Battles"]:
                retlist.append(ent)
        elif ent == "Ash-Greninja" or (ent.split(" ")[0] in {"Mega", "Alolan", "Galarian"}) or (ent.split(" ")[-1] in {"Forme", "Female", "Male"}):
            continue
        else:
            retlist.append(ent)
    return retlist

# return lowercase and whitespace removed string
def lower_and_strip(s):
    if not isinstance(s, str):
        exit("Stop it")
    s = s.lower()
    ret_S = ""
    for i in s:
        if i.isalnum() or i == "_":
            ret_S += i
    return ret_S

# First line contains the headers
# Make a pokemon object every first occurence of the pokedex number in the csv file
# Skip alternate forms for now, add names to list
def parse_data(filename='pokemon.csv'):
    pokedex = Pkmn_Data()

    with open(filename, newline='') as csvfile:
        lines = csv.DictReader(csvfile, delimiter=',')

        # First line contains the headers
        # Don't really need the headers, in each dictionary already, keeping for legacy
        # headers = lines.fieldnames

        # Go to pokemon
        # next(lines)

        alt_formes = []
        added_numbers = set()
        for line in lines:
            # Make pokemon objects

            # Check pokedex number, only want to make one pokemon object per number
            pokemon_num = line['pokedex_number']
            if pokemon_num in added_numbers:
                # Tag on list/set of alternate formes 
                alt_formes.append(line['name'])
            else:
                # When reaching next pokemon, we need to add the alt formes list to the last pokemon in the list
                pokedex.add_alt_forme(int(pokemon_num)-1, alt_formes)
                added_numbers.add(pokemon_num)

                # Clear the alt formes list
                alt_formes = []

                # Make new pokemon object
                new_pokemon = Pkmn(line)
                pokedex.add_pkmn(new_pokemon)
        
    return pokedex

def get_pokedex(filedata='pokemon.csv'):
    return parse_data(filedata)

def reverse_dict(D):
    new_D = {}
    for key in D:
        new_D[D[key]] = key
    return new_D

ind_to_type = reverse_dict(types)

def get_weaknesses(matchups):
    L = []
    for typing in range(len(matchups)):
        if matchups[typing] > 1:
            L.append(ind_to_type[typing])
    return L
def get_resistances(matchups):
    L = []
    for typing in range(len(matchups)):
        if matchups[typing] < 1:
            L.append(ind_to_type[typing])
    return L

if __name__ == "__main__":
    # pokedex = parse_data()
    status = 0