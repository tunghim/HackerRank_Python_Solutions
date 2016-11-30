xml = ''.join(input() for _ in range(int(input())))
import xml.etree.ElementTree as etree
tree = etree.ElementTree(etree.fromstring(xml))

def traverse(node):
  return len(node.attrib) + sum(traverse(child) for child in node)

print(traverse(tree.getroot()))