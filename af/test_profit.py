import unittest, requests
import config

# global gold

class profit(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.api = config.api
        profit.gold = 0

    def test_af_profit_getUserProfit (self):
        params = {
            "userid": 11,
            "chapterId" : 21,
            "token" : "bc6d3446d8fb96375a90ac427cf29bdd"
        }
        response = requests.post(url = self.api + "af/profit/getUserProfit", json = params)
        res = response.json()
        # print(response.text)
        self.assertEqual(res["code"], 200)
        profit.gold = res["data"]["gold"]
        print(self.gold)

    def test_harvest_profit (self):
        params = {
            "userid":11,
            "times":1,
            "token" : "bc6d3446d8fb96375a90ac427cf29bdd"
        }
        response = requests.post(url = self.api + "af/profit/harvestProfit", json = params)
        res = response.json()
        if profit.gold > 0 :
            self.assertEqual(res["code"], 20022)
        else:
            self.assertEqual(res["code"], 10422)

if __name__ == '__main__':
    unittest.main()
        