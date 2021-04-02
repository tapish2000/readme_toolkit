import requests
import json

####
# inputs
####
username = 'tapish2000'

# from https://github.com/user/settings/tokens
token = '90499a48fe97d702d4c9a35dc62c9a9cff26c555'

repo = 'dst-custom-compiler'

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token {}".format(token)
}

url_lang = 'https://api.github.com/repos/{}/{}/languages'.format(username, repo)
# url_contrib = 'https://api.github.com/repos/{}/{}/contributors'.format(username, repo)
url_collab_usernames = 'https://api.github.com/repos/{}/{}/contributors'.format(username, repo)
url_comm_prof = 'https://api.github.com/repos/{}/{}/community/profile'.format(username, repo)
url_release = 'https://api.github.com/repos/{}/{}/releases'.format(username, repo)

out_lang = json.loads(requests.get(url_lang, headers = headers).text)
# out_contrib = json.loads(requests.get(url_contrib, headers = headers).text)
out_collab_usernames = json.loads(requests.get(url_collab_usernames, headers = headers).text)
out_comm_prof = json.loads(requests.get(url_comm_prof, headers = headers).text)
out_release = json.loads(requests.get(url_release, headers = headers).text)

# manipulation of outputs
out_lang = [o for o in out_lang.keys()]
# out_contrib = [o['login'] for o in out_contrib]
out_collab_usernames = [o['login'] for o in out_collab_usernames]


out_collab = []
for each in out_collab_usernames:
    url_collab = 'https://api.github.com/users/{}'.format(each)
    out = json.loads(requests.get(url_collab, headers = headers).text)
    out_collab.append(out['name'])


# print the repo names
data = {}
data["language"] = out_lang
# data["contributors"] = out_contrib
data["collaborators"] = out_collab
data["community-profile"] = out_comm_prof
data["releases"] = out_release

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
