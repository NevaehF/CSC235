# import the json library with cool json support code built in
import json

# function to read data from a json file
def readJsonFile(filePath):
    # open the file
    with open(filePath, 'r') as file:
        data = json.load(file)
    
    # return the data from the json file back to the code that called this function
    return data

# function to write data to the json file
def writeJsonFile(filePathWrite, data):
    # open the file
    with open(filePathWrite, 'w') as file:
        # overwrite the existing data in our json file with our new and improved data
        json.dump(data, file, indent=2)

# set a variable that holds the file name of our json data file
jsonFilePath = "sample_data.json"

# read the data from the json file
jsonData = readJsonFile(jsonFilePath)

# Display the data in the file
print("Here is the original data")
print(jsonData)

# Let's change some of the json data
jsonData[0]['age'] = 28
jsonData[0]['city'] = "Chandler"
# adding a new key/value pair - key: pet | value: Fido
jsonData[0]['pet'] = "Fido"

# Write the modified json data back to the json file (overwriting the existing data)
writeJsonFile(jsonFilePath, jsonData)

# Open the modified json file and show the contents
modifiedJsonData = readJsonFile(jsonFilePath)

print("Modified Data:")
print(modifiedJsonData)
