import unittest, requests
import config

class user(unittest.TestCase):
    def test_getGameData(self):
        params = {
            "userid":11
        }
        response = requests.post(config.api + "af/user/getGameData", json=params)
        res = response.json()
        self.assertEqual(res["code"], 200)
        
    def test_updateGameData(self):
        params = {
            "userid":11,
            "token" : "bc6d3446d8fb96375a90ac427cf29bdd",
            "gold":"0",
            "guide":"1-2",
            "music":0, 
            "audio":0,
            "vibration":0,
            "jeepqh":{
                "attackLv":1,
                "defenseLv":1,
                "hpLv":1
            },
            "tankqh":{
                "attackLv":1,
                "defenseLv":1,
                "hpLv":1
            },
            "boatqh":{
                "attackLv":1,
                "defenseLv":1,
                "hpLv":1
            },
            "chapterData":{
                "chapterId":1,
                "isKill":False
            },
        }
        response = requests.post(config.api + "af/user/updateGameData", json=params)
        # print(response.text)
        res = response.json()
        self.assertEqual(res["code"], 200)
if __name__ == '__main__':
    unittest.main()