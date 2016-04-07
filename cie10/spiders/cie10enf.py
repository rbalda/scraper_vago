# -*- coding: utf-8 -*-
import scrapy
import cie10.items as items
import string
import time


def generate_urls():
    letters = list(string.ascii_lowercase)
    urls=[]
    for l in letters:
        urls.append("http://eciemaps.mspsi.es/ecieMaps/statics/es/basic/cie10/alphabetic_index/ai_enf_%s.html"%(l))
    return urls

class Cie10enfSpider(scrapy.Spider):
    name = "cie10enf"
    allowed_domains = ["http://eciemaps.mspsi.es/ecieMaps/browser/index_10_2008.html"]
    start_urls = generate_urls()

    # def __init__(self):
        # self.driver = webdriver.Firefox()

    def parse(self, response):
        text = response.xpath("//span[@class='aiEntradaPrincipal']/text()")
        elements = response.xpath("//ul[@class='alphabeticIndexList']/li")

        # self.driver.get("%s#search=A&index=enf"%(response.url))
        # time.sleep(2)
        # a = self.driver.find_elements_by_id("enfMenu")[0]
        # a.click()
        # time.sleep(2)
        # b = self.driver.find_elements_by_id("enfA")[0]
        # print b.text
        # b.click()
        #c = self.driver.find_elements_by_id("AARSKOG_2")
        # element = WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.ID, "alphabeticIndexTop")))
        # text = element.find_elements_by_class_name("aiEntradaPrincipal")[0].text
        for t in elements:
            print t
