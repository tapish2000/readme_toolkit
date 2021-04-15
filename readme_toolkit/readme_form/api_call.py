import requests
import json
import base64
import re

def api_call(repo_link):

    username = repo_link.split('/')[-2]

    # from https://github.com/user/settings/tokens
    keys = {}
    with open('config.json', 'r') as config:
        keys = json.load(config)
    
    token = keys["GITHUB_TOKEN"]

    repo = repo_link.split('/')[-1]

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "token {}".format(token)
    }

    url_lang = 'https://api.github.com/repos/{}/{}/languages'.format(username, repo)
    # url_contrib = 'https://api.github.com/repos/{}/{}/contributors'.format(username, repo)
    url_collab_usernames = 'https://api.github.com/repos/{}/{}/collaborators'.format(username, repo)
    url_comm_prof = 'https://api.github.com/repos/{}/{}/community/profile'.format(username, repo)
    url_release = 'https://api.github.com/repos/{}/{}/releases'.format(username, repo)

    out_lang = json.loads(requests.get(url_lang, headers = headers).text)
    # out_contrib = json.loads(requests.get(url_contrib, headers = headers).text)
    out_collab_usernames = json.loads(requests.get(url_collab_usernames, headers = headers).text)
    out_comm_prof = json.loads(requests.get(url_comm_prof, headers = headers).text)
    out_release = json.loads(requests.get(url_release, headers = headers).text)

    # manipulation of outputs
    out_lang = [o for o in out_lang.keys()]
    print(out_collab_usernames)
    out_collab_usernames = [o['login'] for o in out_collab_usernames]


    out_collab = []
    for each in out_collab_usernames:
        url_collab = 'https://api.github.com/users/{}'.format(each)
        out = json.loads(requests.get(url_collab, headers = headers).text)
        out_collab.append({"name": out['name'], "username": each})

    data = {}
    data["language"] = out_lang
    data["collaborators"] = out_collab
    data["community-profile"] = out_comm_prof
    data["releases"] = out_release

    return data

def parse_loc(readme):
    readme = readme.split('\n')
    readme = [line.strip() for line in readme if line != '']

    loc = 0

    i = 0
    while i < len(readme):
        if "```" in readme[i]:
            i += 1
            while(i < len(readme) and "```" not in readme[i]):
                loc += 1
                i += 1
        i += 1
    
    return loc

# def evaluate_sections(sections, readme): 
    

def parse_urls(readme):
    urls = re.findall(r'\[[^][]+]\((https?://[^()]+)\)', readme)
    
    return len(urls)

def parse_images(readme):
    images = re.findall(r'(?:!\[(.*?)\]\((.*?)\))', readme)
    
    return len(images)


def parse_sections(readme):
    readme = readme.split('\n')
    readme = [line.strip() for line in readme if line != '']

    sections = []

    for line in readme:
        if line[0] == '#':
            sections.append(' '.join(line.split(' ')[1:]))

    return sections


def score_generator(repo_link):
    # url = 'http://readme-score-api.herokuapp.com/score.json?url={}&human_breakdown=false&force=false'.format()
    username = repo_link.split('/')[-2]

    # from https://github.com/user/settings/tokens
    keys = {}
    with open('config.json', 'r') as config:
        keys = json.load(config)
    
    token = keys["GITHUB_TOKEN"]

    repo = repo_link.split('/')[-1]

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "token {}".format(token)
    }

    url_readme = 'https://api.github.com/repos/{}/{}/readme'.format(username, repo)
    
    out_readme = json.loads(requests.get(url_readme, headers = headers).text)

    # print (out_readme)

    b64content = out_readme['content']

    base64_message = b64content
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    readme = message_bytes.decode('ascii')

    sections = parse_sections(readme)
    images = parse_images(readme)
    urls = parse_urls(readme)
    loc = parse_loc(readme)

    # evaluate_sections(sections)


    '''
    Score sheet:
    sections:
        About: 8
        Description: 16
        Installation: 16
        Usage: 16
        Contributing: 8
        Author: 12
        Dependency: 14
        license: 1
        Others: 9
    images:
        max((images * 0.25), 5)
    urls:
        max((urls * 0.125), 3)
    loc:
        max((loc * 0.2), 5)
    '''



score_generator('https://github.com/shobhi1310/MedConnect')