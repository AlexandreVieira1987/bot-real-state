from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import string

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class BaseUseCase(ABC):
    
    @abstractmethod
    def execute(self):
      pass


    def __init__(self):
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--disable-extensions')
        self.options.add_argument('--no-sandbox')

        chrome_prefs = {}
        self.options.experimental_options["prefs"] = chrome_prefs
        self.driver = webdriver.Chrome(options=self.options)
        


    def normatize_value(self, value, symbol):
      value = value.replace(symbol, '')
      value = value.replace(',', '')
      value = value.replace('.', ',')

      return value