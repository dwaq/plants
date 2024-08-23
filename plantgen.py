import svgwrite

# dwg = SVG symbols library
# name = name of plant
# minW = minimum width (diameter) of plant in inches
# minW = maximum width (diameter) of plant in inches
# heightRange = text (low, med, high) for height color coding
# height = text description of plant height (feet)
def genPlant(dwg, name, minW, maxW, heightRange, height):
    # define a font size and stroke width based on max size
    fontsize = maxW/10
    strokewidth = fontsize/30

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

    # Add the SVG as a symbol
    symbol = dwg.symbol(id=name.replace(" ", "_"))

    # maximum size
    symbol.add(dwg.circle(center=(maxWr, maxWr), r=maxWr, fill=maxC))

    # minimum size
    symbol.add(dwg.circle(center=(maxWr, maxWr), r=minWr, fill=minC))

    # Plant name
    symbol.add(dwg.text(name, insert=(maxWr, maxWr), font_size=fontsize, font_family='Arial', text_anchor='middle', alignment_baseline='middle', fill='white', stroke='black', stroke_width=strokewidth))

    # plant height
    symbol.add(dwg.text(height, insert=(maxWr, maxWr+fontsize+1), font_size=fontsize, font_family='Arial', text_anchor='middle', alignment_baseline='middle', fill='white', stroke='black', stroke_width=strokewidth))

    # Add the symbol to the defs section of the drawing
    dwg.defs.add(symbol)

    # Create a group
    group = dwg.g(id=name.replace(" ", "_"))

    # Use the symbol within the group
    group.add(dwg.use(symbol))

    # Add the symbol to the drawing
    dwg.add(group)

    # Save the SVG file
    dwg.save()

# Create an SVG drawing
dwg = svgwrite.Drawing('plants/Aromatic Aster.svg', size=(str(24)+'in', str(24)+'in'))
# Set the viewBox attribute
dwg.viewbox(minx=0, miny=0, width=24, height=24)
genPlant(dwg, "Aromatic Aster", 12, 24, "low", "1\' - 2\'")