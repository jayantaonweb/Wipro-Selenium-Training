#Create a scalar variable ${NAME} and print it.
 #Assign two numbers to variables and print their sum.
 #Create a variable ${CITY} and use it inside a sentence.
 #Reassign a variable value inside a test case and log the updated value.
 #Create a list variable @{FRUITS} and print the first item.
 #Loop through a list variable and print each element.
 #Find the length of a list variable.
 #Create a dictionary variable &{USER} and print one key value.
 #Add a new key-value pair to a dictionary variable.
 #Access dictionary values inside a loop and print key and value.
*** Settings ***
Library    Collections

*** Variables ***
${NAME}        Jayanta
${CITY}        Hyderabad

@{FRUITS}      Apple    Banana    Mango

&{USER}        username=admin    password=admin123


*** Test Cases ***
1. Print Scalar Variable
    Log    ${NAME}

2. Add Two Numbers
    ${num1}=    Set Variable    10
    ${num2}=    Set Variable    20
    ${sum}=     Evaluate    ${num1} + ${num2}
    Log    Sum is ${sum}

3. Use Variable Inside Sentence
    Log    I live in ${CITY}

4. Reassign Variable Inside Test Case
    ${NAME}=    Set Variable    Pandey
    Log    Updated Name: ${NAME}

5. Print First Item of List
    Log    ${FRUITS}[0]

6. Loop Through List
    FOR    ${item}    IN    @{FRUITS}
        Log    ${item}
    END

7. Find Length of List
    ${length}=    Get Length    ${FRUITS}
    Log    Length of list is ${length}

8. Print Dictionary Value
    Log    ${USER}[username]

9. Add New Key-Value To Dictionary
    Set To Dictionary    ${USER}    email=jayanta@email.com
    Log    ${USER}[email]

10. Loop Through Dictionary
    FOR    ${key}    ${value}    IN    &{USER}
        Log    Key: ${key} - Value: ${value}
    END
