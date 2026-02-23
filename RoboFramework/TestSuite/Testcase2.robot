*** Settings ***
Library     SeleniumLibrary


*** Test Cases ***

Verify login with valid credentials
        Log To Console     Enter username
        Log To Console     Enter password
        Log To Console     click on login button
        Log To Console     user is on the home page
