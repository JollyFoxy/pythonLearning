from selenium.webdriver.common.by import By

from Selenium.test_sell import testSell


class TestElements(testSell):
    def test_p(self):
        driver = self.driver
        driver.maximize_window()
        element = driver.find_element(By.XPATH, "//h5[.='Elements']")
        element.click()

        element2 = driver.find_element(By.XPATH, "//div[.='Elements']")
        element2.click()
        assert element2.text == "Elements"
        driver.quit()
