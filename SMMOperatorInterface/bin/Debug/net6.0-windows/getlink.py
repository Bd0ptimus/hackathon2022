import requests 
from bs4 import BeautifulSoup as BS 
from selenium import webdriver
import os 
import random
import codecs


check=0
while (check==0):
    #initialization
    list={1:"Технологические ",2:"Точка кипения",3:"Наука",4:"FutureSkills",5:"НТИ",6:"Технологии",7:"Практики будущего"}
    i = random.randint(1,7)
    search = "NeuroNET"

    #get value
    driver = webdriver.Chrome(os.getcwd() + '/chromedriver.exe')
    website = f"http://mediametrics.ru/search/week.html#ru:tm:{search}"
    driver.get(website)
    html = driver.page_source
    soup = BS(html, "html.parser")

    #output the link
    with codecs.open("news_input.txt", "w", "utf-8") as stream:   # or utf-8
        for el in soup.select("#news > .rsearch > .rs-link"): 
            #text = el.select("a")
            check+=1
            href_tag = el.find(href = True)
                #print(href_tag.text)
            stream.write(href_tag.text+'\n'+href_tag['href'] +'\n'+"#"+ search.replace(" ", "_").lower() +'\n \n')
        stream.close()

            
