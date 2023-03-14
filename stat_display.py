import svgwrite
import math

# Fix size of final SVG for now (Image Size and Size of Polygon)
IMG_SIZE = 900
SIZE = 720

dwg = svgwrite.Drawing('test.svg', size=(IMG_SIZE,IMG_SIZE))
# dwg.add(dwg.line((0, 100), (100, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
# dwg.add(dwg.text('Test', insert=(0, 20), fill='red'))
# dwg.add(dwg.polygon([(0,0), (10,10), (10,30)], fill='blue'))
# dwg.save()

# TODO: Create base image
# TODO: Add text for stats at each corner
# TODO: Use lines first stemming from circle
# TODO: Figure out how to variate the shape in the middle to display stats
# TODO: Paramertize output name to match other files

# Serebii does it with a HTML polygon
# <div class="polygon" style="clip-path: polygon(250px 168px,338.77px 198.75px,312.14px 285.88px,250px 347.38px,187.86px 285.88px,196.74px 219.25px)"></div> (Ex: Sawsbuck)
# We will do the same with a svg polygon
# Need to determine the size of the final svg and scale the points according to that

# Need to grab the highest overall stat and have that be the scaling factor
HIGHEST_STAT = 150
# TEST = [100, 120,  130,  90,  60, 110]
TEST = [100, 100, 100, 100, 100, 100]

# input: stats -> expects list of stats in order of HP, ATK, DEF, SPA, SPD, SPE
# output:      -> returns point list for SVG polygon
def gen_polygon_stats(stats):
    ret_L = []
    # HP
    # Line from center straight up (SIZE/2,SIZE/2)->(SIZE/2,0)
    length = stats[0]/HIGHEST_STAT * SIZE/2
    ret_L.append((int(IMG_SIZE/2),int(IMG_SIZE/2-length)))

    # ATK
    # Line from center 30 degrees above right perpendicular (SIZE/2,SIZE/2)->(SIZE-SIZE*SQRT(3)/4,SIZE/4)
    length = stats[1]/HIGHEST_STAT * SIZE/2
    ret_L.append((int(IMG_SIZE/2+length*math.sqrt(3)/2),int(IMG_SIZE/2-length/2)))

    # DEF
    # Line from center 30 degrees below right perpendicular (SIZE/2,SIZE/2)->(SIZE-SIZE*SQRT(3)/4,3*SIZE/4)
    length = stats[2]/HIGHEST_STAT * SIZE/2
    ret_L.append((int(IMG_SIZE/2+length*math.sqrt(3)/2),int(IMG_SIZE/2+length/2)))

    # SPE
    # Line from center straight down (SIZE/2,SIZE/2)->(SIZE/2,SIZE)
    length = stats[5]/HIGHEST_STAT * SIZE/2
    ret_L.append((int(IMG_SIZE/2),int(IMG_SIZE/2+length)))

    # SPD
    # Line from center 30 degrees below left perpendicular (SIZE/2,SIZE/2)->(SIZE/2-SIZE*SQRT(3)/2,3*SIZE/4)
    length = stats[4]/HIGHEST_STAT * SIZE/2
    ret_L.append((int(IMG_SIZE/2-length*math.sqrt(3)/2),int(IMG_SIZE/2+length/2)))

    # SPA
    # Line from center 30 degrees above left perpendicular (SIZE/2,SIZE/2)->(SIZE/2-SIZE*SQRT(3)/4,SIZE/4)
    length = stats[3]/HIGHEST_STAT * SIZE/2
    ret_L.append((int(IMG_SIZE/2-length*math.sqrt(3)/2),int(IMG_SIZE/2-length/2)))

    return ret_L

# Draw hexagons
def gen_polygon(length):
    ret_L = []
    # HP
    # Line from center straight up (SIZE/2,SIZE/2)->(SIZE/2,0)
    # length = stats[0]/HIGHEST_STAT * SIZE/2
    ret_L.append((int(IMG_SIZE/2),int(IMG_SIZE/2-length)))

    # ATK
    # Line from center 30 degrees above right perpendicular (SIZE/2,SIZE/2)->(SIZE-SIZE*SQRT(3)/4,SIZE/4)
    # length = stats[1]/HIGHEST_STAT * SIZE/2
    ret_L.append((int(IMG_SIZE/2+length*math.sqrt(3)/2),int(IMG_SIZE/2-length/2)))

    # DEF
    # Line from center 30 degrees below right perpendicular (SIZE/2,SIZE/2)->(SIZE-SIZE*SQRT(3)/4,3*SIZE/4)
    # length = stats[2]/HIGHEST_STAT * SIZE/2
    ret_L.append((int(IMG_SIZE/2+length*math.sqrt(3)/2),int(IMG_SIZE/2+length/2)))

    # SPE
    # Line from center straight down (SIZE/2,SIZE/2)->(SIZE/2,SIZE)
    # length = stats[5]/HIGHEST_STAT * SIZE/2
    ret_L.append((int(IMG_SIZE/2),int(IMG_SIZE/2+length)))

    # SPD
    # Line from center 30 degrees below left perpendicular (SIZE/2,SIZE/2)->(SIZE/2-SIZE*SQRT(3)/2,3*SIZE/4)
    # length = stats[4]/HIGHEST_STAT * SIZE/2
    ret_L.append((int(IMG_SIZE/2-length*math.sqrt(3)/2),int(IMG_SIZE/2+length/2)))

    # SPA
    # Line from center 30 degrees above left perpendicular (SIZE/2,SIZE/2)->(SIZE/2-SIZE*SQRT(3)/4,SIZE/4)
    # length = stats[3]/HIGHEST_STAT * SIZE/2
    ret_L.append((int(IMG_SIZE/2-length*math.sqrt(3)/2),int(IMG_SIZE/2-length/2)))
    # print(ret_L)
    return ret_L

