*** Settings ***
Library     SeleniumLibrary
Library    OperatingSystem
Library    Collections


*** Variables ***
${url}     https://rahulshettyacademy.com/AutomationPractice/
*** Test Cases ***
Verify link texts
    Open Browser    ${url}    firefox
    Maximize Browser Window
    Set Selenium Implicit Wait    5s
    Wait Until Element Is Visible       xpath://button[@id='openwindow']

    Click Element    xpath://button[@id='openwindow']

    @{windows}=    Get Window Handles
    Log To Console    ${windows}

    Switch Window    ${windows}[1]

    Element Text Should Be    xpath://h3    Upcoming events
    Sleep    2s

    Switch Window    ${windows}[0]

    Close Browser