import unittest, HtmlTestRunner

def getAfSuite():
    suite = unittest.TestSuite()
    all_cases = unittest.defaultTestLoader.discover('/Users/mingyuan/python/game-test/af/', pattern='test*.py')

    for case in all_cases:
        suite.addTests(case)
    return suite 
        
if __name__ == '__main__':
    suite = getAfSuite()
    testRunner=HtmlTestRunner.HTMLTestRunner(output='./game-test/report', template='./game-test/report/index.html', combine_reports=True, report_name="game-test-report",  add_timestamp=False)
    testRunner.run(suite)

