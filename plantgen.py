import svgwrite

# Create an SVG drawing
dwg = svgwrite.Drawing('Aromatic Aster.svg', size=('24in', '24in'))

# Set the viewBox attribute
dwg.viewbox(minx=0, miny=0, width=24, height=24)

# Add a title to the SVG
dwg.set_desc(title='Aromatic Aster')

# maximum size
dwg.add(dwg.circle(center=(12, 12), r=12, fill='lightgreen'))

# minimum size
dwg.add(dwg.circle(center=(12, 12), r=6, fill='green'))

# Plant name
dwg.add(dwg.text('Aromatic Aster', insert=(12, 12), font_size='3', font_family='Arial', text_anchor='middle', alignment_baseline='middle', fill='white', stroke='black', stroke_width='0.1'))

# plant height
dwg.add(dwg.text('1\' - 2\'', insert=(12, 16), font_size='3', font_family='Arial', text_anchor='middle', alignment_baseline='middle', fill='white', stroke='black', stroke_width='0.1'))

# Save the SVG file
dwg.save()
