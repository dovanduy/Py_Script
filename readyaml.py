# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 18:59
# @Author  : chengz
# @File    : readyaml.py
# @Software: PyCharm

import os
import yaml


def _get_yaml():
    """
    解析yaml
    :return: s  字典
    """
    path = os.path.join('ticket_config.yaml')
    f = open(path)
    s = yaml.load(f)
    f.close()
    return s.decode() if isinstance(s, bytes) else s


if __name__ == '__main__':
    print(_get_yaml())