# 教程 2：元素定位与操作（国内用户版）

## 目标

本教程将学习：
1. 元素定位的多种方式
2. 元素操作方法
3. 表单填写与提交（以国内网站为例）
4. 等待策略

## 步骤 1：元素定位方式

### 方式1：通过 ID 定位

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("path/to/chromedriver"))

try:
    driver.get("https://www.baidu.com")
    
    # 通过 ID 定位百度搜索框
    search_box = driver.find_element(By.ID, "kw")
    search_box.send_keys("Python")
    
finally:
    driver.quit()
```

### 方式2：通过 Name 定位

```python
search_box = driver.find_element(By.NAME, "wd")
```

### 方式3：通过 Class Name 定位

```python
search_box = driver.find_element(By.CLASS_NAME, "s_ipt")
```

### 方式4：通过 CSS 选择器定位

```python
search_box = driver.find_element(By.CSS_SELECTOR, "input#kw")
```

### 方式5：通过 XPath 定位

```python
search_box = driver.find_element(By.XPATH, "//input[@id='kw']")
```

## 步骤 2：元素操作

### 输入文本

```python
element.send_keys("Hello World")
```

### 点击元素

```python
element.click()
```

### 清空输入

```python
element.clear()
```

### 获取文本

```python
text = element.text
```

### 获取属性

```python
value = element.get_attribute("value")
```

## 步骤 3：表单操作实战（百度搜索）

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service("path/to/chromedriver"))

try:
    # 访问百度首页
    driver.get("https://www.baidu.com")
    
    # 找到搜索框并输入内容
    search_box = driver.find_element(By.ID, "kw")
    search_box.send_keys("ChromeDriver 教程")
    
    # 等待2秒
    time.sleep(2)
    
    # 清空搜索框
    search_box.clear()
    
    # 输入新内容并按回车提交
    search_box.send_keys("Selenium Python" + Keys.ENTER)
    
    # 等待搜索结果加载
    time.sleep(3)
    
    # 打印结果页面标题
    print("搜索结果:", driver.title)
    
finally:
    driver.quit()
```

## 步骤 4：等待策略

### 隐式等待

```python
driver.implicitly_wait(10)  # 全局等待，最多等待10秒
```

### 显式等待

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)

# 等待元素可见
element = wait.until(EC.visibility_of_element_located((By.ID, "kw")))

# 等待元素可点击
button = wait.until(EC.element_to_be_clickable((By.ID, "su")))
button.click()
```

## 步骤 5：综合实战（完整示例）

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# 初始化浏览器
driver = webdriver.Chrome(service=Service("path/to/chromedriver"))
wait = WebDriverWait(driver, 10)

try:
    # 访问百度
    driver.get("https://www.baidu.com")
    
    # 等待搜索框可见
    search_box = wait.until(EC.visibility_of_element_located((By.ID, "kw")))
    
    # 输入搜索内容
    search_box.send_keys("ChromeDriver")
    
    # 等待搜索按钮可点击并点击
    search_button = wait.until(EC.element_to_be_clickable((By.ID, "su")))
    search_button.click()
    
    # 等待搜索结果加载
    result = wait.until(EC.presence_of_element_located((By.ID, "content_left")))
    
    # 打印搜索结果数量
    results = driver.find_elements(By.CLASS_NAME, "result")
    print(f"搜索结果数量: {len(results)}")
    
finally:
    driver.quit()
```

## 国内用户实战案例

### 案例1：自动搜索并获取结果

```python
def baidu_search(keyword):
    driver = webdriver.Chrome(service=Service("path/to/chromedriver"))
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://www.baidu.com")
        search_box = wait.until(EC.visibility_of_element_located((By.ID, "kw")))
        search_box.send_keys(keyword)
        
        search_button = wait.until(EC.element_to_be_clickable((By.ID, "su")))
        search_button.click()
        
        # 获取搜索结果标题
        results = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".result h3")
        ))
        
        print(f"搜索 '{keyword}' 的结果：")
        for i, result in enumerate(results[:5], 1):
            print(f"{i}. {result.text}")
            
    finally:
        driver.quit()

# 使用示例
baidu_search("Python 教程")
```

### 案例2：豆瓣电影搜索

```python
def douban_movie_search(movie_name):
    driver = webdriver.Chrome(service=Service("path/to/chromedriver"))
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://movie.douban.com")
        
        # 定位搜索框
        search_box = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input#inp-query")
        ))
        search_box.send_keys(movie_name)
        
        # 点击搜索按钮
        search_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        search_button.click()
        
        # 获取搜索结果
        results = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".movie-item-title a")
        ))
        
        print(f"搜索 '{movie_name}' 的结果：")
        for i, result in enumerate(results[:5], 1):
            print(f"{i}. {result.text}")
            
    finally:
        driver.quit()

# 使用示例
douban_movie_search("流浪地球")
```

## 练习

1. 尝试使用不同的定位方式定位元素
2. 编写脚本自动搜索知乎内容
3. 练习使用显式等待

## 下一步

学习 [API 参考](../docs/03-api-reference.md) 了解更多功能
