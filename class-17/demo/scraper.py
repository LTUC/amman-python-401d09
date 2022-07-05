import requests
from bs4 import BeautifulSoup

url = 'https://www.bayt.com/en/jordan/jobs/python-developer-jobs/'

r = requests.get(url)
# print(r.content)
soup = BeautifulSoup(r.content , 'html.parser')

jobs_cards = soup.find_all('li', class_='has-pointer-d')

all_jobs = []

for job in jobs_cards:
    title = job.find('a').contents[0].strip()
    company = job.find('b', class_ = 'jb-company').contents[0].strip()
    desc = job.find('div', class_ = 'jb-descr').contents[0].strip()
    all_jobs.append({
       'title' : title,
       'company' : company,
       'desc' : desc
   })

job_titles = soup.find_all('h2', class_ = 'jb-title')
print(job_titles[0].text)

# import json
# with open('jobs.json', 'w') as file:
#     file.write(json.dumps(all_jobs))

