import svgwrite

dwg = svgwrite.Drawing('test.svg')
dwg.add(dwg.line((0, 100), (100, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.text('Test', insert=(0, 20), fill='red'))
dwg.save()