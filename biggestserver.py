import xml.etree.ElementTree as ET

def handle(node):
  if(node[0].tag == 'servers'):
    biggest = node[0][0].attrib['coreCount']
    indexFinal = 0
    tempIndex = 0
    for child in node[0]:
        if(child.attrib['coreCount'] > biggest):
            indexFinal = tempIndex
            biggest = child.attrib['coreCount']
        tempIndex++
  return node[0][indexFinal].attrib['type']

tree = ET.parse('system.xml')
root = tree.getroot()
handle(root)

