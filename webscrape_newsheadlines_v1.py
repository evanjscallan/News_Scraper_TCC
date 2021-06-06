#Python Webscraper for TheCowboyChannel.com Home Page
             #Written by Evan Scallan
                    #2021
          #***FOR PERSONAL USE ONLY***



from bs4 import BeautifulSoup
import requests

#This is the way that data will be obtained from the website.
source = requests.get('https://www.thecowboychannel.com/').text
soup = BeautifulSoup(source, 'lxml')


#Isolates the news titles, descriptions, and video thumbnail images of the page.
#The for-loop enables the process to be iterated to all of the 'recent news' articles on the page.
for article in soup.find_all('div', class_='Card-container Card-md Card-split-container Card-split-container--sm frn-u-foreground-chrome frn-u-background-chrome'):
#print(article.prettify())

    #TITLE
    title = article.find('div', class_='Card-title Card-split-title Card-split-title--sm')
    title_iso = str(title).replace('<','>').split('>')[2]
    print(title_iso)

    #DESCRIPTION
    description = article.find('p', class_='Card-description Card-split-description Card-description Card-split-description--sm')
    description_iso = str(description).replace('<','>').split('>')[2]
    print(description_iso)

    #VID_THUMBNAIL IMAGE (Work in Progress)
    #vid_thumbnail = article.find('div', class_='imageContainer')
    #vid_thumbnail_iso = str(vid_thumbnail).split(" ")[30]
    #print(vid_thumbnail_iso)

    #INDEXING TOOL
    #indexer = vid_thumbnail_iso.index('640w,')
    #print(indexer)

    #Spacer for easier reading
    print()