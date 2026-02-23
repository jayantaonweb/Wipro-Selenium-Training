*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Select State And City
    Open Browser    ${URL}    chrome
    Maximize Browser Window

    # Wait until dropdown is visible
    Wait Until Element Is Visible    xpath=(//button)[1]
    Click Element    xpath=(//button)[1]
    #Informational alert--accept is for OK button
    Handle Alert        action=ACCEPT       timeout=3
    Sleep     2s
    Click Element     xpath=(//button)[2]
    #Conformational alert --accept is for ok button dismiss is for cancel button
    Handle Alert        action=DISMISS       timeout=3
    Sleep    2s
    #Prompt alert - accept is for ok button dismis is for cancel button
    Click Element    xpath=(//button)[3]
    Input Text Into Alert    Hello
    Sleep     2s
    Close Browser