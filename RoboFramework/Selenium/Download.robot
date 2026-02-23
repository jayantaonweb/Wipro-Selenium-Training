*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${URL}    https://the-internet.herokuapp.com/download

*** Test Cases ***
Select State And City
    Open Browser    ${URL}    chrome
    Maximize Browser Window

    # Wait until dropdown is visible
    Wait Until Element Is Visible       xpath://a[normalize-space()='bb.txt']

    Click Element       xpath://a[normalize-space()='bb.txt']

    ${files}=       List Files In Directory         C:\Users\jh\Downloads
    List Should Contain Value           ${files}        bb.txt
    Sleep     2s

    Close Browser