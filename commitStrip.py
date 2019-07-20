from bs4 import BeautifulSoup
from string import ascii_lowercase
import urllib.request
import requests
import shutil
import os
counter = 0


url ='http://www.commitstrip.com/en/page/'
baseLocation = 'F:/git/commitstrip/Comics/'

if not os.path.exists(baseLocation):
	os.makedirs(baseLocation)

for counter in range (0,50): #looping from the start page to the last page (given maximum,script will break on fail)
	url_page = (url+"{counter}/".format(counter=counter+1)) #appended counter with the link (page number looping)
	print('Url: '+url_page)
	html = urllib.request.urlopen(url_page).read()
	soup = BeautifulSoup(html, 'html.parser')
	 

	classHead = soup.findAll('div',attrs={'class':'excerpt'}) #get all the div elements with the class "excerpt"
	
	for div in classHead: #Loop through all the class "excerpt"
		allLinks = div.findAll('a') #If there are any links inside the div then get those divs in "links"
		for a in allLinks: #Loop through the links for actual links
			link = a['href']
			print ("Links: " + link) #then print only the actual url  
			comicName = link[41:]
			comicName = comicName.replace("/","")
			# print ("Comic name: "+ comicName)
			comicHtml = urllib.request.urlopen(link).read()
			comicSoup = BeautifulSoup(comicHtml,'html.parser')
			

			for comicImageTag in comicSoup.findAll('div', attrs={'class': 'entry-content'}):
				# comicImageNumber = 1
				comicImageLink = comicImageTag.find('img',src=True)
				# print("Comic image link: "+comicImageLink['src'])
				# comicImageLink = comicImageLink['src']
				comicImageLinkName= comicImageLink['src'][55:]
				# print("Comic image link name: "+comicImageLinkName[0])
				
				comicImageLinkNameExtension = comicImageLinkName[-4:]
				absoluteComicImageName = comicName+comicImageLinkNameExtension

				if not os.path.exists(baseLocation+absoluteComicImageName):
					try:
						with open(baseLocation+absoluteComicImageName, 'wb') as f:	
							f.write(urllib.request.urlopen(comicImageLink['src']).read())
							print(u"Downloaded: "+comicName+"\n")
					except:
						print("unicode error\n")
						pass						
				else:
					print('File already exists\n')
					
				

					
			

