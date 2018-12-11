# coding:utf-8
import os
import codecs
import configparser

# 获取绝对路径
proDir = os.path.dirname(os.path.abspath(__file__))
configPath = os.path.join(proDir, "config.ini")
# configPath = os.path.join(proDir, "config.conf")
print configPath


class ReadConfig(object):
    u"""读取配置文件"""

    def __init__(self):
        # 去掉 UTF-8-BOM 头
        fd = open(configPath)
        data = fd.read()
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            rh = codecs.open(configPath, "w")
            rh.write(data)
            rh.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_config(self, category, data):
        value = self.cf.get(category, data)
        return value


if __name__ == '__main__':
    read_config = ReadConfig()
    print read_config.get_config('HTTP', 'base_url')
    print read_config.get_config('EMAIL', 'mail_host')
