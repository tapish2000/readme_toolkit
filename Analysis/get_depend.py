# # make more requests using "gh_session" to create repos, list issues, etc.

import requests
from bs4 import BeautifulSoup
# import json
# data = {}
# with open("repo_details.json",'r') as outfile:
#     data = json.load(outfile)

# username = data['user']
# repo_name = data['repo_name']

repo = "expressjs/express"
page_num = 1
url = 'https://github.com/shobhi1310/medcon_server/network/dependencies'

# print("GET " + url)
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

data = [
    "{}/{}".format(
        t.find('a', {"data-repository-hovercards-enabled":""}).text,
        t.find('a', {"data-hovercard-type":"repository"}).text
    )
    for t in soup.findAll("div", {"class": "Box-row"})
]
f = open("./Dependency.txt",'w')
for i in range(len(data)):
    data[i] = data[i][7:-1].strip()
    f.write(data[i][data[i].find("/")+1:].strip()+'\n')
f.close()
# print(data)
    # paginationContainer = soup.find("button", {"class":"ajax-pagination-btn"}).find('a')
    # if paginationContainer:
    #     url = paginationContainer["href"]
    # else:
    #     break