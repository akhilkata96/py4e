from bs4 import BeautifulSoup
import urllib.request

# List with google queries I want to make
desired_google_queries = ['href' , 'View']

for query in desired_google_queries:
    # Constracting http query
    url = 'http://rerait.telangana.gov.in/SearchList/Search' + query
    # For avoid 403-error using User-Agent
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
    response = urllib.request.urlopen( req )
    html = response.read()
    # Parsing response
    soup = BeautifulSoup(html, 'html.parser')
    # Extracting number of results
    resultStats = soup.find(id="resultStats").string
    print(resultStats)
