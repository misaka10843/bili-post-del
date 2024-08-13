import random
import time

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 '
                  'Safari/537.36 Edg/127.0.0.0'
}


def get_id(bili_id: int, current_offset: int, skip_upload: bool, cookie: dict, file_path: str):
    num = 0
    url = f"https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?host_mid={bili_id}"
    while True:
        print("正在进入新一轮的获取中")
        # 设置偏移量
        if current_offset != 0:
            nurl = url + f"&offset={current_offset}"
        else:
            nurl = url
        print(nurl)
        response = requests.get(nurl, headers=headers, cookies=cookie)
        data = response.json()

        if data["code"] != 0:
            print(f"请求失败，错误码：{data['code']}")
            exit(1)

        has_more = data["data"]["has_more"]
        items = data["data"]["items"]

        for item in items:
            item_id_str = item["id_str"]
            item_type = item["type"]

            if skip_upload and item_type in ["DYNAMIC_TYPE_AV", "DYNAMIC_TYPE_ARTICLE", "DYNAMIC_TYPE_MUSIC"]:
                # 如果 item_type 是 DYNAMIC_TYPE_AV、DYNAMIC_TYPE_ARTICLE 或 DYNAMIC_TYPE_MUSIC，则不做处理
                pass
            else:
                # 如果 item_type 不是 DYNAMIC_TYPE_AV、DYNAMIC_TYPE_ARTICLE 或 DYNAMIC_TYPE_MUSIC，则将 item_id_str 保存到 txt 文件中
                with open(file_path, "a") as f:
                    f.write(item_id_str + "\n")

        if not has_more:
            print("获取完成，已经获取到指定范围内的全部动态id")
            return True

        # 更新 current_offset
        current_offset = data["data"]["offset"]
        # 获取当前存储id行数
        with open(file_path, 'r') as file:
            lines = file.readlines()
        # 每次请求之间随机等待 2-5 秒
        sleep_time = random.uniform(5, 10)
        num += 1
        print(f"获取成功，轮数：{num}，文件内已存储{len(lines) - 1}个动态id，正在停止{sleep_time}秒后继续...")
        time.sleep(sleep_time)
