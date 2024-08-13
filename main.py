import os

from rich.console import Console
from rich.prompt import Prompt, IntPrompt, Confirm

from del_post import del_ready
from get_post import get_id

console = Console(color_system='256', style=None)


def parse_cookie_string(cookie_string):
    cookies = {}
    items = cookie_string.split('; ')
    for item in items:
        key, value = item.split('=', 1)
        cookies[key] = value
    return cookies


def main():
    file_path = "./post_id.txt"

    file = Prompt.ask("您是否已经有了每个动态id一行格式的文本文件，如果有请输入文件路径，如果没有请直接回车",
                      default=None)
    cookie_file = Prompt.ask("您的cookie文件，如果您不知道这是什么，请查看github上的README.md")
    if not os.path.exists(cookie_file):
        print("cookie文件不存在，请确认文件路径")
        exit(1)
    with open(cookie_file, 'r') as f:
        cookie = f.read()
    if file is None:
        bili_id = IntPrompt.ask("请输入您的b站id",)
        if bili_id is None:
            exit(1)
        current_offset = IntPrompt.ask("请输入您希望从哪条动态开始删除(输入动态id,留空为全删除)", default=0)
        skip_upload = Confirm.ask("是否不删除上传稿件(如视频，专栏，不保证能100%识别)", default=True)
        if not get_id(bili_id, current_offset, skip_upload, parse_cookie_string(cookie), file_path):
            print("在运行时发现错误，请查看输出来调整，或者请前往GitHub开设一个issue进行反馈")
            exit(1)
    else:
        file_path = file
    if Confirm.ask(
            f"请注意！如果继续的话在{file_path}中存储的所有动态都会被删除，不排除会出现删除稿件的问题，请核实您的风险然后进行确认，是否开始删除？",
            default=False):
        if not del_ready(parse_cookie_string(cookie), file_path):
            print("在运行时发现错误，请查看输出来调整，或者请前往GitHub开设一个issue进行反馈")
            exit(1)
    print("运行完毕，建议您马上查看b站是否误删/漏删，感谢使用")


if __name__ == '__main__':
    main()
