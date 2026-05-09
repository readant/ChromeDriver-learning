# ChromeDriver 常见问题

## 1. 安装与配置问题

### Q1: ChromeDriver 版本不匹配

**问题描述：**
```
session not created: This version of ChromeDriver only supports Chrome version XX
```

**解决方案：**
1. 查看 Chrome 版本：设置 → 关于 Chrome
2. 下载匹配版本的 ChromeDriver：https://sites.google.com/chromium.org/driver/
3. 确保版本完全匹配

### Q2: ChromeDriver 找不到

**问题描述：**
```
Message: 'chromedriver' executable needs to be in PATH
```

**解决方案：**
1. 将 ChromeDriver 所在目录添加到系统 PATH
2. 或在代码中指定完整路径：
   ```python
   driver = webdriver.Chrome(service=Service("D:/path/to/chromedriver.exe"))
   ```

### Q3: 权限问题（Linux/macOS）

**问题描述：**
```
Permission denied
```

**解决方案：**
```bash
chmod +x /path/to/chromedriver
```

### Q4: 无法启动浏览器

**问题描述：**
```
WebDriverException: unknown error: Chrome failed to start
```

**解决方案：**
1. 确保 Chrome 已正确安装
2. 检查 ChromeDriver 版本是否匹配
3. 尝试添加 `--no-sandbox` 参数：
   ```python
   options.add_argument("--no-sandbox")
   ```

## 2. 元素定位问题

### Q1: 元素定位失败

**问题描述：**
```
NoSuchElementException: Unable to locate element
```

**解决方案：**
1. 检查元素是否存在于页面中
2. 使用显式等待：
   ```python
   from selenium.webdriver.support.ui import WebDriverWait
   from selenium.webdriver.support import expected_conditions as EC
   
   wait = WebDriverWait(driver, 10)
   element = wait.until(EC.presence_of_element_located((By.ID, "kw")))
   ```
3. 检查是否在 iframe 内
4. 检查元素是否为动态加载

### Q2: 元素不可见

**问题描述：**
```
ElementNotVisibleException: element not visible
```

**解决方案：**
1. 等待元素可见：
   ```python
   element = wait.until(EC.visibility_of_element_located((By.ID, "kw")))
   ```
2. 检查元素是否被其他元素遮挡
3. 检查 CSS `display` 或 `visibility` 属性

### Q3: 元素不可点击

**问题描述：**
```
ElementNotInteractableException: element not interactable
```

**解决方案：**
1. 等待元素可点击：
   ```python
   element = wait.until(EC.element_to_be_clickable((By.ID, "su")))
   ```
2. 滚动到元素可见：
   ```python
   driver.execute_script("arguments[0].scrollIntoView(true);", element)
   ```

## 3. 等待问题

### Q1: 页面加载慢

**问题描述：** 页面加载时间过长，导致测试超时。

**解决方案：**
1. 使用显式等待替代隐式等待
2. 设置合理的页面加载超时：
   ```python
   driver.set_page_load_timeout(30)
   ```
3. 禁用不必要的资源加载（图片、CSS等）

### Q2: 动态内容加载问题

**问题描述：** 页面内容通过 AJAX 动态加载，元素定位失败。

**解决方案：**
1. 使用显式等待等待元素出现
2. 监控网络请求完成：
   ```python
   # 等待所有请求完成
   wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
   ```

## 4. 网络问题

### Q1: 无法访问外部网站

**问题描述：**
```
WebDriverException: unknown error: net::ERR_CONNECTION_TIMED_OUT
```

**解决方案：**
1. 检查网络连接
2. 尝试访问国内网站（如百度）
3. 配置代理（如果需要）：
   ```python
   options.add_argument("--proxy-server=http://proxy:port")
   ```

### Q2: SSL 证书错误

**问题描述：**
```
SSL certificate error
```

**解决方案：**
```python
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-insecure-localhost")
```

## 5. 性能问题

### Q1: 测试运行缓慢

**解决方案：**
1. 使用无头模式
2. 禁用图片和不必要的资源
3. 复用浏览器会话
4. 并行执行测试

### Q2: 内存泄漏

**问题描述：** 长时间运行后内存占用过高。

**解决方案：**
1. 确保每次测试后调用 `driver.quit()`
2. 定期重启浏览器
3. 使用测试框架的 fixture 管理资源

## 6. 特殊场景问题

### Q1: 处理验证码

**解决方案：**
1. 使用测试环境（通常关闭验证码）
2. 与开发协作添加测试跳过机制
3. 使用 Mock 数据

### Q2: 处理弹窗

**问题描述：** 页面弹出警告框、确认框等。

**解决方案：**
```python
alert = driver.switch_to.alert
alert.accept()  # 接受
# 或
alert.dismiss()  # 取消
```

### Q3: 处理多窗口

**问题描述：** 点击链接打开新窗口。

**解决方案：**
```python
# 获取当前窗口
current = driver.current_window_handle

# 获取所有窗口
all_windows = driver.window_handles

# 切换到新窗口
for window in all_windows:
    if window != current:
        driver.switch_to.window(window)
        break
```

### Q4: 处理 iframe

**问题描述：** 元素在 iframe 内，无法直接定位。

**解决方案：**
```python
# 切换到 iframe
iframe = driver.find_element(By.ID, "iframe_id")
driver.switch_to.frame(iframe)

# 操作元素
element = driver.find_element(By.ID, "element_id")

# 切回主文档
driver.switch_to.default_content()
```

## 7. 调试技巧

### 7.1 打印页面源码

```python
print(driver.page_source)
```

### 7.2 截图调试

```python
screenshot = driver.get_screenshot_as_png()
with open("debug.png", "wb") as f:
    f.write(screenshot)
```

### 7.3 执行 JavaScript 调试

```python
result = driver.execute_script("return document.querySelector('#kw').value")
print(result)
```

### 7.4 启用详细日志

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 8. 最佳实践总结

1. **使用显式等待**：避免使用 `time.sleep()`
2. **使用配置文件**：管理环境变量和路径
3. **清理资源**：每次测试后调用 `driver.quit()`
4. **使用测试框架**：如 pytest、unittest
5. **优化性能**：使用无头模式、禁用不必要资源
6. **异常处理**：添加 try-except 块

---

[上一章：实践指南](./04-practice.md)
