import os
from time import sleep
import unittest
import HtmlTestRunner
from appium import webdriver
from altunityrunner import AltrunUnityDriver
#from Report import HtmlTestRunner

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SampleAppiumTest(unittest.TestCase):
    altdriver = None
    screenshot_dir = "screenshots"
    platform = "android"

    @classmethod
    def setUpClass (self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['deviceName'] = 'device'
        self.desired_caps['app'] = PATH('../adventure.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.altdriver = AltrunUnityDriver(self.driver, self.platform)

    @classmethod
    def tearDownClass(self):
        self.altdriver.stop()
        self.driver.quit()

    def setUp(self):
        self.set_screenshot_dir('%s/screenshots' % (os.getcwd()))

    def set_screenshot_dir(self, screenshot_dir):
        self.screenshot_dir = screenshot_dir
        if not os.path.exists(screenshot_dir):
            os.mkdir(self.screenshot_dir)

    def test01_check_security_room_loaded(self):
        self.altdriver.wait_for_current_scene_to_be("SecurityRoom")
        self.altdriver.wait_for_element("Player")
        self.driver.save_screenshot(self.screenshot_dir + "/0_security_room_loaded.png")

    def test02_check_interaction_in_security_room(self):
        messageCanvasText = "MessageCanvas"

        self.altdriver.find_element('GuardInteractable').tap()
        self.altdriver.wait_for_element_with_text(messageCanvasText, "Get lost!")
        self.driver.save_screenshot(self.screenshot_dir + "/1_interacted_with_guard.png")

        self.altdriver.find_element("PictureInteractable").tap()
        self.altdriver.wait_for_element_with_text(messageCanvasText, "He looks pretty trustworthy.")
        self.driver.save_screenshot(self.screenshot_dir + "/2_interacted_with_picture.png")

        self.altdriver.find_element("LaserGridInteractable").tap()
        self.altdriver.wait_for_element_with_text(messageCanvasText, "ACCESS DENIED!")
        self.driver.save_screenshot(self.screenshot_dir + "/3_interacted_with_grid.png")

    def test03_check_market_loaded(self):
        messageCanvasText = "MessageCanvas"

        self.altdriver.find_element("DoorToMarketStartingPosition").tap()
        self.altdriver.wait_for_current_scene_to_be("Market")
        self.altdriver.wait_for_element("Player")
        self.driver.save_screenshot(self.screenshot_dir + "/4_market_loaded.png")
        
        
   
               



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SampleAppiumTest)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    #unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test-reports-html'))