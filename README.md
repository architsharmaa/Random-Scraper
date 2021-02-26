# Product Scrapper
The following is the sample scarper to scrape details of  products using links. 
#### Overview
The following scraper is the scraper which scrapes the details of the product using *Beautiful Soup* and *Requests* and later stores them as a csv file database.
* **main** - This contains the actual scraper built using BeautifulSoup / bs4 and Requests 
* **file.csv** - This is the actual csv database with all the required product details ('Product Title','Supplier Name (website)','Stock Status','Product page) sorted under proper headings.
* **link.csv** - This contains the links of all the products whose details are to be fetched

#### Usage Instruction 
* Clone the given github repository using <br><br>
  ```git colne git@github.com:architsharmaa/Scraper-Task.git``` (for SSH keys)<br>
  ```git colne https://github.com/architsharmaa/Scraper-Task.git``` (for https)<br>
* Install the required dependencies using <br>
``` pip install requirements.txt```
* Run the given **scrapper** by running code in main or enter following command<br>
```python main.py```



