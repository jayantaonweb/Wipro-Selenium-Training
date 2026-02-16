# Comphrensions - create list using a single line of code instead of loops
from pythonPrograming.Dictionary import employes

#syntax
#[expression for iterable if condition]

# square of a number
sqs = [x**2 for x in range (1,6)]
print(sqs)

# with the conditions
evennumbers=[x for x in range(10) if x%2 == 0]
print(evennumbers)

#dict comphrension - increasing by 10%
salary = {"A": 50000, "B":60000, "C":70000}
updated_sal = {k : v + 0.1 * v for k, v in salary.items()}
print(updated_sal)

#filtering of dict
employes={"jayant":"Active",
          "Ram":"Active",
          "Shyam":"Inactive"}
active_employees = {k:v for k,v in employes.items() if v=="Active"}
print(active_employees)


#set comphrension
sqs ={x**2 for x in range (1,6)}
print(sqs)

#set comp with the condition
evennumbers = {x for x in range(10) if x%2==0}
print(evennumbers)


