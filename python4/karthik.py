import requests
import bs4
 
url='http://localhost:8000'
 
res = requests.get(url)
 
soup = bs4.BeautifulSoup(res.text, features="html.parser")
 
grid_rows = soup.select('.grid-row')
 
urls = []
 
for grid_row in grid_rows:
  grid_cell = grid_row.select('.grid-cell')[4]
  href = grid_cell.select('a')[0].attrs['href']
  urls.append(href)
for i in range(len(urls)):
    print(urls[i])
#print(urls)

result = []
 
for url in urls:
  data = {}
  resp = requests.get(url)
 
  soup = bs4.BeautifulSoup(resp.text, features="html.parser")
 
  rows = soup.select('.row')
  print(len(rows))
  for row in rows:
    cols = row.select('.col-md-3')
    cols = cols[:34]
    for colIndex in range(len(cols) - 1):
      if colIndex % 2 == 0:
        data[cols[colIndex].text.strip()] = cols[colIndex+1].text.strip()
        print(True)
    print(data)
  result.append(data)
  break
