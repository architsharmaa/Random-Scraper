#importing libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup

# scrapes the product name
def product_name(soup):
    for heading in soup.find_all(["h1"]):
        return heading.text.strip()

# scrapes availablity and categories them
def availability(soup):
    for availability in soup.find_all("span",{"ng-bind":"selector.productAvailability"}):
        if(availability.text == 'Available'):
            return 'In Stock'
        elif(availability.text == 'Out of Stock'):
            return 'Out of Stock'
        else:
            return 'Variant'

#scrapes the seller page link
def seller(soup):
    for link in soup.find_all('a',{"id":"vendor_link"}):
        return 'https://www.midwayusa.com/'+link.get('href')

#reading the links from the csv file
df = pd.read_csv('links.csv')

#creating headers for the csv database
final_li = [['Product Title','Supplier Name (website)','Stock Status','Product page']]

li = []

#loop to iterate over links
for url in df['links']:
    reqs = requests.get(url)                #fetching the url from the net
    soup = BeautifulSoup(reqs.text, 'lxml') #converting the dcrapped dom tree as lxml
    li.append(product_name(soup))           #getting the product name
    li.append(seller(soup))                 #getting the seller link
    li.append(availability(soup))           #getting the availability status
    li.append(url)                          #product page
    final_li.append(li)                     #appending the data for a product into database
    li = []


#converting the dataframe into a csv database
pd.DataFrame(final_li).to_csv('file.csv', header=False, index=False)



