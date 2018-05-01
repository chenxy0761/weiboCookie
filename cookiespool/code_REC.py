#!/usr/bin/python
# -*- coding: utf-8 -*-
import base64
import json
from urllib.parse import urlencode
import urllib.request
from PIL import Image


# ----------------------------------
# 验证码识别调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/60
# ----------------------------------
def codeAPI(image):
    im = base64.b64encode(image)  # 读取文件内容，转换为base64编码

    # 配置您申请的APPKey
    appkey = "3aea8dce136fca20b0243c4121b7563e"

    # 1.识别验证码
    result = request1(im, appkey, "POST")
    return result
    # 2.查询验证码类型代码
    # request2(appkey, "GET")

def main():
    file = open('../pic/92404a1b50cea0ade9166a2224d2ab26.jpg', 'rb')
    image = base64.b64encode(file.read())  # 读取文件内容，转换为base64编码

    # 配置您申请的APPKey
    appkey = "3aea8dce136fca20b0243c4121b7563e"

    # 1.识别验证码
    result = request1(image, appkey, "POST")
    return result
    # 2.查询验证码类型代码
    # request2(appkey, "GET")
    file.close()
    """
    [{'code': '8001', 'description': '任意长度，不确定验证码类型时可选此值，但会影响正确度和效率'}, 
    {'code': '8002', 'description': '任意长度，不确定验证码类型时可选此值，但会影响正确度和效率'}, 
    {'code': '8003', 'description': '1~5位英文'}, 
    {'code': '1001', 'description': '1位 英文或数字'}, 
    {'code': '1002', 'description': '1～2位英文或数字'}, 
    {'code': '1003', 'description': '1～3位英文或数字'}, 
    {'code': '1004', 'description': '1～4位 英文或数字'}, 
    {'code': '1005', 'description': '1～5位 英文或数字'}, 
    {'code': '1006', 'description': '1～6位 英文或数字'}, 
    {'code': '1007', 'description': '1～7位 英文或数字'}, 
    {'code': '1008', 'description': '1～8位 英文或数字'}, 
    {'code': '1009', 'description': '1～9位 英文或数字'}, 
    {'code': '1010', 'description': '1～10位 英文或数字'}, 
    {'code': '1011', 'description': '1～11位 英文或数字'}, 
    {'code': '1012', 'description': '1～12位 英文或数字'}, 
    {'code': '1013', 'description': '1～13位 英文或数字'}, 
    {'code': '1014', 'description': '1～14位 英文或数字'}, 
    {'code': '1015', 'description': '1～15位 英文或数字'}, 
    {'code': '1016', 'description': '1～16位 英文或数字'}, 
    {'code': '1017', 'description': '1～17位 英文或数字'}, 
    {'code': '1018', 'description': '1～18位 英文或数字'}, 
    {'code': '1019', 'description': '1～19位 英文或数字'}, 
    {'code': '1020', 'description': '1～20位 英文或数字'}, 
    {'code': '2001', 'description': '1汉字'}, 
    {'code': '2002', 'description': '1～2汉字'}, 
    {'code': '2003', 'description': '1～3汉字'}, 
    {'code': '2004', 'description': '1～4汉字'}, 
    {'code': '2005', 'description': '1～5汉字'}, 
    {'code': '2006', 'description': '1～6汉字'}, 
    {'code': '2007', 'description': '1～7汉字'}, 
    {'code': '2008', 'description': '1～8汉字'}, 
    {'code': '2009', 'description': '1～9汉字'}, 
    {'code': '2010', 'description': '1～10汉字'}, 
    {'code': '3001', 'description': '1位 英文字'}, 
    {'code': '3002', 'description': '1～2位纯英文'}, 
    {'code': '3003', 'description': '1～3位纯英文'}, 
    {'code': '3004', 'description': '1～4位纯英文'}, 
    {'code': '3005', 'description': '1～5位纯英文'}, 
    {'code': '3006', 'description': '1～6位纯英文'}, 
    {'code': '3007', 'description': '1～7位纯英文'}, 
    {'code': '3008', 'description': '1～8位纯英文'}, 
    {'code': '3009', 'description': '1～9位纯英文'}, 
    {'code': '3010', 'description': '1～10位纯英文'}, 
    {'code': '4001', 'description': '1～1位纯数字'}, 
    {'code': '4002', 'description': '1～2位纯数字'}, 
    {'code': '4003', 'description': '1～3位纯数字'}, 
    {'code': '4004', 'description': '1～4位纯数字'}, 
    {'code': '4005', 'description': '1～5位纯数字'}, 
    {'code': '4006', 'description': '1～6位纯数字'}, 
    {'code': '4007', 'description': '1～7位纯数字'}, 
    {'code': '4008', 'description': '1～8位纯数字'}, 
    {'code': '4009', 'description': '1～9位纯数字'}, 
    {'code': '4010', 'description': '1～10位纯数字'},
    {'code': '5001', 'description': '1位 中英文数字混合'}, 
    {'code': '5002', 'description': '1～2位中英文数字混合'}, 
    {'code': '5003', 'description': '1～3位中英文数字混合'}, 
    {'code': '5004', 'description': '1～4位 中英文数字混合'}, 
    {'code': '5005', 'description': '1～5位中英文数字混合'},
    {'code': '5006', 'description': '1～6位中英文数字混合'}, 
    {'code': '5007', 'description': '1～7位中英文数字混合'}, 
    {'code': '5008', 'description': '1～8位中英文数字混合'}, 
    {'code': '5009', 'description': '1～9位中英文数字混合'}, 
    {'code': '5010', 'description': '1～10位中英文数字混合'},
    {'code': '5011', 'description': '1～11位中英文数字混合'}, 
    {'code': '5012', 'description': '1～12位中英文数字混合'}, 
    {'code': '5013', 'description': '1～13位中英文数字混合'}, 
    {'code': '5014', 'description': '1～14位中英文数字混合'}, 
    {'code': '5015', 'description': '1～15位中英文数字混合'}, 
    {'code': '5016', 'description': '1～16位中英文数字混合'}, 
    {'code': '5017', 'description': '1～17位中英文数字混合'}, 
    {'code': '5018', 'description': '1～18位中英文数字混合'}, 
    {'code': '5019', 'description': '1～19位中英文数字混合'}, 
    {'code': '5020', 'description': '1～20位中英文数字混合'}, 
    {'code': '6001', 'description': '计算题,返还数字结果'}, 
    {'code': '6002', 'description': '计算题,返还汉字结果'}, 
    {'code': '7001', 'description': '坐标题 (返还1次坐标,适用于4选1,N选1)'}, 
    {'code': '7002', 'description': '坐标题 (返还2次坐标,适用于N选2）'}, 
    {'code': '7003', 'description': '坐标题 (返还3次坐标,适用于N选3）'}, 
    {'code': '7004', 'description': '坐标题 (返还4次坐标,适用于九宫格,N选4）'}, 
    {'code': '9001', 'description': '九宫格专用,返还对应汉字数字编号'}, 
    {'code': '3011', 'description': '两个单词,返还一个'}, 
    {'code': '3012', 'description': '两个单词,全部返还'}, 
    {'code': '1900', 'description': '四位英文字母(关闭自动识别)'}]

    """


# 识别验证码
def request1(image, appkey, m="GET"):
    url = "http://op.juhe.cn/vercode/index"
    params = {
        "key": appkey,  # 您申请到的APPKEY
        "codeType": 1005,
        # 验证码的类型，&lt;a href=&quot;http://www.juhe.cn/docs/api/id/60/aid/352&quot; target=&quot;_blank&quot;&gt;查询&lt;/a&gt;
        "base64Str": image,  # 图片文件
        "dtype": "json",  # 返回的数据的格式，json或xml，默认为json

    }
    params = urlencode(params).encode(encoding='UTF8')
    if m == "GET":
        f = urllib.request.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.request.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])
            return str(res["result"])
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")


# 查询验证码类型代码
def request2(appkey, m="GET"):
    url = "http://op.juhe.cn/vercode/codeType"
    params = {
        "key": appkey,  # 您申请到的APPKEY
        "dtype": "json",  # 返回的数据的格式，json或xml，默认为json

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.request.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.request.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")


if __name__ == '__main__':
    main()
