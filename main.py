import unittest, HtmlTestRunner
from af.main import getAfSuite as af_suite

def get_suilt_all():
    suite = unittest.TestSuite()
    suite.addTest(af_suite())
    return suite

def get_runner():
    runner = HtmlTestRunner.HTMLTestRunner(output = './game-test/report', combine_reports = True, report_name = "game-test-report",  add_timestamp = False)
    return runner
        
if __name__ == '__main__':
    get_runner().run(get_suilt_all())



