# -*- coding:utf-8 -*-
import os, shutil


class Files:
    # 创建文件夹，如果存在，就提示，否则就创建
    def make_dir(self, dir):
        if not os.path.exists(dir):
            if '/' not in dir:
                os.mkdir(dir)
            else:
                os.makedirs(dir)
            print('目录创建成功')
        else:
            print('目录已存在')

    # 删除文件夹，如果不存在，就提示，否则就删除
    def remove_dir(self, dir):
        if os.path.exists(dir):
            if os.listdir(dir) != []:
                shutil.rmtree(dir)
                print('目录删除成功')
            else:
                os.rmdir(dir)
        else:
            print('目录不存在')

    # 遍历文件夹内容,这有个小bug：目录下还有文件迭代不出来，如果是文件就可以
    def list_dir(self, path):
        # print(os.listdir(path))
        for dirname, dirs, files in os.walk(path):
            for file in files:
                print(os.path.join(dirname, file).replace('\\', '/'))
            for path in dirs:
                self.list_dir(path)

    # 复制文件夹及其下面所有内容
    def cp_dir(self, src, cpdir):
        shutil.copytree(src, cpdir)

    # 删除文件夹及其下面所有内容
    def del_dir(self, src):
        shutil.rmtree(src)

    # 读文件，根据byte数，不传byte读所有
    def read_file(self, filename, byte=None):
        try:
            f = open(filename, 'r', encoding='utf-8')
            while True:
                if byte == None:
                    line = f.readline()
                else:
                    line = f.readline(byte)  # line=f.readline(2) 每次读2个字节
                if line:
                    print(line.strip('\n'))  # 去掉换行符
                else:
                    break
            f.close()
        except Exception as e:
            print('文件不存在')

    # 写入内容到文件，content传一个列表
    def write_file(self, content, path, model='w+'):
        f = open(path, model, encoding='utf-8')
        f.writelines(content)
        f.close()

    # 复制文件
    def cp_file(self, src, cpdir):
        try:
            shutil.copy(src, cpdir)
        except Exception, e:
            print('文件不存在')

    # 剪切文件
    def mv_file(self, src, cpdir):
        try:
            shutil.move(src, cpdir)
        except Exception as e:
            print('文件不存在')

    # 删除文件
    def rm_file(self, src):
        # open(src, 'w',encoding='utf-8')
        if os.path.exists(src):
            os.remove(src)
        else:
            print('文件不存在')

    # 重命名文件
    def rename_file(self, filename, newfilename):
        try:
            os.rename(filename, newfilename)
        except Exception as e:
            print('文件不存在')


lists = ['信息', '科技']
content = [line + "\n" for line in lists]
filename = './logs/cc/demo1.py2_bak'
f = Files()
# f.makedir(dir)
# f.removedir(dir)
# f.listdir(dir)
# f.read_file(filename)
# f.write_file(content, filename)
# f.cp_dir('./logs', './logs_bak')
# f.rm_file(filename)
# f.rename_file('./logs/cc/demo1.py444', './logs/cc/demo1.py11')
