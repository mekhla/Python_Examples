import xml.etree.ElementTree as ET 
import pandas as pd

#parse XML into Element Tree
tree = ET.parse('xmlparsing.xml')
root = tree.getroot()

# Initialize an empty list to store the parsed data
data = []

# # Iterate through the XML elements
for child in root:
    item_data = {}
    for elem in child:
        item_data[elem.tag] = elem.text
    data.append(item_data)

# Convert to DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print(df)

#Iteration through traditional method 
print(root.attrib)

#Loop over 'name' tag of xmlparsing.xml
# for name in root.iter('name'):
#   print(name.text)














