#JSON - JavaScript Object Notation



import json
with open("C://Users//jkpja//PycharmProjects//Python Advance Programing//DataFormats//employee.json",'r') as file:
    data = json.load(file)


#read the json file load method
print(data)
print(data["name"])


with open("C://Users//jkpja//PycharmProjects//Python Advance Programing//DataFormats//nestedjson.json",'r') as file:
    data = json.load(file)

email = data ["user"]["profile"]["email"]
print(email)

#writing to json file - dumping
data={
  "name": "Harsha",
  "role": "Tester",
  "experience": 5,
  "skills": ["Python", "Automation", "API"]
}

with open("C://Users//jkpja//PycharmProjects//Python Advance Programing//DataFormats//writejson.json",'w')as file:
    json.dump(data,file)

#update or modify the json file
#steps- read json file then modify the data the write it back


with open("C://Users//jkpja//PycharmProjects//Python Advance Programing//DataFormats//updatejson.json",'r')as file:
    data= json.load(file)

#update the value
data["experience"]=6

with open("C://Users//jkpja//PycharmProjects//Python Advance Programing//DataFormats//updatejson.json",'w')as file:
    json.dump(data, file, indent=4)