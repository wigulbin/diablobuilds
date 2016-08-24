from bs4 import BeautifulSoup
from urllib2 import urlopen
from HTMLParser import HTMLParser
from itemSlot import itemSlot
from htmlstripper import strip_tags

BASE_URL = "http://www.diablofans.com"
	
def f(section_url):
	print section_url
	html = urlopen(section_url).read()
	soup = BeautifulSoup(html, "html.parser")
	links = [None]*50
	buildLinks = ["None"]*50
	#print soup
	i = 0
	q = 0
	for link in soup.find_all('a'):
		#print(link.get('href'))
		links[i]=link.get('href')
		endLink = links[i]
		if(endLink != None and len(endLink)>9):
			if(endLink[:8] == "/builds/"):
				buildLinks[q] = links[i]
				#print buildLinks[q]
				q += 1
		links[i]
	#buildcat = soup.find("div","listing-body")
	#print buildcat
	#navbarLinks = [section_url + td.a["href"] for td in buildcat.findAll("td")]
	#print ', '.join(navbarLinks)
	for z in range(0, 50):
		if(buildLinks[z] != None): 
			buildLinks[z] = "http://www.diablofans.com%s" % (buildLinks[z])
			q+=1
	
	return buildLinks

def get_build_items(build_url):
	build_url = "http://www.diablofans.com/builds/82963-s7-gr97-firebird-solo"
	html = urlopen(build_url).read()
	soup = BeautifulSoup(html, "html.parser")
	category = soup.find("ul", "item-selection item-equip")
	itemName = [a.string for a in soup.findAll("a", "build-item")]
	itemTip = [li for li in soup.findAll("li", "item-stat")]
	print category 
	#print itemName
	#print itemTip.pop()
	htstring = str(itemTip.pop())
	htmlstring = strip_tags(htstring)
	print htmlstring
	helm = itemSlot(str(category), "helm", str(category), build_url, htmlstring)
	helm.getitemType()

nav = []
get_build_items("build_url")
#nav = f("http://www.diablofans.com/builds")
#for i in range(0,50):
#	print nav[i]
