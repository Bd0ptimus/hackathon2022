import requests 
from bs4 import BeautifulSoup as BS 
from selenium import webdriver
import os 
import random
import codecs


check=0
while (check==0):
    #initialization
    list={1:"Технологические стандарты",2:"Точка кипения",3:"Наука",4:"FutureSkills",5:"НТИ",6:"Технологии",7:"Практики будущего"}
    i = random.randint(1,7)
    search = list[i]

    #get value
    driver = webdriver.Chrome(os.getcwd() + '/chromedriver.exe')
    website = f"http://mediametrics.ru/search/week.html#ru:tm:{search}"
    driver.get(website)
    html = driver.page_source
    soup = BS(html, "html.parser")

    #output the link
    with open('link.txt','a') as f:#write file
        for el in soup.select("#news > .rsearch > .rs-link"): 
            #text = el.select("a")
            check+=1
            href_tag = el.find(href = True)
            #print(href_tag.text)

            with codecs.open("customer_input.txt", "a", "utf-8") as stream:   # or utf-8
                stream.write(href_tag.text+'\n')
            with codecs.open("customer_input.txt", "a", "utf-8") as stream:   # or utf-8
                stream.write(href_tag['href'] +'\n')
            with codecs.open("customer_input.txt", "a", "utf-8") as stream:   # or utf-8
                stream.write("#"+ search.replace(" ", "_").lower() +'\n\n')
    f.close()
