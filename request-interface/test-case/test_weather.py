# coding:utf-8
import requests
import unittest




class Weather(unittest.TestCase):
    def setUp(self):
        # 101281601
        self.url = 'http://t.weather.sojson.com/api/weather/city/101280601'
        self.headers = {'Content-Type': 'application/json;charset=UTF-8'}

    def test_get_beijing(self):
        u"""查询天气"""
        response = requests.get(url=self.url, headers=self.headers)
        # print response.encoding
        result = response.json()
        if result['status'] == 200:
            city = result['cityInfo']
            print city['city'], '\n'
            data = result['data']
            for cast in data['forecast']:
                # print cast
                date = cast['date']
                high = cast['high']
                low = cast['low']
                fx = cast['fx']
                fl = cast['fl']
                types = cast['type']
                notice = cast['notice']

                print date
                print low, '~', high
                print types, fx, fl
                print notice, '\n'


if __name__ == '__main__':
    unittest.main()
