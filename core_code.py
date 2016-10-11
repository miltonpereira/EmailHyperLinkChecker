
from bs4 import BeautifulSoup
import requests

def verify_hyperlink(Link, LinkTitle):
	try:
		r = requests.get(Link,timeout = 5)
		LinkStatus= (r.status_code)
		print ( LinkTitle, LinkStatus)
		return LinkStatus
	# Here is the list of exceptation handled from request
	except requests.exceptions.ConnectionError as e:
		r = "Max retries exceeded"
		print (LinkTitle,r)
	except requests.exceptions.InvalidSchema as e: 
		print (e)
		r = "No connection adapters"
		print (LinkTitle,r)

with open('doc/html_doc.html', 'r', encoding='utf-8' ) as EmailHtml: # opens and reads html file from the folder
	SourceCode = EmailHtml.read()
	soup = BeautifulSoup(SourceCode,'html.parser')
	
	for link in soup.find_all('a'):
		LinkTitle = (link.get_text())
		emaillink = (link.get('href'))
		verify_hyperlink(emaillink,LinkTitle)



if __name__ == "__main__":
    print("Running as a progam")
    # TODO: Do something useful