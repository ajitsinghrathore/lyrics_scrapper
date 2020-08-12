# lyrics_scrapper


dependencies

     set your own virtual environment

     navigate to .vscode/settings.json file and put your  path for virtual environment  of python
     
     then install these dependencies in your virtual environment
   
     1 ->  pip install bs4
     2 ->  pip install scrapy
    
    
     
    

# how to run it




    open terminal in [settings_file](lyrics_scrapper/L_scrapper folder) and execute the command  "scrapy crawl name_of_first_spider -o lyrics.json"
    
    it will  pull all the songs from [bollywood songs book](https://bollywoodsongsbook.com/)  and store them in the json file named lyrics.json
    there are total around 15000  lyrics out of which i was able to pull out around 8500 songs after that got the error of max retries reached .
    
    
    
    
 # statistical analysis of genre in datasets
 
 ![pie chart](https://github.com/ajitsinghrathore/lyrics_scrapper/blob/master/L_scrapper/Figure_1.png?raw=true)
