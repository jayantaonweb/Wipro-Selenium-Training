*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${URL}    https://www.amazon.in/
*** Test Cases ***
Select State And City
    Open Browser    ${URL}    firefox
    Maximize Browser Window
    Sleep    2s
    # Wait until page is visible
    Wait Until Element Is Visible       xpath://a[normalize-space()='sell]

    Open Context Menu    xpath://a[normalize-space()='Sell']
    Sleep    2s
    #double click

    Double Click Element    xpath://a[normalize-space()='Mobiles']
    Sleep    2s

    Close Browser