import json

def generateJSON(dict, workingYear):

    # yearDict = {}
    # yearDict[workingYear] = dict

    print("Saving...")
    filename = "json/"+str(workingYear) + ".json"
    with open(filename, 'w') as outfile:
        json.dump(dict, outfile)

def openJSON(workingYear):

    print("Opening...")
    with open('json/'+str(workingYear)+".json") as infile:
        previousJSON = json.load(infile)
        return previousJSON

def mergeJSON(previousDict, currentDict, workingYear):

    print("Merging...")
    previousDict.update(currentDict)

    filename = "json/" + str(workingYear) + ".json"
    with open(filename, 'w') as outfile:
        json.dump(dict, outfile)


