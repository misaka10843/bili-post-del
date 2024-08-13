# bili-post-del

一个可以指定删除范围的b站动态删除工具

使用bilibili api进行删除，基本保证不会误删/漏删/风控

API参考文档：[bilibili-API-collect](https://socialsisteryi.github.io/bilibili-API-collect/)

您可以在此处下载exe文件：[releases](https://github.com/misaka10843/bili-post-del/releases)

## 如何使用

本程序完成了获取到删除的步骤，您只需要提供您的cookie即可开始运行

本程序支持任何格式以一个动态id为一行的文本文件来进行删除

如果您在获取到id时出现报错而退出，建议您删除id文件（默认为程序目录下的post_id.txt）中的所有内容，防止重复获取

请注意！在删除/获取动态时请不要更改存储动态id的文件，防止出现问题！

### 如何获取cookie

1. 在浏览器中打开[您的b站主页](https://space.bilibili.com/)
2. 打开开发者工具(F12)后刷新
3. 在网络选项中选择任意请求(推荐第一个)，然后根据图中找到请求标头中的cookie，复制其中的值
   ![image](https://github.com/user-attachments/assets/f3ab6f85-6d05-4adb-b424-04b81caf5935)

4. 在任何地方创建一个文本文件将复制的内容粘贴进去，**请注意不要复制到`cookie:`，并且注意粘贴过去只有1行**（推荐在本程序目录下从创建一个`cookie.txt`，然后在程序需要提供时直接输入`cookie.txt`）

