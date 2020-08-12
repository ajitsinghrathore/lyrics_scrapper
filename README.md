# lyrics_scrapper


dependencies

  set your own virtual environment

  navigate to [settings file](.vscode/settings.json) file and put your  path for virtual environment  of python 
  then install these dependencies in your virtual environment
   
     1 ->  pip install bs4
     2 ->  pip install scrapy
    
    
     
    

## how to run it




  > open terminal in **lyrics_scrapper/L_scrapper folder** and execute the command  ***"scrapy crawl name_of_first_spider -o lyrics.csv"***
   it will  pull all the songs from [bollywood songs book](https://bollywoodsongsbook.com/atoz/all)  and store them in the csv file named lyrics.csv
   there are total around 15000  lyrics .
   
  > open termina; in **lyrics_scrapper/L_scrapper folder ** and execute the commmand ***"scrapy crawl shayari_spyder -o shayari.csv"***
   it will pull all the shayari from [shayaribaaz](http://www.shayaribazar.com/English/) and store them in the csv file named shayari.csv
   there are total around 24000 shayari .
    
    
    
    
 ## statistical analysis of song genre in datasets
 
 ![pie chart](https://github.com/ajitsinghrathore/lyrics_scrapper/blob/master/L_scrapper/Figure_1.png?raw=true)
 
 
 
 ## visualising data of song genre
 
  firstly  fetch all the songs lyrics as per above instructions then [execute this file](L_scrapper/visualization.py) 
 
