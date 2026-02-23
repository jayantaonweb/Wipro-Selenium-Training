*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${URL}    https://the-internet.herokuapp.com/hovers
*** Test Cases ***
Select State And City
    Open Browser    ${URL}    firefox
    Maximize Browser Window
    Sleep    2s
    # Wait until page is visible
    Wait Until Element Is Visible       xpath://div[@class='example']//div[1]//img[1]
    Capture Page Screenshot    C:\Users\jkpja\Downloads
    Capture Element Screenshot      xpath://div[@class='example']//div[1]//img[1]    C:\Users\jkpja\Downloads
    Sleep    2s
    Close Browser