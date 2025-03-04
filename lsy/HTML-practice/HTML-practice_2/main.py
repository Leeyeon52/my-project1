from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:

    driver.get('http://localhost:8080')
    
    title = driver.find_elements(By.TAG_NAME,"title")
    print(title.text)
    
    images = driver.find_elements(By.TAG_NAME, "img")
    print(("\n이미지 src 속성:"))
    for img in images:
        print(("-", img.get_attribute("src")))

    divs = driver.find_elements(By.TAG_NAME, "div")
    print("\n<div> 내부의 <p> 태그:")
    for div in divs:
        p_list = div.find_elements(By.TAG_NAME, "p")  # 'p_list'가 아닌 'p' 사용
        for p in p_list:
            print("-", p.text)
        