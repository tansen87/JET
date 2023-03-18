'''
Author: tansen
Date: 2023-03-18 17:41:48
LastEditors: Please set LastEditors
LastEditTime: 2023-03-18 18:09:23
'''
import logging


class Log:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s: %(message)s',
        datefmt="%H:%M:%S")

    @staticmethod
    def info(message: str):
        logging.info(f"\033[0;32m{message}\033[0m")

    @staticmethod
    def warning(message: str):
        logging.warning(f"\033[0;33m{message}\033[0m")

    @staticmethod
    def error(message: str):
        logging.error(f"\033[0;31m{message}\033[0m")


if __name__ == '__main__':
    # 测试代码
    Log.info("info日志")
    Log.warning("warning日志")
    Log.error("error日志")
    Log.debug("debug日志")
