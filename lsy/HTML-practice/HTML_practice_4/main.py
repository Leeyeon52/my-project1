from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:

    driver.get('http://localhost:8080')

    xpath = '//ol/li'
    print('ol 태그 안에 있는 li 태그의:',xpath)

    elements = driver.find_elements(By.XPATH, xpath)
    print("\n<ol> 내부의 <li> 요소들:")
    for elem in elements:
        print("-", elem.text)
    
    xpath2 = "//*[@class='big']"
    print("\nBig 클래스 요소의 XPath:", xpath2)

    big_elements = driver.find_elements(By.XPATH, xpath2)
    print("\nBig 클래스가 적용된 요소들:")
    for elem in big_elements:
        print("-", elem.text)

    xpath3 = "//ul//*[@class='bold']"
    print("\n<ul> 내부에서 bold 클래스가 적용된 요소의 XPath:", xpath3)

    bold_elements = driver.find_elements(By.XPATH, xpath3)
    print("\n<ul> 내부의 bold 클래스 요소들:")
    for elem in bold_elements:
        print("-", elem.text)