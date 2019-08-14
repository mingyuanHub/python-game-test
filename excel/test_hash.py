import unittest, xlrd, requests, HtmlTestRunner

class wxhash(unittest.TestCase):

    def test_tries(self):
        workbook = xlrd.open_workbook("./python-game-test/excel/test1.xlsx")
        table = workbook.sheet_by_name("test")
        xlsx_num = table.nrows
        # print(xlsx_num)
        for i in range(1, xlsx_num):
            test_id   = table.cell_value(i, 0)
            test_name = table.cell_value(i, 1)
            url       = table.cell_value(i, 2)
            method    = table.cell_value(i, 3)
            data      = table.cell_value(i, 4)
            code      = table.cell_value(i, 5)

            msg = "【"+str(test_id) + "报错啦】"

            if method == "get" :
                response = requests.get("https://qa-api.hub.hashkey.com" + url + "?" + data)
                # print(response.text)
                res = response.json()
                self.assertEqual(res["code"], code, msg)

if __name__ == "__main__":
    testRunner=HtmlTestRunner.HTMLTestRunner(output='./python-game-test/report', template='./python-game-test/report/template.html', combine_reports=True, report_name="game-test-report-excel",  add_timestamp=False)
    case = wxhash('test_tries')
    testRunner.run(case)