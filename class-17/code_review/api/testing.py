string = '/api/capital-finder?country=Jordan'

from urllib import parse

url_componenets = parse.urlsplit(string)
print(url_componenets)

query = parse.parse_qsl(url_componenets.query)
print(query)

dic = dict(query)
print(dic)

