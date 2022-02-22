import pathlib
import os
def test_os_op():
    # 获取当前目录
    path1 = pathlib.Path(os.curdir)
    # 输出当前目录的所有子目录，以及是否为文件
    for subdir in path1.iterdir():
        print(subdir.name, subdir.is_file())

if __name__ == "__main__":
    test_os_op()