from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from db import Especialidade

class Scraping:

    def __init__(self):
        self.options = Options()
        self.browser = webdriver.Chrome(options=self.options)
        self.argument_options = 'window-size=1500,1000'
        self.URL = 'https://saojoseclinica.com.br/'
        self.es = Especialidade()

    def execute(self):
        
        self.options.add_argument(self.argument_options)

        self.browser.get(self.URL)
       
        dct_full = self.mount_dict_especialidades()
        
        for i in range(len(dct_full['links'])):
            self.es.insert(dct_full['especialidades'][i], dct_full['links'][i])
            
        self.browser.quit()

    def mount_dict_especialidades(self):
        dct_full = {}
        links = []
        especialidades = []
        tags_a = []
        submenu_especialidades = self.browser.find_element_by_id('menu-item-1905') \
            .find_element_by_class_name('sub-menu') \
            .find_elements_by_tag_name('li') \
            
        for link in submenu_especialidades:
            tags_a.append(link.find_element_by_tag_name('a'))
            
        for especialidade in tags_a:
            links.append(especialidade.get_attribute('href'))
            especialidades.append(especialidade.get_attribute('innerHTML'))
        
        dct_full['links'] = links
        dct_full['especialidades'] = especialidades

        return dct_full