import xml.etree.ElementTree as ET

#read xml file

#parse XML file into variable tree
tree = ET.parse("C://Users//jkpja//PycharmProjects//Python Advance Programing//DataFormats//employee.xml")
root = tree. getroot() #get the root element
print(root.tag)

#get the first child name / tag
print(root[0].tag)


#get the attribute of the child node
print(root[0].attrib)
print(root[1].attrib)

#fetch all the atributes in child node
for emp in root.findall("employee"):
    emp_id=emp.get("id")
    print(emp_id)
    emp_name=emp.find("name").text
    print(emp_name)

for emp in root.findall("employee"):
    name= emp.find("name").text
    role= emp.find("role").text
    exp = emp.find("experience").text
    print(name, role, exp)

#root ---> child node---> attribute of the child node ---->text of the attributes

#write the data to xmm

#create the root element

root= ET.Element("employees")

#create the child elements

emp1= ET.SubElement(root,"employee",id="101")
ET.SubElement(emp1,"name").text="Harsha"
ET.SubElement(emp1,"role").text="Tester"
ET.SubElement(emp1,"experience").text="5"

#create the child node 2

emp1= ET.SubElement(root,"employee",id="102")
ET.SubElement(emp1,"name").text="Amit"
ET.SubElement(emp1,"role").text="developer"
ET.SubElement(emp1,"experience").text="6"

#write to the file
tree=ET.ElementTree(root)
ET.indent(tree, space="    ")
tree.write("C://Users//jkpja//PycharmProjects//Python Advance Programing//DataFormats//writexml.xml",encoding="utf-8", xml_declaration=True)

#updating the xml

tree = ET.parse("C://Users//jkpja//PycharmProjects//Python Advance Programing//DataFormats//updatexml.xml")
root = tree. getroot()
for emp in root.findall("employee"):
    if emp.get("id")=="101":
        emp.find("experience").text = "16"
ET.indent(tree, space="    ")
tree.write("C://Users//jkpja//PycharmProjects//Python Advance Programing//DataFormats//updatexml.xml",encoding="utf-8", xml_declaration=True)



