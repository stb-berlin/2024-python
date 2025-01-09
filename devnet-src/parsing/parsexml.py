#!/usr/bin/python3

# Fill in this file with the code from parsing XML exercise

import xml.etree.ElementTree as ET
import re

myxml = ET.parse("myfile.xml")
myroot = myxml.getroot()
ns = re.match('{.*}', myroot.tag).group(0)
editconf = myroot.find("{}edit-config".format(ns))
defop = editconf.find("{}default-operation".format(ns))
testop = editconf.find("{}test-option".format(ns))

print(str(defop.text))
print(str(testop.text))
