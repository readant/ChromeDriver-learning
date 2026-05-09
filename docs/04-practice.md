# ChromeDriver 实践指南

## 1. 基础实践

### 1.1 环境配置最佳实践

#### 1.1.1 使用配置文件

创建 `config.py`：

```python
import os

class Config:
    CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH", "./chromedriver")
    DEFAULT_TIMEOUT = 10
    HEADLESS = os.environ.get("HEADLESS", "false").lower() == "true"

def get_driver():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    
    options = Options()
    if Config.HEADLESS:
        options.add_argument("--headless=new")
    
    return webdriver.Chrome(
        service=Service(Config.CHROME_DRIVER_PATH),
        options=options
    )
```

#### 1.1.2 使用环境变量

```bash
# Linux/macOS
export CHROME_DRIVER_PATH="/path/to/chromedriver"
export HEADLESS=true

# Windows
set CHROME_DRIVER_PATH="D:\path\to\chromedriver.exe"
set HEADLESS=true
```

### 1.2 元素定位策略

#### 1.2.1 优先级建议

1. **ID**：最快速、最可靠
2. **CSS选择器**：灵活、高效
3. **XPath**：功能强大但相对较慢
4. **其他**：Name、ClassName、TagName等

#### 1.2.2 XPath 高级用法

```python
# 包含文本
driver.find_element(By.XPATH, "//*[contains(text(), '关键词')]")

# 以...开头
driver.find_element(By.XPATH, "//*[starts-with(@id, 'prefix')]")

# 父节点定位
driver.find_element(By.XPATH, "//input[@id='kw']/parent::div")

# 兄弟节点定位
driver.find_element(By.XPATH, "//input[@id='kw']/following-sibling::button")

# 使用轴
driver.find_element(By.XPATH, "//div[@class='container']//input")
```

#### 1.2.3 CSS 选择器高级用法

```python
# 属性选择器
driver.find_element(By.CSS_SELECTOR, "input[type='text']")
driver.find_element(By.CSS_SELECTOR, "[data-id='123']")

# 层级选择器
driver.find_element(By.CSS_SELECTOR, "div.container > input")
driver.find_element(By.CSS_SELECTOR, "div.container input")

# 伪类
driver.find_element(By.CSS_SELECTOR, "input:first-child")
driver.find_element(By.CSS_SELECTOR, "input:last-child")
driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)")

# 通配符
driver.find_element(By.CSS_SELECTOR, "[class^='prefix']")
driver.find_element(By.CSS_SELECTOR, "[class$='suffix']")
driver.find_element(By.CSS_SELECTOR, "[class*='contains']")
```

## 2. 等待策略实践

### 2.1 显式等待封装

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class WaitHelper:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    def wait_for_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f"元素未找到: {locator}")
            return None
    
    def wait_for_clickable(self, locator):
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print(f"元素不可点击: {locator}")
            return None
    
    def wait_for_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"元素不可见: {locator}")
            return None
```

### 2.2 使用示例

```python
from selenium.webdriver.common.by import By

wait_helper = WaitHelper(driver)

# 等待元素存在
element = wait_helper.wait_for_element((By.ID, "kw"))

# 等待元素可点击
button = wait_helper.wait_for_clickable((By.ID, "su"))
button.click()

# 等待元素可见
result = wait_helper.wait_for_visible((By.CLASS_NAME, "result"))
```

## 3. 页面交互实践

### 3.1 表单处理

```python
def fill_form(driver, data):
    # 填写文本框
    driver.find_element(By.ID, "username").send_keys(data["username"])
    driver.find_element(By.ID, "password").send_keys(data["password"])
    
    # 选择下拉框
    from selenium.webdriver.support.ui import Select
    select = Select(driver.find_element(By.ID, "country"))
    select.select_by_value("CN")
    # 或
    select.select_by_visible_text("中国")
    
    # 选择单选框
    driver.find_element(By.CSS_SELECTOR, "input[name='gender'][value='male']").click()
    
    # 选择复选框
    checkbox = driver.find_element(By.ID, "agree")
    if not checkbox.is_selected():
        checkbox.click()
    
    # 提交表单
    driver.find_element(By.ID, "submit").click()
