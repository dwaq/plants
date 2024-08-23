import svgwrite

# name = name of plant
# minW = minimum width (diameter) of plant in inches
# minW = maximum width (diameter) of plant in inches
# heightRange = text (low, med, high) for height color coding
# height = text description of plant height (feet)
def genPlant(name, minW, maxW, heightRange, height):
    # define a font size (may be calculated later)
    fontsize = 3

    # calculate radius here since they are needed
    maxWr = int(maxW/2)
    minWr = int(minW/2)

    # color code based on height
    if (heightRange == "low"):
        maxC = "pink"
        minC = "red"
    if (heightRange == "med"):
        maxC = "lightgreen"
        minC = "green"
    if (heightRange == "high"):
        maxC = "lightblue"
        minC = "blue"

    # Create an SVG drawing
    dwg = svgwrite.Drawing(name+'.svg', size=(str(maxW)+'in', str(maxW)+'in'))

    # Set the viewBox attribute
    dwg.viewbox(minx=0, miny=0, width=maxW, height=maxW)

    # Add a title to the SVG
    dwg.set_desc(title=name)

    # maximum size
    dwg.add(dwg.circle(center=(maxWr, maxWr), r=maxWr, fill=maxC))

    # minimum size
    dwg.add(dwg.circle(center=(maxWr, maxWr), r=minWr, fill=minC))

    # Plant name
    dwg.add(dwg.text(name, insert=(maxWr, maxWr), font_size=fontsize, font_family='Arial', text_anchor='middle', alignment_baseline='middle', fill='white', stroke='black', stroke_width='0.1'))

    # plant height
    dwg.add(dwg.text(height, insert=(maxWr, maxWr+fontsize+1), font_size=fontsize, font_family='Arial', text_anchor='middle', alignment_baseline='middle', fill='white', stroke='black', stroke_width='0.1'))

    # Save the SVG file
    dwg.save()


genPlant("Aromatic Aster", 12, 24, "low", "1\' - 2\'")