
import requests
import xml.etree.ElementTree as et
import xml.dom.minidom  
import xml

url = input('please enter an RSS Feed url : ')

data = requests.get(url)

print(data.content)

stree = et.fromstring(data.content)

items = stree[0].findall('item') #.findall('title')

titles = [ i[0].text for i in items if i[0].tag == 'title']   
descriptions = [ i[2].text for i in items if i[2].tag == 'description']   
links = [ i[1].text for i in items if i[1].tag == 'link']   

print('RSS Feed : \n------------------------------------------------------')
for i in range(len(titles)):
    print('\nTitle :' ,titles[i], '\nDescription : ' , descriptions[i], '\nLink : ', links[i], '\n')
    print('\n------------------------------------------------------')

