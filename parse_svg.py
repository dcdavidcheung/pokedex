import os

# Copy all to new directory to store a copy
# os.system("mkdir ../alt_formes_sprites")
# for svg in os.listdir(os.getcwd()+"/../svg_sprites"):
#     if "-" in svg:
#         print(svg)
#         os.system(f'scp {os.getcwd()+"/../svg_sprites/"+svg} {os.getcwd()+"/../alt_formes_sprites"}')

# Change name so that we remove alt formes for now
# e.g. arceus-normal.svg becomes arceus.svg, but mime-jr.svg stays
# for svg in os.listdir(os.getcwd()+"/../svg_sprites"):
#     if "-" in svg:
#         split_name = svg.split(".svg")[0].split("-")
#         skip = {"o", "oh", "jr", "mr", "nidoran", "porygon", "tapu", "null"}
#         different_form = True
#         for i in skip:
#             if i in split_name:
#                 print(svg)
#                 different_form = False
        
        # if different_form:
        #     print(f'Changing {os.getcwd()+"/../svg_sprites/"+svg} to {os.getcwd()+"/../svg_sprites/"+split_name[0]+".svg"}')

            # Uncomment to change
            # os.system(f'mv {os.getcwd()+"/../svg_sprites/"+svg} {os.getcwd()+"/../svg_sprites/"+split_name[0]+".svg"}')

# Parse new open source repo
# Convert with another open source repo
from stats import parse_data
pokedex = parse_data()
cwd = os.getcwd()
# Each image is specified by 3 digit number, meant for non negative
def convert_to_3_digit_string(number):
    number = int(number)
    if number < 100:
        if number < 10:
            return "00"+str(number)
        return "0"+str(number)
    return str(number)

# Need to deal with Farfetch'd line and other names with "'"
def name_converter(name):
    return "_".join(name.lower().split(" "))

# os.system("mkdir ../own_converted")
os.system(f"scp {cwd}/../open_source_repos/vtracer/vtracer .")
for pokemon in pokedex.pokemon_list:
    # os.system(f"./vtracer --input ./../open_source_repos/Pokemon/assets/imagesHQ/{convert_to_3_digit_string(pokemon.nat_dex_num)}.png --output ../own_converted/{pokemon.name.lower()}.svg")
    # os.system(f"./vtracer --input ./../open_source_repos/Pokemon/src/imageDownloader/serebii_download/{convert_to_3_digit_string(pokemon.nat_dex_num)}.png --output ../serebii_shiny_svg/{pokemon.name.lower()}_s.svg")
    # os.system(f"./vtracer --input ./../open_source_repos/Pokemon/src/imageDownloader/normal/{convert_to_3_digit_string(pokemon.nat_dex_num)}.png --output ../serebii_normal_svg/{pokemon.name.lower()}.svg")

    # Shinies
    os.system(f"./vtracer --input ./../open_source_repos/Pokemon/src/imageDownloader/serebii_download/{convert_to_3_digit_string(pokemon.nat_dex_num)}.png --output ../serebii_shiny_svg/{name_converter(pokemon.name)}_s.svg -f 1 -p 8 -g 64 -c 64 -l 4 -s 64")
    # Normal
    os.system(f"./vtracer --input ./../open_source_repos/Pokemon/src/imageDownloader/normal/{convert_to_3_digit_string(pokemon.nat_dex_num)}.png --output ../serebii_normal_svg/{name_converter(pokemon.name)}.svg -f 1 -p 8 -g 64 -c 64 -l 4 -s 64")
    # Gray scale
    os.system(f"./vtracer --input ./../open_source_repos/Pokemon/src/imageDownloader/normal/{convert_to_3_digit_string(pokemon.nat_dex_num)}.png --output ../serebii_normal_svg/{name_converter(pokemon.name)}.svg -f 1 -p 8 -g 64 -c 64 -l 4 -s 64")
    # Black silhouette
    # Shiny variants
# os.system("rm vtracer")