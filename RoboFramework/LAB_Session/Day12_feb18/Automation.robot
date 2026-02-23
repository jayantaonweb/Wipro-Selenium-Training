*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.saucedemo.com/

*** Test Cases ***
Verify login scenario with valid credentials
    Open Browser    ${url}    firefox

    # maximize the browser window
    Maximize Browser Window

    # wait till the element is loaded
    Wait Until Element Is Visible    xpath://input[@id='user-name']

    # enter the text in the username field
    Input Text    xpath://input[@id='user-name']    standard_user

    # enter text into the password
    Input Text    xpath://input[@name='password']    secret_sauce

    # click login button
    Click Element    xpath://input[@type='submit']

    # validate that the user is on the home page
    Wait Until Element Is Visible    xpath://span[@class='title']
    Element Should Be Visible    xpath://span[@class='title']


    # close browser
    Close Browser
