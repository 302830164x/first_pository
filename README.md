# web-UI 自动化测试示例

---

## 框架设计

- pytest
- selenium
- POM页面对象模型（Page Object Model）

---

## 目录结构

    common                 ——这个包中存放的是常见的通用的类，如读取配置文件
    config                 ——配置文件目录
    logs                   ——日志
    page                   ——基类
    page_element           ——页面元素位置
    page_object	           ——页面对象类
    report                 ——报告文件
    TestCase               ——测试用例
    utils                  ——工具类
    conftest.py            ——pytest胶水文件
    pytest.ini             ——pytest配置文件
    run_case.py            ——启动文件，生产报告

---

## 运行

### 安装依赖

```shell
pip install -r requirements.txt
```

### 执行主文件

* 在项目根目录执行`run_case.py`文件即可运行项目
