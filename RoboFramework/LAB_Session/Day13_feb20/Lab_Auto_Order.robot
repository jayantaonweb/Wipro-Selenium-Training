*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     XML

*** Variables ***
${url}     https://practice.automationtesting.in/

*** Test Cases ***
Order Automation
    Open Browser    ${url}    chrome
    # maximize the browser window
    Maximize Browser Window
    # wait till the element is loaded
    Wait Until Element Is Visible       xpath://li[@class='post-160 product type-product status-publish has-post-thumbnail product_cat-selenium product_tag-ruby product_tag-selenium has-post-title no-post-date has-post-category has-post-tag has-post-comment has-post-author first instock downloadable taxable shipping-taxable purchasable product-type-simple']//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'][normalize-space()='Add to basket']

    Scroll Element Into View        xpath://div[@id='text-22-sub_row_1-0-2-1-0']//ul[@class='products']
    # item 1
    Click Element       xpath://li[@class='post-160 product type-product status-publish has-post-thumbnail product_cat-selenium product_tag-ruby product_tag-selenium has-post-title no-post-date has-post-category has-post-tag has-post-comment has-post-author first instock downloadable taxable shipping-taxable purchasable product-type-simple']//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'][normalize-space()='Add to basket']
    Sleep    2s
    Go To    https://practice.automationtesting.in/basket/

    Sleep    3s
    Scroll Element Into View    xpath://div[@id='content']

    Click Element    xpath://a[@class='checkout-button button alt wc-forward']

    #Billing Details
    Input Text    xpath://input[@id='billing_first_name']    Jayant
    Input Text    xpath://input[@id='billing_last_name']    Pandey
    Input Text    xpath://input[@id='billing_email']    jay@abc.com
    Input Text    xpath://input[@id='billing_phone']    1234567890
    
    Scroll Element Into View    xpath://h3[@id='order_review_heading']
    
    Input Text    xpath://input[@id='billing_address_1']    asdf
    Input Text    xpath://input[@id='billing_city']    qwert

    Input Text    xpath://input[@id='billing_postcode']    123456

    Sleep    2s
    Scroll Element Into View    xpath://h4[normalize-space()='Subscribe Here']
    Sleep    1s

    Click Button    //input[@id='place_order']


    Wait Until Element Is Visible    xpath://p[@class='woocommerce-thankyou-order-received']
    Sleep    3s
    # close browser
    Close Browser