```

### 3.2 文件上传

```python
# 找到文件上传输入框
upload_input = driver.find_element(By.ID, "file-upload")

# 直接发送文件路径
upload_input.send_keys("C:/path/to/file.txt")

# 或使用绝对路径
import os
file_path = os.path.abspath("test.txt")
upload_input.send_keys(file_path)
```

### 3.3 处理动态内容

```python
def scroll_to_element(driver, element):
    # 滚动到元素可见
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

def infinite_scroll(driver, scroll_count=5):
    # 无限滚动模拟
    for _ in range(scroll_count):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        import time
        time.sleep(2)
```

## 4. 高级技巧

### 4.1 网络请求拦截

```python
def intercept_network_requests(driver):
    # 启用网络监控
    driver.execute_cdp_cmd('Network.enable', {})
    
    # 设置请求拦截
    def request_interceptor(request):
        if request['resourceType'] == 'Image':
            driver.execute_cdp_cmd('Network.abortRequest', {'requestId': request['requestId']})
    
    # 监听请求
    driver.execute_cdp_cmd('Network.setRequestInterception', {
        'patterns': [{'urlPattern': '*', 'resourceType': 'Image'}]
    })
    
    driver.on('request', request_interceptor)
```

### 4.2 性能监控

```python
def get_performance_metrics(driver):
    metrics = driver.execute_cdp_cmd('Performance.getMetrics', {})
    for metric in metrics['metrics']:
        print(f"{metric['name']}: {metric['value']}")

# 使用示例
get_performance_metrics(driver)
```

### 4.3 模拟移动设备

```python
from selenium.webdriver.chrome.options import Options

mobile_emulation = {
    "deviceName": "iPhone 12"
}

options = Options()
options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(options=options)
driver.get("https://www.baidu.com")
```

### 4.4 处理验证码

**注意**：自动化测试应尽量避免验证码场景。如果必须处理，可以：

1. **使用测试环境**：通常测试环境会关闭验证码
2. **与开发协作**：添加测试跳过机制
3. **使用第三方服务**：如打码平台（不推荐用于正规测试）

## 5. 测试框架集成

### 5.1 与 unittest 集成

```python
import unittest
from selenium import webdriver

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    
    def test_search(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID, "kw").send_keys("Selenium")
        self.driver.find_element(By.ID, "su").click()
        self.assertIn("Selenium", self.driver.title)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```

### 5.2 与 pytest 集成

```python
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_search(driver):
    driver.get("https://www.baidu.com")
    driver.find_element(By.ID, "kw").send_keys("Selenium")
    driver.find_element(By.ID, "su").click()
    assert "Selenium" in driver.title
```

## 6. 性能优化

### 6.1 优化策略

| 策略 | 说明 |
|------|------|
| **无头模式** | 无界面运行，节省资源 |
| **禁用图片** | 减少网络请求 |
| **限制资源** | 禁用JavaScript、CSS等 |
| **复用浏览器** | 使用 Chrome DevTools Protocol 复用已有浏览器 |
| **合理等待** | 使用显式等待替代 time.sleep() |

### 6.2 优化配置示例

```python
from selenium.webdriver.chrome.options import Options

options = Options()

# 无头模式
options.add_argument("--headless=new")

# 禁用GPU
options.add_argument("--disable-gpu")

# 禁用图片
options.add_argument("--blink-settings=imagesEnabled=false")

# 禁用JavaScript（谨慎使用）
# options.add_argument("--disable-javascript")

# 禁用CSS（谨慎使用）
# options.add_argument("--disable-stylesheets")

# 禁用扩展
options.add_argument("--disable-extensions")

# 禁用通知
options.add_argument("--disable-notifications")

# 禁用弹窗拦截
options.add_argument("--disable-popup-blocking")

# 禁用默认浏览器检查
options.add_argument("--no-default-browser-check")

# 禁用首次运行检查
options.add_argument("--no-first-run")

# 禁用组件更新
options.add_argument("--disable-component-update")

driver = webdriver.Chrome(options=options)
```

---

[上一章：API 参考](./03-api-reference.md) | [下一章：常见问题](./05-faq.md)
