import unittest, requests
import config

# global gold

class profit(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.api = config.api
        self.gold = 0

    def test_af_profit_getUserProfit (self):
        params = {
            "userid": 4,
            "chapterId" : 21
        }
        response = requests.post(url = self.api + "af/profit/getUserProfit", json = params)
        res = response.json()
        # print(response.text)
        self.assertEqual(res["code"], 200)
        self.gold = res["data"]["gold"]

    def test_harvest_profit (self):
        params = {
            "userid":4,
            "times":1
        }
        response = requests.post(url = self.api + "af/profit/harvestProfit", json = params)
        res = response.json()
        if self.gold > 0 :
            self.assertEqual(res["code"], 200)
        else :
            self.assertEqual(res["code"], 104)

if __name__ == '__main__':
    unittest.main()
        