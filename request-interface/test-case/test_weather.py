# coding:utf-8
import requests
import unittest


class Weather(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 101281601
        cls.url = 'http://t.weather.sojson.com/api/weather/city/101280601'
        cls.headers = {'Content-Type': 'application/json;charset=UTF-8'}

    def test_get_beijing(self):
        u"""查询天气"""
        response = requests.get(self.url, self.headers)
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

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
