#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：blog_server 
@File    ：async_config.py
@Author  ：szhu9903
@Date    ：2022/12/8 23:35 
'''
from . import async_func

# 查询响应每次间隔时间
GET_ACK_TIME_INTERVAL = 2
# 查询响应次数
GET_ACK_COUNT = 6

async_cmd_map = {
    'query_env_cmd':{
        'func': async_func.general_deal_message,
        'req_event': '010302',
        'ack_event': '030302',
    }
}
