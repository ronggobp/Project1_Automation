from modules.book import Book
from modules.magazine import Magazine
from modules.dvd import Dvd
from modules.cd import Cd
from modules.catalog import Catalog
import json

# get data from json
with open('files/catalog.json', 'r') as f:
    data_json = json.load(f)

# create object from data json
books = []
cds = []
dvds = []
magazines = []

for item in data_json:
    if item['source'] == 'book':
        books.append(Book(
            title=item['title'],
            upc=item['upc'],
            subject=item['subject'],
            issbn=item['issbn'],
            authors=item['authors'],
            dds_number=item['dds_number'],
        ))
    elif item['source'] == 'cd':
        cds.append(Cd(
            title=item['title'],
            upc=item['upc'],
            subject=item['subject'],
            artist=item['artist']
        ))
    elif item['source'] == 'dvd':
        dvds.append(Dvd(
            title=item['title'],
            upc=item['upc'],
            subject=item['subject'],
            actors=item['actors'],
            director=item['director'],
            genre=item['genre']
        ))
    elif item['source'] == 'magazine':
        magazines.append(Magazine(
            title=item['title'],
            upc=item['upc'],
            subject=item['subject'],
            volume=item['volume'],
            issue=item['issue']
        ))
    else:
        pass

# collect all data
catalog_all = [books, cds, dvds, magazines]

# run search & result
input_search = 'test'
results = Catalog(catalog_all).search(input_search)
if results:
    for index, result in enumerate(results):
        print(f'result ke--{index+1} | {result}')
else:
    print('no result')