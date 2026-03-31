import os

def clear_console():
    # nt 代表 Windows，posix 代表 Linux 或 Mac
    os.system('cls' if os.name == 'nt' else 'clear')

# 调用函数即可清空
clear_console()