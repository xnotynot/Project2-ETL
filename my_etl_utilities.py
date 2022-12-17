import csv
import json

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def convert_csv_to_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = {}
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
             
            # Assuming a column named 'No' to
            # be the primary key
            key = rows['No']
            data[key] = rows
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

def convert_to_json(df, keyCol, jsonData):
    # create a dictionary
    data = {}
        # Convert each row into a dictionary
        # and add it to data
    for rows in df:
            # Assuming a column named 'No' to
            # be the primary key
            key = rows[keyCol]
            data[key] = rows
    jsonData = data