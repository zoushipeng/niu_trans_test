import sys
import json
from urllib import request, parse

if __name__ == '__main__':
    while 1:
        src_utf8 = input("输入需要翻译的内容:")
        method = 'GET'
        apikey = 'bb0c6201b84f7c55ec243d40375bc26f'
        language_request = "http://www.niutrans.online:6130/NiuTransServer/language?" + parse.urlencode({"src_text": src_utf8})
        language_data = request.Request(language_request)
        language_response = request.urlopen(language_data)
        from_language = language_response.read().decode()
        if from_language:
            from_data= json.loads(from_language)["language"]

        to_data = "zh" if from_data != "zh" else "en"

        values = {
            "from": from_data,
            "to": to_data,
            "src_text": src_utf8,
            "apikey": apikey
        }

        data = parse.urlencode(values).encode("utf-8")


        host = 'http://api.niutrans.vip'
        path = '/NiuTransServer/translation'
        querys = 'from=en&to=zh&src_text=hello&apikey='+apikey
        bodys = {}
        url = host + path # + '?' + querys

        request_data = request.Request(url, data, method=method)
        response_data = request.urlopen(request_data)
        content = response_data.read().decode()
        if content:
            print(content)