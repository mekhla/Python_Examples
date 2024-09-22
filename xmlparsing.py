import xml.etree.ElementTree as ET 

#parse XML into Element Tree
tree = ET.parse('xmlparsing.xml')
root = tree.getroot()

#Root 
print(root.tag)
print(len(root))

#Access the Root child 
print(root[0].tag)
print(len(root[0]))

#Loop overroot Children
for child in root:
  for i in child: 
    print(i.tag)
    print(i.text)

    

