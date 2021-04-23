import requests
import json
import base64
import re
import nltk
from monkeylearn import MonkeyLearn

nltk.download('wordnet')

from nltk.corpus import wordnet

# Global Variables
section_score_sheet = {
    "about" : 8,
    "description" : 16,
    "installation" : 16,
    "usage" : 16,
    "contributing" : 8,
    "author" : 12,
    "dependency" : 14,
    "license" : 1,
    "others" : 9
}
max_section_score = 100
max_image_score = 5
max_url_score = 3
max_loc_score = 5
image_weightage = 0.25
url_weightage = 0.125
loc_weightage = 0.2
similarity_threshold = 0.4

keys = {}
with open('config.json', 'r') as config:
    keys = json.load(config)


def api_call(repo_link):

    username = repo_link.split('/')[-2]

    # from https://github.com/user/settings/tokens
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
    # print(out_collab_usernames)
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

def similarity_index(word, words):
    temp = []

    for word1 in words:
        if word == word1:
            return 1
        wordnet1 = wordnet.synsets(word)
        wordnet2 = wordnet.synsets(word1)
        if wordnet1 and wordnet2:               # Check if both are non-empty
            temp.append(wordnet1[0].wup_similarity(wordnet2[0]))
    if temp:
        return max(temp)
    return 0

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

def parse_urls(readme):
    urls = re.findall(r'\[[^][]+]\((https?://[^()]+)\)', readme)
    
    return len(urls)

def parse_images(readme):
    images = re.findall(r'(?:!\[(.*?)\]\((.*?)\))', readme)
    
    return len(images)

def parse_sections_content(readme):
    readme = readme.split('#')
    readme = [line.strip() for line in readme if line.replace(' ', '') != '']

    content = []

    for line in readme:
        line = line.replace('\n', ' ')
        if len(line) > 0:
            content.append(line)

    return content

def parse_sections(readme):
    readme = readme.split('\n')
    readme = [line.strip() for line in readme if line.replace(' ', '') != '']

    sections = []

    for line in readme:
        if len(line) > 0 and line[0] == '#':
            sections.append(' '.join(line.split(' ')[1:]).lower())
    
    return sections

def evaluate_content(content):
    # MonkeyLearn Setup
    ml = MonkeyLearn(keys['MONKEYLEARN_API_KEY'])
    model_id = keys['MONKEYLEARN_MODEL_ID']

    response = ml.classifiers.classify(model_id, content)

    return set(res['classifications'][0]['tag_name'] for res in response.body)

def evaluate_sections(sections, content, repo_name):
    score = 0

    template_sections = {}
    with open('template_sections.json', 'r') as datafile:
        template_sections = json.load(datafile)
    
    # Add synonyms of repo name in the template sections
    template_sections['description'].append(repo_name)
    for syn in wordnet.synsets(repo_name):
        for lemma in syn.lemmas():
            template_sections['description'].append(lemma.name())

    # Synonyms for sectiosns in user's readme
    print(sections)
    sections_synonyms = set()
    for section in sections:
        sections_synonyms.add(section)
        for syn in wordnet.synsets(section):
            for lemma in syn.lemmas():
                sections_synonyms.add(lemma.name())
    
    # Tag names from the content
    tag_names = evaluate_content(content)
    
    print(template_sections)
    print("-"*15)
    print(sections_synonyms)
    print("-"*15)
    print(tag_names)

    count = 0                                           # To count how many headings are matched
    score_sheet = section_score_sheet
    for key, section_set in template_sections.items():
        for section in section_set:
            if score_sheet[key]:
                if (similarity_index(section, list(sections_synonyms)) >= similarity_threshold
                    or similarity_index(section, list(tag_names)) >= similarity_threshold):        # If headings' synonyms match directly
                    count += 1
                    score += score_sheet[key]
                    score_sheet[key] = 0

    if len(sections) > count:
        score += min(len(sections) - count, score_sheet['others'])

    return score


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
    base64_bytes = base64_message.encode('utf-8')
    message_bytes = base64.b64decode(base64_bytes)
    readme = message_bytes.decode('utf-8')

    sections = parse_sections(readme)
    section_content = parse_sections_content(readme)
    images = parse_images(readme)
    urls = parse_urls(readme)
    loc = parse_loc(readme)

    sections_score = evaluate_sections(sections, section_content, repo)
    images_score = min((images * image_weightage), max_image_score)
    urls_score = min((urls * url_weightage), max_url_score)
    loc_score = min((loc * loc_weightage), max_loc_score)

    score = sections_score + images_score + urls_score + loc_score
    # Converting to percentage
    score = round((score / (max_section_score + max_image_score + max_url_score + max_loc_score)) * 100, 2)

    print(score)

    output = [
        "score: " + str(score) + "%",
        "sections: " + str(sections),
        "images: " + str(images),
        "urls: " + str(urls),
        "Lines of Code: " + str(loc)
    ]

    return output, score

score_generator('https://github.com/tapish2000/readme-toolkit')
# similarity_index('about', ['Health & Medicine', 'Computers & Internet', 'Health & Medicine', 'Consumer Electronics', 'Travel', 'Computers & Internet', 'Computers & Internet'])