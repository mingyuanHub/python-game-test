import unittest, xlrd, requests

api = "http://localhost:8084/"

workbook_path = "./python-game-test/excel/test.xlsx"

def getWorkbook():
    global workbook
    workbook = xlrd.open_workbook(workbook_path)
    return workbook

def getTable(name):
    workbook = getWorkbook()
    table = workbook.sheet_by_name(name)
    return table

def getNums(table):
    num = table.nrows
    return num

def getCelValue(table, rowx, colx):
    value = table.cell_value(rowx, colx)
    return(value)


class login(unittest.TestCase):
    
    def test_1(self):

        table = getTable("test")
        xlsx_num = getNums(table);
        for i in range(1, xlsx_num):
            test_id   = getCelValue(table, i, 0)
            test_name = getCelValue(table, i, 1)
            url       = getCelValue(table, i, 2)
            method    = getCelValue(table, i, 3)
            data      = getCelValue(table, i, 4)
            code      = getCelValue(table, i, 5)

            if method == 0 :
                # print(api + url + "?=" + data)
                response = requests.get(api + url + "?" + data)
                # print(response.text)
                res = response.json()
                self.assertEqual(res["code"], code)



        # self.assertEqual(1,2)

if __name__ == "__main__":
    unittest.main()