# Add text to display stats
def write_stats(length, dwg):
    # HP
    # Line from center straight up (SIZE/2,SIZE/2)->(SIZE/2,0)
    # length = stats[0]/HIGHEST_STAT * SIZE/2
    dwg.add(dwg.text(' HP: {}'.format(TEST[0]), insert=(int(IMG_SIZE/2),int(IMG_SIZE/2-length)), fill='red'))

    # ATK
    # Line from center 30 degrees above right perpendicular (SIZE/2,SIZE/2)->(SIZE-SIZE*SQRT(3)/4,SIZE/4)
    # length = stats[1]/HIGHEST_STAT * SIZE/2
    dwg.add(dwg.text('ATK: {}'.format(TEST[0]), insert=(int(IMG_SIZE/2+length*math.sqrt(3)/2),int(IMG_SIZE/2-length/2)), fill='red'))

    # DEF
    # Line from center 30 degrees below right perpendicular (SIZE/2,SIZE/2)->(SIZE-SIZE*SQRT(3)/4,3*SIZE/4)
    # length = stats[2]/HIGHEST_STAT * SIZE/2
    dwg.add(dwg.text('DEF: {}'.format(TEST[0]), insert=(int(IMG_SIZE/2+length*math.sqrt(3)/2),int(IMG_SIZE/2+length/2)), fill='red'))

    # SPE
    # Line from center straight down (SIZE/2,SIZE/2)->(SIZE/2,SIZE)
    # length = stats[5]/HIGHEST_STAT * SIZE/2
    dwg.add(dwg.text('SPE: {}'.format(TEST[0]), insert=(int(IMG_SIZE/2),int(IMG_SIZE/2+length)), fill='red'))

    # SPD
    # Line from center 30 degrees below left perpendicular (SIZE/2,SIZE/2)->(SIZE/2-SIZE*SQRT(3)/2,3*SIZE/4)
    # length = stats[4]/HIGHEST_STAT * SIZE/2
    dwg.add(dwg.text('SPD: {}'.format(TEST[0]), insert=(int(IMG_SIZE/2-length*math.sqrt(3)/2),int(IMG_SIZE/2+length/2)), fill='red'))

    # SPA
    # Line from center 30 degrees above left perpendicular (SIZE/2,SIZE/2)->(SIZE/2-SIZE*SQRT(3)/4,SIZE/4)
    # length = stats[3]/HIGHEST_STAT * SIZE/2
    dwg.add(dwg.text('SPA: {}'.format(TEST[0]), insert=(int(IMG_SIZE/2-length*math.sqrt(3)/2),int(IMG_SIZE/2-length/2)), fill='red'))

def add_polygon(points):
    dwg.add(dwg.polygon(points, fill='gray'))

dwg.add(dwg.polygon([(0,0),(IMG_SIZE,0),(IMG_SIZE,IMG_SIZE),(0,IMG_SIZE)], fill='beige'))
dwg.add(dwg.polygon(gen_polygon_stats(TEST), fill='#64daec'))
# Have text for stat and number here
# dwg.add(dwg.polygon(gen_polygon(((IMG_SIZE-SIZE)/2+SIZE)/2), stroke="red", fill="none"))
write_stats(((IMG_SIZE-SIZE)/2+SIZE)/2, dwg)
dwg.add(dwg.polygon(gen_polygon(SIZE/2), stroke="green", fill="none"))
dwg.add(dwg.polygon(gen_polygon(SIZE*3/8), stroke="green", fill="none"))
dwg.add(dwg.polygon(gen_polygon(SIZE/4), stroke="green", fill="none"))
dwg.add(dwg.polygon(gen_polygon(SIZE/8), stroke="green", fill="none"))
dwg.add(dwg.polygon(gen_polygon(SIZE/32), stroke="green", fill="none"))
# add_polygon(TEST)
dwg.save()