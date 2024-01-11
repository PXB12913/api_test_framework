import requests
import base64

# 获取token
def get_token():
    url = ''
    params = ''
    # resq = requests.get(url=url, params=params)
    # return resq.json()['token']
    return "dksfhdsjkfkkf"

# 加token
def token_headers(headers):
    headers['Authorization'] = get_token()
    return headers

# 加密请求参数
def encrypt_data(data, params):
    for param in params:
        data[param] = base64.b64encode(data[param].encode('utf-8')).decode('utf-8')
    return data

# 文件上传参数转换
def file_data(data, params):
    for param in params:
        data[param] = open(data[param], 'rb')
    return data