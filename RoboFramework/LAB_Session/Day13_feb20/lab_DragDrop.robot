*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${URL}    https://www.tutorialspoint.com/selenium/practice/droppable.php
*** Test Cases ***
Select State And City
    Open Browser    ${URL}    firefox
    Maximize Browser Window
    Sleep    3s
    # Wait until dropdown is visible
    Wait Until Element Is Visible       //div[@id='draggable']
    Sleep    2s
    Drag And Drop    //div[@id='draggable']    //div[@id='droppable']
    Sleep     2s

    Close Browser