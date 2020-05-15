import xml.etree.ElementTree as ET
tree = ET.parse('system.xml')
system = tree.getroot()
servers = sorted(system[0], key=lambda x: int(x.attrib["coreCount"]))
for item in servers:
	print(item.attrib)