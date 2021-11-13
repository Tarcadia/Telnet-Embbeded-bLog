#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import logging;

VERSION = 'v20211111';

logger = logging.getLogger(__name__);
logger.setLevel(logging.DEBUG);
_logger_ch = logging.StreamHandler();
_logger_ch.setLevel(logging.DEBUG);
_logger_formatter = logging.Formatter(fmt='\033[0m%(asctime)s \033[1;34m[%(levelname)s]\033[0;33m[%(name)s]\033[0m >> %(message)s', datefmt='%H:%M');
_logger_ch.setFormatter(_logger_formatter);
logger.addHandler(_logger_ch);
logger.info('Running...');



import BNYYCS;

# 初始化BNYYCS模块
# BNYYCE模块通过open/close对进行访问，open返回一个update的迭代器
# open可使用with进行
# 开始轮询和

serv = BNYYCS.__bnyycs_main__.BNYYCS(host = "localhost");
try:
    with serv.open() as updates:
        for update in updates:
            if update:
                logger.debug(update);
except:
    logger.info('Ended.');