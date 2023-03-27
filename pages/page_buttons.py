from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from conftest import get_driver


class ButtonPage:
    driver  = get_driver
    button_double_click = WebElement.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
    button_dinamic_click = WebElement.find_element(By.XPATH,
                                                   "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button")
    button_right_click = WebElement.find_element(By.XPATH, "//button[@id='rightClickBtn']")
