
import requests
import xml.etree.ElementTree as et
import xml

url = input('Please enter an RSS Feed url :')

data = requests.get(url)

print(data.content)

stree = et.fromstring(data.content)

items = stree[0].findall('item')


pos = [ i.tag for i in items[0] ]

titles = [ i[pos.index('title')].text for i in items ]   
descriptions =  [ i[pos.index('description')].text for i in items ]   
links = [ i[pos.index('link')].text for i in items ]    

print('RSS Feed : \n------------------------------------------------------')
for i in range(len(titles)):
    print('\nTitle :' ,titles[i], '\nDescription : ' , descriptions[i], '\nLink : ', links[i], '\n')
    print('\n------------------------------------------------------')
