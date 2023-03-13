import svgwrite

# Fix size of final SVG for now
SIZE = 720

dwg = svgwrite.Drawing('test.svg')
dwg.add(dwg.line((0, 100), (100, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.text('Test', insert=(0, 20), fill='red'))
dwg.add(dwg.polygon([(0,0), (10,10), (10,30)], fill='blue'))
dwg.save()

# TODO: Create base image
# TODO: Add text for stats at each corner
# TODO: Use lines first stemming from circle
# TODO: Figure out how to variate the shape in the middle to display stats
# TODO: Paramertize output name to match other files

# Serebii does it with a HTML polygon
# <div class="polygon" style="clip-path: polygon(250px 168px,338.77px 198.75px,312.14px 285.88px,250px 347.38px,187.86px 285.88px,196.74px 219.25px)"></div> (Ex: Sawsbuck)
# We will do the same with a svg polygon
# Need to determine the size of the final svg and scale the points according to that