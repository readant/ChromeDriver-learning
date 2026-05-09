# 资源管理指南

## 📁 资源目录结构

```
learning/
├── resources/
│   ├── images/          # 图片资源
│   │   ├── diagrams/    # 流程图、架构图
│   │   ├── screenshots/ # 截图
│   │   └── icons/       # 图标
│   ├── videos/          # 视频资源
│   │   ├── demos/       # 演示视频
│   │   └── tutorials/   # 教程视频
│   └── screenshots/     # 自动化截图
│       ├── by-date/     # 按日期组织
│       └── by-topic/    # 按主题组织
```

## 📸 截图命名规范

### 命名格式

```
{日期}-{主题}-{序号}.{扩展名}
```

### 示例

```
2026-05-09-baidu-search-001.png
2026-05-09-element-locator-002.png
2026-05-10-form-submission-001.png
```

## 🎥 视频资源规范

### 命名格式

```
{日期}-{主题}-{类型}.{扩展名}
```

### 类型说明

- `demo`: 演示视频
- `tutorial`: 教程视频
- `error`: 错误演示

### 示例

```
2026-05-09-baidu-search-demo.mp4
2026-05-09-wait-strategy-tutorial.mp4
2026-05-10-element-not-found-error.mp4
```

## 🖼️ 图片资源规范

### 图片类型

1. **流程图** (`diagrams/`)
   - 使用 draw.io 或类似工具创建
   - 格式：SVG 或 PNG
   - 命名：`{主题}-flow.svg`

2. **截图** (`screenshots/`)
   - 使用 ChromeDriver 自动截图
   - 格式：PNG
   - 命名：按日期命名

3. **图标** (`icons/`)
   - 格式：SVG 或 PNG
   - 尺寸：64x64 或 128x128

## 🔗 资源引用规范

### 在 Markdown 中引用

```markdown
![图片描述](../resources/images/screenshots/2026-05-09-baidu-search-001.png)

[视频演示](../resources/videos/demos/2026-05-09-baidu-search-demo.mp4)
```

### 在 Obsidian 中引用

```markdown
![[resources/images/screenshots/2026-05-09-baidu-search-001.png]]
```

## 📊 资源管理最佳实践

### 1. 定期清理

- 每月清理过期资源
- 归档不常用的资源到 `archive/` 目录

### 2. 版本控制

- 小文件（< 10MB）纳入 Git 版本控制
- 大文件使用 Git LFS 或外部存储

### 3. 备份策略

- 定期备份重要资源
- 使用云存储同步

### 4. 资源索引

- 在笔记中记录资源位置
- 使用标签分类资源

## 🎯 资源使用示例

### 在代码中截图

```python
# 截图并保存到指定目录
screenshot_path = "learning/resources/screenshots/2026-05-09-baidu-search-001.png"
driver.save_screenshot(screenshot_path)
```

### 在笔记中引用

```markdown
## 实践结果

**截图展示：**

![[resources/screenshots/2026-05-09-baidu-search-001.png]]

**视频演示：**

[点击观看演示视频](../resources/videos/demos/2026-05-09-baidu-search-demo.mp4)
```

## 📝 资源清单模板

```markdown
## 资源清单

### 图片资源
- [ ] 流程图
- [ ] 截图
- [ ] 图标

### 视频资源
- [ ] 演示视频
- [ ] 教程视频
- [ ] 错误演示

### 代码资源
- [ ] 完整代码
- [ ] 代码片段
- [ ] 测试用例
```

## 🔍 资源搜索技巧

### 按日期搜索

```
path:resources/images 2026-05-09
```

### 按主题搜索

```
path:resources/images baidu-search
```

### 按类型搜索

```
path:resources/images tag:screenshot
```

## 📚 相关链接

- [[资源管理配置]]
- [[Obsidian 使用指南]]
- [[学习笔记模板]]
