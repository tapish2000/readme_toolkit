def get_repo_name(repo_link):
  temp = repo_link.split('/')
  return temp[-1]



repo_link = input("Enter the Repository Link: ")
repo_name = get_repo_name(repo_link)
maj_lang = input(" What is the major language used in the repository: ")
purp_repo = input(" What is the purpose of the repository [eg: for timepass]: ")

readme_f = open("output_readme.md", "w")
lines = []

# Repository name and tagline
lines.append("# " + repo_name)
lines.append("The " + repo_name + " is a " + maj_lang + " repository " + purp_repo)

# Repository description
lines.append("# Description")

# Installation
lines.append("# Installation")

# Usage
lines.append("# Usage")

# Authors and Acknowledgment
lines.append("# Authors and Acknowledgment")

# Contributing
lines.append("# Contributing")

# Basic syntax of Markdown


readme_f.writelines(lines)
readme_f.close()