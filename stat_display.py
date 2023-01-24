import svgwrite

dwg = svgwrite.Drawing('test.svg')
dwg.add(dwg.line((0, 100), (100, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.text('Test', insert=(0, 20), fill='red'))
dwg.save()

# TODO: Create base image
# TODO: Add text for stats at each corner
# TODO: Use lines first stemming from circle
# TODO: Figure out how to variate the shape in the middle to display stats
# TODO: Paramertize output name to match other files