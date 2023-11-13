import yaml
import time
from select import webdriver
from selenium.webdriver.chrome.service import Service

with open ('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)

service = Service(testdata["driver_path"])
options = webdriver.ChromeOptions()
class Site:
    def __init__(self, address):
        self.driver = webdriver.Chrome(servise=Service, options=options)
        self.driver.maximixe_window()
        self.driver.get(address)
        time.sleep(testdata["sleep_time"])
