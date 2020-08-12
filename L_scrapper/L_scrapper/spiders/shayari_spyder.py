from ..items import  shayari_item
import  scrapy
from bs4 import BeautifulSoup
import re

class  ShayarSpider(scrapy.Spider):
   
    name = "shayari_spyder"
    handle_httpstatus_list = [404,500,502]
    genre_number = 0
    page_number = 1
    shayari_number = 1
    current_genre_link = ""
    all_genre_links = []
    start_urls = ["http://www.shayaribazar.com/english"]


    def parse(self, response):
        if response.status in ShayarSpider.handle_httpstatus_list:
            print("error in switching to next page")
            yield 

        ShayarSpider.all_genre_links = response.css("#demo1 a::attr(href)").extract()
    
        print("fetching from genre ______________-*****************************_________"+ ShayarSpider.all_genre_links[ShayarSpider.genre_number])
        ShayarSpider.page_number = 1
        try :
            ShayarSpider.current_genre_link = ShayarSpider.all_genre_links[ShayarSpider.genre_number]
        except :
            return

        link = ShayarSpider.current_genre_link + "?page="+str(ShayarSpider.page_number)
        yield  response.follow(link, self.sub_parse)





         


    def sub_parse(self,response):
            if response.status in ShayarSpider.handle_httpstatus_list:
                print("error in getting sub page ")
                yield 

            
            headings = response.css(".main_head::text").extract()
            shayaris = response.css("p").extract()

    
            if len(headings) != 0 :
                for heading,shayari in zip(headings , shayaris):
                    
                    item  = shayari_item()
                    item["shayari"] = [re.sub(r"<p>|</p>","",i) for i in shayari.split("<br>")]
                    item["title"] = heading
                    item["shayari_id"] = ShayarSpider.shayari_number
                    ShayarSpider.shayari_number +=1

                    yield  item

                ShayarSpider.page_number +=1  
                new_url =  ShayarSpider.current_genre_link +"?page="+str(ShayarSpider.page_number)
                print(new_url+"**************************************************"+str(ShayarSpider.page_number))
                yield response.follow(new_url, self.sub_parse)


            else :
                ShayarSpider.genre_number +=1
                ShayarSpider.page_number = 1
                print("fetching from genre ______________-*****************************_________"+ str(ShayarSpider.genre_number))

                try :
                    ShayarSpider.current_genre_link = ShayarSpider.all_genre_links[ShayarSpider.genre_number]
                except :
                    return

                link = ShayarSpider.current_genre_link + "?page="+str(ShayarSpider.page_number)
                yield  response.follow(link, self.sub_parse)





