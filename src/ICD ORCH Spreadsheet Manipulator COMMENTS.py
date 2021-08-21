import csv

codeList = []
tempCodeList = []
dataList = []

with open('ICD CODES ORCH.csv', newline='') as codes:
    reader = csv.reader(codes)
    for row in reader:
        tempCodeList.append(row) #imported codes into list
        

tempCodeList = tempCodeList[10:] #got rid of the stuff at the beginning so it is only dealing with the 6 different groups of cities

for col in range(0, len(tempCodeList[0])):
    codeList.append([])
for row in range(0, len(tempCodeList)):
    for col in range(0, len(tempCodeList[0])):
           if tempCodeList[row][col] != "":
            codeList[col].append(tempCodeList[row][col]) #flipped list over its diagonal so it's easier to access data

with open('2021OrchestraTest.csv', newline='') as database:
    reader = csv.reader(database)
    for row in reader:
        dataList.append(row) #import data into list
        def isEnglish(s):
            try:
                s.encode(encoding='utf-8').decode('ascii')
            except UnicodeDecodeError:
                return False
            else:
                return True

    assert not isEnglish('slabiky, ale liší se podle významu')
    assert isEnglish('English')
    assert not isEnglish('ގެ ފުރަތަމަ ދެ އަކުރު ކަ')
    assert not isEnglish('how about this one : 通 asfަ')
    assert isEnglish('?fd4))45s&')

dataList[0].append("COMP.CODE")
dataList[0].append("COMP.LIVE")
dataList[0].append("LAO.GROUP") #enter column headers

code = [[],[],[],[],[],[]]
live = [[],[]]
nextIndex = 0
nextArray = "CODE"
with open('2021Codebanks.txt') as banks:
    for line in banks:
        case = 0;
        index = -1;
        for word in line.split(","):
            if case == 0: #case=0 exactly once per row, so this statement only activates once
                if word[:1] == "C": #activates for the "COMP.CODE" and "COMP.LIVE" lines
                    case = 1
                elif word[:1] == "'": #activates for lines containing names
                    case = 2
                else: #activates for line breaks; case 3 is never called, because we never need to do anything with the line breaks
                    case = 3
            if case == 1:
                nextIndex = int(word[-2:-1])-1 #lists start at index 0, but txt file starts at index 1
                nextArray = word[-7:-3] #the brackets return a substring (in this case, either "CODE" or "LIVE" to choose which list the next line goes into
            elif case == 2:
                if nextArray == "CODE":
                    if word[:1] == "'":
                        word = word[1:] #removes quotation mark from front
                        index += 1 #moves on to the next space, which is empty
                        code[nextIndex].append(word)
                    else:
                        word = word[:-1]
                        if word[-1:] == "'":
                            word = word[:-1] #removes quotation mark from back
                        code[nextIndex][index] = code[nextIndex][index] + "," + word #appends to the current space (which is of the form "lastname")
                elif nextArray == "LIVE":
                    if word[:1] == "'":
                        word = word[1:]
                        index += 1
                        live[nextIndex].append(word)
                    else:
                        word = word[:-1]
                        if word[-1:] == "'":
                            word = word[:-1]
                        live[nextIndex][index] = live[nextIndex][index] + "," + word

for row in dataList:
    if row[0] == "ENSEMBLE": #skips the first row, which is column headers (before, it used to put numbers later in the first row, because of the else statements)
        continue
    elif row[1] in code[5]:
        row.append("6")
    elif row[1] in code[4]:
        row.append("5")
    elif row[1] in code[3]:
        row.append("4")
    elif row[1] in code[2]:
        row.append("3")
    elif row[1] in code[1]:
        row.append("2")
    else:
        row.append("1") #above if statement checks which race and gender the composer is
    if row[1] in live[0]:
        row.append("1")
    else:
        row.append("2") #this if statement checks whether the composer is alive or dead
    for x in range(0,len(codeList)):
        if row[0] in codeList[x]:
            row.append(str(x+1))
            break #adds a bit of efficiency because if an orchestra is in one group, it can't be in another group, so we don't need to check all the rest

for row in dataList:
    print(", ".join(row))

with open("ORCH Test.csv", "w+", newline="") as product:
    writer = csv.writer(product) #boiler-plate code to open and prep csv file to be written
    writer.writerows(dataList)
