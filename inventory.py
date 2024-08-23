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

        width = row[2].split("-")

        minW = int(width[0])*12
        maxW = int(width[1])*12
        heightRange = row[3]
        height = row[4]


        plantgen.genPlant(name, minW, maxW, heightRange, height)

        # exit after 1st row (testing)
        if r==1:
            exit()
