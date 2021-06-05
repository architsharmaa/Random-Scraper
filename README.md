# Product Scraper

The following is the sample scarper to scrape details of products using links.

#### Overview

The code scrapes the details of the product using _Beautiful Soup_ and _Requests_ and later stores them as a csv file database using _Pandas_.

- **main** - This contains the scraper built using BeautifulSoup / bs4 and Requests.
- **file.csv** - This is the actual CSV database with all the required product details ('Product Title','Supplier Name (website)','Stock Status','Product page) sorted under proper headings.
- **link.csv** - This contains the links of all the products whose details are to be fetched.

#### Usage Instruction

- Clone the given github repository using <br><br>
  `git clone git@github.com:architsharmaa/Scraper-Task.git` (for SSH keys)<br>
  `git clone https://github.com/architsharmaa/Scraper-Task.git` (for https)<br>

- Install the required dependencies using <br>
  ` pip install -r requirements.txt`
- Run the given **scraper** by running code in main or enter following command<br>
  `python main.py`
