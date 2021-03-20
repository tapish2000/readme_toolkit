# import requests
# import json

# ####
# # inputs
# ####
# username = 'shobhi1310'

# # from https://github.com/user/settings/tokens
# token = 'e539a459bed4433e1cf69ba404b1ebfa68642ab7'

# repos_url = 'https://api.github.com/repos/tapish2000/medconnect-web/dependencies'

# # create a re-usable session object with the user creds in-built
# gh_session = requests.Session()
# gh_session.auth = (username, token)

# # get the list of repos belonging to me
# repos = json.loads(gh_session.get(repos_url).text)

# # print the repo names
# f = open("Dump.json",'w')
# f.write(str(repos))
# f.close()
    
# # make more requests using "gh_session" to create repos, list issues, etc.

import requests
from bs4 import BeautifulSoup

repo = "expressjs/express"
page_num = 1
url = 'https://github.com/tapish2000/medconnect-web/network/dependencies'.format(repo)

print("GET " + url)
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
print(data)
    # paginationContainer = soup.find("button", {"class":"ajax-pagination-btn"}).find('a')
    # if paginationContainer:
    #     url = paginationContainer["href"]
    # else:
    #     break