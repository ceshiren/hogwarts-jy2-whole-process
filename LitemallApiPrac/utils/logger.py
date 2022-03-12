# @Author   : Clifford
# @File     : logger
# @Time     : 2022/3/12 17:24


import logging


def info(msg):
    """
    日志方法
    :param msg: 要打印到日志中的信息
    :return: info 级别的日志
    """

    # 指定 log 日志的存放位置（需要先创建目录，否则会报错）
    # 指定日志的编码格式
    file_handler = logging.FileHandler(filename="../logs/apitest.log", encoding="utf-8")
    # 设置日志的等级
    logging.getLogger().setLevel(logging.INFO)
    # 设置日志的内容格式
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
    file_handler.setFormatter(formatter)

    steam_handler = logging.StreamHandler()
    # 日志格式与句柄的绑定
    steam_handler.setFormatter(formatter)

    # 设置生效
    logging.getLogger().addHandler(file_handler)
    logging.getLogger().addHandler(steam_handler)

    return logging.info(msg)