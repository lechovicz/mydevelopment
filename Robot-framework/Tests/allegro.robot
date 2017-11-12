*** Settings ***

Documentation  Some basic things
Library  Selenium2Library
*** Variables ***
${Webpage}  https://allegro.pl
${Browser}  chrome
${product}  python

*** Test Cases ***

TestCase1
    [Documentation]  Search for a particular product
    [Tags]  Smoke

    Open browser  ${webpage}  ${Browser}
    wait until page contains  Urodziny Allegro
    input text  xpath=html/body/div[3]/div[3]/nav/div[1]/div/div[1]/div/div/form/input[1]  ${product}
    click button  szukaj
    click link  partial link=naukowe
    click link  partial link=Wydanie IV

    #Close browser


*** Keywords ***


