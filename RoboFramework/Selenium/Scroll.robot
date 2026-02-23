*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${URL}    https://amazon.in/
*** Test Cases ***
Verify radio buttons
    Open Browser        ${url}        chrome
    # maximize the browser window
    Maximize Browser Window
    Set Selenium Implicit Wait    5s
    Scroll Element Into View        link=Sell on Amazon
    Sleep    2s
    Click Element        link=Sell on Amazon
    Sleep    2s
    Title Should Be    Amazon.in: Selling on Amazon - Start Selling Now
    # close browser
    Close Browser