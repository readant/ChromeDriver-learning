from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import get_driver_path

def get_driver():
    driver_path = get_driver_path()
    if driver_path:
        return webdriver.Chrome(service=Service(driver_path))
    from webdriver_manager.chrome import ChromeDriverManager
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def element_locator():
    driver = get_driver()
    
    try:
        driver.get("https://www.baidu.com")
        
        element_by_id = driver.find_element(By.ID, "kw")
        print("通过ID定位:", element_by_id.tag_name)
        
        element_by_name = driver.find_element(By.NAME, "wd")
        print("通过Name定位:", element_by_name.tag_name)
        
        element_by_class = driver.find_element(By.CLASS_NAME, "s_ipt")
        print("通过ClassName定位:", element_by_class.tag_name)
        
        element_by_xpath = driver.find_element(By.XPATH, '//input[@id="kw"]')
        print("通过XPath定位:", element_by_xpath.tag_name)
        
        element_by_css = driver.find_element(By.CSS_SELECTOR, "input#kw")
        print("通过CSS选择器定位:", element_by_css.tag_name)
        
        elements_by_tag = driver.find_elements(By.TAG_NAME, "input")
        print("通过TagName定位到的元素数量:", len(elements_by_tag))
        
    finally:
        driver.quit()

if __name__ == "__main__":
    element_locator()
