import random
import time

import requests

# 设置请求头，包括 Cookie
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

# 构建请求 URL
url = "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/rm_dynamic"


def del_post(dynamic_id, cookies):
    # 替换为你要删除的动态的 id
    # 准备请求数据
    data = {
        "dynamic_id": dynamic_id,
        "csrf_token": cookies['bili_jct'],
        "csrf": cookies['bili_jct']
    }

    # 发送 POST 请求
    response = requests.post(url, headers=headers, data=data, cookies=cookies)

    # 解析响应
    if response.status_code == 200:
        result = response.json()
        if result["code"] == 0:
            print(f"动态 {dynamic_id} 删除成功")
            return True
        elif result["code"] == 500404:
            print(f"动态 {dynamic_id} 已经删除，跳过")
            return True
        else:
            print(f"删除动态失败，错误码：{result['code']}")
            return False
    else:
        print(f"请求失败，状态码：{response.status_code}")
        return False


def del_ready(cookie: dict, file_path: str):
    # 读取 output.txt 文件中的所有行
    with open(file_path, "r") as f:
        lines = f.readlines()
    all_num = len(lines)
    num = all_num
    # 遍历文件中的每一行，提取动态 id
    for line in lines:
        print(f"检测到{all_num}条动态，准备删除")
        if not line.strip():
            return True
        dynamic_id = int(line.strip())  # 假设动态 id 是整数类型，如果不是整数类型，请根据实际情况修改
        print(f"开始删除动态 id：{dynamic_id}")
        if del_post(dynamic_id, cookie):
            num -= 1
            # 每次请求之间随机等待 2-5 秒
            sleep_time = random.uniform(1, 3)
            print(f"总共有{all_num}条动态，还剩{num}条，正在停止{sleep_time}秒后继续...")
            time.sleep(sleep_time)
        else:
            print("我们在删除动态id:{dynamic_id} 遇见了问题，请您将此id之前的id都删除之后重试防止删除已删除的动态")
            exit(1)
    return True
