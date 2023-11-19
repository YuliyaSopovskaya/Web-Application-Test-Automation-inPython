import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)

# service = Service(testdata["driver_path"])
service = ChromeService(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

class Site:
    def __init__(self, address):
        self.driver = webdriver.Chrome(service=service, options=options)

        # self.driver = webdriver.Chrome(service=Service(testdata["driver_path"]), options=options)
        self.driver.maximize_window()
        self.driver.get(address)
        time.sleep(testdata["sleep_time"])

    def find_element(self, mode, path):
        if mode == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == "xpath":
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    def get_element_property(self, mode, path, property):  #режим поиска / путь / свойства
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)

    def close(self):
        self.driver.close()
