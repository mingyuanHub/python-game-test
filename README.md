# python-game-test
游戏接口自动化测试

>  `Python` 自动化测试
###### 一 自动化测试项目开发准备 （后面会对每个模块详情）
- `Python` ：熟练Python基础语法
- `Requests`：熟练简单的 Get，Post 接口请求
- `Unittest`：熟练简单的`unittest.TestCase`，`unittest.TestSuite()` 实现
- `HtmlTestRunner`：熟练生成简单的测试报告

###### 二 自动化测试项目开发流程
> TestCase 实现

  1. 引入扩展：unittest， Requests
  2. 文件业务功能的类名称
  3. 创建测试用例 【test_开头】
      - 1  定义 接口url， 参数param
      - 2 requests 请求，获取返回参数
      - 3 断言

> main.py【入口文件及主文件】

1.  引入扩展：unittest， HtmlTestRunner
2.  创建 测试套件，按需插入 TestCase 和  test
3.  创建 测试用例运行器 runner
4.  运行器 运行 套件  【 runner.run(suite) 】

> 执行生成测试报告

###### 报告结果截图如下 
![image.png](https://upload-images.jianshu.io/upload_images/19009365-3fff70dc9d81c9ed.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)