from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import get_driver_path


def get_driver():
    """
    获取 Chrome 浏览器驱动实例
    
    Returns:
        webdriver.Chrome: Chrome 浏览器驱动实例
    """
    driver_path = get_driver_path()
    if driver_path:
        return webdriver.Chrome(service=Service(driver_path))
    from webdriver_manager.chrome import ChromeDriverManager
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def advanced_features():
    """
    高级功能示例
    
    演示以下高级功能：
    1. 截图功能：保存当前页面截图
    2. Cookie 操作：获取、添加、删除 Cookie
    3. 执行 JavaScript：通过 execute_script 执行 JS 代码
    """
    driver = get_driver()
    
    try:
        driver.get("https://www.baidu.com")
        
        screenshot = driver.get_screenshot_as_png()
        with open("screenshot.png", "wb") as f:
            f.write(screenshot)
        print("截图已保存为 screenshot.png")
        
        cookies = driver.get_cookies()
        print("当前页面Cookie数量:", len(cookies))
        for cookie in cookies[:3]:
            print(f"  - {cookie['name']}: {cookie['value']}")
        
        driver.add_cookie({"name": "test_cookie", "value": "test_value"})
        print("已添加测试Cookie")
        
        current_url = driver.execute_script("return window.location.href")
        print("通过JS获取URL:", current_url)
        
        page_title = driver.execute_script("return document.title")
        print("通过JS获取标题:", page_title)
        
        driver.delete_all_cookies()
        print("已删除所有Cookie")
        
    finally:
        driver.quit()


if __name__ == "__main__":
    advanced_features()
