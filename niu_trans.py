import sys
import time
import requests

apikey = 'bb0c6201b84f7c55ec243d40375bc26f'

if __name__ == '__main__':
    while 1:
        src_input = input("请输入需要翻译的文字:")

        start1 = time.time()
        language_request = "http://www.niutrans.online:6130/NiuTransServer/language?src_text=" + src_input
        language_response = requests.get(language_request)
        try:
            json_data = language_response.json()
            from_data = json_data["language"]
            end1 = time.time() - start1
            print("请求源语言类型耗时:" + str(end1 * 1000) + "ms")
            print(json_data)
        except ValueError:
            print("解析json失败")
            sys.exit(0)

        to_data = "en" if from_data == "zh" else "zh"

        values = {
            "from": from_data,
            "to": to_data,
            "src_text": src_input,
            "apikey": apikey
        }

        start2 = time.time()
        host = 'http://api.niutrans.vip/NiuTransServer/translation'
        response_data = requests.get(host, values)
        end2 = time.time() - start2
        print("请求翻译接口耗时:" + str(end2 * 1000) + "ms")

        print(response_data.text)


