# coding:utf-8
import configparser


class ReadConfig(object):
    u"""设置配置文件"""

    def __init__(self):
        # 第一步：创建conf对象
        self.cf = configparser.ConfigParser()

    def set_data(self):
        # 第二步：添加section、option的值
        # section
        self.cf.add_section("HTTP")
        # 参数分别为：section, option, value
        self.cf.set("HTTP", "base_url", "https://www.csdn.net/")
        self.cf.set("HTTP", "port", "80")

        self.cf.add_section("EMAIL")
        self.cf.set("EMAIL", "mail_host", "smtp.163.com")
        self.cf.set("EMAIL", "mail_port", "25")

        # self.cf.add_section("DATA")

        # "DEFAULT" section默认不显示  怎么读取这个值？
        self.cf.setdefault('DEFAULT', {'a': 1, 'b': 2})

        # 第三步：写入文件
        with open("config.conf", 'w')as conf:
            self.cf.write(conf)

        # 打印所有的section 列表形式
        print self.cf.sections()

    def get_data(self, section, option):
        # 第四步：读取配置文件中的section、options的值
        return self.cf.get(section, option)


if __name__ == '__main__':
    read_config = ReadConfig()

    read_config.set_data()

    print read_config.get_data("HTTP", "base_url")
    print read_config.get_data("EMAIL", "mail_host")


