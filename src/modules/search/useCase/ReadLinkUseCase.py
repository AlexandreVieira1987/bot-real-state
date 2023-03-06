from src.shared.BaseUseCase import BaseUseCase
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import string
import pandas as pd

class ReadLinkUseCase(BaseUseCase):
    
    def __init__(self):
        super().__init__()
    

    def execute(self):
        links = open('src/shared/database/links/for-sale.txt', 'r')
        infos = []

        count = 1
        for link in links:
            self.driver.get(link)
            title, sub_title = self.title_sub_title()
            area = self.area()

            info = {
              'area': area,
              'title': title, 
              'sub_title': sub_title,
              'link': link,
              'infos': self.infos()
            }

            infos.append(info)

            print(count)
            count = count + 1
            


        df = pd.DataFrame(infos)
        df.to_json('src/shared/database/links/infos.json')
        df.to_parquet('src/shared/database/links/infos.parquet', engine='pyarrow', compression = 'gzip')

        

    def title_sub_title(self):
        try:
            header_title = self.driver.find_element(By.CLASS_NAME, 'header-title')
            header = header_title.get_attribute('innerHTML')

            soup = BeautifulSoup(header, 'html.parser')
            title = soup.find('span').get_text()
            sub_title = soup.find('div').find('span').get_text()
            
            return title, sub_title
        except Exception:
            return '', ''


    def infos(self):
        info_primary = self.driver.find_element(By.CLASS_NAME, 'info-primary')
        itens_info = info_primary.get_attribute('innerHTML')

        soup = BeautifulSoup(itens_info, 'html.parser')
        divs = soup.find_all('div')

        infos = {}
        for div in divs:
            span = div.find('span').get_text()
            table = span.maketrans('', '', string.digits)
            text = span.translate(table)

            numbers = [char for char in span if char.isdigit()]

            if text != None:
                infos[span] = ''.join(numbers)

        return infos
    

    def area(self):
        try:
            info = self.driver.find_element(By.XPATH, '/html/body/div[3]/section/div/div/div/div[3]/div[2]/div[1]/div[3]/div/div[1]/span')
        except Exception:
            return ''


        return info.text

    