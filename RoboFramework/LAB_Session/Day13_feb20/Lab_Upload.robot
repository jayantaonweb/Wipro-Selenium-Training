*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***
${url}     https://www.tutorialspoint.com/selenium/practice/upload-download.php

*** Test Cases ***
Verify radio buttons
    Open Browser    ${url}    firefox
    # maximize the browser window
    Maximize Browser Window
    Sleep    3s
    # wait till the element is loaded
    Wait Until Element Is Visible       //a[@id='downloadButton']
    Choose File    xpath://input[@id='file-upload']    "C:\Users\jkpja\OneDrive\Pictures\Screenshots\Screenshot 2026-02-20 100446.png"
    # clikc the upload button

    Click Element       xpath://input[@id='file-submit']
    Sleep    2s
    # click on check box 3
    Element Text Should Be      xpath://h3[normalize-space()='File Uploaded!']      File Uploaded!
    Sleep    2s
    # close browser
    Close Browser
