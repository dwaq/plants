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
        
        minW = float(width[0])*conversion

        # if there isn't a max, just keep it the same as min
        try:
            maxW = float(width[1])*conversion
        except:
            maxW = minW

        heightRange = row[3]


        height = row[4]

        print((name, minW, maxW, heightRange, height))
        print()
        plantgen.genPlant(name, minW, maxW, heightRange, height)

        # exit after 1st row (testing)
        # if r==2:
        #     exit()
