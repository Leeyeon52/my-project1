from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:

    driver.get('http://localhost:8080')

    
    ol =driver.find_elements(By.TAG_NAME, "ol")
    print(type(ol))
    li_list = ol.find_elements(By.TAG_NAME, "li")
    print(type(li_list))
    
    for li in li_list:
        print(li_list)


    big_list =driver.find_elements(By.TAG_NAME, "big")
    for big in big_list:
        print(big_list)

    ul = driver.find_elements(By.TAG_NAME, "ul")
    bold = ul.find_elements(By.TAG_NAME, "bold")
    print(bold)
      


