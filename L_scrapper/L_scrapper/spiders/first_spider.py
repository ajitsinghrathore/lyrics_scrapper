from ..items import  lyrics_item
import  scrapy
from bs4 import BeautifulSoup

class first_spider(scrapy.Spider):
    name = "name_of_first_spider"
    handle_httpstatus_list = [404,500,502]
    page_number = 1
    song_number = 1
    base_url = "https://bollywoodsongsbook.com/atoz/all?page=1"
    start_urls = ["https://bollywoodsongsbook.com/atoz/all?page=1"]

    def parse(self, response):

        if response.status in first_spider.handle_httpstatus_list:
            print("error in switching to next page")
            yield 

        all_links = response.css(".text-dark::attr(href)").extract()

        if len(all_links) != 0 :
            #print("fetching from page ______________-*****************************_________"+ str(first_spider.page_number))

            for link in all_links:
                yield response.follow(link, self.sub_parse)

            first_spider.page_number +=1
            print("******************************************************************************")
            new_url = "https://bollywoodsongsbook.com/atoz/all?page="+str(first_spider.page_number)
            yield  response.follow(new_url, self.parse)










    def sub_parse(self , response):

        if response.status in first_spider.handle_httpstatus_list:
            print("error in getting sub page ")
            yield 

        song_id =  first_spider.song_number
        first_spider.song_number +=1
        
        song_lyrics_raw = response.css(".col-sm-12+ .col-md-6").extract_first()
        soup = BeautifulSoup(song_lyrics_raw)  
        song_lyrics = [  i.get_text()  for i in soup.find_all("p")]
        
        genere = response.css(".col-sm-12.mb-5").re(r"<strong>Genre:</strong>(.*)\|")[0]
        heading = response.css("h2::text").extract_first()
        

        item = lyrics_item()

        item['title'] = heading
        item['song_id'] = song_id
        item["lyrics"] = song_lyrics
        item['genere'] = genere

        yield item         