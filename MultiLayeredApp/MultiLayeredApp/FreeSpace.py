
materialsL = [
    {"Name":"AL2","Type": "Metal"},
    {"Name":"Fe3","Type": "Iron"}
]



rowIndex = 0
for material in materialsL:
    columnLength = len(materialsL[0].values())
    for columnIndex in range(columnLength):
        inner = list(material.keys())[columnIndex]
        print(inner)
        pass
    rowIndex += 1
