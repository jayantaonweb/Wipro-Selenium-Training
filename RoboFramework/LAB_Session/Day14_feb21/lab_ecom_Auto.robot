*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     XML

*** Variables ***
${url}     https://automationexercise.com/
${Name}     ABCDEF
${email}        abcdef@asdf
${password}     123456
${incorrect_email}      mnbv@jklo

*** Test Cases ***
Regester User
    Open Browser    ${url}    firefox
    # maximize the browser window
    Maximize Browser Window
    Sleep    2s
    Remove Ad Overlay
    Title Should Be    Automation Exercise
    
    Click Element    xpath://a[normalize-space()='Signup / Login']

    Remove Ad Overlay
    Element Should Be Visible    xpath://h2[normalize-space()='New User Signup!']


    Input Text    xpath://input[@placeholder='Name']    ${Name}
    Input Text    xpath://input[@data-qa='signup-email']    ${email}

    Sleep    2s
    Click Element    xpath://button[normalize-space()='Signup']

    Element Should Be Visible    xpath://b[normalize-space()='Enter Account Information']
    Remove Ad Overlay
    Sleep    1s
    Click Element    xpath://input[@id='id_gender1']
    Wait Until Element Is Visible    xpath://b[normalize-space()='Address Information']
    Input Text    xpath://input[@id='password']    ${password}
    


    Select From List By Label    xpath://select[@id='days']     1
    Select From List By Label    xpath://select[@id='months']       January
    Select From List By Label    xpath://select[@id='years']     2010

    Click Element    xpath://input[@id='newsletter']
    Click Element    xpath://input[@id='optin']

    Wait Until Element Is Visible    xpath://input[@id='state']


    Input Text    xpath://input[@id='first_name']    Jay
    Input Text    xpath://input[@id='last_name']    Pandey
    Input Text    xpath://input[@id='company']    ABC
    Input Text    xpath://input[@id='address1']    asdfqwer
    Input Text    xpath://input[@id='address2']    qwer

    Select From List By Label    xpath://select[@id='country']      India

    Wait Until Element Is Visible    xpath://button[normalize-space()='Create Account']

    Input Text    xpath://input[@id='state']    asdfqwe
    Input Text    xpath://input[@id='city']    asd
    Input Text    xpath://input[@id='zipcode']    456123
    Input Text    xpath://input[@id='mobile_number']    1234567890

    Click Element    xpath://button[normalize-space()='Create Account']

    Element Should Be Visible    xpath://b[normalize-space()='Account Created!']
    Remove Ad Overlay
    Click Element    xpath://a[@class='btn btn-primary']

    Remove Ad Overlay
    Element Text Should Be    //b[normalize-space()='${Name}']    ${Name}

    Sleep    2s
    # close browser
    Close Browser


*** Test Cases ***
Login User with correct email and password
    Open Browser    ${url}    firefox
    # maximize the browser window
    Maximize Browser Window
    Sleep    2s
    Remove Ad Overlay
    Title Should Be    Automation Exercise

    Click Element    xpath://a[normalize-space()='Signup / Login']

    Element Should Be Visible    xpath://h2[normalize-space()='Login to your account']

    Remove Ad Overlay
    Input Text    xpath://input[@data-qa='login-email']    ${email}
    Input Text    xpath://input[@placeholder='Password']    ${password}

    Sleep    2s
    Click Element    xpath://button[normalize-space()='Login']
    Element Text Should Be    //b[normalize-space()='${Name}']    ${Name}

    Sleep    2s
    # close browser
    Close Browser


*** Test Cases ***
Login User with incorrect email and password
    Open Browser    ${url}    firefox
    # maximize the browser window
    Maximize Browser Window
    Sleep    2s
    Remove Ad Overlay
    Title Should Be    Automation Exercise

    Click Element    xpath://a[normalize-space()='Signup / Login']

    Element Should Be Visible    xpath://h2[normalize-space()='Login to your account']

    Remove Ad Overlay
    Input Text    xpath://input[@data-qa='login-email']    ${incorrect_email}
    Input Text    xpath://input[@placeholder='Password']    ${password}

    Sleep    2s
    Click Element    xpath://button[normalize-space()='Login']
    Element Text Should Be    xpath://p[normalize-space()='Your email or password is incorrect!']    Your email or password is incorrect!

    Sleep    2s
    # close browser
    Close Browser


*** Test Cases ***
Logout User
    Open Browser    ${url}    firefox
    # maximize the browser window
    Maximize Browser Window
    Sleep    1s
    Remove Ad Overlay
    Title Should Be    Automation Exercise

    Click Element    xpath://a[normalize-space()='Signup / Login']

    Element Should Be Visible    xpath://h2[normalize-space()='Login to your account']

    Remove Ad Overlay
    Input Text    xpath://input[@data-qa='login-email']    ${email}
    Input Text    xpath://input[@placeholder='Password']    ${password}

    Sleep    1s
    Click Element    xpath://button[normalize-space()='Login']
    Element Text Should Be    //b[normalize-space()='${Name}']    ${Name}

    Sleep    1s
    Click Element    xpath://a[normalize-space()='Logout']
    Title Should Be    Automation Exercise - Signup / Login

    Sleep    1s
    # close browser
    Close Browser


*** Test Cases ***
Register User with existing email
    Open Browser    ${url}    firefox
    # maximize the browser window
    Maximize Browser Window
    Sleep    1s
    Remove Ad Overlay
    Title Should Be    Automation Exercise

    Click Element    xpath://a[normalize-space()='Signup / Login']

    Remove Ad Overlay
    Element Should Be Visible    xpath://h2[normalize-space()='New User Signup!']


    Input Text    xpath://input[@placeholder='Name']    ${Name}
    Input Text    xpath://input[@data-qa='signup-email']    ${email}

    Sleep    1s
    Click Element    xpath://button[normalize-space()='Signup']
    
    Element Text Should Be    xpath://p[normalize-space()='Email Address already exist!']    Email Address already exist!
    Sleep    1s
    Close Browser

*** Test Cases ***
Contact Us Form
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Sleep    1s
    Remove Ad Overlay
    Title Should Be    Automation Exercise
    Click Element    xpath://a[normalize-space()='Contact us']
    Remove Ad Overlay
    #Wait Until Element Is Visible    xpath://h2[normalize-space()='Get In Touch']
    Element Should Be Visible      xpath://h2[normalize-space()='Get In Touch']

    Input Text    xpath://input[@placeholder='Name']    ${Name}
    Input Text    xpath://input[@placeholder='Email']    ${email}
    Input Text    xpath://input[@placeholder='Subject']   asdfghjk asdfghj
    Input Text    xpath://textarea[@id='message']    qwertyuiopasdfghjklzxcvbnmqwertyuioasdfghjklzxcvbnm

    #Choose File    xpath://input[@name='upload_file']    C:\Users\jkpja\PycharmProjects\RoboFramework\LAB_Session\Day14_feb21\image_upload.png
    Click Element    xpath://input[@name='submit']
    Handle Alert        action=ACCEPT       timeout=3

    Remove Ad Overlay
    Element Text Should Be    xpath://div[@class='status alert alert-success']    Success! Your details have been submitted successfully.

    Clear Element    xpath://span[normalize-space()='Home']

    Sleep    1s
    Close Browser










*** Keywords ***
Remove Ad Overlay
    Execute JavaScript    document.querySelectorAll("[class*='ads'], [id*='ads'], iframe, ins").forEach(e => e.remove());
    Execute JavaScript    document.body.style.overflow = 'auto';