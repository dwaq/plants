import csv
import plantgen

# Open the CSV file
with open('Inventory.csv', 'r') as file:
    reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for r, row in enumerate(reader):
        # skip the header
        if r==0:
            continue

        print(r, row)

        name = row[0]

        width = row[4]

        # already in inches
        if '"' in width:
            conversion = 1
            # remove unit
            width = width.strip('"')
        # convert to inches
        # else:
            conversion = 12

        # split into min and max
        width = width.split("-")
        
        minW = int(float(width[0])*conversion)

        # if there isn't a max, just keep it the same as min
        try:
            maxW = int(float(width[1])*conversion)
        except:
            maxW = minW

        heightRange = row[3]

        # pretty print height
        height = row[2].split("-")
        print(height)
        # range
        try:
            height = height[0]+"' - "+height[1]+"'"
        # single number
        except:
            height = height[0]+"'"

        print((name, minW, maxW, heightRange, height))
        print()
        plantgen.genPlant(name, minW, maxW, heightRange, height)

        # exit after 1st row (testing)
        # if r==2:
        #     exit()
