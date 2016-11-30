import xml.etree.ElementTree as etree

def goDeeper(root):
    return (1 + max([goDeeper(node) for node in root ])) if len(root)>0 else 0

xml = ''.join(input() for _ in range(int(input())))
tree = etree.ElementTree(etree.fromstring(xml))
root = tree.getroot()

print(goDeeper(root))