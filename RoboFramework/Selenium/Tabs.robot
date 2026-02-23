*** Settings ***
Library     SeleniumLibrary
Library    OperatingSystem
Library    Collections


*** Variables ***
${url}     https://the-internet.herokuapp.com/windows
*** Test Cases ***
Verify link texts
    Open Browser    ${url}    firefox
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

    Click Element    link=Click Here

    @{windows}=    Get Window Handles
    Log To Console    ${windows}

    Switch Window    ${windows}[1]

    Element Text Should Be    xpath://h3    New Window

    Switch Window    ${windows}[0]

    Close Browser