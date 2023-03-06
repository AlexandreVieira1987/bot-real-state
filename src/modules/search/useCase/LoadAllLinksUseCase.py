from src.shared.BaseUseCase import BaseUseCase
from selenium.webdriver.common.by import By
from src.shared.providers.queue.celery import queue_read_link

class LoadAllLinksUseCase(BaseUseCase):
    
    def __init__(self):
        super().__init__()
    
    
    def execute(self):
        for url in self.__providers():
            page = 0
            while True:
                ground = self.__load_all_links(page, url)
                if ground == False:
                  break

                page = page + 1
            

    def __providers(self):
       return [
          'https://www.d10imoveis.com.br/imoveis/a-venda',
          'https://www.claudioimoveis.net/imoveis/a-venda',
          'https://www.phpimoveis.com.br/imoveis/a-venda',
          'https://www.prismaimobiliaria.net/imoveis/a-venda'
       ]


    def __load_all_links(self, page, url):
        if page > 0:
          url = url + '?pagina=' + str(page)

        try: 
            self.driver.get(url)

            listing_results = self.driver.find_element(By.CLASS_NAME, 'listing-results')
            links = listing_results.find_elements(By.TAG_NAME, 'a')
            
            if links == []:
                print('end of search')
                return False  

            hrefs = []
            file_links = open('src/shared/database/links/for-sale.txt', 'a')
            for link in links:
                href = link.get_attribute('href')
                print(href)

                if href.find('imovel/') > 0:
                  hrefs.append(href)

            unique_links = list(set(hrefs))
            for href in unique_links:
                file_links.write(href + '\n')
                queue_read_link.delay(href)

        except Exception:
          print('error on save link')
    