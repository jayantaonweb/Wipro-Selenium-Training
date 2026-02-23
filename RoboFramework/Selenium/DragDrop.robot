*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${URL}    https://the-internet.herokuapp.com/drag_and_drop

*** Test Cases ***
Select State And City
    Open Browser    ${URL}    firefox
    Maximize Browser Window
    Sleep    3s
    # Wait until dropdown is visible
    Wait Until Element Is Visible       xpath://div[@id='column-a']
    Sleep    2s
    Drag And Drop    xpath://div[@id='column-a']    xpath://div[@id='column-b']
    Sleep     2s

    Close Browser