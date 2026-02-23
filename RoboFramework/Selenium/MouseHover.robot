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
    Mouse Over      xpath://div[@class='example']//div[1]//img[1]
    Sleep    2s
    Element Should Be Visible    xpath://h5[contains(text(),'name: user1')]

    Close Browser