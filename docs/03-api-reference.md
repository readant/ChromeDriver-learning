# ChromeDriver API 参考

## 1. WebDriver 基础 API

### 1.1 浏览器控制

#### 启动浏览器

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 方式1：指定路径
driver = webdriver.Chrome(service=Service("path/to/chromedriver"))

# 方式2：自动下载（需要网络）
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```

#### 关闭浏览器

```python
driver.quit()        # 关闭所有窗口并退出进程
driver.close()       # 关闭当前窗口
```

### 1.2 页面导航

```python
driver.get("https://www.baidu.com")  # 访问URL
driver.back()                         # 返回上一页
driver.forward()                      # 前进到下一页
driver.refresh()                      # 刷新页面
```

### 1.3 窗口管理

```python
driver.maximize_window()              # 最大化窗口
driver.minimize_window()              # 最小化窗口
driver.set_window_size(800, 600)      # 设置窗口大小
driver.set_window_position(100, 100)  # 设置窗口位置
```

## 2. 元素定位 API

### 2.1 定位方式

| 方法 | 说明 | 示例 |
|------|------|------|
| `find_element(By.ID, value)` | 通过ID定位 | `find_element(By.ID, "kw")` |
| `find_element(By.NAME, value)` | 通过Name定位 | `find_element(By.NAME, "wd")` |
| `find_element(By.CLASS_NAME, value)` | 通过类名定位 | `find_element(By.CLASS_NAME, "s_ipt")` |
| `find_element(By.TAG_NAME, value)` | 通过标签名定位 | `find_element(By.TAG_NAME, "input")` |
| `find_element(By.XPATH, value)` | 通过XPath定位 | `find_element(By.XPATH, "//input[@id='kw']")` |
| `find_element(By.CSS_SELECTOR, value)` | 通过CSS选择器定位 | `find_element(By.CSS_SELECTOR, "input#kw")` |
| `find_element(By.LINK_TEXT, value)` | 通过链接文本定位 | `find_element(By.LINK_TEXT, "新闻")` |
| `find_element(By.PARTIAL_LINK_TEXT, value)` | 通过部分链接文本定位 | `find_element(By.PARTIAL_LINK_TEXT, "新")` |

### 2.2 定位多个元素

```python
elements = driver.find_elements(By.TAG_NAME, "input")
for element in elements:
    print(element.get_attribute("name"))
```

## 3. 元素操作 API

### 3.1 基本操作

```python
element = driver.find_element(By.ID, "kw")

element.click()                        # 点击元素
element.send_keys("Hello World")       # 输入文本
element.clear()                        # 清空输入
element.submit()                       # 提交表单
```

### 3.2 获取元素信息

```python
element.text                           # 获取文本内容
element.get_attribute("value")         # 获取属性值
element.is_displayed()                 # 判断是否可见
element.is_enabled()                   # 判断是否可用
element.is_selected()                  # 判断是否选中
element.location                       # 获取位置
element.size                           # 获取尺寸
```

### 3.3 键盘操作

```python
from selenium.webdriver.common.keys import Keys

element.send_keys(Keys.ENTER)          # 回车键
element.send_keys(Keys.TAB)            # Tab键
element.send_keys(Keys.BACKSPACE)      # 退格键
element.send_keys(Keys.CONTROL, 'a')   # Ctrl+A
```

### 3.4 鼠标操作

```python
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)
actions.move_to_element(element)       # 移动到元素
actions.click_and_hold(element)        # 按住鼠标
actions.release(element)               # 释放鼠标
actions.double_click(element)          # 双击
actions.context_click(element)         # 右键点击
actions.drag_and_drop(source, target)  # 拖拽
actions.perform()                      # 执行操作
```

## 4. 等待机制 API

### 4.1 隐式等待

```python
driver.implicitly_wait(10)  # 全局等待，最多10秒
```

### 4.2 显式等待

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10, poll_frequency=0.5)

# 等待元素存在
element = wait.until(EC.presence_of_element_located((By.ID, "kw")))

# 等待元素可见
element = wait.until(EC.visibility_of_element_located((By.ID, "kw")))

# 等待元素可点击
element = wait.until(EC.element_to_be_clickable((By.ID, "su")))

# 等待标题包含特定文本
wait.until(EC.title_contains("百度"))

# 等待URL包含特定文本
wait.until(EC.url_contains("search"))
```

## 5. 高级 API

### 5.1 Cookie 操作

```python
# 获取所有Cookie
cookies = driver.get_cookies()

# 获取指定Cookie
cookie = driver.get_cookie("name")

# 添加Cookie
driver.add_cookie({"name": "test", "value": "value"})

# 删除指定Cookie
driver.delete_cookie("name")

# 删除所有Cookie
driver.delete_all_cookies()
```

### 5.2 JavaScript 执行

```python
# 执行JavaScript并获取返回值
title = driver.execute_script("return document.title")
print(title)

# 执行JavaScript（无返回值）
driver.execute_script("document.getElementById('kw').value = 'Hello'")

# 同步执行（等待脚本完成）
result = driver.execute_script("""
    return new Promise(resolve => {
        setTimeout(() => resolve('done'), 1000);
    });
""")
```

### 5.3 截图功能

```python
# 截取整个页面
screenshot = driver.get_screenshot_as_png()
with open("full_page.png", "wb") as f:
    f.write(screenshot)

# 截取指定元素
element = driver.find_element(By.ID, "kw")
element_screenshot = element.screenshot_as_png
with open("element.png", "wb") as f:
    f.write(element_screenshot)
```

### 5.4 窗口切换

```python
# 获取当前窗口句柄
current_window = driver.current_window_handle

# 获取所有窗口句柄
all_windows = driver.window_handles

# 切换到指定窗口
driver.switch_to.window(all_windows[1])

# 切换到新窗口
for window in all_windows:
    if window != current_window:
        driver.switch_to.window(window)
        break
```

### 5.5 框架切换

```python
# 切换到iframe
iframe = driver.find_element(By.ID, "iframe_id")
driver.switch_to.frame(iframe)

# 切换回主文档
driver.switch_to.default_content()
```

### 5.6 警告框处理

```python
# 切换到警告框
alert = driver.switch_to.alert

# 获取警告框文本
print(alert.text)

# 接受警告框
alert.accept()

# 取消警告框
alert.dismiss()

# 向警告框输入文本
alert.send_keys("Hello")
```

## 6. 浏览器配置

### 6.1 ChromeOptions

```python
from selenium.webdriver.chrome.options import Options

options = Options()

# 无头模式（无界面）
options.add_argument("--headless=new")

# 禁用GPU
options.add_argument("--disable-gpu")

# 设置窗口大小
options.add_argument("--window-size=1920,1080")

# 禁用图片加载
options.add_argument("--blink-settings=imagesEnabled=false")

# 添加扩展
options.add_extension("path/to/extension.crx")

# 启动浏览器
driver = webdriver.Chrome(service=Service("path/to/chromedriver"), options=options)
```

### 6.2 常用参数

| 参数 | 说明 |
|------|------|
| `--headless=new` | 无头模式 |
| `--disable-gpu` | 禁用GPU加速 |
| `--window-size=W,H` | 设置窗口大小 |
| `--start-maximized` | 启动时最大化 |
| `--incognito` | 无痕模式 |
| `--disable-extensions` | 禁用扩展 |
| `--disable-notifications` | 禁用通知 |

---

[上一章：原理介绍](./02-principle.md) | [下一章：实践指南](./04-practice.md)
