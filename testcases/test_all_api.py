import pytest
from utils.usercase_utils import *
from utils.request_utils import *
from utils.response_utils import *
from settings import *
import logging

@pytest.mark.parametrize('usercases', get_usercases(r'接口功能测试用例.xlsx'))
def test_api(usercases):
    # 获取请求地址, 请求方式, 请求地址参数, 请求头参数, 请求体参数, 返回值
    logging.info('用例{}开始测试...'.format(usercases[0]))
    url = root_url + usercases[4]
    method = usercases[5]
    params = eval(usercases[6]) if isinstance(usercases[6], str) else {}
    headers = eval(usercases[7]) if isinstance(usercases[7], str) else {}
    data = eval(usercases[8]) if isinstance(usercases[8], str) else {}
    res = eval(usercases[9])
    logging.info('获取用例完成...')

    # 请求组装
    # 判断是否要鉴权
    if isinstance(usercases[10], str):
        headers = token_headers(headers)
        logging.info('加权:headers={}...'.format(headers))

    # 判断是否要加密
    if isinstance(usercases[11], str):
        data = encrypt_data(data, eval(usercases[11]))
        logging.info('加密:data={}...'.format(data))

    # 文件上传参数
    if isinstance(usercases[12], str):
        data = file_data(data, eval(usercases[12]))
        logging.info('文件参数:data={}...'.format(data))

    # 发出请求
    resq = True
    result = resq
    logging.info('请求完成...')

    # 返回值校验
    # 数据库校验
    if isinstance(usercases[13], str):
        t = eval(usercases[13])
        sql = t['sql']
        params = t['params']
        logging.info('数据库校验成功...')
        assert 200 == 200 and verify_mysql(result, sql, params)
        return

    assert 200 == 200