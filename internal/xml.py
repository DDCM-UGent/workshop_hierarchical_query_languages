from lxml import etree

class XMLDocument:

    def __init__(self, filename):
        self.doc = read_xml(filename)
    
    def xpath(self, query):
        if len(query) == 0:
            return None
        return self.doc.xpath(query)

def read_xml(filename):
    with open(filename, 'r') as h:
        doc = etree.parse(h)
    return doc

def pprint(element):
    if element is None:
        print('Empty Query')
    elif type(element) is list:
        for e in element:
            pprint(e)
    else:
        if type(element) is etree._ElementUnicodeResult:
            print(element)
        else:
            etree.indent(element, space='  ')
            xml = etree.tostring(element, pretty_print=True)
            print(xml.decode(), end='')
