import csv
import requests
from bs4 import BeautifulSoup

url = 'http://rerait.telangana.gov.in/SearchList/Search'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html,'html.parser')
table = soup.find('table', attrs={'class': 'resultsTable'})

list_of_rows = []
for row in table.findAll('tr')[1:]:
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("./inmates.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["s.no","proj name","promoter name","last modified","view details","view application","view certificate"])
writer.writerows(list_of_rows)
